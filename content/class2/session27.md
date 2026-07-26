# Session 27: AND Logic Game

**Class 2: Fun with Electronics & Mechanics**  
Tier 1 - Junior Makers | Tier 1 Kit

![AND Logic Game](https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80)

> **Session 27** | 80 Minutes | Tier 1 - Junior Makers

---

## Class Schedule (80 Minutes)

| Time | Activity | Focus |
|:---|:---|:---|
| **0-20 min** | Theory | Dono buttons ek saath dabaao tabhi buzzer bajega — AND ... |
| **20-65 min** | Practical Lab | Hands-on building and testing |
| **65-75 min** | Debug & Fix | Troubleshoot and improve |
| **75-80 min** | Quick Quiz | 3-question knowledge check |

**Keywords:** `AND gate mein output HIGH kab hota hai?` | `Jab DONO inputs HIGH hoon — Tab hi output HIGH hota hai`

---

## Theory (20 Minutes)

### Logic Gates — The Foundation of Computing!
Logic gates digital computers ki basic building blocks hain.

**AND Gate:**
Output = HIGH only when ALL inputs are HIGH

**Truth Table:**
| Input A | Input B | Output |
|---|---|---|
| 0 (No press) | 0 (No press) | 0 (No sound) |
| 1 (Press) | 0 (No press) | 0 (No sound) |
| 0 (No press) | 1 (Press) | 0 (No sound) |
| 1 (Press) | 1 (Press) | 1 (SOUND!) |

**How to Make AND with Switches:**
Series connection = AND gate!
Both must close → current flows

**Real World AND gate:**
- Safety systems (both hands on buttons to operate dangerous machine)
- Bank vault (two keys needed simultaneously)
- Nuclear launch (two officers, two keys)

---

## Practical Lab (45 Minutes)

### Build AND Logic Game!

### Materials:
- 9V Battery
- 2 Push Buttons
- Active Buzzer
- Jumper Wires

### Wiring (SERIES = AND):
```
Battery(+) → Button1 → Button2 → Buzzer(+) → Battery(−)
```

### Test ALL Combinations:
| Button 1 | Button 2 | Buzzer |
|---|---|---|
| Release | Release | ? |
| Press | Release | ? |
| Release | Press | ? |
| Press BOTH | Press BOTH | ? |

Expected: Only last row = BUZZ!

### Real-Life Application Thinking:
Design a "Safe Factory Machine" that only operates when:
- Operator 1 presses button (safety confirmed)
- AND Operator 2 presses button (second confirmation)
This prevents accidents!



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

**Q1.** AND gate mein output HIGH kab hota hai?
> Answer: Jab DONO inputs HIGH hoon — Tab hi output HIGH hota hai

**Q2.** AND gate switches mein series ya parallel?
> Answer: Series mein — dono close ho tab hi current flow karta hai

**Q3.** Real life mein AND logic ka ek safety example?
> Answer: Nuclear launch — 2 officers 2 keys ek saath ghoomayein tab hi missile



---

## Completion Checklist

- `[ ]` Understood the theory behind AND Logic Game
- `[ ]` Successfully built and tested the project
- `[ ]` Wrote observations in notebook
- `[ ]` Can explain the working principle
- `[ ]` Completed the quiz
