# Session 19: Security Box

**Class 2: Fun with Electronics & Mechanics**  
Tier 1 - Junior Makers | Tier 1 Kit

![Security Box](https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80)

> **Session 19** | 80 Minutes | Tier 1 - Junior Makers

---

## Class Schedule (80 Minutes)

| Time | Activity | Focus |
|:---|:---|:---|
| **0-20 min** | Theory | Box khulne par automatically alarm bajao — tilt switch ... |
| **20-65 min** | Practical Lab | Hands-on building and testing |
| **65-75 min** | Debug & Fix | Troubleshoot and improve |
| **75-80 min** | Quick Quiz | 3-question knowledge check |

**Keywords:** `Tilt switch kaise kaam karta hai?` | `Andar ek ball hoti hai — tilt hone par ball contacts ko touch karti hai — circuit complete!`

---

## Theory (20 Minutes)

### Security System Concept
Real burglar alarms isi principle par kaam karte hain:
```
Normal state: Circuit OPEN → No alarm
Intrusion: Circuit CLOSES → ALARM!
```

**Types of Security Sensors:**
- **Magnetic Reed Switch**: Door/window frame par magnet + switch
- **IR Beam**: Beam toot jaaye → alarm
- **Pressure Sensor**: Floor par paon rakha → alarm
- **Tilt Switch**: Box/door khulne par → alarm (YEH AAJA BANAYENGE!)

**Tilt Switch Working:**
```
Tilt Switch = Small ball inside a cylinder
Upright: Ball at bottom = No contact = OPEN
Tilted: Ball rolls to side = Touches contacts = CLOSED!
```

---

## Practical Lab (45 Minutes)

### Build the Security Box!

### Version 1 — Tilt Switch Method:
Materials: Small box, tilt switch (or DIY with ball bearing), buzzer, 9V battery

**Wiring:**
```
Battery(+) → Tilt Switch → Buzzer(+)
Buzzer(−) → Battery(−)
```

**Setup:**
1. Tilt switch inside box ke LID par glue karo
2. Lid CLOSED (normal position) → tilt switch OPEN → No alarm
3. Lid OPEN → tilt switch TILTS → CLOSES → BUZZER ALARMS!

### Version 2 — DIY with Paperclip:
Lid ek paperclip se connected hai. Lid open → paperclip circuit complete → buzzer!

### Creative Add-ons:
- Tin box mein valuables rakhna design karo
- Decorate as a "Treasure Chest"
- Add an LED indicator along with buzzer



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

**Q1.** Tilt switch kaise kaam karta hai?
> Answer: Andar ek ball hoti hai — tilt hone par ball contacts ko touch karti hai — circuit complete!

**Q2.** Security box normally circuit open rakhta hai ya closed?
> Answer: Open — sirf box khulne par (tilt) close hota hai aur alarm bajta hai

**Q3.** Real burglar alarm mein kaun sa sensor sabse common hai?
> Answer: Magnetic reed switch — door/window frame par magnet + switch pair



---

## Completion Checklist

- `[ ]` Understood the theory behind Security Box
- `[ ]` Successfully built and tested the project
- `[ ]` Wrote observations in notebook
- `[ ]` Can explain the working principle
- `[ ]` Completed the quiz
