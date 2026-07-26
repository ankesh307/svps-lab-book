# Session 15: Traffic Lights

**Class 2: Fun with Electronics & Mechanics**  
Tier 1 - Junior Makers | Tier 1 Kit

![Traffic Lights](https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80)

> **Session 15** | 80 Minutes | Tier 1 - Junior Makers

---

## Class Schedule (80 Minutes)

| Time | Activity | Focus |
|:---|:---|:---|
| **0-20 min** | Theory | 3 switches se Red, Yellow, Green LEDs manually control ... |
| **20-65 min** | Practical Lab | Hands-on building and testing |
| **65-75 min** | Debug & Fix | Troubleshoot and improve |
| **75-80 min** | Quick Quiz | 3-question knowledge check |

**Keywords:** `Traffic light mein Yellow light kab aati hai?` | `Red se Green aur Green se Red ke beech mein — warning phase`

---

## Theory (20 Minutes)

### Traffic Light System
Real traffic lights computerized hain par aaj hum MANUAL control banayenge!

**Traffic Light Sequence:**
```
RED    (30 sec) → Stop! Danger!
YELLOW (5 sec)  → Slow down, warning
GREEN  (30 sec) → Go! Safe to move
```

**Color Psychology:**
- 🔴 RED = STOP — most visible color, instinctive danger signal
- 🟡 YELLOW = WARNING — intermediate, prepare to stop/go
- 🟢 GREEN = GO — historically safe color, "clear"

**Circuit Design:**
Each LED needs its OWN switch so we can control them independently.
This is a **multi-switch parallel circuit!**

---

## Practical Lab (45 Minutes)

### Components:
- 9V Battery
- Red LED x1, Yellow LED x1, Green LED x1
- 220Ω Resistors x3
- Push Buttons x3
- Jumper Wires

### Wiring (3 Independent Circuits):
```
Battery(+) → Switch1 → 220Ω → Red LED(+), Red LED(−) → Battery(−)
Battery(+) → Switch2 → 220Ω → Yellow LED(+), Yellow LED(−) → Battery(−)
Battery(+) → Switch3 → 220Ω → Green LED(+), Green LED(−) → Battery(−)
```

### Role Play Activity:
- Student 1: Controls the switches
- Student 2: Acts as a car driver
- Student 3: Pedestrian

Follow proper traffic light sequence:
Red 5 sec → Yellow 2 sec → Green 5 sec → Yellow 2 sec → Repeat!

### Challenge:
Can you add a BUZZER that beeps when RED is ON? (Pedestrian signal!)



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

**Q1.** Traffic light mein Yellow light kab aati hai?
> Answer: Red se Green aur Green se Red ke beech mein — warning phase

**Q2.** 3 LEDs alag alag control karne ke liye kya chahiye?
> Answer: 3 alag switches — ek per LED

**Q3.** Traffic light circuit mein LEDs series mein hain ya parallel mein?
> Answer: Parallel mein — har LED ka apna independent circuit hai



---

## Completion Checklist

- `[ ]` Understood the theory behind Traffic Lights
- `[ ]` Successfully built and tested the project
- `[ ]` Wrote observations in notebook
- `[ ]` Can explain the working principle
- `[ ]` Completed the quiz
