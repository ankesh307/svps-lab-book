# Session 18: Servo Motor Intro

**Class 4: Breadboards, Arduino Basics & Sensors**  
Tier 2 - Smart Coders | Tier 2 Kit

![Servo Motor Intro](https://images.unsplash.com/photo-1553406830-ef2513450d76?w=800&auto=format&fit=crop&q=80)

> **Session 18** | 80 Minutes | Tier 2 - Smart Coders

---

## Class Schedule (80 Minutes)

| Time | Activity | Focus |
|:---|:---|:---|
| **0-20 min** | Theory | Servo.h library attach() write() 0-180 degrees sweep ka... |
| **20-65 min** | Practical Lab | Hands-on building and testing |
| **65-75 min** | Debug & Fix | Troubleshoot and improve |
| **75-80 min** | Quick Quiz | 3-question knowledge check |

**Keywords:** `Servo.h` | `attach()` | `write()` | `0-180` | `Sweep`

---

## Theory (20 Minutes)

### What Makes Servo Special?
Regular DC Motor: Freely spins, no position control
**Servo Motor**: EXACTLY rotates to commanded ANGLE!

**Inside a Servo:**
```
[DC Motor] + [Gear Box] + [Potentiometer] + [Control Circuit]
     ↑              ↑              ↑               ↑
  Power        Speed reduce   Position feedback  Error correction
```

**PWM Signal Control:**
Servo reads PWM (Pulse Width Modulation) signals:
```
1.0ms pulse → 0° (full left)
1.5ms pulse → 90° (center)
2.0ms pulse → 180° (full right)
```

**Arduino Servo Library:**
The Servo.h library handles all PWM timing automatically!
You just write: `myServo.write(90);` → Servo goes to 90°!

**Real-World Uses:**
- Robot arm joints
- RC car steering
- Camera pan/tilt systems
- Airplane control surfaces

---

## Practical Lab (45 Minutes)

### Components:
- Arduino Uno
- SG90 Servo Motor
- Jumper Wires (M-F)
- USB Cable

### Servo Pin Identification:
```
Orange/Yellow wire = PWM Signal (Arduino pin 9)
Red wire = VCC (5V)
Brown/Black wire = GND
```

### Wiring:
```
Servo Orange → Arduino Pin 9
Servo Red → Arduino 5V
Servo Brown → Arduino GND
```

### Code: Servo Sweep 0° to 180°:
```cpp
#include <Servo.h>

Servo myServo;

void setup() {
    myServo.attach(9);  // Servo on pin 9
    Serial.begin(9600);
}

void loop() {
    // Sweep from 0 to 180
    for (int angle = 0; angle <= 180; angle++) {
        myServo.write(angle);
        Serial.print("Angle: ");
        Serial.println(angle);
        delay(15);
    }
    
    // Sweep back from 180 to 0
    for (int angle = 180; angle >= 0; angle--) {
        myServo.write(angle);
        delay(15);
    }
}
```

## Code

```cpp
#include <Servo.h>

Servo myServo;  // Create servo object

void setup() {
    myServo.attach(9);  // Attach servo to pin 9
    Serial.begin(9600);
    Serial.println("Servo Motor Ready!");
    myServo.write(0);   // Start at 0 degrees
    delay(500);
}

void loop() {
    // Sweep from 0 to 180 degrees
    for (int pos = 0; pos <= 180; pos += 1) {
        myServo.write(pos);
        Serial.print("Position: ");
        Serial.print(pos);
        Serial.println(" degrees");
        delay(15);
    }
    delay(500);
    
    // Return to 0
    for (int pos = 180; pos >= 0; pos -= 1) {
        myServo.write(pos);
        delay(15);
    }
    delay(500);
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

**Q1.** Servo motor regular DC motor se alag kyun hai?
> Answer: Servo exact angle par ruk sakta hai — position control hoti hai

**Q2.** SG90 servo ke 3 wires ka kya kaam hai?
> Answer: Orange = PWM signal, Red = 5V power, Brown/Black = GND

**Q3.** myServo.write(90) kya karta hai?
> Answer: Servo ko exactly 90 degree (center position) par le jaata hai



---

## Completion Checklist

- `[ ]` Understood the theory behind Servo Motor Intro
- `[ ]` Successfully built and tested the project
- `[ ]` Wrote observations in notebook
- `[ ]` Can explain the working principle
- `[ ]` Completed the quiz
