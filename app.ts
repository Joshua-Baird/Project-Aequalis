import { scenes as scenesObj } from './scenes';

const scenes: Record<string, Scene> = scenesObj.scenes;

const sceneEl = document.getElementById("scene") as HTMLElement;
const titleEl = document.getElementById("scene-title") as HTMLElement;
const textEl = document.getElementById("scene-text") as HTMLElement;
const choicesEl = document.getElementById("choices") as HTMLElement;
const restartBtn = document.getElementById("restart") as HTMLButtonElement;

let current = "intro";

let timerInterval: NodeJS.Timeout | null = null;

function ambienceClassFor(key: string): string {
    switch (key) {
        case "laser":
            return "ambience-laser";
        case "data":
            return "ambience-data";
        case "blackhole":
            return "ambience-blackhole";
        case "engineering":
            return "ambience-engineering";
        case "bridge":
            return "ambience-bridge";
        default:
            return "ambience-default";
    }
}

function clearAmbience(): void {
    sceneEl.classList.remove(
        "ambience-laser",
        "ambience-data",
        "ambience-blackhole",
        "ambience-engineering",
        "ambience-bridge",
        "ambience-default"
    );
}

let isTyping = false;
let skipTyping = false;

async function typeText(fullText: string, element: HTMLElement, speed = 18): Promise<void> {
    isTyping = true;
    skipTyping = false;
    // clear element and create a single caret element
    element.innerHTML = "";
    const caret = document.createElement("span");
    caret.className = "caret";
    element.appendChild(caret);

    // Insert characters as text nodes before the caret to avoid re-parsing innerHTML repeatedly
    for (let i = 0; i < fullText.length; i++) {
        if (skipTyping) break;
        const ch = fullText[i];
        if (ch === "\n") {
            const br = document.createElement("br");
            element.insertBefore(br, caret);
        } else {
            const tn = document.createTextNode(ch);
            element.insertBefore(tn, caret);
        }
        // keep panel scrolled to bottom while typing
        const panel = element.closest(".scene-inner") as HTMLElement;
        if (panel) panel.scrollTop = panel.scrollHeight;
        await new Promise((res) => setTimeout(res, speed));
    }

    // finish fast if skipped: render full text safely
    if (skipTyping) {
        element.innerHTML = escapeHtml(fullText).replace(/\n/g, "<br>");
    }

    // remove caret
    if (element.contains(caret)) element.removeChild(caret);
    isTyping = false;
}

interface Scene {
    title?: string;
    textLines?: string[];
    text?: string;
    ambience?: string;
    choices?: Array<{ text: string; target: string }>;
    image?: string;
    imageOpacity?: string;
    speed?: number;
    hideChoicesInitially?: boolean;
    continueButtonText?: string;
    nextScene?: string;
    resetTimerTo?: number;
}

function renderScene(id: string): void {
    const s = scenes[id] as Scene;
    if (!s) return;
    current = id;
    titleEl.textContent = s.title || "";

    // Stop any running timer when changing scenes, but preserve timer for scenes in the timed sequence
    const isTimedScene = (id === "data_part2" || id === "fissle" || id === "fissle_attempt" || id === "fissle_part2");

    if (!isTimedScene && timerInterval !== null) {
        clearInterval(timerInterval);
        timerInterval = null;
        const timer = document.getElementById("timer");
        if (timer) timer.textContent = "";
    }

    // ambience
    clearAmbience();
    sceneEl.classList.add(ambienceClassFor(s.ambience || ""));

    // mode classes for datapad/terminal
    sceneEl.classList.remove("terminal-mode", "datapad-mode");
    if (s.ambience === "data") {
        sceneEl.classList.add("datapad-mode");
    }
    if (
        s.ambience === "laser" ||
        (s.title && s.title.toLowerCase().includes("terminal"))
    ) {
        sceneEl.classList.add("terminal-mode");
    }

    // render text with typing effect
    const fullText = Array.isArray(s.textLines)
        ? s.textLines.join("\n")
        : s.text || "";
    // disable choices while typing
    choicesEl.innerHTML = "";
    // start typing
    // apply scene background image if provided
    const bgEl = document.getElementById("scene-bg") as HTMLElement;
    if (bgEl) {
        if (s.image) {
            bgEl.style.backgroundImage = `url("${s.image}")`;
            bgEl.style.opacity = s.imageOpacity || "0.18";
        } else {
            bgEl.style.backgroundImage = "";
        }
    }

    typeText(fullText, textEl, s.speed || 12).then(() => {
        // after typing completes, render choices
        const choices = s.choices || [];

        if (s.hideChoicesInitially) {
            // Show a continue button to reveal choices
            const continueBtn = document.createElement("button");
            continueBtn.className = "choice-btn";
            continueBtn.innerHTML = "<strong>" + escapeHtml(s.continueButtonText || "View Schematic") + "</strong>";
            continueBtn.setAttribute("data-choice-index", "0");
            continueBtn.onclick = () => {
                const nextScene = s.nextScene || "fissle_part2";
                if (scenes[nextScene]) {
                    renderScene(nextScene);
                    // Check if this scene should reset the timer
                    const nextSceneData = scenes[nextScene] as Scene;
                    if (nextSceneData && nextSceneData.resetTimerTo !== undefined) {
                        startTimer(nextSceneData.resetTimerTo);
                    } else if (nextScene === "data_part2" || nextScene === "fissle_part2") {
                        startTimer(90);
                    }
                } else {
                    choicesEl.innerHTML = "";
                    renderChoices(choices);
                    startTimer();
                }
            };
            choicesEl.appendChild(continueBtn);
        } else {
            renderChoices(choices);
        }
    });
}

