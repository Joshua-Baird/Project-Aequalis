'''An epic story of grand preportions! hopefully you enjoy it!'''
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
os.chdir(BASE_DIR)
#I had to change some things in these prints, thats why I'm printing instead of catting.
#  I have brought them up here for clarity (and practice ;)

#The functions that print the cargo bay, bridge and fissle
#prints the bridge, changing only the time
def bridge(attempted):
    time = None
    if attempted:
        time = "00:54"
    else:
        time = "01:34"
    print(f"""
----------------------------------------------------------------------------------------------------------------------------------------------------------------
You tap Bridge on the transport menu and hold your breath.
The pad stutters, then the transport UI slides into a single-line progress bar.
----------------------------------------------------------
INITIATING SHORT-RANGE TRANSFER — DESTINATION: BRIDGE
Engaging local field… stabilizing matrix…
----------------------------------------------------------
The floor hums. Light crawls across the walls like water. For a half-second the world feels wrong—your weight lurches, your limbs feel slightly unmoored—then a ribbon of cold light snakes around you from foot to shoulder.
The pad in your hand vibrates with the field’s pulse.
-------------------------------------------
⚠ POWER DRAW: HIGH — TEMPORARY RESERVE {time}
⚠ ESTIMATED CHARGE FOR TRANSFER: 00:40
-------------------------------------------
The transport field tightens. You feel it—tension along your skin, that same stretchy, brushed sensation you felt when you were brought here.
For an instant you swear you see a double-outline of yourself, faint and out of sync, like a reflection that hasn’t quite caught up.

The world flickers. Your body feels like it’s been stretched thin—pulled apart—then snapped back together with a painful jolt.
When your vision clears, you’re standing on the bridge.

It’s in surprisingly good condition. Fully lit. Every console gleams in stark contrast to the emergency-red haze of the transport bay.
All except for one thing—the viewport on the far wall.

For a moment, you think it’s malfunctioning. The view is almost entirely black—a deep, endless void swallowing the stars. Only along the left quarter of the glass do a few warped streaks of light twist and shimmer, like reflections on rippling water.

You blink, expecting the distortion to fade—but nothing changes. Then it hits you:
this isn’t a screen. It’s a window.

The Genesis isn’t adrift in deep space. It’s staring directly into the mouth of a black hole.

Your data pad beeps, automatically syncing with the bridge systems.

————————————————————————————
SYSTEM ACCESS GRANTED — BRIDGE COMMAND
VESSEL DESIGNATION: Experimental Craft Aequalis
STATUS: Stable
ENERGY LEVELS: 100%
LIFE SIGNS: 2 detected — Bridge, Cargo Hold
————————————————————————————

Without prompt, the pad begins playing an audio log—crackling, distorted, but still intelligible.

“Project Aequalis log. The sickness has increased in severity. It’s as if the subjects’ entire cellular structure is… weakened. Almost anything can be fatal. Research into bringing in a—”

The recording cuts off mid-sentence as alarms scream through the bridge.

“Operation Sanus initiated,” a metallic voice announces from the intercom.

You glance down at your pad as new alerts flood the display:

————————————————————————————————
⚠ WARNING: CONTAINMENT BREACH DETECTED — CARGO HOLD
⚠ WARNING: INBOUND TRANSPORT — ORIGIN UNKNOWN
ENERGY LEVELS: 52% REMAINING
————————————————————————————————

Whatever’s beaming in is consuming a massive amount of power.

The lights dim. A surge of energy ripples through the hull, vibrating under your boots like thunder.

—————————————————————————————
⚠ WARNING: ENERGY LEVELS CRITICALLY LOW
POWER REMAINING: 10%
SHIELD INTEGRITY: COMPROMISED
—————————————————————————————
What do you do?
1. Seal the Cargo Hold and eject it — along with whoever or whatever is inside.
2. Head to the Transport Bay — find out who just transported in. Maybe whatever’s in Cargo can seal the breach before it’s too late.

          """)

