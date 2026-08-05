# Session 14: Basic Auth verification

**Class 7 – AI TRACK**  
Tier Curriculum | Connect Shiksha

![Basic Auth verification](https://images.unsplash.com/photo-1581092160607-ee22621dd758?w=800&auto=format&fit=crop&q=80)

> **Session 14** | 80 Minutes | AI Track

---

## Class Schedule (80 Minutes)

| Time | Activity | Focus |
|:---|:---|:---|
| **0-20 min** | Theory | Checking client base64 auth headers to allow server access.... |
| **20-65 min** | Practical Lab | Hands-on building and testing |
| **65-75 min** | Debug & Fix | Troubleshoot and improve |
| **75-80 min** | Quick Quiz | 3-question knowledge check |

**Keywords:** `Basic Auth` | `Base64 login` | `HTTP security`

---

## Theory (20 Minutes)

### Core Concept
Checking client base64 auth headers to allow server access.

### Component Specifications
* **Key Device:** Basic Auth verification
* **Usage Parameter:** Basic Auth / Base64 login / HTTP security

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

```python
# Python OpenCV AI Tracking Script
import cv2
import serial

ser = serial.Serial('COM3', 9600)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    # Apply color masking or face detection
    # Send control values to Serial COM
    ser.write(b'MOVE_LEFT\n')
    cv2.imshow('AI Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
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

**Q2.** What is the purpose of `Basic Auth`?
> Answer: It acts as the key parameter for control and calibration in today's setup.

**Q3.** Name a real-world application of this session's project.
> Answer: Smart automation, aerospace tracking, or local control grids.
