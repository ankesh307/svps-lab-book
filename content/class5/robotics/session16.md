# Session 16: Bluetooth Module (HC-05) Serial Setup

**Class 5 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

![Bluetooth Module (HC-05) Serial Setup](https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&auto=format&fit=crop&q=80)

> **Session 16** | 80 Minutes | ROBOTICS Track

---

## Class Schedule (80 Minutes)

| Time | Activity | Focus |
|:---|:---|:---|
| **0-20 min** | Theory | Establish serial communication between Arduino and a phone v... |
| **20-65 min** | Practical Lab | Hands-on building and testing |
| **65-75 min** | Debug & Fix | Troubleshoot and improve |
| **75-80 min** | Quick Quiz | 3-question knowledge check |

**Keywords:** `HC-05 Bluetooth` | `Serial Communication` | `Baud Rate 9600`

---

## Theory (20 Minutes)

### Core Concept
Establish serial communication between Arduino and a phone via HC-05 bluetooth.

### Component Specifications
* **Key Device:** Bluetooth Module (HC-05) Serial Setup
* **Usage Parameter:** HC-05 Bluetooth / Serial Communication / Baud Rate 9600

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

**Q2.** What is the purpose of `HC-05 Bluetooth`?
> Answer: It acts as the key parameter for control and calibration in today's setup.

**Q3.** Name a real-world application of this session's project.
> Answer: Smart automation, aerospace tracking, or local control grids.
