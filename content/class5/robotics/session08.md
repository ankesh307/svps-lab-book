# Session 08: IR Obstacle Sensor (Burglar Alarm)

**Class 5 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

![IR Obstacle Sensor (Burglar Alarm)](https://images.unsplash.com/photo-1517055720413-77a282b11dd9?w=800&auto=format&fit=crop&q=80)

> **Session 08** | 80 Minutes | ROBOTICS Track

---

## Class Schedule (80 Minutes)

| Time | Activity | Focus |
|:---|:---|:---|
| **0-20 min** | Theory | Use an IR sensor to detect movement and sound a burglar warn... |
| **20-65 min** | Practical Lab | Hands-on building and testing |
| **65-75 min** | Debug & Fix | Troubleshoot and improve |
| **75-80 min** | Quick Quiz | 3-question knowledge check |

**Keywords:** `IR Sensor` | `Obstacle Detect` | `Burglar Alarm`

---

## Theory (20 Minutes)

### Core Concept
Use an IR sensor to detect movement and sound a burglar warning alarm.

### Component Specifications
* **Key Device:** IR Obstacle Sensor (Burglar Alarm)
* **Usage Parameter:** IR Sensor / Obstacle Detect / Burglar Alarm

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
// C++ Arduino Code
#include <Servo.h>
Servo myServo;

void setup() {
    Serial.begin(9600);
    myServo.attach(9);
    pinMode(13, OUTPUT);
}

void loop() {
    myServo.write(90);
    digitalWrite(13, HIGH);
    delay(1000);
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

**Q2.** What is the purpose of `IR Sensor`?
> Answer: It acts as the key parameter for control and calibration in today's setup.

**Q3.** Name a real-world application of this session's project.
> Answer: Smart automation, aerospace tracking, or local control grids.