#prints the cargo bay changing only the time
def cargo(attempted):
    time = None
    if attempted:
        time = "00:54"
    else:
        time = "01:34"
    print(f"""
----------------------------------------------------------------------------------------------------------------------------------------------------------------
You tap Cargo Bay on the transport menu and hold your breath.
The pad stutters, then the transport UI slides into a single-line progress bar.
----------------------------------------------------------
INITIATING SHORT-RANGE TRANSFER — DESTINATION: CARGO BAY
Engaging local field… stabilizing matrix…
----------------------------------------------------------
The floor hums. Light crawls across the walls like water. For a half-second the world feels wrong—your weight lurches, your limbs feel slightly unmoored—then a ribbon of cold light snakes around you from foot to shoulder.
The pad in your hand vibrates with the field’s pulse.
-------------------------------------------
⚠ POWER DRAW: HIGH — TEMPORARY RESERVE {time}
⚠ ESTIMATED CHARGE FOR TRANSFER: 00:40
-------------------------------------------
The transport field tightens. You feel it—tension along your skin, that same stretchy, brushed sensation you felt when you were brought here.
For an instant you swear you see a double-outline of yourself, faint and out of sync, like a reflection that hasn’t quite caught up.

The world flickers. Your body feels like it’s been stretched thin—pulled apart—then snapped back together with a painful jolt.
When your vision clears, you’re standing on the bridge.

It’s vast—three decks tall, lined with towering stacks of sealed containers. Unlike the flickering lights of the transport bay, this section is calm, almost serene.
The air feels heavier here, still charged with the faint hum of environmental stabilizers.
Crates of food rations, medical supplies, and precision equipment fill the room—essentials for survival.
But you also spot containers marked with red hazard sigils and high-value clearance codes. Whatever this ship was hauling, it was important.

At the far end of the bay, a flickering blue force field holds back a breach in the hull. 
Beyond it, you glimpse open space—the black vacuum bending light in impossible ways.
The ship’s proximity alarms hum softly in the background.

Your data pad chimes and syncs to local systems:
---------------------------------------------------------------
CARGO BAY STATUS: PARTIAL CONTAINMENT FAILURE
BREACH LOCATION: Section C-4
FORCE FIELD INTEGRITY: 28% — TEMPORARY HOLD
EXTERNAL CONDITIONS: Gravitational Anomaly Detected — High Risk
WARNING: Containment Field Requires Continuous Power
---------------------------------------------------------------
You glance toward the far wall. The cargo ejection array looms there—a massive reinforced aperture lined with yellow hazard lights. Through its shimmering field, you can see it now:

a black hole.

It dominates the view—a swirling maelstrom of light and darkness, bending the stars into distorted rings. 
The ship is teetering dangerously close to the event horizon.
Your pulse quickens.

Then, suddenly, the deck shudders.
A deep vibration rolls through the ship, accompanied by a blinding surge of blue-white light that streaks across the walls like lightning.
The hum of the stabilizers dies instantly.
The red emergency lights flare.

Your data pad explodes with warnings.
-----------------------------------------------------
⚠ POWER SURGE DETECTED — SOURCE UNKNOWN
⚠ ENERGY LEVELS CRITICAL — AUXILIARY SYSTEMS OFFLINE
⚠ FORCE FIELD FAILURE — SECTION C-4
-----------------------------------------------------
You turn toward the breach just in time to see the containment field collapse in a crackling shower of sparks. 
The vacuum howls as loose debris is sucked toward the rupture. Crates shift, sliding across the deck.
You grab the nearest handhold as the pressure drops.

Somewhere near the lockers along the wall, a spacesuit glints under the flashing lights. It’s intact—oxygen pack still charged.
If you move fast, you might be able to seal the breach manually before the ship loses the entire bay.

Or you could head for the doors to your left, seal the cargo bay from the outside, and eject the entire section before the failure spreads.
It would mean losing everything in it… but maybe saving the rest of the ship.

What do you do?
1. Grab the spacesuit and try to patch the breach before the bay collapses.
2. Seal and eject the Cargo Bay, then head to Engineering to see if you can restore power and pull away from the black hole.
    """)

