# Session 04: First Blink Code

**Class 4: Breadboards, Arduino Basics & Sensors**  
Tier 2 - Smart Coders | Tier 2 Kit

![First Blink Code](https://images.unsplash.com/photo-1553406830-ef2513450d76?w=800&auto=format&fit=crop&q=80)

> **Session 04** | 80 Minutes | Tier 2 - Smart Coders

---

## Class Schedule (80 Minutes)

| Time | Activity | Focus |
|:---|:---|:---|
| **0-20 min** | Theory | Arduino ka pehla sketch LED_BUILTIN ko blink karwao set... |
| **20-65 min** | Practical Lab | Hands-on building and testing |
| **65-75 min** | Debug & Fix | Troubleshoot and improve |
| **75-80 min** | Quick Quiz | 3-question knowledge check |

**Keywords:** `Blink` | `setup()` | `loop()` | `LED_BUILTIN`

---

## Theory (20 Minutes)

### Arduino Programming Basics
Arduino programs ko **Sketch** kehte hain.
Every sketch mein 2 required functions hote hain:

```cpp
void setup() {
    // Runs ONCE at startup
    // Pin modes, initial settings
}

void loop() {
    // Runs FOREVER (repeat)
    // Main program logic
}
```

**Key Functions:**
- `pinMode(pin, mode)` → Pin ko INPUT ya OUTPUT set karo
- `digitalWrite(pin, value)` → Pin HIGH (5V) ya LOW (0V) karo
- `delay(ms)` → Program ko ms milliseconds ke liye rok do

**LED_BUILTIN:**
Arduino Uno mein Pin 13 par built-in LED hota hai!
Hum isse seedha code se control kar sakte hain.

**Blink Logic:**
```
LED ON (HIGH) → wait 1 second → LED OFF (LOW) → wait 1 second → repeat
```

---

## Practical Lab (45 Minutes)

### Step-by-Step First Blink!

### Hardware Setup:
Arduino Uno ko laptop se USB cable se connect karo.

### Arduino IDE Setup:
1. Tools → Board → Arduino Uno
2. Tools → Port → COMx (check Device Manager)
3. Click ✓ (Verify) phir → (Upload)

### Code:
```cpp
void setup() {
    pinMode(LED_BUILTIN, OUTPUT);
    // LED_BUILTIN = Pin 13
}

void loop() {
    digitalWrite(LED_BUILTIN, HIGH);  // LED ON
    delay(1000);                       // 1 second
    digitalWrite(LED_BUILTIN, LOW);   // LED OFF
    delay(1000);                       // 1 second
}
```

### Experiment:
- delay(1000) → 1 second blink
- delay(500) → Fast blink
- delay(100) → Very fast blink (strobe!)
- delay(2000) → Slow blink

### Upload aur observe!

## Code

```cpp
void setup() {
    // LED_BUILTIN = Pin 13 on Arduino Uno
    pinMode(LED_BUILTIN, OUTPUT);
    Serial.begin(9600);
    Serial.println("Arduino Blink Started!");
}

void loop() {
    digitalWrite(LED_BUILTIN, HIGH);   // Turn LED ON
    Serial.println("LED: ON");
    delay(1000);                        // Wait 1 second
    
    digitalWrite(LED_BUILTIN, LOW);    // Turn LED OFF
    Serial.println("LED: OFF");
    delay(1000);                        // Wait 1 second
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

**Q1.** Arduino sketch mein 2 required functions kaun se hain?
> Answer: setup() — ek baar chalta hai, aur loop() — hamesha repeat hota hai

**Q2.** delay(500) kitne time ke liye program rokta hai?
> Answer: 500 milliseconds = 0.5 seconds

**Q3.** LED_BUILTIN Arduino Uno mein kaun sa pin hai?
> Answer: Pin 13



---

## Completion Checklist

- `[ ]` Understood the theory behind First Blink Code
- `[ ]` Successfully built and tested the project
- `[ ]` Wrote observations in notebook
- `[ ]` Can explain the working principle
- `[ ]` Completed the quiz
