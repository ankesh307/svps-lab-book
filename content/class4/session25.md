# Session 25: LCD Hello World

**Class 4: Breadboards, Arduino Basics & Sensors**  
Tier 2 - Smart Coders | Tier 2 Kit

![LCD Hello World](https://images.unsplash.com/photo-1553406830-ef2513450d76?w=800&auto=format&fit=crop&q=80)

> **Session 25** | 80 Minutes | Tier 2 - Smart Coders

---

## Class Schedule (80 Minutes)

| Time | Activity | Focus |
|:---|:---|:---|
| **0-20 min** | Theory | LiquidCrystal_I2C init backlight setCursor print Hello ... |
| **20-65 min** | Practical Lab | Hands-on building and testing |
| **65-75 min** | Debug & Fix | Troubleshoot and improve |
| **75-80 min** | Quick Quiz | 3-question knowledge check |

**Keywords:** `LCD` | `I2C` | `setCursor()` | `print()` | `Hello World`

---

## Theory (20 Minutes)

### LCD 16x2 Display
16 columns × 2 rows = 32 character display

**I2C Interface:**
Normal LCD ko 16 wires chahiye!
I2C module lagaane ke baad sirf 4 wires!

```
Normal LCD:    I2C LCD:
16 wires  →   4 wires (VCC, GND, SDA, SCL)
```

**I2C Protocol:**
```
SDA (Serial Data) = Data wire
SCL (Serial Clock) = Timing wire
```

**I2C Address:**
Each I2C device has a unique address (usually 0x27 or 0x3F for LCD)

**Library Required:**
Install "LiquidCrystal_I2C" from Arduino Library Manager

**LCD Coordinate System:**
```
(col, row)
(0,0) → Top-left corner
(15,0) → Top-right
(0,1) → Bottom-left
(15,1) → Bottom-right
```

---

## Practical Lab (45 Minutes)

### Components:
- Arduino Uno
- LCD 1602 with I2C module
- Jumper Wires (M-F)

### Wiring (I2C):
```
LCD GND → Arduino GND
LCD VCC → Arduino 5V
LCD SDA → Arduino A4 (SDA)
LCD SCL → Arduino A5 (SCL)
```

### Install Library First:
Tools → Manage Libraries → Search "LiquidCrystal I2C" → Install

### Code:
```cpp
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
    lcd.init();
    lcd.backlight();
    lcd.setCursor(0, 0);
    lcd.print("Hello, World!");
    lcd.setCursor(0, 1);
    lcd.print("Arduino Rocks!");
}

void loop() {
    // Static display — nothing in loop
}
```

### Challenge: Scrolling Text!
```cpp
void loop() {
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("Namaste India!");
    delay(2000);
}
```

## Code

```cpp
#include <Wire.h>
#include <LiquidCrystal_I2C.h>

// I2C address 0x27, 16 columns, 2 rows
LiquidCrystal_I2C lcd(0x27, 16, 2);

void setup() {
    lcd.init();          // Initialize LCD
    lcd.backlight();     // Turn on backlight
    
    // Row 1: Hello World
    lcd.setCursor(0, 0);
    lcd.print("Hello, World!");
    
    // Row 2: Your name
    lcd.setCursor(0, 1);
    lcd.print("Arduino Ready!");
    
    delay(3000);         // Show for 3 seconds
}

void loop() {
    // Alternating messages every 2 seconds
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("NextGen STEM");
    lcd.setCursor(0, 1);
    lcd.print("Class 4 Ready!");
    delay(2000);
    
    lcd.clear();
    lcd.setCursor(0, 0);
    lcd.print("I Love Coding!");
    lcd.setCursor(0, 1);
    lcd.print("  Arduino :) ");
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

**Q1.** LCD 16x2 mein kitne characters display ho sakte hain?
> Answer: 32 characters — 16 columns × 2 rows

**Q2.** I2C protocol mein kitni wires use hoti hain?
> Answer: 4 wires — VCC, GND, SDA (data), SCL (clock)

**Q3.** lcd.setCursor(5, 1) kahan cursor set karta hai?
> Answer: Column 5, Row 1 (second row, 6th position) par



---

## Completion Checklist

- `[ ]` Understood the theory behind LCD Hello World
- `[ ]` Successfully built and tested the project
- `[ ]` Wrote observations in notebook
- `[ ]` Can explain the working principle
- `[ ]` Completed the quiz
