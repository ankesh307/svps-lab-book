# Session 09: Reverse Air

**Class 2: Fun with Electronics & Mechanics**  
Tier 1 - Junior Makers | Tier 1 Kit

![Reverse Air](https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80)

> **Session 09** | 80 Minutes | Tier 1 - Junior Makers

---

## Class Schedule (80 Minutes)

| Time | Activity | Focus |
|:---|:---|:---|
| **0-20 min** | Theory | Motor ke wires ulte karo aur fan ka direction badal jaa... |
| **20-65 min** | Practical Lab | Hands-on building and testing |
| **65-75 min** | Debug & Fix | Troubleshoot and improve |
| **75-80 min** | Quick Quiz | 3-question knowledge check |

**Keywords:** `Motor ke wires swap karne se kya hota hai?` | `Motor ka rotation direction reverse ho jaata hai`

---

## Theory (20 Minutes)

### Motor Polarity and Reverse
DC Motor ki khaasiyat: **Wires swap karo → Direction reverse!**

```
Normal:    Battery(+) → Motor(Red) → Spins CLOCKWISE
Reversed:  Battery(+) → Motor(Black) → Spins COUNTER-CLOCKWISE
```

**Why Does This Happen?**
Current direction change → Magnetic field direction change → Rotation reverses!

**Real-World Applications:**
- 🚗 Car window (up/down) = same motor, reversed current
- 🔧 Electric drill (forward/reverse)
- 🏗️ Elevator (up/down)
- 🤖 Robot (forward/backward)

**H-Bridge Circuit** (advanced concept preview):
```
Motor Driver IC lets us reverse current direction electronically!
```

---

## Practical Lab (45 Minutes)

### Experiment: Swap & Observe!

**Round 1 — Normal Direction:**
```
Battery(+) → Motor Red → spins → observe direction → note: CLOCKWISE or COUNTER-CLOCKWISE
```

**Round 2 — Reversed:**
Carefully swap the two motor wires:
```
Battery(+) → Motor Black (was negative) → direction REVERSES!
```

### Build a DPDT Switch Control:
A DPDT (Double Pole Double Throw) switch lets you reverse direction with a flip!

### Application Activity:
Make a "Two-Direction Fan":
- Position A: Blows air TOWARDS you
- Position B: Blows air AWAY from you

### Record Results:
| Wire Connection | Rotation Direction |
|---|---|
| Red = + | ? |
| Black = + | ? |



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

**Q1.** Motor ke wires swap karne se kya hota hai?
> Answer: Motor ka rotation direction reverse ho jaata hai

**Q2.** DPDT switch kya karta hai?
> Answer: Motor ki polarity switch karta hai — forward/reverse control

**Q3.** Real mein forward/reverse motor kahan use hoti hai?
> Answer: Car windows, elevators, electric drills, robots



---

## Completion Checklist

- `[ ]` Understood the theory behind Reverse Air
- `[ ]` Successfully built and tested the project
- `[ ]` Wrote observations in notebook
- `[ ]` Can explain the working principle
- `[ ]` Completed the quiz
