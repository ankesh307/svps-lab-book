# Session 07: Parallel Lights

**Class 2: Fun with Electronics & Mechanics**  
Tier 1 - Junior Makers | Tier 1 Kit

![Parallel Lights](https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80)

> **Session 07** | 80 Minutes | Tier 1 - Junior Makers

---

## Class Schedule (80 Minutes)

| Time | Activity | Focus |
|:---|:---|:---|
| **0-20 min** | Theory | House wiring ki tarah 2 LEDs alag alag paths par lagao.... |
| **20-65 min** | Practical Lab | Hands-on building and testing |
| **65-75 min** | Debug & Fix | Troubleshoot and improve |
| **75-80 min** | Quick Quiz | 3-question knowledge check |

**Keywords:** `Parallel circuit mein voltage ka kya hota hai?` | `Har component ko poori voltage milti hai`

---

## Theory (20 Minutes)

### Parallel Circuit
Parallel mein har component ka APNA rasta hota hai.

```
Battery(+) ─┬─ Resistor → LED1 ─┐
            │                    ├─ Battery(−)
            └─ Resistor → LED2 ─┘
```

**Key Properties:**
- Har LED ko POORI voltage milti hai (9V each)
- Current alag alag paths mein divide hota hai
- Ek LED fuse → DOOSRI LED jalta rehta hai!

**Why Houses Use Parallel:**
```
Main Switch → ─┬─ Light 1 (220V)
               ├─ Fan (220V)
               ├─ AC (220V)
               └─ TV (220V)
```
Har appliance independently kaam karta hai!

---

## Practical Lab (45 Minutes)

### Components:
- 9V Battery
- 2 LEDs (different colors preferred)
- 2 Resistors (220Ω each)
- Jumper Wires

### Wiring:
```
Battery(+) ─┬─ 220Ω ─→ LED1(+), LED1(−) ─→ Battery(−)
            └─ 220Ω ─→ LED2(+), LED2(−) ─→ Battery(−)
```

### Experiment Steps:
1. Both LEDs connected — observe brightness
2. Remove LED1 — LED2 still works!
3. Remove LED2 — LED1 still works!

### Comparison Table:
| Property | Series | Parallel |
|---|---|---|
| Voltage per LED | Shared (Less) | Full (More) |
| Brightness | Dimmer | Brighter |
| One fails | Both off | Other stays on |
| Current path | One | Multiple |



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

**Q1.** Parallel circuit mein voltage ka kya hota hai?
> Answer: Har component ko poori voltage milti hai

**Q2.** Ghar ki wiring series mein hoti hai ya parallel mein?
> Answer: Parallel — isliye ek appliance band hone par doosri chalta rehta hai

**Q3.** Parallel circuit mein ek LED band hone par doosri?
> Answer: Jalta rehta hai — apna alag path hai



---

## Completion Checklist

- `[ ]` Understood the theory behind Parallel Lights
- `[ ]` Successfully built and tested the project
- `[ ]` Wrote observations in notebook
- `[ ]` Can explain the working principle
- `[ ]` Completed the quiz
