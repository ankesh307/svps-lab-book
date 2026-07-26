# Session 28: OR Logic Game

**Class 2: Fun with Electronics & Mechanics**  
Tier 1 - Junior Makers | Tier 1 Kit

![OR Logic Game](https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80)

> **Session 28** | 80 Minutes | Tier 1 - Junior Makers

---

## Class Schedule (80 Minutes)

| Time | Activity | Focus |
|:---|:---|:---|
| **0-20 min** | Theory | Do switches mein se koi bhi dabao — light jale! OR logi... |
| **20-65 min** | Practical Lab | Hands-on building and testing |
| **65-75 min** | Debug & Fix | Troubleshoot and improve |
| **75-80 min** | Quick Quiz | 3-question knowledge check |

**Keywords:** `OR gate mein output HIGH kab hota hai?` | `Jab KISI BHI ek input ya dono HIGH hoon — sirf tab nahi jab dono LOW hoon`

---

## Theory (20 Minutes)

### OR Gate Logic
Output = HIGH if ANY input is HIGH

**Truth Table:**
| Input A | Input B | Output |
|---|---|---|
| 0 | 0 | 0 (No light) |
| 1 | 0 | 1 (LIGHT!) |
| 0 | 1 | 1 (LIGHT!) |
| 1 | 1 | 1 (LIGHT!) |

**How to Make OR with Switches:**
PARALLEL connection = OR gate!
Any switch closed → current flows

**Real World OR gate:**
- Hospital call system (any patient room calls → nurse station bell)
- Home alarm (front door OR back door opens → alarm)
- Elevator (any floor button pressed → elevator responds)

**Compare AND vs OR:**
```
AND (Series):  ALL must press → output
OR (Parallel): ANY can press → output
```

---

## Practical Lab (45 Minutes)

### Build OR Logic Game!

### Materials:
- 9V Battery
- 2 Push Buttons
- LED + 220Ω Resistor
- Jumper Wires

### Wiring (PARALLEL = OR):
```
Battery(+) ─┬─ Button1 ─┐
            │            ├─ LED(+) → LED(−) → Battery(−)
            └─ Button2 ─┘
```

### Test ALL Combinations:
| Button 1 | Button 2 | LED |
|---|---|---|
| Release | Release | ? |
| Press | Release | ? |
| Release | Press | ? |
| Press | Press | ? |

Expected: All except first row = LED ON!

### Extension: Build a Hospital Call System!
- Button A = Room 101 (Patient 1 calls)
- Button B = Room 102 (Patient 2 calls)
- Either pressing → Nurse station LED lights up!



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

**Q1.** OR gate mein output HIGH kab hota hai?
> Answer: Jab KISI BHI ek input ya dono HIGH hoon — sirf tab nahi jab dono LOW hoon

**Q2.** OR gate switches parallel mein kyun lagte hain?
> Answer: Parallel mein koi bhi path complete ho sakta hai — koi bhi switch close karo current flow

**Q3.** Hospital mein OR logic kaise use hota hai?
> Answer: Kisi bhi patient room se call → nurse station mein alert — OR gate!



---

## Completion Checklist

- `[ ]` Understood the theory behind OR Logic Game
- `[ ]` Successfully built and tested the project
- `[ ]` Wrote observations in notebook
- `[ ]` Can explain the working principle
- `[ ]` Completed the quiz
