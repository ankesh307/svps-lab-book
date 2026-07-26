# Session 01: Battery Magic

**Class 2: Fun with Electronics & Mechanics**  
Tier 1 - Junior Makers | Tier 1 Kit

![Battery Magic](https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80)

> **Session 01** | 80 Minutes | Tier 1 - Junior Makers

---

## Class Schedule (80 Minutes)

| Time | Activity | Focus |
|:---|:---|:---|
| **0-20 min** | Theory | Aaj hum dekhenge ki bijli kaise kaam karti hai! 9V batt... |
| **20-65 min** | Practical Lab | Hands-on building and testing |
| **65-75 min** | Debug & Fix | Troubleshoot and improve |
| **75-80 min** | Quick Quiz | 3-question knowledge check |

**Keywords:** `Battery ke kitne terminals hote hain?` | `2 — Positive (+) aur Negative (−)`

---

## Theory (20 Minutes)

### What is Electricity?
Bijli electrons ke flow se banti hai. Ek battery mein do terminals hote hain:
- **Positive (+)**: Yahaan se current nikalta hai
- **Negative (−)**: Yahaan current wapas aata hai

Battery → Wire → LED → Wire → Battery — yahi ek **closed circuit** hai!

**Battery Parts:**
```
  ________
 |  9V    |
 | + | −  |  ← Terminals
 |________|
   |     |
  Red   Black
  Wire   Wire
   |     |
  [LED Lights Up!]
```

**Key Vocabulary:**
- **Electron**: Bijli banane wala tiny particle
- **Current**: Electrons ka flow (Ampere mein measure hota hai)
- **Voltage**: Battery ki pushing power (Volts mein)

---

## Practical Lab (45 Minutes)

### Components Required
| Component | Quantity | Purpose |
|---|---|---|
| 9V Battery | 1 | Power source |
| Battery Snap Connector | 1 | Connect battery |
| Red LED | 1 | Light indicator |
| 220 Ohm Resistor | 1 | Protect LED |
| Red Wire | 1 | + connection |
| Black Wire | 1 | − connection |

### Step 1: Identify LED Legs
```
    LED
   /   \
  +     −
(Long) (Short)
Anode  Cathode
```

### Step 2: Add Resistor
LED seedha battery se **connect mat karo** — burn ho jaayega!
Pehle **220Ω resistor** lagao LED ke saath series mein.

### Step 3: Complete Circuit
```
9V Battery (+) → Red Wire → Resistor → LED (long leg)
LED (short leg) → Black Wire → 9V Battery (−)
```

### Step 4: Observe!
Wires properly lagao → LED jal jaayegi!



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

**Q1.** Battery ke kitne terminals hote hain?
> Answer: 2 — Positive (+) aur Negative (−)

**Q2.** LED mein kaun sa leg positive hota hai?
> Answer: Lamba leg (Anode) positive hota hai

**Q3.** Resistor kyun zaroori hai?
> Answer: LED ko zyada current se protect karne ke liye



---

## Completion Checklist

- `[ ]` Understood the theory behind Battery Magic
- `[ ]` Successfully built and tested the project
- `[ ]` Wrote observations in notebook
- `[ ]` Can explain the working principle
- `[ ]` Completed the quiz
