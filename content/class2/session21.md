# Session 21: Forward/Reverse Car

**Class 2: Fun with Electronics & Mechanics**  
Tier 1 - Junior Makers | Tier 1 Kit

![Forward/Reverse Car](https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80)

> **Session 21** | 80 Minutes | Tier 1 - Junior Makers

---

## Class Schedule (80 Minutes)

| Time | Activity | Focus |
|:---|:---|:---|
| **0-20 min** | Theory | Special switch wiring se 1-motor car ko forward aur bac... |
| **20-65 min** | Practical Lab | Hands-on building and testing |
| **65-75 min** | Debug & Fix | Troubleshoot and improve |
| **75-80 min** | Quick Quiz | 3-question knowledge check |

**Keywords:** `DPDT switch ka full form kya hai?` | `Double Pole Double Throw`

---

## Theory (20 Minutes)

### DPDT Switch for Motor Reversal
DPDT = Double Pole Double Throw

**Normal wiring:** Motor ek direction mein chalta hai
**DPDT switch:** Current ki direction change karta hai → Motor reverse!

```
DPDT Switch Positions:
Position 1 (Forward):
  Battery(+) → Motor(Red), Motor(Black) → Battery(−)
  
Position 2 (Reverse):
  Battery(+) → Motor(Black), Motor(Red) → Battery(−)
  
Position 3 (Center/Off):
  Battery disconnected → Motor stops
```

**DPDT Switch Internal Diagram:**
```
   Common ──[Pole1]──[throw A]
                  └──[throw B]
   Common ──[Pole2]──[throw A]
                  └──[throw B]
```
Flip switch → connections swap → motor reverses!

---

## Practical Lab (45 Minutes)

### Build Forward/Reverse Car!

### Materials:
- Gear motor car from session 10
- DPDT slide switch
- 9V Battery
- Extra jumper wires

### DPDT Wiring for Motor Reversal:
```
Battery (+) → DPDT Pin 1
Battery (−) → DPDT Pin 6
Motor Red → DPDT Pin 2
Motor Black → DPDT Pin 5

DPDT Pin 3 → Battery (−) [Internal cross connection]
DPDT Pin 4 → Battery (+) [Internal cross connection]
```

This creates the polarity reversal!

### Test:
- Switch Position 1: Car goes FORWARD
- Switch Position 2: Car goes BACKWARD  
- Switch Center: Car STOPS

### Add Steering (Optional):
Use a second DPDT to control left-right motor speed variation!



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

**Q1.** DPDT switch ka full form kya hai?
> Answer: Double Pole Double Throw

**Q2.** Motor reverse karne ke liye current mein kya change karna padta hai?
> Answer: Current direction reverse karni padti hai — wires swap karte hain

**Q3.** DPDT switch center position mein kya hota hai?
> Answer: Motor disconnect ho jaata hai — car ruk jaati hai



---

## Completion Checklist

- `[ ]` Understood the theory behind Forward/Reverse Car
- `[ ]` Successfully built and tested the project
- `[ ]` Wrote observations in notebook
- `[ ]` Can explain the working principle
- `[ ]` Completed the quiz
