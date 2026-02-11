# Scenes — Project Aequalis

This file aggregates all scene text and choices from the `scenes` folder so an AI can follow the story easily. Each section links to the original JSON file and preserves the scene text and choice targets.

---

## Intro — [scenes/intro.json](scenes/intro.json)

Text:

You shock awake, the ringing in your ears so intense you can barely think. Where am I? You wonder, forcing your eyes open. Your memory is blank—just flashes of light, shouting, and then… nothing.

The room around you is dark, lit only by the faint glow of a flickering DATA pad lying on the floor. To your right, mounted on the wall, is a LASER pistol, its charge indicator blinking faintly red. Beyond the open doorway, a corridor stretches into shadow. You push yourself upright. Somewhere deep within the hull, a low groan echoes through the metal, drawn-out and distant, like the ship itself is under strain.

The sound fades, replaced by another noise. Clank. Clank. Clank. Footsteps—or something like them—coming from the hallway beyond the open door. Getting closer. Your pulse spikes. What do you do? Grab the DATA pad, maybe you can lock it out or go for the LASER gun to stun whatever is coming

Choices:

- Grab the DATA pad (`data`) → target: `data`
- Grab the LASER pistol (`laser`) → target: `laser`

---

## Laser Pistol — [scenes/laser.json](scenes/laser.json)

Text:

Your pulse quickens as the clanking grows louder. Whatever's coming, it's not subtle—and it's getting close. You grab the laser pistol from its mount, thumb brushing over the setting dial. You make sure it's set to stun. No sense killing someone if it's just crew.

The footsteps echo closer through the corridor. Metal grinds. A faint, rasping breath. A figure steps into view. Human-shaped. You fire a stun pulse. The shot hits square in the chest; the figure collapses, but the smell of burnt ozone and scorched flesh suggests the effect went far deeper than a normal stun. The body is charred in places, features warped—familiar, but distorted.

The ship groans; the deck hums beneath your boots. You can't stay.

Choices:

- Search the body → target: `loot`
- Keep moving → target: `black_hole`

---

## Loot / Datapad — [scenes/loot.json](scenes/loot.json)

Text:

You step closer to the body and retrieve a scorched data pad. The log reveals "PROJECT AEQUALIS // TRANSPORTATION RESEARCH DIVISION" and notes about temporal-spatial bifurcation, replication events, and cellular degradation. The realization: you may have killed a version of yourself.

Energy levels are critical and shields compromised. The datapad map suggests two routes: Escape Pods or Engineering.

Choices:

- Escape Pods → target: `escape_pod_ending`
- Engineering → target: `hallway_ending`

---

## Black Hole — [scenes/black_hole.json](scenes/black_hole.json)

Text:

You move through a scorched corridor; a viewport shows stars warped around something so black it feels like a hole. A broken placard reads: PROJECT AEQUALIS — Phase IV: Cognitive Stabilization via Professional Transfer. You see a ladder to the Bridge and a flickering sign to Engineering.

Choices:

- Head for the Bridge → target: `bridge_ending`
- Go to Engineering → target: `engeneering_shooter_ending`

---

## Bridge — [scenes/bridge.png](scenes/bridge.png) (JSON: [scenes/bridge_transport.json](scenes/bridge_transport.json) and [scenes/bridge_ending.json](scenes/bridge_ending.json))

Text (Bridge entry):

You arrive on the bridge, consoles mostly functional, but the viewport looks into a void—the ship stares directly into the mouth of a black hole. System access shows PROJECT: Aequalis, status and warnings: containment breach, inbound transport, energy levels critical. Choices include sealing the Cargo Hold or heading to the Transport Bay.

Choices (from bridge scene):

- Seal the Cargo Hold and eject it → target: `ejector_ending`
- Head to the Transport Bay → target: `transport_ending`

Text (Bridge Ending — [scenes/bridge_ending.json](scenes/bridge_ending.json)):

You climb to the bridge. Systems show PROJECT: Aequalis with SHIELD STATUS: OFFLINE and DISTANCE TO SINGULARITY: 0.004 parsecs. Life sign detected in Engineering. You contact Engineering and hear "Working on it." Warnings escalate; shields offline, gravitational stress critical.

No choices — narrative continues toward stabilization attempts.

---

## Cargo Bay — [scenes/cargo.json](scenes/cargo.json)

Text:

