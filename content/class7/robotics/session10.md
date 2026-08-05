# Session 10: Quad Motor CW/CCW map

**Class 7 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

![Quad Motor CW/CCW map](https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80)

> **Session 10** | 80 Minutes | ROBOTICS Track

---

## Class Schedule (80 Minutes)

| Time | Activity | Focus |
|:---|:---|:---|
| **0-20 min** | Theory | Configure clockwise and counter-clockwise motor distribution... |
| **20-65 min** | Practical Lab | Hands-on building and testing |
| **65-75 min** | Debug & Fix | Troubleshoot and improve |
| **75-80 min** | Quick Quiz | 3-question knowledge check |

**Keywords:** `Motor mapping` | `CW/CCW rotation` | `Propellers`

---

## Theory (20 Minutes)

### Core Concept
Configure clockwise and counter-clockwise motor distributions.

### Component Specifications
* **Key Device:** Quad Motor CW/CCW map
* **Usage Parameter:** Motor mapping / CW/CCW rotation / Propellers

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
// NodeMCU ESP8266 Wi-Fi Robot Code
#include <ESP8266WiFi.h>
#include <ESP8266WebServer.h>

ESP8266WebServer server(80);

void handleRoot() {
    server.send(200, "text/html", "<h1>ESP8266 Web Robot Active!</h1>");
}

void setup() {
    WiFi.begin("SSID", "PASSWORD");
    server.on("/", handleRoot);
    server.begin();
}

void loop() {
    server.handleClient();
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

**Q2.** What is the purpose of `Motor mapping`?
> Answer: It acts as the key parameter for control and calibration in today's setup.

**Q3.** Name a real-world application of this session's project.
> Answer: Smart automation, aerospace tracking, or local control grids.
