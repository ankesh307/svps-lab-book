# Session 16: Magic Wand

**Class 2: Fun with Electronics & Mechanics**  
Tier 1 - Junior Makers | Tier 1 Kit

![Magic Wand](https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80)

> **Session 16** | 80 Minutes | Tier 1 - Junior Makers

---

## Class Schedule (80 Minutes)

| Time | Activity | Focus |
|:---|:---|:---|
| **0-20 min** | Theory | 5 colorful LEDs connect karo aur ek glowing wand banao!... |
| **20-65 min** | Practical Lab | Hands-on building and testing |
| **65-75 min** | Debug & Fix | Troubleshoot and improve |
| **75-80 min** | Quick Quiz | 3-question knowledge check |

**Keywords:** `Red aur Blue LED ke forward voltage mein kya fark hai?` | `Red ~2V, Blue ~3.3V — Blue ko zyada voltage chahiye`

---

## Theory (20 Minutes)

### LED Color and Voltage
Alag alag color ke LEDs ko ALAG alag voltage chahiye:
| LED Color | Forward Voltage |
|---|---|
| Red | 1.8 - 2.2V |
| Yellow | 2.0 - 2.4V |
| Green | 2.0 - 2.4V |
| Blue | 3.0 - 3.6V |
| White | 3.0 - 3.6V |

**Why Resistors are Important:**
Without resistor: LED current = very high → LED burns in seconds!
With resistor: Current is controlled to safe 20mA

**Ohm's Law (R = V/I):**
```
R = (Battery Voltage − LED Voltage) / LED Current
R = (9V − 2V) / 0.02A = 350Ω → Use 330Ω or 220Ω resistor
```

---

## Practical Lab (45 Minutes)

### Build Your Magic Wand!

### Materials:
- 9V Battery
- 5 LEDs (different colors: Red, Yellow, Green, Blue, White)
- 5 Resistors (220Ω each)
- A wooden stick/pen as the wand handle
- Tape and jumper wires

### Circuit (All 5 LEDs in Parallel):
```
Battery(+) ─┬─ R1 → Red LED ─┐
            ├─ R2 → Yellow ──┤
            ├─ R3 → Green ───┤─ Battery(−)
            ├─ R4 → Blue ────┤
            └─ R5 → White ───┘
```

### Assembly:
1. Sare wires ek wooden stick par tape karo
2. LEDs stick ke upar-neeche lagate jao
3. Battery end par tape karo
4. Switch ON karo → Your wand lights up!

### Decoration Challenge:
Foil paper ya glitter se wand decorate karo! Present to class!



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

**Q1.** Red aur Blue LED ke forward voltage mein kya fark hai?
> Answer: Red ~2V, Blue ~3.3V — Blue ko zyada voltage chahiye

**Q2.** Bina resistor ke LED kya hota hai?
> Answer: Zyada current se LED burn/fuse ho jaata hai seconds mein

**Q3.** 5 LEDs wand mein series mein hain ya parallel?
> Answer: Parallel — sab ko poori battery voltage milti hai



---

## Completion Checklist

- `[ ]` Understood the theory behind Magic Wand
- `[ ]` Successfully built and tested the project
- `[ ]` Wrote observations in notebook
- `[ ]` Can explain the working principle
- `[ ]` Completed the quiz
