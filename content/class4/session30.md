# Session 30: Troubleshooting

**Class 4: Breadboards, Arduino Basics & Sensors**  
Tier 2 - Smart Coders | Tier 2 Kit

![Troubleshooting](https://images.unsplash.com/photo-1553406830-ef2513450d76?w=800&auto=format&fit=crop&q=80)

> **Session 30** | 80 Minutes | Tier 2 - Smart Coders

---

## Class Schedule (80 Minutes)

| Time | Activity | Focus |
|:---|:---|:---|
| **0-20 min** | Theory | Teacher ne bug daala — systematic debugging se fault fi... |
| **20-65 min** | Practical Lab | Hands-on building and testing |
| **65-75 min** | Debug & Fix | Troubleshoot and improve |
| **75-80 min** | Quick Quiz | 3-question knowledge check |

**Keywords:** `Debug` | `Fault Finding` | `Systematic` | `Fix` | `Problem`

---

## Theory (20 Minutes)

### Systematic Debugging — The Engineer's Mindset

**The Scientific Method for Bugs:**
1. **Observe**: Kya problem hai? (LED nahi jal raha, code upload nahi hota, etc.)
2. **Hypothesize**: Possible causes socho
3. **Test**: Ek ek karke check karo
4. **Conclude**: Issue find karo aur fix karo

**Common Hardware Bugs:**
| Problem | Possible Cause |
|---|---|
| LED nahi jal raha | LED reversed, loose wire, burnt LED, no power |
| Code upload nahi hota | Wrong COM port, USB issue, wrong board selected |
| Sensor random values | Loose connection, floating pin |
| Everything off | Battery dead, power rail not connected |

**Debugging Tools:**
- Serial Monitor (data check)
- Multimeter (voltage check)
- LED test (circuit check)
- Code blink (is Arduino alive?)

---

## Practical Lab (45 Minutes)

### Bug Hunt Challenge!

### Teacher Setup (Secret!):
Teacher mein 5 circuits mein intentional bugs daale hain:
1. LED legs reversed (polarity)
2. Resistor missing
3. Wrong COM port
4. Loose power wire
5. LED and resistor in wrong order

### Student Task:
Each group gets ONE buggy circuit. Find the bug in 10 minutes!

### Debugging Protocol:
```
Step 1: Check power — Battery connected? Rails connected?
Step 2: Check components — LED polarity correct?
Step 3: Check wires — Any loose connections?
Step 4: Check code — COM port? Board type?
Step 5: Use Serial Monitor — Any output?
```

### Scoring:
| Found bug in | Points |
|---|---|
| < 3 minutes | 100 |
| 3-7 minutes | 75 |
| 7-10 minutes (with hint) | 50 |

### Present your debugging process to class!

## Code

```cpp
// Debugging Helper Code
void setup() {
    Serial.begin(9600);
    Serial.println("=== System Check ===");
    
    // Test all digital pins
    for (int pin = 2; pin <= 13; pin++) {
        pinMode(pin, OUTPUT);
        digitalWrite(pin, HIGH);
        delay(100);
        digitalWrite(pin, LOW);
    }
    Serial.println("Pin test complete!");
    
    // Test analog pins
    Serial.println("Analog readings:");
    for (int pin = A0; pin <= A5; pin++) {
        Serial.print("A");
        Serial.print(pin - A0);
        Serial.print(": ");
        Serial.println(analogRead(pin));
    }
    Serial.println("=== Debug Complete ===");
}

void loop() {
    // Keep alive signal
    Serial.println("Arduino is alive!");
    delay(2000);
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

**Q1.** Systematic debugging mein pehla step kya hai?
> Answer: Observe — problem ko clearly define karo pehle

**Q2.** LED nahi jal raha — sab se pehle kya check karenge?
> Answer: Power connection, LED polarity (long leg = +), aur resistor presence

**Q3.** Code upload nahi ho raha — kya check karoge?
> Answer: Tools > Port mein correct COM port, Tools > Board mein Arduino Uno selected



---

## Completion Checklist

- `[ ]` Understood the theory behind Troubleshooting
- `[ ]` Successfully built and tested the project
- `[ ]` Wrote observations in notebook
- `[ ]` Can explain the working principle
- `[ ]` Completed the quiz