#prints fissle changing destination and time
def fissle(player_choice):
    if player_choice == "2":
        destination = "Escape Pods"
    elif player_choice == "4":
        destination = "Crew Quarters"
    else:
        destination = "Engineering"
    print(f"""
----------------------------------------------------------------------------------------------------------------------------------------------------------------
You tap {destination} on the transport menu and hold your breath.
The pad stutters, then the transport UI slides into a single-line progress bar.
----------------------------------------------------------
INITIATING SHORT-RANGE TRANSFER — DESTINATION: {destination.upper()}
Engaging local field… stabilizing matrix…
----------------------------------------------------------
The floor hums. Light crawls across the walls like water. For a half-second the world feels wrong—your weight lurches, your limbs feel slightly unmoored—then a ribbon of cold light snakes around you from foot to shoulder.
The pad in your hand vibrates with the field’s pulse.
-------------------------------------------
⚠ POWER DRAW: HIGH — TEMPORARY RESERVE 1:34
⚠ ESTIMATED CHARGE FOR TRANSFER: 00:40
-------------------------------------------
The transport field tightens. You feel it—tension along your skin, that same stretchy, brushed sensation you felt when you were brought here.
For an instant you swear you see a double-outline of yourself, faint and out of sync, like a reflection that hasn’t quite caught up.

Then the pad screams:
----------------------------------------------------
⚠ ERROR: INSUFFICIENT ENERGY — TRANSFER INTERRUPTED
⚠ FIELD COLLAPSING — EMERGENCY RECALL
----------------------------------------------------
The light collapses inward like a pulled breath. The pull in your gut releases and you stumble, gripping the console to steady yourself.
The corridor feels too loud; your heartbeat thunders in your ears.

The data pad updates, numbers scrolling with ugly jitter:
----------------------------------------------------------------------
TEMPORARY POWER ESTABLISHED
POWER CELL REMAINING: 00:54
TRANSPORT SYSTEM STANDBY — NEXT ATTEMPT WILL CONSUME REMAINING RESERVE
----------------------------------------------------------------------
You swallow. Whatever you just felt—whatever that brief double-image was—didn’t finish.
But it used up time. You used almost forty seconds of the last reserve and got nothing but a collapsed field and the memory of being stretched.

A faint smear of light lingers on the wall where the field formed, like a ghost burn.
Your hands tremble where they rested against the console.

You have seconds to decide—and the pad makes the choices painfully clear.

1. Bridge
2. Escape Pods
3. Cargo Hold
4. Crew Quarters
5. Engineering

What do you do now?
    """)

#prints fissle ending only changing destination
def fissle_ending(player_choice):
    if player_choice == "2":
        destination = "Escape Pods"
    elif player_choice == "4":
        destination = "Crew Quarters"
    else:
        destination = "Engineering"
    print(f"""
----------------------------------------------------------------------------------------------------------------------------------------------------------------
You tap {destination} on the transport menu and hold your breath.
The pad stutters, then the transport UI slides into a single-line progress bar.
----------------------------------------------------------
INITIATING SHORT-RANGE TRANSFER — DESTINATION: {destination.upper()}
Engaging local field… stabilizing matrix…
----------------------------------------------------------
The floor hums. Light crawls across the walls like water. For a half-second the world feels wrong—your weight lurches, your limbs feel slightly unmoored—then a ribbon of cold light snakes around you from foot to shoulder.
The pad in your hand vibrates with the field’s pulse.
-------------------------------------------
⚠ POWER DRAW: HIGH — TEMPORARY RESERVE 00:54
⚠ ESTIMATED CHARGE FOR TRANSFER: 00:40
-------------------------------------------
The transport field tightens. You feel it—tension along your skin, that same stretchy, brushed sensation you felt when you were brought here.
For an instant you swear you see a double-outline of yourself, faint and out of sync, like a reflection that hasn’t quite caught up.

Then the pad screams:
----------------------------------------------------
⚠ ERROR: INSUFFICIENT ENERGY — TRANSFER INTERRUPTED
⚠ FIELD COLLAPSING — EMERGENCY RECALL
----------------------------------------------------
Then it all collapses.
The light, the sound — gone in an instant, leaving only the heavy silence of spent machinery.

The pad flickers one final time:
-------------------------------------------
TEMPORARY POWER RESERVE: 00:12
SYSTEM FAILURE — DOOR OVERRIDE INITIATED
-------------------------------------------
Your breath catches. The control panel by the bay door begins to glow red.
Hydraulics hiss.

A single, echoing clank rings through the chamber as the seals disengage.
The timer on the pad ticks down — 00:09… 00:08…

Each second feels like it’s being counted inside your skull.

00:05… 00:04…

The door begins to rise.
Metal grinds against metal, and a thin blade of dim light cuts across the floor, widening as the gap grows.

You take a step back.
Something — someone — stands in the doorway, a dark silhouette lit only by the glow of a data pad in their hand.

You blink.
They blink back.

The light catches their face — and your stomach twists.
It’s you.

Your stance, your clothes, your face, staring back from the hall — eyes wide, frozen in the same stunned disbelief that grips you now.

For a suspended heartbeat, neither of you moves.
Then the data pads die.

Blackness swallows everything.

— End of Part 1 —
    """)
