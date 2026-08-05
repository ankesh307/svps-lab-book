# Session 01: Transition to Text Coding (C++ in Arduino IDE)

**Class 5 – AI TRACK**  
Tier Curriculum | Connect Shiksha

![Transition to Text Coding (C++ in Arduino IDE)](https://images.unsplash.com/photo-1553406830-ef2513677491?w=800&auto=format&fit=crop&q=80)

> **Session 01** | 80 Minutes | AI Track

---

## Class Schedule (80 Minutes)

| Time | Activity | Focus |
|:---|:---|:---|
| **0-20 min** | Theory | Compare visual blocks vs text-based syntax, semicolon rules,... |
| **20-65 min** | Practical Lab | Hands-on building and testing |
| **65-75 min** | Debug & Fix | Troubleshoot and improve |
| **75-80 min** | Quick Quiz | 3-question knowledge check |

**Keywords:** `C++ Text` | `Semicolon Rule` | `Syntax Intro`

---

## Theory (20 Minutes)

### Core Concept
Compare visual blocks vs text-based syntax, semicolon rules, and brace matching.

### Component Specifications
* **Key Device:** Transition to Text Coding (C++ in Arduino IDE)
* **Usage Parameter:** C++ Text / Semicolon Rule / Syntax Intro

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
// C++ Corgi API Parsing Logic
#include <Arduino.h>
void setup() {
    Serial.begin(9600);
}
void loop() {
    if(Serial.available() > 0) {
        String gesture = Serial.readStringUntil('\n');
        if(gesture == "hand_up") {
            // Turn on LED
        }
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

**Q2.** What is the purpose of `C++ Text`?
> Answer: It acts as the key parameter for control and calibration in today's setup.

**Q3.** Name a real-world application of this session's project.
> Answer: Smart automation, aerospace tracking, or local control grids.
