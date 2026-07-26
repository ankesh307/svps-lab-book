# Session 04: Doorbell Alarm

**Class 2: Fun with Electronics & Mechanics**  
Tier 1 - Junior Makers | Tier 1 Kit

![Doorbell Alarm](https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80)

> **Session 04** | 80 Minutes | Tier 1 - Junior Makers

---

## Class Schedule (80 Minutes)

| Time | Activity | Focus |
|:---|:---|:---|
| **0-20 min** | Theory | Push button dabao aur buzzer baje! Apna pehla functiona... |
| **20-65 min** | Practical Lab | Hands-on building and testing |
| **65-75 min** | Debug & Fix | Troubleshoot and improve |
| **75-80 min** | Quick Quiz | 3-question knowledge check |

**Keywords:** `Active buzzer aur passive buzzer mein kya fark hai?` | `Active ko sirf power chahiye, passive ko code se frequency deni padti hai`

---

## Theory (20 Minutes)

### Active Buzzer vs Passive Buzzer
**Active Buzzer**: Seedha power do → sound aata hai (aaj hum yahi use karenge)
**Passive Buzzer**: Code se frequency deni padti hai

### How Push Button Works
```
Button NOT pressed:       Button PRESSED:
  Pin1   Pin2              Pin1   Pin2
   |       |                |_____|
  (No connection)          (Connected!)
  No current               Current flows!
```

### Doorbell Circuit Concept:
```
Visitor button dabata hai → Circuit complete → Buzzer bolta hai → 
Ghar wala sun leta hai!
```
Yahi aaj tum banayoge! :)

---

## Practical Lab (45 Minutes)

### Components:
| Item | Qty |
|---|---|
| 9V Battery + Snap | 1 |
| Active Buzzer (5V) | 1 |
| Push Button | 1 |
| Jumper Wires | 4 |

### Wiring:
```
Battery (+) ──→ Push Button (Pin 1)
Push Button (Pin 2) ──→ Buzzer (+) [Longer leg]
Buzzer (−) ──→ Battery (−)
```

### Test Your Doorbell:
- Button dabao → Buzzer BEEPS!
- Button choro → Buzzer STOPS!

### Creative Challenge: 
Cardboard ka door banao. Button darwaze ke bahar lagao aur wire andar tak le jao. Real doorbell ready!

**Buzzer ka symbol:**
```
   )))
  (((  ← Sound waves
   |||
  [Buzzer]
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

**Q1.** Active buzzer aur passive buzzer mein kya fark hai?
> Answer: Active ko sirf power chahiye, passive ko code se frequency deni padti hai

**Q2.** Push button normally kaise hota hai — ON ya OFF?
> Answer: Normally OPEN — dabane par CLOSE hota hai

**Q3.** Doorbell mein push button kahan lagta hai?
> Answer: Darwaze ke bahar — visitor dabaata hai



---

## Completion Checklist

- `[ ]` Understood the theory behind Doorbell Alarm
- `[ ]` Successfully built and tested the project
- `[ ]` Wrote observations in notebook
- `[ ]` Can explain the working principle
- `[ ]` Completed the quiz
