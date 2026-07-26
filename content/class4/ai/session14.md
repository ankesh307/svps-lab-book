# Session 14: Keypad character matrix

**Class 4 – AI TRACK**  
Tier Curriculum | Connect Shiksha

![Keypad character matrix](https://images.unsplash.com/photo-1581092160607-ee22621dd758?w=800&auto=format&fit=crop&q=80)

> **Session 14** | 80 Minutes | AI Track

---

## Class Schedule (80 Minutes)

| Time | Activity | Focus |
|:---|:---|:---|
| **0-20 min** | Theory | Mapping matrix intersections to ASCII char outputs.... |
| **20-65 min** | Practical Lab | Hands-on building and testing |
| **65-75 min** | Debug & Fix | Troubleshoot and improve |
| **75-80 min** | Quick Quiz | 3-question knowledge check |

**Keywords:** `Keypad matrix` | `ASCII char` | `Intersections`

---

## Theory (20 Minutes)

### Core Concept
Mapping matrix intersections to ASCII char outputs.

### Component Specifications
* **Key Device:** Keypad character matrix
* **Usage Parameter:** Keypad matrix / ASCII char / Intersections

### Why it matters
Understanding this technology helps build systems that make a real difference in automation, industrial control, smart homes, and autonomous robotics.

---

## Practical Lab (45 Minutes)

### Step 1: Collect Components
Gather all necessary components for today's session.

### Step 2: Connection / Setup
Follow the block diagram and secure all cables. Ensure a stable connection.

### Step 3: Write Code
Here is the code structure for today:

```cpp
// C++ Logic Controls
void setup() {
    pinMode(2, INPUT_PULLUP);
    pinMode(13, OUTPUT);
}

void loop() {
    if(digitalRead(2) == LOW) {
        digitalWrite(13, HIGH);
    } else {
        digitalWrite(13, LOW);
    }
}
```

---

## Troubleshooting Guide

| Problem | Solution |
|:---|:---|
| No signal output | Check VCC and Ground rails configuration |
| Serial logs offline | Check connection rate (Baud mismatch) |
| System freezing | Clean compile variables, reset board |

---

## Quiz (5 Minutes)

**Q1.** Explain what you built today in your own words.

**Q2.** What is the purpose of `Keypad matrix`?
> Answer: It acts as the key parameter for control and calibration in today's setup.

**Q3.** Name a real-world application of this session's project.
> Answer: Smart automation, aerospace tracking, or local control grids.