The vast cargo bay has stacks of sealed containers and hazard-marked crates. A flickering force field holds a hull breach; outside is a black hole. Power surges then fail; the containment field collapses. A spacesuit is available; you can try to patch the breach or seal and eject the cargo.

Choices:

- Grab the spacesuit and try to patch the breach → target: `ejected_ending`
- Seal and eject the Cargo Bay → target: `engeneering_cargo_ending`

---

## Data Pad — [scenes/data.json](scenes/data.json)

Text (part 1):

You grab the data pad and restore temporary power to close a door. The pad reveals vessel info (ARV Genesis Transit) and that long-distance transport lacks sufficient energy. The transport menu lists destinations; temporary power est. choices are locked behind limited charge.

Choices:

Next scene continues to `data_part2` (transport destinations).

---

## Data Pad — Destinations — [scenes/data_part2.json](scenes/data_part2.json)

Text:

Transport destinations: Bridge, Escape Pods, Cargo Hold, Crew Quarters, Engineering. Power cell depleting; transport will deactivate soon. You must choose quickly.

Choices:

- Bridge → target: `transport_begin`
- Escape Pods → target: `transport_begin`
- Cargo Hold → target: `transport_begin`
- Crew Quarters → target: `transport_begin`
- Engineering → target: `transport_begin`

---

## Transport Sequence Begins — [scenes/fissle.json](scenes/fissle.json)

Text:

You initiate short-range transfer to a chosen destination. The pad warns of high power draw and temporary reserve error; you feel a double-image sensation and the field tightens. The UI includes route choices and penalties for delay.

Choices (route selection):

- Bridge → `bridge_transport`
- Cargo Hold → `cargo`
- Escape Pods → `fissle`
- Crew Quarters → `fissle`
- Engineering → `fissle`

---

## Transport Failed - Final — [scenes/fissle_ending.json](scenes/fissle_ending.json)

Text:

After a failed transfer, power diverts to emergency systems; doors override and the scene ends with a face-to-face moment with another version of you, then blackness.

---

## Ejected / Escape Pods — [scenes/ejected_ending.json](scenes/ejected_ending.json)

Text:

You don an emergency suit as the cargo bay fails and are ejected into space when the section detaches. You drift away, watch the bridge through the viewport, and see yourself on the bridge—an instance of the duplication/replication theme. The narrative ends with you drifting into the void. — End of Part 1

---

## Ejector Ending — [scenes/ejector_ending.json](scenes/ejector_ending.json)

Text:

From the bridge you order the cargo hold ejected to prevent destruction. Debris drifts toward the black hole; among it, a suited figure—possibly salvageable—drifts away. Regret and resolve follow.

---

## Engineering — Cargo Eject — [scenes/engeneering_cargo_ending.json](scenes/engeneering_cargo_ending.json)

Text:

You seal the cargo hold from the outside and eject it. The ship survives in a diminished state. You stagger to Engineering, work on the core with frantic repairs, then meet another version of yourself. Together you restore some power, but hull and shields remain critical. — End of Part 1

---

## Engineering — Shooter Ending — [scenes/engeneering_shooter_ending.json](scenes/engeneering_shooter_ending.json)

Text:

You head to Engineering and find someone already working—another you. You work together to reroute power, rebuild conduits, and restore partial energy. The ship stabilizes briefly before new warnings indicate time is running out. — End of Part I

---

## Escape Pod Ending — [scenes/escape_pod_ending.json](scenes/escape_pod_ending.json)

Text:

You launch an escape pod and watch from its viewport as stars and the ship are dragged into a black hole. The pod's systems fail and reality fractures; the scene ends as nothing remains.

---

## Hallway — [scenes/hallway_ending.json](scenes/hallway_ending.json)

Text:

You encounter another version of yourself in a hallway after a violent confrontation with a wrench. He reveals he ejected the cargo to save the ship. The two of you move toward Engineering together, determined to restore power. — End of Part 1

---

## Transport Bay — Final — [scenes/transport_ending.json](scenes/transport_ending.json)

Text:

You rush to the Transport Bay. Darkness, failing panels, and a figure in the chamber. A flash of blue; you collapse as your double shoots you. Your last thought: you killed yourself. — End of Part 1

---

## Notes

- Each section above preserves scene text and choice targets. Use this file as a single source-of-truth to feed an AI for story context.
- The original JSON files remain unchanged in `scenes/`.
