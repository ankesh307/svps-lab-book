# Session 10: Potentiometer Dial

**Class 4: Breadboards, Arduino Basics & Sensors**  
Tier 2 - Smart Coders | Tier 2 Kit

![Potentiometer Dial](https://images.unsplash.com/photo-1553406830-ef2513450d76?w=800&auto=format&fit=crop&q=80)

> **Session 10** | 80 Minutes | Tier 2 - Smart Coders

---

## Class Schedule (80 Minutes)

| Time | Activity | Focus |
|:---|:---|:---|
| **0-20 min** | Theory | 10K pot A0 pin se analogRead 0-1023 values Serial Monit... |
| **20-65 min** | Practical Lab | Hands-on building and testing |
| **65-75 min** | Debug & Fix | Troubleshoot and improve |
| **75-80 min** | Quick Quiz | 3-question knowledge check |

**Keywords:** `Potentiometer` | `analogRead` | `A0` | `0-1023`

---

## Theory (20 Minutes)

### What is a Potentiometer?
Potentiometer = Variable Resistor (Knob wala)

**Internal Structure:**
```
Pin 1 ─── [Resistive Track] ─── Pin 3
                 ↑
           Pin 2 (Wiper)
           moves along track
```

- Turn LEFT → Wiper resistance decreases toward Pin 1 → Low voltage output
- Turn RIGHT → Wiper resistance increases → High voltage output

**Analog vs Digital:**
```
Digital: Only 0 or 1 (LOW or HIGH)
Analog:  0 to 5V (any value in between!)
```

**Arduino analogRead():**
```
analogRead(A0) returns 0 to 1023
0 = 0V, 1023 = 5V (10-bit ADC)
```

**Voltage Formula:**
```
Voltage = (analogRead value / 1023) × 5V
```

---

## Practical Lab (45 Minutes)

### Components:
- Arduino Uno
- 10K Potentiometer
- Jumper Wires (M-M and M-F)
- Laptop with Arduino IDE

### Wiring:
```
Potentiometer:
  Left Pin (1) → Arduino 5V
  Middle Pin (2) → Arduino A0 (Analog input)
  Right Pin (3) → Arduino GND
```

### Code: Read & Display Potentiometer
```cpp
void setup() {
    Serial.begin(9600);
    Serial.println("Potentiometer Test Started!");
}

void loop() {
    int potValue = analogRead(A0);  // 0-1023
    float voltage = potValue * (5.0 / 1023.0);
    
    Serial.print("Raw Value: ");
    Serial.print(potValue);
    Serial.print(" | Voltage: ");
    Serial.print(voltage, 2);
    Serial.println("V");
    
    delay(200);
}
```

### Open Serial Monitor (Ctrl+Shift+M)
Slowly turn the knob and watch values change!

## Code

```cpp
void setup() {
    Serial.begin(9600);
    Serial.println("=== Potentiometer Test ===");
    Serial.println("Turn the knob slowly...");
}

void loop() {
    int rawValue = analogRead(A0);
    float voltage = rawValue * (5.0 / 1023.0);
    
    // Map to percentage
    int percent = map(rawValue, 0, 1023, 0, 100);
    
    Serial.print("Value: ");
    Serial.print(rawValue);
    Serial.print(" | Voltage: ");
    Serial.print(voltage, 2);
    Serial.print("V | Level: ");
    Serial.print(percent);
    Serial.println("%");
    
    delay(200);  // Update every 200ms
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

**Q1.** analogRead() function ki return value range kya hai?
> Answer: 0 to 1023 (10-bit ADC — 2^10 = 1024 values)

**Q2.** Potentiometer ka middle pin kya output deta hai?
> Answer: Variable voltage — knob position ke anusaar 0V se 5V tak

**Q3.** analogRead(A0) = 512 to kitne volt correspond karta hai?
> Answer: 512/1023 × 5V ≈ 2.5V — exactly half voltage



---

## Completion Checklist

- `[ ]` Understood the theory behind Potentiometer Dial
- `[ ]` Successfully built and tested the project
- `[ ]` Wrote observations in notebook
- `[ ]` Can explain the working principle
- `[ ]` Completed the quiz
