# Session 02: C++ Variables and Data Types

**Class 5 – AI TRACK**  
Tier Curriculum | Connect Shiksha

![C++ Variables and Data Types](https://images.unsplash.com/photo-1581092160607-ee22621dd758?w=800&auto=format&fit=crop&q=80)

> **Session 02** | 80 Minutes | AI Track

---

## Class Schedule (80 Minutes)

| Time | Activity | Focus |
|:---|:---|:---|
| **0-20 min** | Theory | Learn how to declare int, float, char, and bool variables fo... |
| **20-65 min** | Practical Lab | Hands-on building and testing |
| **65-75 min** | Debug & Fix | Troubleshoot and improve |
| **75-80 min** | Quick Quiz | 3-question knowledge check |

**Keywords:** `Variables` | `int` | `float` | `bool` | `char`

---

## Theory (20 Minutes)

### Core Concept
Learn how to declare int, float, char, and bool variables for sensor data.

### Component Specifications
* **Key Device:** C++ Variables and Data Types
* **Usage Parameter:** Variables / int / float / bool / char

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

**Q2.** What is the purpose of `Variables`?
> Answer: It acts as the key parameter for control and calibration in today's setup.

**Q3.** Name a real-world application of this session's project.
> Answer: Smart automation, aerospace tracking, or local control grids.