with open("intro.txt", encoding="utf-8") as f:
    print(f.read())
choice = input("Enter DATA or LASER: ")
#if they choose the data pad
if choice.lower() == "data":
    with open("data.txt", encoding="utf-8") as f:
        print(f.read())
    choice = input("Please enter a number 1-5: ")
    should_fissle = ["2", "4", "5"]
    #if they choose the bridge
    if choice == "1":
        bridge(False)
        choice = input("Please enter 1 or 2: ")
        #if they choose transport
        if choice == "1":
            with open("ejector_ending.txt", encoding="utf-8") as f:
                print(f.read())
        #if they choose containment breach
        elif choice == "2":
            with open("transport_ending.txt", encoding="utf-8") as f:
                print(f.read())
        else:
            print("Please enter a valid response (1 or 2)")

    #if they choose the cargo bay
    elif choice == "3":
        cargo(False)
        choice = input("Please enter 1 or 2: ")
        #if they choose to contain the breach
        if choice == "1":
            with open("ejected_ending.txt", encoding="utf-8") as f:
                print(f.read())
        #if they choose to go to engeneering
        elif choice == "2":
            with open("engeneering_cargo_ending.txt", encoding="utf-8") as f:
                print(f.read())
        else:
            print("Please enter a valid response (1 or 2)")

    #if they choose the fissle
    elif choice in should_fissle:
        fissle(choice)
        choice = input("Please enter a number 1-5: ")
        #if they choose the bridge
        if choice == "1":
            bridge(True)
            choice = input("Please enter 1 or 2: ")
            #if they choose to contain the breach
            if choice == "1":
                with open("ejected_ending.txt", encoding="utf-8") as f:
                    print(f.read())
            #if they choose to go to engeneering
            elif choice == "2":
                with open("engeneering_cargo_ending.txt", encoding="utf-8") as f:
                    print(f.read())
            else:
                print("Please enter a valid response (1 or 2)")

        #if they choose the cargo bay
        elif choice == "3":
            cargo(True)
            choice = input("Please enter 1 or 2: ")
            #if they choose to contain the breach
            if choice == "1":
                with open("ejected_ending.txt", encoding="utf-8") as f:
                    print(f.read())
            #if they choose to go to engeneering
            elif choice == "2":
                with open("engeneering_cargo_ending.txt", encoding="utf-8") as f:
                    print(f.read())
            else:
                print("Please enter a valid response (1 or 2)")
        #if they choose the fissle again
        elif choice in should_fissle:
            fissle_ending(choice)
        else:
            print("Please enter a valid response (1 or 2 or 3 or 4 or 5)")
    #if tey give an invalid responce
    else:
        print("please give a valid response")

#if they choose the laser
elif choice.lower() == "laser":
    with open("laser.txt", encoding="utf-8") as f:
        print(f.read())
    choice = input("Please enter 1 or 2: ")
    #if they choose to loot the corps
    if choice == "1":
        with open("loot.txt", encoding="utf-8") as f:
            print(f.read())
        choice = input("Please enter 1 or 2: ")
        #if they choose to go to the escape pod
        if choice == "1":
            with open("escape_pod.txt", encoding="utf-8") as f:
                print(f.read())
        #if they choose to go to engeneering
        elif choice == "2":
            with open("hallway_ending.txt", encoding="utf-8") as f:
                print(f.read())
        else:
            print("Please enter a valid response (1 or 2)")

    #if they choose to keep on the move
    elif choice == "2":
        with open("black_hole.txt", encoding="utf-8") as f:
            print(f.read())
        choice = input("Please enter 1 or 2: ")
        #if they choose go to the bridge
        if choice == "1":
            with open("bridge_ending.txt", encoding="utf-8") as f:
                print(f.read())
        #if they choose to go to engeneering
        elif choice == "2":
            with open("engeneering_shooter_ending.txt", encoding="utf-8") as f:
                print(f.read())
        else:
            print("Please enter a valid response (1 or 2)")

#if they give an invalid response
else:
    print("Please enter a valid responce (data or laser)")
