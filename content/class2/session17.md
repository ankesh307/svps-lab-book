# Session 17: Wire Maze Game

**Class 2: Fun with Electronics & Mechanics**  
Tier 1 - Junior Makers | Tier 1 Kit

![Wire Maze Game](https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80)

> **Session 17** | 80 Minutes | Tier 1 - Junior Makers

---

## Class Schedule (80 Minutes)

| Time | Activity | Focus |
|:---|:---|:---|
| **0-20 min** | Theory | Bent wire pe ring ghuma bina touch kiye — touch hone pa... |
| **20-65 min** | Practical Lab | Hands-on building and testing |
| **65-75 min** | Debug & Fix | Troubleshoot and improve |
| **75-80 min** | Quick Quiz | 3-question knowledge check |

**Keywords:** `Wire maze game mein circuit kab complete hota hai?` | `Jab ring maze wire ko touch karta hai`

---

## Theory (20 Minutes)

### The Game Circuit Concept
Yeh ek simple continuity tester game hai!

```
LOOP (metal ring) → touches WIRE → circuit COMPLETE → BUZZER rings!
```

**Game Rules:**
- Bent wire = Maze
- Metal ring = Player's controller
- Goal: Ring wire maze se nikalo bina touch kiye
- Touch = BUZZER BEEPS → You LOST!

**Circuit Logic:**
Normally the circuit is OPEN (ring not touching wire) → Buzzer silent
Ring touches wire → Circuit CLOSED → Buzzer rings!

**Engineering Thinking:**
Yeh circuit operation rooms mein use hota hai! Surgeons ko "buzz out" nahi karna hota while operating — steady hands required!

---

## Practical Lab (45 Minutes)

### Build the Wire Maze Game!

### Materials:
- Thick copper wire / thick iron wire (maze)
- Thin wire loop (player's ring)
- 9V Battery
- Active Buzzer
- Wooden base

### Construction:
**Step 1 — Make the Maze:**
Thick wire ko interesting shapes mein bend karo (zig-zag, loops, curves)
Both ends ko wooden base mein fix karo

**Step 2 — Make the Ring:**
Thin wire ka 1cm diameter ring banao
This is the "wand" the player moves

**Step 3 — Wiring:**
```
Battery(+) → Buzzer(+)
Buzzer(−) → Wire Maze (start end)
Wire Maze (other end) connected through RING
Ring → Battery(−)

(Ring touching maze = circuit complete = BUZZ!)
```

### How to Play:
1. Ring ko maze ke ek end par start karo
2. Doosre end tak pohonchne ki koshish karo
3. Touch karo → BUZZ! → Start over!
4. Jo player bina buzz ke pahunche → WON!



---

## Common Problems & Fixes

| Problem | Solution |
|:---|:---|
| Nothing working | Check power connections first |
| Incorrect output | Verify wiring against diagram |
| Code not uploading | Check COM port and board selection |
| Unexpected values | Check sensor connections |

---

## Quiz (5 Minutes)

**Q1.** Wire maze game mein circuit kab complete hota hai?
> Answer: Jab ring maze wire ko touch karta hai

**Q2.** Wire maze game ka medical use kya hai?
> Answer: Surgeons ke haath ki steadiness test karna — Operation Simulation game

**Q3.** Is circuit mein buzzer normally ON hoga ya OFF?
> Answer: OFF — sirf tab ON jab ring wire ko touch kare



---

## Completion Checklist

- `[ ]` Understood the theory behind Wire Maze Game
- `[ ]` Successfully built and tested the project
- `[ ]` Wrote observations in notebook
- `[ ]` Can explain the working principle
- `[ ]` Completed the quiz