function renderChoices(choices: Array<{ text: string; target: string }>): void {
    if (choices.length === 0) {
        const c = document.createElement("button");
        c.className = "btn btn-primary";
        c.textContent = "Restart";
        c.onclick = () => goTo("intro");
        choicesEl.appendChild(c);
    } else {
        choices.forEach((ch, idx) => {
            const b = document.createElement("button");
            b.className = "choice-btn";
            b.innerHTML = "<strong>" + escapeHtml(ch.text) + "</strong>";
            b.setAttribute("data-choice-index", String(idx + 1));
            b.onclick = () => {
                const next =
                    typeof ch.target === "string" ? ch.target : ch.target;
                if (next && scenes[next]) renderScene(next);
            };
            choicesEl.appendChild(b);
        });
    }
}

function goTo(id: string): void {
    if (!scenes[id]) return;
    renderScene(id);
}

function escapeHtml(str: string | null): string {
    if (str == null) return "";
    return String(str)
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/\'/g, "&#39;");
}

async function init(): Promise<void> {
    renderScene(current);
}

restartBtn.addEventListener("click", () => goTo("intro"));

init();

// allow skipping typing by clicking or pressing Space/Enter
document.addEventListener("keydown", (e) => {
    if (isTyping) {
        if (e.key === " " || e.key === "Enter") {
            skipTyping = true;
            e.preventDefault();
        }
        return;
    }
    // if not typing, allow number keys to pick choices (1-based)
    if (!isTyping && /[1-9]/.test(e.key)) {
        const keyNum = parseInt(e.key, 10);
        // Find button with matching data-choice-index
        const btn = Array.from(choicesEl.children).find(
            child => (child as HTMLElement).getAttribute("data-choice-index") === String(keyNum)
        ) as HTMLButtonElement;
        if (btn) btn.click();
    }
});

export function startTimer(duration: number = 90, onComplete?: () => void) {
    const timer = document.getElementById("timer");
    if (timer) {
        // Clear any existing timer
        if (timerInterval !== null) {
            clearInterval(timerInterval);
            timerInterval = null;
        }

        let seconds = duration;

        timerInterval = setInterval(() => {
            seconds--;
            const minutes = Math.floor(seconds / 60);
            const secs = seconds % 60;
            const display = `${String(minutes).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
            timer.textContent = display;

            if (seconds <= 0) {
                if (timerInterval) clearInterval(timerInterval);
                timerInterval = null;
                timer.textContent = "";
                if (onComplete) {
                    onComplete();
                } else {
                    goTo("fissle_ending");
                }
            }
        }, 1000);

        // Set initial display
        const minutes = Math.floor(seconds / 60);
        const secs = seconds % 60;
        const display = `${String(minutes).padStart(2, '0')}:${String(secs).padStart(2, '0')}`;
        timer.textContent = display;
    }
}

document.getElementById("timer-starter")?.addEventListener("click", () => {
    startTimer();
});