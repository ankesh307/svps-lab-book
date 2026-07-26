# Session 06: Series Lights

**Class 2: Fun with Electronics & Mechanics**  
Tier 1 - Junior Makers | Tier 1 Kit

![Series Lights](https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80)

> **Session 06** | 80 Minutes | Tier 1 - Junior Makers

---

## Class Schedule (80 Minutes)

| Time | Activity | Focus |
|:---|:---|:---|
| **0-20 min** | Theory | Diwali lights ki tarah 2 LEDs ek line mein lagao. Serie... |
| **20-65 min** | Practical Lab | Hands-on building and testing |
| **65-75 min** | Debug & Fix | Troubleshoot and improve |
| **75-80 min** | Quick Quiz | 3-question knowledge check |

**Keywords:** `Series circuit mein current ka kitna rasta hota hai?` | `Sirf ek rasta — current sab components se ek ek karke guzarta hai`

---

## Theory (20 Minutes)

### Series Circuit
Series mein components ek LINE mein lagte hain. Current sirf EK rasta le sakta hai.

```
Battery(+) → LED1 → LED2 → Battery(−)
             ↑             ↑
          First           Second
           LED             LED
```

**Key Properties:**
- Same current sab mein flow karta hai
- Voltage divide ho jaata hai (6V battery → 3V + 3V)
- Ek LED burn out → DONO band! (Christmas lights problem!)

**Real-World Example:**
Old-style Diwali LED string — ek bulb fuse → poori string band!

**Voltage Divider:**
```
9V Battery → LED1 (gets ~4.5V) → LED2 (gets ~4.5V) → GND
```

---

## Practical Lab (45 Minutes)

### Components:
- 9V Battery + Snap
- 2 LEDs (any color)
- 1 Resistor 220Ω (one resistor is enough!)
- Jumper Wires

### Wiring:
```
Battery(+) → 220Ω Resistor → LED1(+)
LED1(−) → LED2(+)
LED2(−) → Battery(−)
```

### Observations:
1. Do both LEDs light up? ___
2. Are they equally bright? ___
3. Remove one LED — what happens to the other? ___

### Compare:
Connect LEDs separately (parallel) and compare brightness!
Series = Dimmer (voltage shared)
Parallel = Brighter (full voltage each)



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

**Q1.** Series circuit mein current ka kitna rasta hota hai?
> Answer: Sirf ek rasta — current sab components se ek ek karke guzarta hai

**Q2.** Ek LED fuse hone par doosri LED ka kya hoga?
> Answer: Doosri LED bhi band ho jaayegi — circuit break ho jaata hai

**Q3.** Series mein voltage kaise divide hota hai?
> Answer: Har component ko equal share milta hai — 9V ÷ 2 LEDs = 4.5V each



---

## Completion Checklist

- `[ ]` Understood the theory behind Series Lights
- `[ ]` Successfully built and tested the project
- `[ ]` Wrote observations in notebook
- `[ ]` Can explain the working principle
- `[ ]` Completed the quiz
