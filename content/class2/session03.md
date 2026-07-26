# Session 03: Switch Control

**Class 2: Fun with Electronics & Mechanics**  
Tier 1 - Junior Makers | Tier 1 Kit

![Switch Control](https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80)

> **Session 03** | 80 Minutes | Tier 1 - Junior Makers

---

## Class Schedule (80 Minutes)

| Time | Activity | Focus |
|:---|:---|:---|
| **0-20 min** | Theory | Rocker Switch lagao aur light ko ON/OFF karo bina wire ... |
| **20-65 min** | Practical Lab | Hands-on building and testing |
| **65-75 min** | Debug & Fix | Troubleshoot and improve |
| **75-80 min** | Quick Quiz | 3-question knowledge check |

**Keywords:** `Rocker switch kya karta hai?` | `Circuit ko open ya close karke current flow control karta hai`

---

## Theory (20 Minutes)

### How a Switch Works
Switch ek **mechanical device** hai jo circuit ko open ya close karta hai.

**Types of Switches:**
1. **Rocker Switch** (Seesaw switch) — aaj hum yahi use karenge
2. Push Button — dabate hain to ON, chorte hain to OFF
3. Toggle Switch — ek position se doosri position mein jaata hai

```
Switch OFF (Open):       Switch ON (Closed):
Battery → [   ] → LED   Battery → [===] → LED
         switch                   switch
         OPEN                     CLOSED
         (No light)               (Light ON!)
```

**Real World**: Ghar ki light ka switch wohi karta hai — circuit ko open/close!

---

## Practical Lab (45 Minutes)

### Components Required
- 9V Battery + Snap
- Rocker Switch
- LED + 220Ω Resistor
- Jumper Wires

### Wiring:
```
Battery (+) → Red Wire → Rocker Switch (Pin 1)
Rocker Switch (Pin 2) → Resistor → LED (+)
LED (−) → Black Wire → Battery (−)
```

### Test:
1. Switch position 1: LED ON ✓
2. Switch position 2: LED OFF ✓

### Challenge Activity:
Add a SECOND LED in parallel — both should turn ON/OFF with the same switch!
```
Battery(+) → Switch → [LED1] → Battery(−)
                  ↘ [LED2] → Battery(−)
```



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

**Q1.** Rocker switch kya karta hai?
> Answer: Circuit ko open ya close karke current flow control karta hai

**Q2.** Switch ON hone par circuit kya hota hai?
> Answer: Closed circuit ban jaata hai — current flow karta hai

**Q3.** Ghar mein switch ke 3 example batao
> Answer: Light switch, fan switch, AC switch



---

## Completion Checklist

- `[ ]` Understood the theory behind Switch Control
- `[ ]` Successfully built and tested the project
- `[ ]` Wrote observations in notebook
- `[ ]` Can explain the working principle
- `[ ]` Completed the quiz
