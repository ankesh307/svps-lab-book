# Session 01: Breadboard Intro

**Class 4: Breadboards, Arduino Basics & Sensors**  
Tier 2 - Smart Coders | Tier 2 Kit

![Breadboard Intro](https://images.unsplash.com/photo-1553406830-ef2513450d76?w=800&auto=format&fit=crop&q=80)

> **Session 01** | 80 Minutes | Tier 2 - Smart Coders

---

## Class Schedule (80 Minutes)

| Time | Activity | Focus |
|:---|:---|:---|
| **0-20 min** | Theory | Breadboard rows rails internal connections samjho LED w... |
| **20-65 min** | Practical Lab | Hands-on building and testing |
| **65-75 min** | Debug & Fix | Troubleshoot and improve |
| **75-80 min** | Quick Quiz | 3-question knowledge check |

**Keywords:** `Breadboard` | `Rows` | `Power Rail` | `No Solder`

---

## Theory (20 Minutes)

### What is a Breadboard?
Breadboard ek **solderless prototyping board** hai. Yahan hum wires aur components TEMPORARILY connect kar sakte hain — solder kiye bina!

**Breadboard Internal Connections:**
```
Horizontal rows (1-30):
a b c d e | f g h i j
─────────────────────
Each horizontal row is INTERNALLY connected!
Pin 1a connects to 1b, 1c, 1d, 1e (same node)

Vertical power rails (sides):
Red (+) strip: All connected together
Blue (−) strip: All connected together
```

**Rules:**
- Component ke ek leg ek row mein, doosra leg DIFFERENT row mein
- Never jump wires across the center gap!
- Power rails side mein hain — components middle mein!

---

## Practical Lab (45 Minutes)

### Breadboard Practice!

### Exercise 1 — LED Test:
```
Connect:
- Red wire: Power rail (+) → Row 10, column (a)
- LED: Long leg → Row 10 (b), Short leg → Row 12 (b)
- Resistor: Row 12 (c) → Row 14 (c)
- Black wire: Row 14 (d) → Power rail (−)
- Connect 9V battery to power rails
```
LED jalta hai!

### Exercise 2 — Identify Connections:
Teacher will set up a mystery circuit. Students must draw which rows are connected.

### Breadboard Diagram Practice:
Draw the following on paper:
```
+Rail: [───────────────]
       [a b c d e|f g h]
Row1:  [○ ○ ○ ○ ○|○ ○ ○]  ← Row 1 (internally connected left side, right side separate)
Row2:  [○ ○ ○ ○ ○|○ ○ ○]
...
-Rail: [───────────────]
```

## Code

```cpp
// No code needed for this session — hardware only!
// But here's a preview of what Arduino can do:
void setup() {
    pinMode(13, OUTPUT);  // Pin 13 as OUTPUT
}
void loop() {
    digitalWrite(13, HIGH);  // Turn LED ON
    delay(1000);
    digitalWrite(13, LOW);   // Turn LED OFF  
    delay(1000);
}
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

**Q1.** Breadboard ki ek row mein kaun kaun se holes internally connected hain?
> Answer: Ek row ke a,b,c,d,e sab connected hain (left side); f,g,h,i,j alag (right side)

**Q2.** Breadboard mein solder kyun nahi karna padta?
> Answer: Holes mein metal clips hain — component legs ya wires push karne par friction se contact ban jaata hai

**Q3.** Breadboard mein + aur − rails kahan hoti hain?
> Answer: Sides par — vertical red (+) strip aur blue (−) strip



---

## Completion Checklist

- `[ ]` Understood the theory behind Breadboard Intro
- `[ ]` Successfully built and tested the project
- `[ ]` Wrote observations in notebook
- `[ ]` Can explain the working principle
- `[ ]` Completed the quiz
