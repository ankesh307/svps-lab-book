# Class 2 Robotics Custom Override Content for Sessions 3-30
import os
import base64

def get_base64_image(image_filename):
    image_path = os.path.join(r"C:\Users\ankes\.gemini\antigravity\scratch\curriculum_app\images", image_filename)
    if os.path.exists(image_path):
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            return f"data:image/png;base64,{encoded_string}"
    return ""

# Reusable SVG Pointing Hand (Human Touch)
def get_hand_svg(x, y, label="Press/Connect"):
    return f"""
  <g transform="translate({x}, {y})">
    <!-- Click Ripple Animation -->
    <circle cx="0" cy="0" r="10" fill="none" stroke="#ef4444" stroke-width="2">
      <animate attributeName="r" values="6;20" dur="1.2s" repeatCount="indefinite"/>
      <animate attributeName="stroke-opacity" values="1;0" dur="1.2s" repeatCount="indefinite"/>
    </circle>
    <circle cx="0" cy="0" r="4" fill="#ef4444"/>
    <!-- Pointing Hand Vector -->
    <g transform="rotate(-30) translate(-10, -5)">
      <path d="M 0 10 L 0 25 C 0 28, 4 30, 8 30 C 12 30, 14 28, 14 25 L 14 12 C 14 10, 16 9, 17 9 C 19 9, 20 11, 20 12 L 20 18 C 20 19, 22 18, 23 18 C 24 18, 25 19, 25 20 L 25 25 C 25 32, 17 35, 10 35 L 6 35 C 0 35, -5 30, -5 24 L -5 10 C -5 7, -2 5, 0 5 C 2 5, 5 7, 5 10 L 5 18 L 0 18 Z" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
    </g>
    <rect x="-35" y="32" width="70" height="15" rx="3" fill="#ef4444"/>
    <text x="0" y="42" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">{label}</text>
  </g>
"""

def get_custom_session(num):
    s1 = get_base64_image("kit_overview.jpg")
    
    # Session 3: Battery Basics
    if num == 3:
        s2 = get_base64_image("battery_snap.jpg")
        s5 = get_base64_image("leds_buzzer.jpg")
        return f"""# Session 03: Battery Basics 🔋

**Class 2 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Introduction to Power Source
![Battery Overview]({s2})

> **Battery aur circuits ke electrical flow ka introductory guide**

---

## 📸 Slide 2: Anode vs Cathode
* **Positive Terminal (+):** Red wire (anode) current send karta hai.
* **Negative Terminal (-):** Black wire (cathode) current receive karta hai.
* **Voltage Flow:** 9V battery high voltage power supply karti hai jo LEDs aur motors ko directly chalati hai.

---

## 📸 Slide 3: Visual Circuit Diagram 🎨
<svg width="450" height="240" viewBox="0 0 450 240" style="display: block; margin: 20px auto; background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 12px; font-family: sans-serif;">
  <defs>
    <pattern id="grid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#f1f5f9" stroke-width="1"/>
    </pattern>
  </defs>
  <rect width="100%" height="100%" fill="url(#grid)" rx="12"/>
  
  <!-- 9V Battery -->
  <g transform="translate(40, 50)">
    <rect x="0" y="20" width="80" height="110" rx="8" fill="#1e293b" stroke="#0f172a" stroke-width="3"/>
    <rect x="15" y="5" width="20" height="15" fill="#cbd5e1" stroke="#94a3b8" stroke-width="2"/>
    <circle cx="25" cy="5" r="4" fill="#64748b"/>
    <rect x="45" y="5" width="20" height="15" fill="#cbd5e1" stroke="#94a3b8" stroke-width="2"/>
    <circle cx="55" cy="5" r="5" fill="#64748b"/>
    <text x="40" y="65" font-size="16" font-weight="bold" fill="#ffffff" text-anchor="middle">9V</text>
    <text x="40" y="85" font-size="11" fill="#94a3b8" text-anchor="middle">BATTERY</text>
    <!-- Terminal Labels with polarity signs -->
    <circle cx="25" cy="40" r="8" fill="#ef4444"/>
    <text x="25" y="44" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">+</text>
    <text x="25" y="60" font-size="8" fill="#ef4444" text-anchor="middle">Positive</text>
    <circle cx="55" cy="40" r="8" fill="#3b82f6"/>
    <text x="55" y="44" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">-</text>
    <text x="55" y="60" font-size="8" fill="#3b82f6" text-anchor="middle">Negative</text>
  </g>

  <!-- LED -->
  <g transform="translate(300, 50)">
    <!-- Legs -->
    <line x1="25" y1="90" x2="25" y2="150" stroke="#ef4444" stroke-width="4" stroke-linecap="round"/>
    <line x1="55" y1="90" x2="55" y2="135" stroke="#3b82f6" stroke-width="4" stroke-linecap="round"/>
    <rect x="15" y="80" width="50" height="10" rx="2" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="2"/>
    <path d="M 20 80 Q 20 20 40 20 Q 60 20 60 80 Z" fill="#10b981" fill-opacity="0.8" stroke="#047857" stroke-width="3"/>
    <circle cx="40" cy="50" r="30" fill="#10b981" fill-opacity="0.15" stroke="#10b981" stroke-opacity="0.3" stroke-width="2" stroke-dasharray="4,4"/>
    <text x="40" y="115" font-size="12" font-weight="bold" fill="#047857" text-anchor="middle">LED</text>
    <!-- Leg polarities -->
    <circle cx="25" cy="155" r="7" fill="#ef4444"/>
    <text x="25" y="159" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">+</text>
    <circle cx="55" cy="140" r="7" fill="#3b82f6"/>
    <text x="55" y="144" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">-</text>
  </g>

  <!-- Wires with flow markers -->
  <path d="M 65 55 L 65 30 L 325 30 L 325 50" fill="none" stroke="#ef4444" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="190" y="22" font-size="10" font-weight="bold" fill="#ef4444" text-anchor="middle">🔴 Red Wire (+ Positive Flow)</text>
  <path d="M 95 55 L 95 180 L 355 180 L 355 50" fill="none" stroke="#1e293b" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="220" y="195" font-size="10" font-weight="bold" fill="#1e293b" text-anchor="middle">⚫ Black Wire (- Return Loop)</text>
  
  {get_hand_svg(325, 90, "Connect +")}
</svg>

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 🔴 **Red Wire (Positive Connection):** Battery snap ke **Red Wire (+)** ko LED ke **Long Leg (+)** se direct connect karein.
* ⚫ **Black Wire (Negative Connection):** Battery snap ke **Black Wire (-)** ko LED ke **Short Leg (-)** se connect karein.
* ⚡ **Glow Check:** Jaise hi dono wires connect honge, current flow start ho jayega aur LED chalegi!

---

## 📸 Slide 5: Student Task — Hands-On Practice
![LED Output]({s5})

1. **LED Glow Task:** Battery aur snap connector select karein. Wires ko LED se correct nodes me connect karke LED light ON karein.
2. **❓ Quiz Question:** LED ki kaunsi leg positive(+) hoti hai?
> **Answer:** Lambi leg (Longer lead) hamesha positive (+) hoti hai.
"""

    # Session 4: Open & Closed Circuit
    elif num == 4:
        s4 = get_base64_image("switches_buttons.jpg")
        s5 = get_base64_image("leds_buzzer.jpg")
        return f"""# Session 04: Open & Closed Circuit 🔌

**Class 2 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Loop and Switch Principle
![Rocker Switch]({s4})

> **Rocker switch se complete loop control check karna**

---

## 📸 Slide 2: Open vs Closed Loop
* **Closed Circuit (ON):** Loop continuous hai, current flow hota hai aur LED glow karti hai.
* **Open Circuit (OFF):** Loop broken hai, switch position circuit ko break karti hai jisse current flow ruk jata hai.

---

## 📸 Slide 3: Visual Circuit Diagram 🎨
<svg width="450" height="240" viewBox="0 0 450 240" style="display: block; margin: 20px auto; background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 12px; font-family: sans-serif;">
  <rect width="100%" height="100%" fill="#f8fafc" rx="12"/>
  
  <!-- 9V Battery -->
  <g transform="translate(20, 50)">
    <rect x="0" y="20" width="70" height="100" rx="8" fill="#1e293b" stroke="#0f172a" stroke-width="3"/>
    <text x="35" y="70" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">9V BATTERY</text>
    <circle cx="25" cy="45" r="7" fill="#ef4444"/>
    <text x="25" y="49" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">+</text>
    <circle cx="45" cy="45" r="7" fill="#3b82f6"/>
    <text x="45" y="49" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">-</text>
  </g>

  <!-- Rocker Switch -->
  <g transform="translate(160, 50)">
    <rect x="0" y="20" width="90" height="60" rx="6" fill="#3b82f6" stroke="#1d4ed8" stroke-width="3"/>
    <text x="45" y="55" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">SWITCH</text>
    <rect x="15" y="80" width="10" height="15" fill="#cbd5e1"/>
    <rect x="65" y="80" width="10" height="15" fill="#cbd5e1"/>
    <text x="20" y="110" font-size="9" fill="#64748b" text-anchor="middle">In</text>
    <text x="70" y="110" font-size="9" fill="#64748b" text-anchor="middle">Out</text>
  </g>

  <!-- LED -->
  <g transform="translate(340, 50)">
    <line x1="20" y1="80" x2="20" y2="130" stroke="#ef4444" stroke-width="4" stroke-linecap="round"/>
    <line x1="40" y1="80" x2="40" y2="115" stroke="#3b82f6" stroke-width="4" stroke-linecap="round"/>
    <path d="M 10 70 Q 10 20 30 20 Q 50 20 50 70 Z" fill="#ef4444" fill-opacity="0.8" stroke="#b91c1c" stroke-width="3"/>
    <text x="30" y="95" font-size="10" font-weight="bold" fill="#b91c1c" text-anchor="middle">LED</text>
    <circle cx="20" cy="135" r="7" fill="#ef4444"/>
    <text x="20" y="139" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">+</text>
    <circle cx="40" cy="120" r="7" fill="#3b82f6"/>
    <text x="40" y="124" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">-</text>
  </g>

  <!-- Connections -->
  <path d="M 45 50 L 45 25 L 175 25 L 175 50" fill="none" stroke="#ef4444" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M 225 50 L 225 25 L 360 25 L 360 50" fill="none" stroke="#eab308" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="295" y="18" font-size="10" font-weight="bold" fill="#eab308" text-anchor="middle">🟡 Yellow Wire (+)</text>
  <path d="M 65 50 L 65 150 L 380 150 L 380 50" fill="none" stroke="#1e293b" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  
  {get_hand_svg(205, 10, "Press Switch")}
</svg>

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 🔴 **Step 1:** Battery snap ke **Red Wire (+)** ko **Rocker Switch** ke Pin 1 par connect karein.
* 🟡 **Step 2:** Rocker Switch ke Pin 2 se ek **extra wire (Yellow)** lekar **LED ke Long Leg (+)** par connect karein.
* ⚫ **Step 3:** Battery snap ke **Black Wire (-)** ko directly **LED ke Short Leg (-)** par lagayein.
* 🔄 **Toggle Check:** Switch ON karne par current flow complete ho jayega aur light chalegi!

---

## 📸 Slide 5: Student Task — Hands-On Practice
![LED Toggle]({s5})

1. **ON/OFF Switch Loop:** Rocker switch ko series path me wire karein aur button toggle karke LED ON/OFF setup demonstrate karein.
2. **❓ Quiz Question:** Open circuit me current flow hota hai ya nahi?
> **Answer:** open circuit me path break hone ki wajah se current flow nahi hota.
"""

    # Session 5: Series Circuit
    elif num == 5:
        s5 = get_base64_image("leds_buzzer.jpg")
        return f"""# Session 05: Series Circuit 🔗

**Class 2 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Single Path Loop
![LEDs in Series]({s5})

> **2 LEDs ko end-to-end chain system me connect karna**

---

## 📸 Slide 2: Series Rules
* **Single Path:** Current flow hone ke liye sirf ek line/rasta hota hai.
* **Split Voltage:** 9V battery ka voltage dono LEDs me split ho jata hai, jisse LEDs thoda dim glow karti hain.
* **Failure Loop:** Agar ek LED nikal di jaye, toh poora circuit open ho jayega aur dusri LED bhi band ho jayegi.

---

## 📸 Slide 3: Visual Circuit Diagram 🎨
<svg width="450" height="240" viewBox="0 0 450 240" style="display: block; margin: 20px auto; background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 12px; font-family: sans-serif;">
  <rect width="100%" height="100%" fill="#f8fafc" rx="12"/>
  
  <!-- 9V Battery -->
  <g transform="translate(20, 50)">
    <rect x="0" y="20" width="70" height="100" rx="8" fill="#1e293b" stroke="#0f172a" stroke-width="3"/>
    <text x="35" y="70" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">9V BATTERY</text>
    <circle cx="25" cy="45" r="7" fill="#ef4444"/>
    <text x="25" y="49" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">+</text>
    <circle cx="45" cy="45" r="7" fill="#3b82f6"/>
    <text x="45" y="49" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">-</text>
  </g>

  <!-- LED 1 -->
  <g transform="translate(190, 50)">
    <line x1="20" y1="80" x2="20" y2="130" stroke="#ef4444" stroke-width="4"/>
    <line x1="40" y1="80" x2="40" y2="115" stroke="#3b82f6" stroke-width="4"/>
    <path d="M 10 70 Q 10 20 30 20 Q 50 20 50 70 Z" fill="#10b981" fill-opacity="0.8" stroke="#047857" stroke-width="3"/>
    <text x="30" y="95" font-size="10" font-weight="bold" fill="#047857" text-anchor="middle">LED 1</text>
    <circle cx="20" cy="135" r="7" fill="#ef4444"/>
    <text x="20" y="139" font-size="9" fill="#ffffff" text-anchor="middle">+</text>
    <circle cx="40" cy="120" r="7" fill="#3b82f6"/>
    <text x="40" y="124" font-size="9" fill="#ffffff" text-anchor="middle">-</text>
  </g>

  <!-- LED 2 -->
  <g transform="translate(320, 50)">
    <line x1="20" y1="80" x2="20" y2="130" stroke="#ef4444" stroke-width="4"/>
    <line x1="40" y1="80" x2="40" y2="115" stroke="#3b82f6" stroke-width="4"/>
    <path d="M 10 70 Q 10 20 30 20 Q 50 20 50 70 Z" fill="#a855f7" fill-opacity="0.8" stroke="#7e22ce" stroke-width="3"/>
    <text x="30" y="95" font-size="10" font-weight="bold" fill="#7e22ce" text-anchor="middle">LED 2</text>
    <circle cx="20" cy="135" r="7" fill="#ef4444"/>
    <text x="20" y="139" font-size="9" fill="#ffffff" text-anchor="middle">+</text>
    <circle cx="40" cy="120" r="7" fill="#3b82f6"/>
    <text x="40" y="124" font-size="9" fill="#ffffff" text-anchor="middle">-</text>
  </g>

  <!-- Connections -->
  <path d="M 45 50 L 45 25 L 210 25 L 210 50" fill="none" stroke="#ef4444" stroke-width="4" stroke-linejoin="round"/>
  
  <path d="M 230 50 L 230 150 L 340 150 L 340 50" fill="none" stroke="#3b82f6" stroke-width="4"/>
  <text x="285" y="165" font-size="10" font-weight="bold" fill="#3b82f6" text-anchor="middle">🔵 Blue Wire (Series Joint)</text>
  
  <path d="M 65 50 L 65 180 L 360 180 L 360 50" fill="none" stroke="#1e293b" stroke-width="4"/>
  
  {get_hand_svg(285, 90, "Wire here")}
</svg>

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 🔴 **Step 1:** Battery snap ke **Red Wire (+)** ko **LED 1 ke Long Leg (+)** par connect karein.
* 🔵 **Step 2 (Chain Connection):** **LED 1 ke Short Leg (-)** ko ek wire se **LED 2 ke Long Leg (+)** se connect karein.
* ⚫ **Step 3:** **LED 2 ke Short Leg (-)** ko battery snap ke **Black Wire (-)** se connect karein.
* 💡 **Observation:** Check karein ki single LED ke mukable dono LEDs ki light thodi dim (kam bright) hai ya nahi.

---

## 📸 Slide 5: Student Task — Hands-On Practice
1. **Series Chain Build:** 2 LEDs ko end-to-end connect karke loop complete karein aur single LED ke mukable brightness change check karein.
2. **❓ Quiz Question:** Series circuit me agar ek wire break ho jaye toh kya hoga?
> **Answer:** Pura circuit band ho jayega aur saare outputs OFF ho jayenge.
"""

    # Session 6: Parallel Circuit
    elif num == 6:
        s5 = get_base64_image("leds_buzzer.jpg")
        return f"""# Session 06: Parallel Circuit 🔀

**Class 2 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Multiple Path Nodes
![Parallel LEDs]({s5})

> **Independent path networks for multiple outputs**

---

## 📸 Slide 2: Parallel Rules
* **Multiple Paths:** Current flow hone ke liye har output ke pass apna rasta hota hai.
* **Equal Voltage:** Dono LEDs ko pura 9V power milta hai, isiliye dono full brightness me chalti hain.
* **Independent Nodes:** Ek LED disconnect karne par dusri LED band nahi hoti.

---

## 📸 Slide 3: Visual Circuit Diagram 🎨
<svg width="450" height="240" viewBox="0 0 450 240" style="display: block; margin: 20px auto; background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 12px; font-family: sans-serif;">
  <rect width="100%" height="100%" fill="#f8fafc" rx="12"/>
  
  <!-- 9V Battery -->
  <g transform="translate(20, 50)">
    <rect x="0" y="20" width="70" height="100" rx="8" fill="#1e293b" stroke="#0f172a" stroke-width="3"/>
    <text x="35" y="70" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">9V BATTERY</text>
    <circle cx="25" cy="45" r="7" fill="#ef4444"/>
    <text x="25" y="49" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">+</text>
    <circle cx="45" cy="45" r="7" fill="#3b82f6"/>
    <text x="45" y="49" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">-</text>
  </g>

  <!-- Junction Red -->
  <circle cx="170" cy="25" r="6" fill="#ef4444"/>
  <text x="170" y="15" font-size="9" font-weight="bold" fill="#ef4444" text-anchor="middle">Joint A (+)</text>

  <!-- Junction Black -->
  <circle cx="170" cy="150" r="6" fill="#1e293b"/>
  <text x="170" y="165" font-size="9" font-weight="bold" fill="#1e293b" text-anchor="middle">Joint B (-)</text>

  <!-- LED 1 -->
  <g transform="translate(230, 50)">
    <line x1="20" y1="80" x2="20" y2="130" stroke="#ef4444" stroke-width="4"/>
    <line x1="40" y1="80" x2="40" y2="115" stroke="#3b82f6" stroke-width="4"/>
    <path d="M 10 70 Q 10 20 30 20 Q 50 20 50 70 Z" fill="#10b981" fill-opacity="0.8" stroke="#047857" stroke-width="3"/>
    <text x="30" y="95" font-size="10" font-weight="bold" fill="#047857" text-anchor="middle">LED 1</text>
    <circle cx="20" cy="135" r="6" fill="#ef4444"/>
    <circle cx="40" cy="120" r="6" fill="#3b82f6"/>
  </g>

  <!-- LED 2 -->
  <g transform="translate(340, 50)">
    <line x1="20" y1="80" x2="20" y2="130" stroke="#ef4444" stroke-width="4"/>
    <line x1="40" y1="80" x2="40" y2="115" stroke="#3b82f6" stroke-width="4"/>
    <path d="M 10 70 Q 10 20 30 20 Q 50 20 50 70 Z" fill="#a855f7" fill-opacity="0.8" stroke="#7e22ce" stroke-width="3"/>
    <text x="30" y="95" font-size="10" font-weight="bold" fill="#7e22ce" text-anchor="middle">LED 2</text>
    <circle cx="20" cy="135" r="6" fill="#ef4444"/>
    <circle cx="40" cy="120" r="6" fill="#3b82f6"/>
  </g>

  <!-- Connections -->
  <path d="M 45 50 L 45 25 L 170 25" fill="none" stroke="#ef4444" stroke-width="4"/>
  <path d="M 170 25 L 250 25 L 250 50" fill="none" stroke="#ef4444" stroke-width="4"/>
  <path d="M 250 25 L 360 25 L 360 50" fill="none" stroke="#ef4444" stroke-width="4"/>

  <path d="M 270 50 L 270 150 L 170 150" fill="none" stroke="#1e293b" stroke-width="4"/>
  <path d="M 380 50 L 380 150 L 270 150" fill="none" stroke="#1e293b" stroke-width="4"/>
  <path d="M 170 150 L 65 150 L 65 50" fill="none" stroke="#1e293b" stroke-width="4"/>
  
  {get_hand_svg(170, 75, "Splitting Node")}
</svg>

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 🔴 **Step 1:** Dono LEDs ke **Long Legs (+)** ko aapas mein ek joint (Joint A) par jodein aur use battery ke **Red Wire (+)** se connect karein.
* ⚫ **Step 2:** Dono LEDs ke **Short Legs (-)** ko dusre joint (Joint B) par jodein aur use battery ke **Black Wire (-)** se connect karein.
* 💡 **Verify:** Ek LED ko nikal kar check karein — dusri LED abhi bhi full brightness me chalti rahegi!

---

## 📸 Slide 5: Student Task — Hands-On Practice
1. **Parallel Setup Challenge:** 2 LEDs ko parallel grid me design karein. Ek LED nikal kar confirm karein ki dusri LED chal rahi hai ya nahi.
2. **❓ Quiz Question:** Parallel wiring me voltage drop hota hai ya same rehta hai?
> **Answer:** Same rehta hai! Har branch ko barabar voltage milta hai.
"""

    # Session 7: Push Button Circuit
    elif num == 7:
        s4 = get_base64_image("switches_buttons.jpg")
        return f"""# Session 07: Push Button Circuit 🔘

**Class 2 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Momentary Logic Switch
![Push Button]({s4})

> **Press to turn ON logic and momentary connections**

---

## 📸 Slide 2: Normally Open button
* **Momentary action:** Ye switch tab tak circuit connect rakhta hai jab tak ise finger se dabaye rakha jaye.
* **Button terminals:** Tactile switch ke pins key press karne par close hotey hain.

---

## 📸 Slide 3: Visual Circuit Diagram 🎨
<svg width="450" height="240" viewBox="0 0 450 240" style="display: block; margin: 20px auto; background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 12px; font-family: sans-serif;">
  <rect width="100%" height="100%" fill="#f8fafc" rx="12"/>
  
  <!-- 9V Battery -->
  <g transform="translate(20, 50)">
    <rect x="0" y="20" width="70" height="100" rx="8" fill="#1e293b" stroke="#0f172a" stroke-width="3"/>
    <text x="35" y="70" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">9V BATTERY</text>
    <circle cx="25" cy="45" r="7" fill="#ef4444"/>
    <text x="25" y="49" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">+</text>
    <circle cx="45" cy="45" r="7" fill="#3b82f6"/>
    <text x="45" y="49" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">-</text>
  </g>

  <!-- Push Button -->
  <g transform="translate(180, 50)">
    <rect x="0" y="20" width="80" height="60" rx="8" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="3"/>
    <circle cx="40" cy="50" r="16" fill="#ef4444" stroke="#b91c1c" stroke-width="2"/>
    <text x="40" y="100" font-size="10" font-weight="bold" fill="#475569" text-anchor="middle">PUSH SWITCH</text>
    <line x1="15" y1="80" x2="15" y2="95" stroke="#475569" stroke-width="3"/>
    <line x1="65" y1="80" x2="65" y2="95" stroke="#475569" stroke-width="3"/>
  </g>

  <!-- LED -->
  <g transform="translate(340, 50)">
    <line x1="20" y1="80" x2="20" y2="130" stroke="#ef4444" stroke-width="4"/>
    <line x1="40" y1="80" x2="40" y2="115" stroke="#3b82f6" stroke-width="4"/>
    <path d="M 10 70 Q 10 20 30 20 Q 50 20 50 70 Z" fill="#10b981" fill-opacity="0.8" stroke="#047857" stroke-width="3"/>
    <text x="30" y="95" font-size="10" font-weight="bold" fill="#047857" text-anchor="middle">LED</text>
    <circle cx="20" cy="135" r="7" fill="#ef4444"/>
    <circle cx="40" cy="120" r="7" fill="#3b82f6"/>
  </g>

  <!-- Connections -->
  <path d="M 45 50 L 45 25 L 195 25 L 195 50" fill="none" stroke="#ef4444" stroke-width="4"/>
  <path d="M 245 50 L 245 25 L 360 25 L 360 50" fill="none" stroke="#eab308" stroke-width="4"/>
  <text x="300" y="18" font-size="10" font-weight="bold" fill="#eab308" text-anchor="middle">🟡 Yellow Wire (+)</text>
  <path d="M 65 50 L 65 150 L 380 150 L 380 50" fill="none" stroke="#1e293b" stroke-width="4"/>
  
  {get_hand_svg(220, 30, "Press Switch")}
</svg>

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 🔴 **Step 1:** Battery snap ke **Red Wire (+)** ko **Push Button** ke Pin 1 par connect karein.
* 🟡 **Step 2:** Push Button ke Pin 2 se ek wire lekar **LED ke Long Leg (+)** par lagayein.
* ⚫ **Step 3:** Battery snap ke **Black Wire (-)** ko directly **LED ke Short Leg (-)** se connect karein.
* 👆 **Push Test:** Button ko press karein — push karte hi LED chalegi, finger hatate hi band ho jayegi.

---

## 📸 Slide 5: Student Task — Hands-On Practice
1. **Key Press Light:** Push button tactile pins use karke momentary buzzer/LED circuit compile karein.
2. **❓ Quiz Question:** Door bell me kaun sa switch use hota hai — rocker or push button?
> **Answer:** Push Button! Kyunki doorbell momentary control ke liye hoti hai.
"""

    # Session 8: Mini Torch Project
    elif num == 8:
        s2 = get_base64_image("battery_snap.jpg")
        return f"""# Session 08: Mini Torch Project 🔦

**Class 2 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Handheld Torch Design
![Torch Battery Snap]({s2})

> **LED, Switch aur Battery se portable torch model assemble karna**

---

## 📸 Slide 2: Design Modules
* **Cardboard body:** Wires aur battery ko securely hold karne ke liye chassis structure.
* **Focussed light:** Bright LED reflector jo clear beam light dega.
* **Control button:** Rocker switch loop ON/OFF karne ke liye.

---

## 📸 Slide 3: Visual Circuit Diagram 🎨
<svg width="450" height="240" viewBox="0 0 450 240" style="display: block; margin: 20px auto; background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 12px; font-family: sans-serif;">
  <rect width="100%" height="100%" fill="#f8fafc" rx="12"/>
  
  <!-- 9V Battery -->
  <g transform="translate(20, 50)">
    <rect x="0" y="20" width="70" height="100" rx="8" fill="#1e293b" stroke="#0f172a" stroke-width="3"/>
    <text x="35" y="70" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">9V BATTERY</text>
    <circle cx="25" cy="45" r="7" fill="#ef4444"/>
    <text x="25" y="49" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">+</text>
    <circle cx="45" cy="45" r="7" fill="#3b82f6"/>
    <text x="45" y="49" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">-</text>
  </g>

  <!-- Slide Switch -->
  <g transform="translate(170, 50)">
    <rect x="0" y="20" width="90" height="50" rx="6" fill="#475569" stroke="#334155" stroke-width="3"/>
    <rect x="35" y="10" width="20" height="12" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="2"/>
    <text x="45" y="52" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">SLIDE SWITCH</text>
    <rect x="15" y="70" width="8" height="15" fill="#cbd5e1"/>
    <rect x="65" y="70" width="8" height="15" fill="#cbd5e1"/>
  </g>

  <!-- Torch LED -->
  <g transform="translate(340, 50)">
    <line x1="20" y1="80" x2="20" y2="130" stroke="#ef4444" stroke-width="4"/>
    <line x1="40" y1="80" x2="40" y2="115" stroke="#3b82f6" stroke-width="4"/>
    <path d="M 10 70 Q 10 20 30 20 Q 50 20 50 70 Z" fill="#eab308" fill-opacity="0.8" stroke="#ca8a04" stroke-width="3"/>
    <circle cx="30" cy="45" r="25" fill="#eab308" fill-opacity="0.2" stroke="#eab308" stroke-opacity="0.4" stroke-width="1" stroke-dasharray="2,2"/>
    <text x="30" y="95" font-size="10" font-weight="bold" fill="#ca8a04" text-anchor="middle">TORCH LED</text>
    <circle cx="20" cy="135" r="6" fill="#ef4444"/>
    <circle cx="40" cy="120" r="6" fill="#3b82f6"/>
  </g>

  <!-- Connections -->
  <path d="M 45 50 L 45 25 L 185 25 L 185 50" fill="none" stroke="#ef4444" stroke-width="4"/>
  <path d="M 235 50 L 235 25 L 360 25 L 360 50" fill="none" stroke="#eab308" stroke-width="4"/>
  <path d="M 65 50 L 65 150 L 380 150 L 380 50" fill="none" stroke="#1e293b" stroke-width="4"/>
  
  {get_hand_svg(215, 20, "Slide ON")}
</svg>

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 🔴 **Step 1:** Battery snap ke **Red Wire (+)** ko **Slide Switch** ke side pin par jodein.
* 🟡 **Step 2:** Switch ke center pin se extra wire lekar **Torch LED ke positive leg (+)** se connect karein.
* ⚫ **Step 3:** Battery snap ke **Black Wire (-)** ko directly **LED ke negative leg (-)** se jodein.
* 🛠️ **Body Assembly:** Cardboard paper roll banakar battery aur switch ko tape se chipkaye.

---

## 📸 Slide 5: Student Task — Hands-On Practice
1. **Torch Assembly:** Model assemble karein aur check check test karein.
2. **❓ Quiz Question:** Torch me component parts kis direction me judtey hain?
> **Answer:** Series circuit chain direction me.
"""

    # Session 9: Buzzer Introduction
    elif num == 9:
        s5 = get_base64_image("leds_buzzer.jpg")
        return f"""# Session 09: Buzzer Introduction 🔊

**Class 2 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Sound Output Components
![Buzzer Component]({s5})

> **Active buzzer sound frequency aur polarity rules**

---

## 📸 Slide 2: Active Buzzer Basics
* **Polarity matters:** Long leg positive (+) aur short leg negative (-) hoti hai.
* **Active Sound:** Iske andar oscillator circuit embedded hota hai, isiliye sirf DC voltage dene par beep/tone sound chalu ho jata hai.

---

## 📸 Slide 3: Visual Circuit Diagram 🎨
<svg width="450" height="240" viewBox="0 0 450 240" style="display: block; margin: 20px auto; background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 12px; font-family: sans-serif;">
  <rect width="100%" height="100%" fill="#f8fafc" rx="12"/>
  
  <!-- 9V Battery -->
  <g transform="translate(40, 50)">
    <rect x="0" y="20" width="80" height="100" rx="8" fill="#1e293b" stroke="#0f172a" stroke-width="3"/>
    <text x="40" y="65" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">9V BATTERY</text>
    <circle cx="25" cy="45" r="7" fill="#ef4444"/>
    <text x="25" y="49" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">+</text>
    <circle cx="55" cy="45" r="7" fill="#3b82f6"/>
    <text x="55" y="49" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">-</text>
  </g>

  <!-- Active Buzzer -->
  <g transform="translate(300, 50)">
    <circle cx="40" cy="50" r="30" fill="#000000" stroke="#334155" stroke-width="3"/>
    <circle cx="40" cy="50" r="10" fill="#1e293b"/>
    <line x1="25" y1="80" x2="25" y2="130" stroke="#ef4444" stroke-width="4"/>
    <line x1="55" y1="80" x2="55" y2="115" stroke="#3b82f6" stroke-width="4"/>
    <text x="40" y="15" font-size="12" font-weight="bold" fill="#0f172a" text-anchor="middle">BUZZER</text>
    <circle cx="25" cy="135" r="6" fill="#ef4444"/>
    <text x="25" y="139" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">+</text>
    <circle cx="55" cy="120" r="6" fill="#3b82f6"/>
    <text x="55" y="124" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">-</text>
  </g>

  <!-- Connections -->
  <path d="M 65 55 L 65 30 L 325 30 L 325 50" fill="none" stroke="#ef4444" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="190" y="22" font-size="11" font-weight="bold" fill="#ef4444" text-anchor="middle">🔴 RED WIRE (+)</text>
  
  <path d="M 95 55 L 95 160 L 355 160 L 355 50" fill="none" stroke="#1e293b" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <text x="220" y="175" font-size="11" font-weight="bold" fill="#1e293b" text-anchor="middle">⚫ BLACK WIRE (-)</text>
  
  {get_hand_svg(325, 80, "Buzzer +")}
</svg>

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 🔴 **Red Wire (Buzzer Positive):** Battery snap ke **Red Wire (+)** ko active buzzer ke **Long Leg (+)** se direct touch/connect karein.
* ⚫ **Black Wire (Buzzer Negative):** Battery snap ke **Black Wire (-)** ko active buzzer ke **Short Leg (-)** se connect karein.
* 🔊 **Note:** Correct wire touch karte hi high-pitch warning alarm start ho jayega.

---

## 📸 Slide 5: Student Task — Hands-On Practice
1. **Beep Sound Test:** Battery se buzzer direct chala kar tone sound generate karein. Swapping polarity test karein (reverse wiring karne par kya sound aayega?).
2. **❓ Quiz Question:** Active buzzer me logic reverse lagane par buzzer sound aata hai?
> **Answer:** Nahi, buzzer damage ho sakta hai ya tone band rahega.
"""

    # Session 10: Door Bell Project
    elif num == 10:
        s4 = get_base64_image("switches_buttons.jpg")
        return f"""# Session 10: Door Bell Project 🔔

**Class 2 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Smart Bell mockup
![Push Button]({s4})

> **Push button aur active buzzer se interactive bell system banana**

---

## 📸 Slide 2: Flow Logic
* **Button Normal state:** Open circuit, buzzer silent.
* **Button Pressed state:** Closed circuit, current triggers active buzzer, alert sound alarm.

---

## 📸 Slide 3: Visual Circuit Diagram 🎨
<svg width="450" height="240" viewBox="0 0 450 240" style="display: block; margin: 20px auto; background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 12px; font-family: sans-serif;">
  <rect width="100%" height="100%" fill="#f8fafc" rx="12"/>
  
  <!-- 9V Battery -->
  <g transform="translate(20, 50)">
    <rect x="0" y="20" width="70" height="100" rx="8" fill="#1e293b" stroke="#0f172a" stroke-width="3"/>
    <text x="35" y="70" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">9V BATTERY</text>
    <circle cx="25" cy="45" r="7" fill="#ef4444"/>
    <text x="25" y="49" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">+</text>
    <circle cx="45" cy="45" r="7" fill="#3b82f6"/>
    <text x="45" y="49" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">-</text>
  </g>

  <!-- Push Button -->
  <g transform="translate(180, 50)">
    <rect x="0" y="20" width="80" height="60" rx="8" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="3"/>
    <circle cx="40" cy="50" r="16" fill="#ef4444" stroke="#b91c1c" stroke-width="2"/>
    <text x="40" y="100" font-size="10" font-weight="bold" fill="#475569" text-anchor="middle">PUSH BUTTON</text>
  </g>

  <!-- Buzzer -->
  <g transform="translate(330, 50)">
    <circle cx="40" cy="50" r="25" fill="#000000" stroke="#334155" stroke-width="3"/>
    <line x1="25" y1="75" x2="25" y2="120" stroke="#ef4444" stroke-width="4"/>
    <line x1="55" y1="75" x2="55" y2="110" stroke="#3b82f6" stroke-width="4"/>
    <text x="40" y="15" font-size="10" font-weight="bold" fill="#475569" text-anchor="middle">BUZZER</text>
    <circle cx="25" cy="125" r="6" fill="#ef4444"/>
    <circle cx="55" cy="115" r="6" fill="#3b82f6"/>
  </g>

  <!-- Connections -->
  <path d="M 45 50 L 45 25 L 195 25 L 195 50" fill="none" stroke="#ef4444" stroke-width="4"/>
  <path d="M 245 50 L 245 25 L 355 25 L 355 50" fill="none" stroke="#eab308" stroke-width="4"/>
  <text x="300" y="18" font-size="10" font-weight="bold" fill="#eab308" text-anchor="middle">🟡 Yellow Wire (+)</text>
  <path d="M 65 50 L 65 150 L 385 150 L 385 50" fill="none" stroke="#1e293b" stroke-width="4"/>
  
  {get_hand_svg(220, 30, "Press Bell")}
</svg>

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 🔴 **Step 1:** Battery snap ke **Red Wire (+)** ko **Push Button** ke Terminal 1 par connect karein.
* 🟡 **Step 2:** Push Button ke Terminal 2 se wire lekar **Buzzer ke positive leg (+)** par connect karein.
* ⚫ **Step 3:** Battery snap ke **Black Wire (-)** ko directly **Buzzer ke negative leg (-)** se jodein.
* 🔔 **Interactive Check:** Door bell switch cardboard sheet par chipka kar use press karke test karein.

---

## 📸 Slide 5: Student Task — Hands-On Practice
1. **Doorbell Prototype:** Cardboard frame par doorbell model fix karein aur press check test karein.
2. **❓ Quiz Question:** Smart doorbell alarm loop kis logic switch se controlled hota hai?
> **Answer:** Tactile push button logic se.
"""

    # Session 11: Motor Introduction
    elif num == 11:
        s3 = get_base64_image("gear_motor_wheels.jpg")
        return f"""# Session 11: Motor Introduction 🔌

**Class 2 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Mechanical energy converter
![Motor Component]({s3})

> **DC motor rotation shaft and rotation directions**

---

## 📸 Slide 2: DC Motor basics
* **Electromagnetism:** Electrical energy ko mechanical rotary power me badalta hai.
* **No polarity restrictions:** Motor wires exchange karne par rotation direction clockwise se counter-clockwise badal jati hai.

---

## 📸 Slide 3: Visual Circuit Diagram 🎨
<svg width="450" height="240" viewBox="0 0 450 240" style="display: block; margin: 20px auto; background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 12px; font-family: sans-serif;">
  <rect width="100%" height="100%" fill="#f8fafc" rx="12"/>
  
  <!-- Battery -->
  <g transform="translate(30, 50)">
    <rect x="0" y="20" width="70" height="100" rx="8" fill="#1e293b" stroke="#0f172a" stroke-width="3"/>
    <text x="35" y="70" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">9V BATTERY</text>
    <circle cx="25" cy="45" r="7" fill="#ef4444"/>
    <text x="25" y="49" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">+</text>
    <circle cx="45" cy="45" r="7" fill="#3b82f6"/>
    <text x="45" y="49" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">-</text>
  </g>

  <!-- DC Motor -->
  <g transform="translate(280, 50)">
    <circle cx="50" cy="50" r="35" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="3"/>
    <circle cx="50" cy="50" r="8" fill="#94a3b8"/>
    <!-- Terminals -->
    <rect x="10" y="45" width="8" height="10" fill="#ef4444"/>
    <rect x="82" y="45" width="8" height="10" fill="#3b82f6"/>
    <text x="14" y="40" font-size="8" font-weight="bold" fill="#ef4444" text-anchor="middle">(+)</text>
    <text x="86" y="40" font-size="8" font-weight="bold" fill="#3b82f6" text-anchor="middle">(-)</text>
    <text x="50" y="105" font-size="11" font-weight="bold" fill="#475569" text-anchor="middle">DC MOTOR</text>
  </g>

  <!-- Connections -->
  <path d="M 55 50 L 55 25 L 290 25 L 290 50" fill="none" stroke="#ef4444" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M 75 50 L 75 150 L 362 150 L 362 50" fill="none" stroke="#1e293b" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  
  {get_hand_svg(290, 80, "Connect Motor")}
</svg>

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 🔴 **Step 1:** Battery snap ke **Red Wire (+)** ko DC motor ke pehle terminal se connect karein.
* ⚫ **Step 2:** Battery snap ke **Black Wire (-)** ko DC motor ke dusre terminal se connect karein.
* 🔄 **Polarity Reverse Test:** Wires ko switch karein — observe karein ki motor ka rotating shaft opposite direction me ghum raha hai.

---

## 📸 Slide 5: Student Task — Hands-On Practice
1. **Spin Direction Swap:** Motor ko direct battery se chala kar RPM speed check karein aur polarity switch karke rotating shaft direction test swap karein.
2. **❓ Quiz Question:** Motor ke wires ko exchange karne par kya motor kharab ho jayegi?
> **Answer:** Nahi, uski spin hone ki direction (clockwise/anticlockwise) bas reverse ho jayegi.
"""

    # Session 12: Propeller Fan
    elif num == 12:
        s4 = get_base64_image("toy_motor_propeller.jpg")
        return f"""# Session 12: Propeller Fan 💨

**Class 2 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Utility Desk Fan Model
![Toy Motor Propeller]({s4})

> **DC Toy Motor axle par propeller blades mount karke mini fan banana**

---

## 📸 Slide 2: Physics of Fan
* **Blade Pitch:** Blades ka bent angle hawa ko aage push karta hai (air displacement).
* **RPM Requirement:** High rotation rate (RPM) se aane wali thandi hawa generate karna.

---

## 📸 Slide 3: Visual Circuit Diagram 🎨
<svg width="450" height="240" viewBox="0 0 450 240" style="display: block; margin: 20px auto; background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 12px; font-family: sans-serif;">
  <rect width="100%" height="100%" fill="#f8fafc" rx="12"/>
  
  <!-- Battery -->
  <g transform="translate(30, 50)">
    <rect x="0" y="20" width="70" height="100" rx="8" fill="#1e293b" stroke="#0f172a" stroke-width="3"/>
    <text x="35" y="70" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">9V BATTERY</text>
    <circle cx="25" cy="45" r="7" fill="#ef4444"/>
    <text x="25" y="49" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">+</text>
    <circle cx="45" cy="45" r="7" fill="#3b82f6"/>
    <text x="45" y="49" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">-</text>
  </g>

  <!-- DC Motor with propeller -->
  <g transform="translate(260, 50)">
    <circle cx="50" cy="50" r="30" fill="#cbd5e1" stroke="#94a3b8" stroke-width="2"/>
    <!-- Propeller Blades -->
    <path d="M 50 20 Q 20 0 10 30 Q 30 50 50 50 Z" fill="#0ea5e9" fill-opacity="0.7"/>
    <path d="M 50 80 Q 80 100 90 70 Q 70 50 50 50 Z" fill="#0ea5e9" fill-opacity="0.7"/>
    <path d="M 20 50 Q 0 80 30 90 Q 50 70 50 50 Z" fill="#0ea5e9" fill-opacity="0.7"/>
    <path d="M 80 50 Q 100 20 70 10 Q 50 30 50 50 Z" fill="#0ea5e9" fill-opacity="0.7"/>
    <circle cx="50" cy="50" r="6" fill="#e2e8f0"/>
  </g>

  <!-- Connections -->
  <path d="M 55 50 L 55 25 L 270 25 L 270 50" fill="none" stroke="#ef4444" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M 75 50 L 75 160 L 350 160 L 350 50" fill="none" stroke="#1e293b" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  
  {get_hand_svg(270, 70, "Mount Propeller")}
</svg>

---

## 📸 Slide 4: Step-by-Step Connection Guide
* ⚙️ **Step 1:** Ek plastic propeller fan ko DC motor ke spindle shaft par gently push karke mount karein.
* 🔴 **Step 2:** Snap ke **Red Wire (+)** aur **Black Wire (-)** ko motor pins par connect karein.
* 💨 **Airflow Direction Check:** Fan ko switch on karke check karein ki hawa front side aa rahi hai ya nahi.

---

## 📸 Slide 5: Student Task — Hands-On Practice
1. **Mini Desk Fan:** Motor and propeller attach karke stand build karein.
2. **❓ Quiz Question:** Hawa ko forward push karne ke liye motor ki spin direction kya honi chahiye?
> **Answer:** Spin direction aisi honi chahiye ki propeller blades hawa ko back side se cut karke front push karein.
"""

    # Session 13: Wind Power Challenge
    elif num == 13:
        s4 = get_base64_image("toy_motor_propeller.jpg")
        return f"""# Session 13: Wind Power Challenge 🌀

**Class 2 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Aerodynamics test
![Propeller Fan]({s4})

> **Propeller blade angle aur airflow thrust values analyze karna**

---

## 📸 Slide 2: Air thrust metrics
* **Optimal angle:** Blades ka pitch angle jitna perfect hoga, output power utni hi badh jayegi.
* **Thrust direction:** Backwards displacement front propulsion force generate karti hai.

---

## 📸 Slide 3: Visual Circuit Diagram 🎨
<svg width="450" height="240" viewBox="0 0 450 240" style="display: block; margin: 20px auto; background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 12px; font-family: sans-serif;">
  <rect width="100%" height="100%" fill="#f8fafc" rx="12"/>
  
  <!-- Generator Motor -->
  <g transform="translate(60, 50)">
    <circle cx="50" cy="50" r="30" fill="#cbd5e1" stroke="#94a3b8" stroke-width="2"/>
    <path d="M 50 20 Q 20 0 10 30 Q 30 50 50 50 Z" fill="#0ea5e9" fill-opacity="0.7"/>
    <path d="M 50 80 Q 80 100 90 70 Q 70 50 50 50 Z" fill="#0ea5e9" fill-opacity="0.7"/>
    <text x="50" y="100" font-size="10" font-weight="bold" fill="#0284c7" text-anchor="middle">WIND GENERATOR</text>
  </g>

  <!-- Output LED -->
  <g transform="translate(300, 50)">
    <line x1="20" y1="80" x2="20" y2="130" stroke="#ef4444" stroke-width="4"/>
    <line x1="40" y1="80" x2="40" y2="115" stroke="#3b82f6" stroke-width="4"/>
    <path d="M 10 70 Q 10 20 30 20 Q 50 20 50 70 Z" fill="#10b981" fill-opacity="0.8" stroke="#047857" stroke-width="3"/>
    <circle cx="30" cy="45" r="20" fill="#10b981" fill-opacity="0.15" stroke="#10b981" stroke-opacity="0.3" stroke-width="1" stroke-dasharray="3,3"/>
    <text x="30" y="95" font-size="10" font-weight="bold" fill="#047857" text-anchor="middle">GLOWING LED</text>
    <circle cx="20" cy="135" r="6" fill="#ef4444"/>
    <circle cx="40" cy="120" r="6" fill="#3b82f6"/>
  </g>

  <!-- Connections -->
  <path d="M 110 75 L 320 75" fill="none" stroke="#ef4444" stroke-width="4" stroke-linecap="round"/>
  <text x="215" y="65" font-size="9" font-weight="bold" fill="#ef4444" text-anchor="middle">🔴 POSITIVE WIRE (+)</text>
  
  <path d="M 110 95 L 340 95" fill="none" stroke="#1e293b" stroke-width="4" stroke-linecap="round"/>
  <text x="215" y="110" font-size="9" font-weight="bold" fill="#1e293b" text-anchor="middle">⚫ NEGATIVE WIRE (-)</text>
  
  {get_hand_svg(60, 10, "Blow Wind")}
</svg>

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 🌀 **Step 1:** Motor ke shaft par propeller lagakar use generator setup mein switch karein.
* 💡 **Step 2:** Motor ke output wires ko directly **LED legs** se connect karein.
* 💨 **Step 3:** Propeller par tez hawa (fan/blow) dalein aur check karein ki generator logic se LED jalti hai ya nahi.
* 📐 **Angle adjustment:** Blades ke bent angle ko modify karke maximum brightness check karein.

---

## 📸 Slide 5: Student Task — Hands-On Practice
1. **Thrust angle check:** Propeller blades ke pitch angle ko manually (slightly) bend karke airflow output pressure test karein.
2. **❓ Quiz Question:** Kya speed aur blade angles coordinate hote hain?
> **Answer:** Haan, blade angle thrust aur airflow rate control karta hai.
"""

    # Session 14: Gear Motor
    elif num == 14:
        s3 = get_base64_image("gear_motor_wheels.jpg")
        return f"""# Session 14: Gear Motor ⚙️

**Class 2 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Speed vs Torque
![Gear Motor]({s3})

> **High-torque BO gear motor aur simple toy motor ka mechanism comparison**

---

## 📸 Slide 2: Gear Reduction logic
* **Torque:** Heavy weight uthane ya push karne ki capability.
* **Gears inside:** Motor ke internal gears speed ko reduce karke pull/push capacity ko multiply karte hain.

---

## 📸 Slide 3: Visual Circuit Diagram 🎨
<svg width="450" height="240" viewBox="0 0 450 240" style="display: block; margin: 20px auto; background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 12px; font-family: sans-serif;">
  <rect width="100%" height="100%" fill="#f8fafc" rx="12"/>
  
  <!-- Battery -->
  <g transform="translate(30, 50)">
    <rect x="0" y="20" width="70" height="100" rx="8" fill="#1e293b" stroke="#0f172a" stroke-width="3"/>
    <text x="35" y="70" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">9V BATTERY</text>
    <circle cx="25" cy="45" r="7" fill="#ef4444"/>
    <text x="25" y="49" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">+</text>
    <circle cx="45" cy="45" r="7" fill="#3b82f6"/>
    <text x="45" y="49" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">-</text>
  </g>

  <!-- BO Gear Motor -->
  <g transform="translate(240, 50)">
    <rect x="0" y="20" width="120" height="60" rx="6" fill="#f59e0b" stroke="#d97706" stroke-width="3"/>
    <circle cx="95" cy="50" r="12" fill="#cbd5e1" stroke="#94a3b8" stroke-width="2"/>
    <rect x="90" y="45" width="10" height="10" fill="#94a3b8"/>
    <!-- Polarities -->
    <rect x="5" y="45" width="8" height="10" fill="#ef4444"/>
    <rect x="5" y="65" width="8" height="10" fill="#3b82f6"/>
    <text x="60" y="100" font-size="11" font-weight="bold" fill="#b45309" text-anchor="middle">BO GEAR MOTOR</text>
  </g>

  <!-- Connections -->
  <path d="M 55 50 L 55 25 L 245 25 L 245 50" fill="none" stroke="#ef4444" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  <path d="M 75 50 L 75 160 L 280 160 L 280 100 L 245 100 L 245 75" fill="none" stroke="#1e293b" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
  
  {get_hand_svg(335, 10, "Test Shaft Torque")}
</svg>

---

## 📸 Slide 4: Step-by-Step Connection Guide
* ⚙️ **Step 1:** Gear motor ke terminals par battery snap ke **Red (+)** aur **Black (-)** wires attach karein.
* 🌀 **Step 2:** Motor ke rotating axle (spindle shaft) par directly finger se pressure banayein.
* 💡 **Observe:** Gear ratio reduction ki wajah se motor ki torque itni zyaada hogi ki ise haath se rokna impossible ho jayega.

---

## 📸 Slide 5: Student Task — Hands-On Practice
1. **Torque Resistance Test:** Dono motors chalakar shaft ko finger tip se rokhne ka pressure compare karein.
2. **❓ Quiz Question:** Robot wheels chalane ke liye kaun si motor use karni chahiye?
> **Answer:** Gear Motor, kyunki iska torque aur wheel load capability zyada hoti hai.
"""

    # Session 15: Wheel Motion
    elif num == 15:
        s3 = get_base64_image("gear_motor_wheels.jpg")
        return f"""# Session 15: Wheel Motion 🛞

**Class 2 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Rolling Robot Base
![Gear Motor Wheels]({s3})

> **DC BO Gear motor shaft par toy rubber wheels lagakar movement check**

---

## 📸 Slide 2: Movement Physics
* **Friction:** Rubber grip tire wheels ko slips se bacha kar maximum displacement deta hai.
* **Axle lock:** Wheel center hole ko D-shaft motor spindle par lock karna.

---

## 📸 Slide 3: Visual Circuit Diagram 🎨
<svg width="450" height="240" viewBox="0 0 450 240" style="display: block; margin: 20px auto; background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 12px; font-family: sans-serif;">
  <rect width="100%" height="100%" fill="#f8fafc" rx="12"/>
  
  <!-- BO Gear Motor -->
  <g transform="translate(40, 50)">
    <rect x="0" y="20" width="120" height="60" rx="6" fill="#f59e0b" stroke="#d97706" stroke-width="3"/>
    <circle cx="95" cy="50" r="10" fill="#94a3b8"/>
    <text x="60" y="100" font-size="11" font-weight="bold" fill="#b45309" text-anchor="middle">GEAR MOTOR</text>
  </g>

  <!-- Rubber Wheel -->
  <g transform="translate(240, 40)">
    <circle cx="60" cy="60" r="45" fill="#1e293b" stroke="#475569" stroke-width="4"/>
    <path d="M 60 15 L 60 25" stroke="#ffffff" stroke-width="3"/>
    <path d="M 60 95 L 60 105" stroke="#ffffff" stroke-width="3"/>
    <path d="M 15 60 L 25 60" stroke="#ffffff" stroke-width="3"/>
    <path d="M 95 60 L 105 60" stroke="#ffffff" stroke-width="3"/>
    <circle cx="60" cy="60" r="12" fill="#cbd5e1" stroke="#94a3b8" stroke-width="2"/>
    <rect x="56" y="56" width="8" height="8" fill="#475569"/>
    <text x="60" y="125" font-size="11" font-weight="bold" fill="#1e293b" text-anchor="middle">RUBBER WHEEL</text>
  </g>

  <!-- Coupling line -->
  <path d="M 135 100 L 240 100" fill="none" stroke="#ef4444" stroke-width="3" stroke-dasharray="4,4"/>
  
  {get_hand_svg(180, 50, "Press-fit Axle")}
</svg>

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 🛞 **Step 1:** Toy rubber wheel ke center hole (D-shape) ko BO Gear Motor ke axle shaft par carefully line up karke press-fit karein.
* 🔴 **Step 2:** Battery snap ke **Red (+)** aur **Black (-)** wires ko gear motor ke terminals se jodein.
* 🏃‍♂️ **Step 3:** Setup ko floor par rakhein aur check karein ki friction aur axle motion se robot base kitni smooth chalti hai.

---

## 📸 Slide 5: Student Task — Hands-On Practice
1. **Rolling Chassis:** Gear motor par wheels mount karke motor battery loop connect karein aur ground run test karein.
2. **❓ Quiz Question:** Wheel slides and slips se bachne ke liye tire rubber grid grip kyu zaroori hai?
> **Answer:** Grip badhane aur rolling friction generate karne ke liye.
"""

    # Session 16: Straight Line Challenge
    elif num == 16:
        s3 = get_base64_image("gear_motor_wheels.jpg")
        return f"""# Session 16: Straight Line Challenge 📏

**Class 2 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Direction Alignment
![Motor Wheels]({s3})

> **Robot chassis base ko exact straight route par balance karna**

---

## 📸 Slide 2: Alignment Parameters
* **Weight Distribution:** Dono side equal balance weight hona zaroori hai.
* **Axle alignment:** Dual motor axes perfectly 180 degrees linear hone chahiye.

---

## 📸 Slide 3: Visual Circuit Diagram 🎨
<svg width="450" height="240" viewBox="0 0 450 240" style="display: block; margin: 20px auto; background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 12px; font-family: sans-serif;">
  <rect width="100%" height="100%" fill="#f8fafc" rx="12"/>
  
  <!-- Left Motor -->
  <g transform="translate(40, 20)">
    <rect x="0" y="20" width="80" height="40" rx="4" fill="#f59e0b" stroke="#d97706" stroke-width="2"/>
    <circle cx="70" cy="40" r="15" fill="#1e293b"/>
    <text x="40" y="80" font-size="10" font-weight="bold" fill="#b45309" text-anchor="middle">LEFT WHEEL</text>
  </g>

  <!-- Right Motor -->
  <g transform="translate(40, 120)">
    <rect x="0" y="20" width="80" height="40" rx="4" fill="#f59e0b" stroke="#d97706" stroke-width="2"/>
    <circle cx="70" cy="40" r="15" fill="#1e293b"/>
    <text x="40" y="80" font-size="10" font-weight="bold" fill="#b45309" text-anchor="middle">RIGHT WHEEL</text>
  </g>

  <!-- Battery -->
  <g transform="translate(240, 60)">
    <rect x="0" y="20" width="60" height="80" rx="6" fill="#1e293b" stroke="#0f172a" stroke-width="3"/>
    <text x="30" y="65" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">9V BATTERY</text>
  </g>

  <!-- Connections -->
  <path d="M 270 60 L 270 10 L 90 10 L 90 40" fill="none" stroke="#ef4444" stroke-width="3" stroke-linejoin="round"/>
  <path d="M 270 10 L 90 10 L 90 140" fill="none" stroke="#ef4444" stroke-width="3" stroke-linejoin="round"/>
  
  <path d="M 285 60 L 285 190 L 110 190 L 110 160" fill="none" stroke="#334155" stroke-width="3" stroke-linejoin="round"/>
  <path d="M 285 190 L 110 190 L 110 60" fill="none" stroke="#334155" stroke-width="3" stroke-linejoin="round"/>
  
  {get_hand_svg(285, 20, "Verify Wiring")}
</svg>

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 🔴 **Step 1:** Dono gear motors ko parallel connection mein wire karein taaki dono ko barabar power mile.
* 🛞 **Step 2:** Robot chassis ke dono side ke wheels ko exact center parallel direction mein scale se align karein.
* 🏃‍♂️ **Step 3:** Floor par 1-meter straight line draw karein aur robot ko us par run karke directional error adjust karein.

---

## 📸 Slide 5: Student Task — Hands-On Practice
1. **Straight Line Run:** Robot car chassis floor line par straight chala kar deviations note karein.
2. **❓ Quiz Question:** Robot car ke ek side bhagne ka key reason kya ho sakta hai?
> **Answer:** Motor speed mismatch ya ek wheel me extra friction/weight.
"""

    # Session 17: Distance Challenge
    elif num == 17:
        s3 = get_base64_image("gear_motor_wheels.jpg")
        return f"""# Session 17: Distance Challenge ⏱️

**Class 2 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Speed, Distance & Time math
![Chassis base]({s3})

> **Robot base 1 meter track running time measurements**

---

## 📸 Slide 2: Speed calculation
* **Distance:** Floor track measurement exact 1 meter.
* **Formula:** Speed = Distance (1 meter) / Time (seconds).

---

## 📸 Slide 3: Visual Circuit Diagram 🎨
<svg width="450" height="240" viewBox="0 0 450 240" style="display: block; margin: 20px auto; background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 12px; font-family: sans-serif;">
  <rect width="100%" height="100%" fill="#f8fafc" rx="12"/>
  
  <!-- Path Line -->
  <line x1="50" y1="120" x2="400" y2="120" stroke="#94a3b8" stroke-width="4" stroke-dasharray="6,6"/>
  
  <!-- Robot Start -->
  <g transform="translate(50, 80)">
    <rect x="0" y="10" width="50" height="30" rx="4" fill="#f59e0b" stroke="#d97706" stroke-width="2"/>
    <circle cx="15" cy="40" r="10" fill="#1e293b"/>
    <circle cx="35" cy="40" r="10" fill="#1e293b"/>
    <text x="25" y="5" font-size="10" font-weight="bold" fill="#b45309" text-anchor="middle">START</text>
  </g>

  <!-- Robot Finish -->
  <g transform="translate(320, 80)">
    <rect x="0" y="10" width="50" height="30" rx="4" fill="#f59e0b" stroke="#d97706" stroke-width="2" opacity="0.5"/>
    <circle cx="15" cy="40" r="10" fill="#1e293b" opacity="0.5"/>
    <circle cx="35" cy="40" r="10" fill="#1e293b" opacity="0.5"/>
    <text x="25" y="5" font-size="10" font-weight="bold" fill="#64748b" text-anchor="middle">FINISH</text>
  </g>

  <!-- Flag -->
  <line x1="390" y1="60" x2="390" y2="120" stroke="#475569" stroke-width="3"/>
  <polygon points="390,60 415,70 390,80" fill="#ef4444"/>

  <!-- Distance text -->
  <text x="220" y="150" font-size="14" font-weight="bold" fill="#1e293b" text-anchor="middle">EXACTLY 1 METER (100 CM)</text>
  
  {get_hand_svg(360, 20, "Time Stops")}
</svg>

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 📐 **Step 1:** Floor par exactly 1 meter (100 cm) ki target line draw karein.
* ⏱️ **Step 2:** Robot car ko start line par place karein aur switch ON karte hi stopwatch start karein.
* 🏁 **Step 3:** Robot ke target line cross karte hi timer stop karein aur use time log sheet me record karein.

---

## 📸 Slide 5: Student Task — Hands-On Practice
1. **Timer Run:** Robot base coordinate path runtime check stop-watch se trace karein.
2. **❓ Quiz Question:** Agar robot 1 meter travel karne me 5 seconds leta hai toh speed kya hogi?
> **Answer:** 1 / 5 = 0.2 meters/second.
"""

    # Session 18: Speed Challenge
    elif num == 18:
        s2 = get_base64_image("battery_snap.jpg")
        return f"""# Session 18: Speed Challenge ⚡

**Class 2 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Voltage and speed effects
![Battery Snap]({s2})

> **Voltage inputs vs motor output rotations speed observe process**

---

## 📸 Slide 2: Voltage relationship
* **Higher voltage (9V):** Higher coil current, maximum motor rotation speed.
* **Lower voltage (3V):** Lower torque values, slower speeds.

---

## 📸 Slide 3: Visual Circuit Diagram 🎨
<svg width="450" height="240" viewBox="0 0 450 240" style="display: block; margin: 20px auto; background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 12px; font-family: sans-serif;">
  <rect width="100%" height="100%" fill="#f8fafc" rx="12"/>
  
  <!-- Low Voltage Side -->
  <g transform="translate(30, 40)">
    <rect x="0" y="20" width="50" height="80" rx="4" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="2"/>
    <text x="25" y="65" font-size="10" font-weight="bold" fill="#475569" text-anchor="middle">3V CELL</text>
    <circle cx="120" cy="60" r="20" fill="#cbd5e1"/>
    <path d="M 120 30 A 30 30 0 0 1 150 60" fill="none" stroke="#475569" stroke-width="2"/>
    <text x="120" y="105" font-size="9" fill="#475569" text-anchor="middle">SLOW SPIN</text>
  </g>

  <!-- High Voltage Side -->
  <g transform="translate(250, 40)">
    <rect x="0" y="20" width="50" height="80" rx="4" fill="#1e293b" stroke="#0f172a" stroke-width="2"/>
    <text x="25" y="65" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">9V BATTERY</text>
    <circle cx="120" cy="60" r="20" fill="#f59e0b"/>
    <path d="M 120 30 A 30 30 0 1 1 150 60" fill="none" stroke="#f59e0b" stroke-width="3"/>
    <text x="120" y="105" font-size="9" font-weight="bold" fill="#b45309" text-anchor="middle">FAST SPIN ⚡</text>
  </g>
  
  {get_hand_svg(250, 10, "Connect 9V")}
</svg>

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 🔴 **Step 1:** Motor ko pehle 2 double-A batteries (3V source) se connect karke rotation speed dekhein.
* ⚡ **Step 2:** Uske baad motor ko directly 9V square battery (high voltage) se connect karein.
* 📈 **Compare:** Observe karein ki kaise voltage level badhne se motor ka RPM aur power speed improve hoti hai.

---

## 📸 Slide 5: Student Task — Hands-On Practice
1. **Multi Voltage run:** Motor loop voltage change karke 3V aur 9V motor rotation speeds comparison analyze karein.
2. **❓ Quiz Question:** Motor speed directly kis electrical variable par depend hoti hai?
> **Answer:** Voltage levels input par.
"""

    # Session 19: Vibration Motor
    elif num == 19:
        s6 = get_base64_image("vibration_coin_motor.jpg")
        return f"""# Session 19: Vibration Motor 📳

**Class 2 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Eccentric Rotating Mass
![Coin Motor]({s6})

> **Flat Coin shape vibration motor safety and applications**

---

## 📸 Slide 2: Silent vibrations
* **Unbalanced mass:** Shaft rotation weight shifts vibrations patterns create karti hain.
* **Common uses:** Mobile phones pagers and vibrot toys.

---

## 📸 Slide 3: Visual Circuit Diagram 🎨
<svg width="450" height="240" viewBox="0 0 450 240" style="display: block; margin: 20px auto; background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 12px; font-family: sans-serif;">
  <rect width="100%" height="100%" fill="#f8fafc" rx="12"/>
  
  <!-- 3V Battery -->
  <g transform="translate(40, 50)">
    <rect x="0" y="20" width="80" height="90" rx="6" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="3"/>
    <text x="40" y="65" font-size="12" font-weight="bold" fill="#475569" text-anchor="middle">3V BATTERY</text>
    <circle cx="25" cy="45" r="7" fill="#ef4444"/>
    <text x="25" y="49" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">+</text>
    <circle cx="55" cy="45" r="7" fill="#3b82f6"/>
    <text x="55" y="49" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">-</text>
  </g>

  <!-- Vibration Coin Motor -->
  <g transform="translate(280, 50)">
    <circle cx="50" cy="50" r="30" fill="#64748b" stroke="#475569" stroke-width="3"/>
    <path d="M 50 50 L 70 30 A 25 25 0 0 1 70 70 Z" fill="#ef4444" opacity="0.8"/>
    <path d="M 90 40 Q 95 50 90 60" fill="none" stroke="#ef4444" stroke-width="2"/>
    <path d="M 10 40 Q 5 50 10 60" fill="none" stroke="#ef4444" stroke-width="2"/>
    <text x="50" y="105" font-size="10" font-weight="bold" fill="#475569" text-anchor="middle">COIN MOTOR</text>
  </g>

  <!-- Connections -->
  <path d="M 65 50 L 65 30 L 310 30 L 310 50" fill="none" stroke="#ef4444" stroke-width="4"/>
  <path d="M 95 50 L 95 160 L 350 160 L 350 50" fill="none" stroke="#3b82f6" stroke-width="4"/>
  
  {get_hand_svg(280, 30, "Feel Vibration")}
</svg>

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 🔴 **Step 1:** Coin vibration motor ke Red (+) wire ko battery positive se connect karein.
* 🔵 **Step 2:** Motor ke Blue (-) wire ko battery negative se connect karein.
* 📳 **Observe:** Internal asymmetric load high speed par rotate hone se vibration waves feel hone lagengi.

---

## 📸 Slide 5: Student Task — Hands-On Practice
1. **Vibration Feel test:** Coin motor wire snap battery touch karke silent vibration levels index card patterns compare karein.
2. **❓ Quiz Question:** Coin motor ke vibrations kis weight configuration se generated hote hain?
> **Answer:** Unbalanced/asymmetric internal weight rotation se.
"""

    # Session 20: Dancing Robot
    elif num == 20:
        s6 = get_base64_image("vibration_coin_motor.jpg")
        return f"""# Session 20: Dancing Robot 🤖

**Class 2 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Vibrobot Toy project
![Vibration Motor]({s6})

> **Coin motor vibrations se cardboard dancing toy prototype banana**

---

## 📸 Slide 2: Structure Design
* **Lightweight body:** Craft cardboard or brush bristle feet.
* **Vibration transfer:** Flat motor chassis coordinate center of mass me mount karna.

---

## 📸 Slide 3: Visual Circuit Diagram 🎨
<svg width="450" height="240" viewBox="0 0 450 240" style="display: block; margin: 20px auto; background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 12px; font-family: sans-serif;">
  <rect width="100%" height="100%" fill="#f8fafc" rx="12"/>
  
  <!-- Vibrobot Chassis -->
  <g transform="translate(150, 40)">
    <polygon points="40,20 110,20 130,100 20,100" fill="#f59e0b" stroke="#d97706" stroke-width="3"/>
    <line x1="30" y1="100" x2="20" y2="130" stroke="#475569" stroke-width="4"/>
    <line x1="60" y1="100" x2="50" y2="130" stroke="#475569" stroke-width="4"/>
    <line x1="90" y1="100" x2="80" y2="130" stroke="#475569" stroke-width="4"/>
    <line x1="120" y1="100" x2="110" y2="130" stroke="#475569" stroke-width="4"/>
    
    <rect x="55" y="5" width="40" height="15" rx="3" fill="#1e293b"/>
    <path d="M 50 12 Q 45 12 50 2" stroke="#ef4444" stroke-width="1.5" fill="none"/>
    <path d="M 100 12 Q 105 12 100 2" stroke="#ef4444" stroke-width="1.5" fill="none"/>
    <text x="75" y="60" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">TOY BODY</text>
  </g>
  
  {get_hand_svg(230, 20, "Place Motor")}
</svg>

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 📦 **Step 1:** Cardboard or paper use karke ek chota lightweight design model banayein.
* 📳 **Step 2:** Vibration motor ko tape se cardboard body ke center par mount karein.
* 🔋 **Step 3:** Battery connect karke toy ko table par rakhein. Vibration energy transfer hone se legs slip honge aur toy dance karne lagega!

---

## 📸 Slide 5: Student Task — Hands-On Practice
1. **Vibrobot Bug:** Cardboard and paper legs build karke bug design karein aur battery connect karke desk dancing patterns verify run karein.
2. **❓ Quiz Question:** Vibrobot bug linear run karne ke liye weight distribution balance hona zaroori hai?
> **Answer:** Haan, weight balance linear trajectory determine karta hai.
"""

    # Session 21: LED Decoration
    elif num == 21:
        s5 = get_base64_image("leds_buzzer.jpg")
        return f"""# Session 21: LED Decoration 💡

**Class 2 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Creative lights panel
![LED lights]({s5})

> **Multiple colorful LEDs connect karke lighting grids design banana**

---

## 📸 Slide 2: Parallel nodes grid
* **Decoration safety:** 9V battery series-parallel resistance mapping guidelines check.
* **Creative layout:** Star shapes or home design grid alignment patterns.

---

## 📸 Slide 3: Visual Circuit Diagram 🎨
<svg width="450" height="240" viewBox="0 0 450 240" style="display: block; margin: 20px auto; background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 12px; font-family: sans-serif;">
  <rect width="100%" height="100%" fill="#f8fafc" rx="12"/>
  
  <!-- 9V Battery -->
  <g transform="translate(20, 50)">
    <rect x="0" y="20" width="70" height="100" rx="8" fill="#1e293b" stroke="#0f172a" stroke-width="3"/>
    <text x="35" y="70" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">9V BATTERY</text>
  </g>

  <!-- Parallel Grid of 3 LEDs -->
  <!-- LED 1 -->
  <g transform="translate(160, 50)">
    <line x1="15" y1="80" x2="15" y2="120" stroke="#ef4444" stroke-width="3"/>
    <line x1="35" y1="80" x2="35" y2="110" stroke="#3b82f6" stroke-width="3"/>
    <path d="M 5 70 Q 5 20 25 20 Q 45 20 45 70 Z" fill="#ef4444" fill-opacity="0.8" stroke="#b91c1c" stroke-width="2"/>
  </g>

  <!-- LED 2 -->
  <g transform="translate(250, 50)">
    <line x1="15" y1="80" x2="15" y2="120" stroke="#ef4444" stroke-width="3"/>
    <line x1="35" y1="80" x2="35" y2="110" stroke="#3b82f6" stroke-width="3"/>
    <path d="M 5 70 Q 5 20 25 20 Q 45 20 45 70 Z" fill="#10b981" fill-opacity="0.8" stroke="#047857" stroke-width="2"/>
  </g>

  <!-- LED 3 -->
  <g transform="translate(340, 50)">
    <line x1="15" y1="80" x2="15" y2="120" stroke="#ef4444" stroke-width="3"/>
    <line x1="35" y1="80" x2="35" y2="110" stroke="#3b82f6" stroke-width="3"/>
    <path d="M 5 70 Q 5 20 25 20 Q 45 20 45 70 Z" fill="#eab308" fill-opacity="0.8" stroke="#ca8a04" stroke-width="2"/>
  </g>

  <!-- Rails -->
  <path d="M 45 50 L 45 25 L 365 25 L 365 50" fill="none" stroke="#ef4444" stroke-width="4"/>
  <path d="M 275 25 L 275 50" fill="none" stroke="#ef4444" stroke-width="4"/>
  <path d="M 185 25 L 185 50" fill="none" stroke="#ef4444" stroke-width="4"/>
  
  <path d="M 65 50 L 65 150 L 385 150 L 385 50" fill="none" stroke="#1e293b" stroke-width="4"/>
  <path d="M 295 150 L 295 50" fill="none" stroke="#1e293b" stroke-width="4"/>
  <path d="M 205 150 L 205 50" fill="none" stroke="#1e293b" stroke-width="4"/>
  
  {get_hand_svg(275, 10, "Connect Parallel")}
</svg>

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 🎨 **Step 1:** Cardboard template par star ya home shape draw karke LEDs ke liye small holes karein.
* 🔴 **Step 2:** Sabhi LEDs ke positive nodes (+) ko aapas mein ek common wire (parallel) se link karein.
* ⚫ **Step 3:** Negative nodes (-) ko common black wire se connect karke battery ground line se jodein.

---

## 📸 Slide 5: Student Task — Hands-On Practice
1. **Design Panel:** 5 LEDs parallel layout node setup board design karke lights panel build karein.
2. **❓ Quiz Question:** Decoration lights panel me parallel node kyu useful hai?
> **Answer:** Kyunki ek LED damage hone par grid me baki saari lights chalti rehti hain.
"""

    # Session 22: Traffic Signal
    elif num == 22:
        s5 = get_base64_image("leds_buzzer.jpg")
        return f"""# Session 22: Traffic Signal 🚥

**Class 2 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Logic Control signal
![LEDs Signal]({s5})

> **Red, Yellow aur Green LEDs manual traffic poles project setup**

---

## 📸 Slide 2: Control states
* **Red LED (Stop):** Toggle Switch position 1.
* **Yellow LED (Ready):** Switch position 2.
* **Green LED (Go):** Switch position 3.

---

## 📸 Slide 3: Visual Circuit Diagram 🎨
<svg width="450" height="240" viewBox="0 0 450 240" style="display: block; margin: 20px auto; background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 12px; font-family: sans-serif;">
  <rect width="100%" height="100%" fill="#f8fafc" rx="12"/>
  
  <!-- Red Switch & LED -->
  <g transform="translate(40, 20)">
    <rect x="0" y="10" width="50" height="30" rx="3" fill="#ef4444" stroke="#991b1b" stroke-width="2"/>
    <text x="25" y="30" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">RED SW</text>
    <circle cx="110" cy="25" r="15" fill="#ef4444"/>
    <path d="M 50 25 L 95 25" stroke="#ef4444" stroke-width="3"/>
  </g>

  <!-- Yellow Switch & LED -->
  <g transform="translate(40, 75)">
    <rect x="0" y="10" width="50" height="30" rx="3" fill="#eab308" stroke="#ca8a04" stroke-width="2"/>
    <text x="25" y="30" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">YEL SW</text>
    <circle cx="110" cy="25" r="15" fill="#eab308"/>
    <path d="M 50 25 L 95 25" stroke="#eab308" stroke-width="3"/>
  </g>

  <!-- Green Switch & LED -->
  <g transform="translate(40, 130)">
    <rect x="0" y="10" width="50" height="30" rx="3" fill="#10b981" stroke="#047857" stroke-width="2"/>
    <text x="25" y="30" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">GRN SW</text>
    <circle cx="110" cy="25" r="15" fill="#10b981"/>
    <path d="M 50 25 L 95 25" stroke="#10b981" stroke-width="3"/>
  </g>

  <!-- Common Battery -->
  <g transform="translate(300, 50)">
    <rect x="0" y="20" width="70" height="100" rx="8" fill="#1e293b" stroke="#0f172a" stroke-width="3"/>
    <text x="35" y="70" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">9V BATTERY</text>
  </g>

  <!-- Battery positive to all switches -->
  <path d="M 315 50 L 315 15 L 40 15 L 40 30" fill="none" stroke="#ef4444" stroke-width="3"/>
  <path d="M 40 15 L 40 85" fill="none" stroke="#ef4444" stroke-width="3"/>
  <path d="M 40 85 L 40 140" fill="none" stroke="#ef4444" stroke-width="3"/>

  <!-- All LEDs to Battery Negative -->
  <path d="M 165 45 L 335 45 L 335 50" fill="none" stroke="#1e293b" stroke-width="3"/>
  <path d="M 165 100 L 335 100 L 335 50" fill="none" stroke="#1e293b" stroke-width="3"/>
  <path d="M 165 155 L 335 155 L 335 50" fill="none" stroke="#1e293b" stroke-width="3"/>
  
  {get_hand_svg(65, 85, "Switch ON")}
</svg>

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 🚥 **Step 1:** Cardboard pole par sequence wise **RED**, **YELLOW**, aur **GREEN** LEDs place karein.
* 🔘 **Step 2:** Har LED ke series path mein ek dedicated slide switch wire karein.
* 🔌 **Step 3:** Sabhi switches ko battery (+) aur sabhi LEDs ke common negative nodes ko battery (-) se jodein. Switch toggle karke traffic signals control karein.

---

## 📸 Slide 5: Student Task — Hands-On Practice
1. **Signal Pole:** Cardboard box signal design red/yellow/green indicators parallel wire structure connect.
2. **❓ Quiz Question:** Real traffic light signaling automatically controlled hoti hai?
> **Answer:** Haan, program codes sequence time parameters loop logic se.
"""

    # Session 23: Emergency Alarm
    elif num == 23:
        s5 = get_base64_image("leds_buzzer.jpg")
        return f"""# Session 23: Emergency Alarm 🚨

**Class 2 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Siren indicator project
![Buzzer Alarm]({s5})

> **Buzzer tone sound and LED flashing sync systems**

---

## 📸 Slide 2: Sync alert
* **Audio output:** Buzzer warning sound generate.
* **Visual output:** LED red alert signal indication.

---

## 📸 Slide 3: Visual Circuit Diagram 🎨
<svg width="450" height="240" viewBox="0 0 450 240" style="display: block; margin: 20px auto; background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 12px; font-family: sans-serif;">
  <rect width="100%" height="100%" fill="#f8fafc" rx="12"/>
  
  <!-- 9V Battery -->
  <g transform="translate(20, 50)">
    <rect x="0" y="20" width="70" height="100" rx="8" fill="#1e293b" stroke="#0f172a" stroke-width="3"/>
    <text x="35" y="70" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">9V BATTERY</text>
  </g>

  <!-- Push Button -->
  <g transform="translate(150, 50)">
    <rect x="0" y="20" width="75" height="50" rx="6" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="2"/>
    <circle cx="37" cy="45" r="12" fill="#ef4444"/>
    <text x="37" y="85" font-size="9" font-weight="bold" fill="#475569" text-anchor="middle">PUSH SWITCH</text>
  </g>

  <!-- Red LED -->
  <g transform="translate(270, 40)">
    <circle cx="20" cy="40" r="12" fill="#ef4444"/>
    <text x="20" y="65" font-size="9" font-weight="bold" fill="#ef4444" text-anchor="middle">RED LED</text>
  </g>

  <!-- Buzzer -->
  <g transform="translate(360, 40)">
    <circle cx="20" cy="40" r="15" fill="#000000"/>
    <text x="20" y="65" font-size="9" font-weight="bold" fill="#000000" text-anchor="middle">BUZZER</text>
  </g>

  <!-- Connections -->
  <path d="M 45 50 L 45 25 L 165 25 L 165 50" fill="none" stroke="#ef4444" stroke-width="3"/>
  <path d="M 210 50 L 210 25 L 290 25 L 290 40" fill="none" stroke="#eab308" stroke-width="3"/>
  <path d="M 290 25 L 380 25 L 380 40" fill="none" stroke="#eab308" stroke-width="3"/>
  
  <path d="M 290 52 L 290 150 L 65 150 L 65 50" fill="none" stroke="#1e293b" stroke-width="3"/>
  <path d="M 380 55 L 380 150 L 290 150" fill="none" stroke="#1e293b" stroke-width="3"/>
  
  {get_hand_svg(185, 30, "Trigger Siren")}
</svg>

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 🔴 **Step 1:** Battery snap ke **Red Wire (+)** ko main control switch ke pin 1 par jodein.
* 🔌 **Step 2:** Switch ke Pin 2 se wire lekar use parallel lines me split karein (Red LED + active buzzer).
* ⚫ **Step 3:** LED aur buzzer ke **negative legs (-)** ko battery snap ke **Black Wire (-)** se jodein. Button dabane par alarm aur flashing light start honge!

---

## 📸 Slide 5: Student Task — Hands-On Practice
1. **Siren system:** Press button indicator series buzzer and LED light connection compile.
2. **❓ Quiz Question:** Emergency vehicles (Ambulance/Police) me kaun se feedback variables use hote hain?
> **Answer:** Siren (sound) aur red-blue flashing lights (visual indicator).
"""

    # Session 24: Windmill Project
    elif num == 24:
        s4 = get_base64_image("three_d_pen_filaments.jpg")
        return f"""# Session 24: Windmill Project 🌾

**Class 2 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Rotating Windmill tower
![Windmill tower]({s4})

> **Motor propeller blades vertical tower sticks assembly design**

---

## 📸 Slide 2: Windmill mechanics
* **Energy conversion:** Mechanical fan generator logic.
* **Tower balance:** Solid base stand for motor support weight loads.

---

## 📸 Slide 3: Visual Circuit Diagram 🎨
<svg width="450" height="240" viewBox="0 0 450 240" style="display: block; margin: 20px auto; background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 12px; font-family: sans-serif;">
  <rect width="100%" height="100%" fill="#f8fafc" rx="12"/>
  
  <!-- Battery -->
  <g transform="translate(30, 50)">
    <rect x="0" y="20" width="70" height="100" rx="8" fill="#1e293b" stroke="#0f172a" stroke-width="3"/>
    <text x="35" y="70" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">9V BATTERY</text>
  </g>

  <!-- Slide Switch -->
  <g transform="translate(150, 60)">
    <rect x="0" y="10" width="60" height="30" rx="4" fill="#3b82f6" stroke="#1d4ed8" stroke-width="2"/>
    <text x="30" y="28" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">SWITCH</text>
  </g>

  <!-- Tower Motor -->
  <g transform="translate(310, 50)">
    <rect x="0" y="20" width="60" height="40" fill="#cbd5e1" stroke="#94a3b8" stroke-width="2"/>
    <path d="M 30 0 L 30 80" stroke="#0ea5e9" stroke-width="4"/>
    <path d="M -10 40 L 70 40" stroke="#0ea5e9" stroke-width="4"/>
    <text x="30" y="105" font-size="10" font-weight="bold" fill="#475569" text-anchor="middle">WINDMILL MOTOR</text>
  </g>

  <!-- Connections -->
  <path d="M 55 50 L 55 25 L 160 25 L 160 60" fill="none" stroke="#ef4444" stroke-width="3"/>
  <path d="M 200 60 L 200 25 L 320 25 L 320 50" fill="none" stroke="#ef4444" stroke-width="3"/>
  <path d="M 75 50 L 75 160 L 350 160 L 350 90" fill="none" stroke="#1e293b" stroke-width="3"/>
  
  {get_hand_svg(180, 45, "Switch ON")}
</svg>

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 🗼 **Step 1:** Ice cream sticks aur craft sheets ko jodhkar 15cm uncha vertical tower banayein.
* 🔌 **Step 2:** DC motor ko tower ke top bracket par securely tape se mount karein.
* 🔴 **Step 3:** Switch ko tower ke base par lagayein, wires ko tower ke sath connect karke motor battery loop complete karein.

---

## 📸 Slide 5: Student Task — Hands-On Practice
1. **Windmill Model:** Ice cream sticks use structure wind turbine design motor propeller shaft connect.
2. **❓ Quiz Question:** Windmill blades kis power source se rotate hoti hain?
> **Answer:** Wind energy (hawa ke flow) se.
"""

    # Session 25: Mini Car Model
    elif num == 25:
        s3 = get_base64_image("gear_motor_wheels.jpg")
        return f"""# Session 25: Mini Car Model 🚗

**Class 2 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Chassis run test
![Car Chassis]({s3})

> **Switch battery and motor wheels chassis assembly parameters**

---

## 📸 Slide 2: Complete integration
* **Switch panel:** On/off switch path loop.
* **Chassis run:** Dual BO motor wheels alignment.

---

## 📸 Slide 3: Visual Circuit Diagram 🎨
<svg width="450" height="240" viewBox="0 0 450 240" style="display: block; margin: 20px auto; background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 12px; font-family: sans-serif;">
  <rect width="100%" height="100%" fill="#f8fafc" rx="12"/>
  
  <!-- Car Base -->
  <rect x="80" y="30" width="220" height="130" rx="8" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="2"/>
  
  <!-- Wheels -->
  <rect x="60" y="20" width="40" height="20" rx="3" fill="#1e293b"/>
  <rect x="60" y="140" width="40" height="20" rx="3" fill="#1e293b"/>
  <rect x="220" y="20" width="40" height="20" rx="3" fill="#1e293b"/>
  <rect x="220" y="140" width="40" height="20" rx="3" fill="#1e293b"/>

  <!-- Motors -->
  <rect x="200" y="45" width="40" height="20" fill="#f59e0b"/>
  <rect x="200" y="115" width="40" height="20" fill="#f59e0b"/>

  <!-- Battery inside -->
  <rect x="100" y="55" width="50" height="70" rx="4" fill="#475569"/>
  <text x="125" y="95" font-size="9" fill="#ffffff" text-anchor="middle">BATTERY</text>

  <!-- Switch -->
  <rect x="160" y="80" width="30" height="20" fill="#3b82f6"/>
  <text x="175" y="92" font-size="8" fill="#ffffff" text-anchor="middle">SW</text>
  
  <text x="190" y="190" font-size="12" font-weight="bold" fill="#1e293b" text-anchor="middle">TOP-DOWN CHASSIS WIRING VIEW</text>
  
  {get_hand_svg(175, 55, "Slide Switch")}
</svg>

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 🚗 **Step 1:** Cardboard chassis ke bottom par dono BO gear motors ko glue se flat parallel mount karein.
* 🔌 **Step 2:** Switch aur battery ko top panel par lagakar dono motors ke loops series connection me laye.
* 🛞 **Step 3:** Motors par rubber wheels mount karke floor switch run check karein.

---

## 📸 Slide 5: Student Task — Hands-On Practice
1. **Moving Toy Car:** Base assembly finalize wheels battery snap secure trace ground test run.
2. **❓ Quiz Question:** Car wheels ko direct stop switch control series connect kiya jata hai?
> **Answer:** Yes, switch circuit ko break karke stop condition banata hai.
"""

    # Session 26: Obstacle Push Car
    elif num == 26:
        s3 = get_base64_image("gear_motor_wheels.jpg")
        return f"""# Session 26: Obstacle Push Car 📦

**Class 2 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Momentum push check
![Push Car]({s3})

> **Bumper design structural strength and object displacement capacity**

---

## 📸 Slide 2: Push parameters
* **Bumper strength:** Solid front panel.
* **Friction coefficient:** Rubber tires grip power output force conversion.

---

## 📸 Slide 3: Visual Circuit Diagram 🎨
<svg width="450" height="240" viewBox="0 0 450 240" style="display: block; margin: 20px auto; background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 12px; font-family: sans-serif;">
  <rect width="100%" height="100%" fill="#f8fafc" rx="12"/>
  
  <!-- Car Chassis -->
  <g transform="translate(60, 60)">
    <rect x="0" y="0" width="160" height="80" rx="6" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="2"/>
    <circle cx="40" cy="80" r="18" fill="#1e293b"/>
    <circle cx="120" cy="80" r="18" fill="#1e293b"/>
    <!-- Glued front bumper -->
    <rect x="155" y="-10" width="12" height="100" fill="#475569" rx="2"/>
    <text x="80" y="45" font-size="11" font-weight="bold" fill="#475569" text-anchor="middle">ROBOT CAR</text>
  </g>

  <!-- Obstacle Box -->
  <g transform="translate(280, 70)">
    <rect x="0" y="0" width="80" height="70" fill="#d97706" stroke="#b45309" stroke-width="2"/>
    <text x="40" y="40" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">OBSTACLE</text>
  </g>
  
  {get_hand_svg(225, 40, "Push Bumper")}
</svg>

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 🛡️ **Step 1:** Ek flat rectangular cardboard sheet ko front bumper box ki tarah design karein.
* 🚗 **Step 2:** Is bumper ko chassis ke front side par tape aur hot glue se solid weld karein.
* 📦 **Step 3:** Car ke aage paper cup/matchbox rakhein. Motor start karke displacement and push distance record karein.

---

## 📸 Slide 5: Student Task — Hands-On Practice
1. **Push challenge:** Robot front cardboard bumper design coordinate matchbox push check test.
2. **❓ Quiz Question:** Object push karne ke liye motor ka RPM speed high hona zaroori hai ya torque?
> **Answer:** High torque (Gear Motor power) push karne ke liye useful hai.
"""

    # Session 27: Creative Robot
    elif num == 27:
        s1 = get_base64_image("kit_overview.jpg")
        return f"""# Session 27: Creative Robot 🎨

**Class 2 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: System integration model
![Kit tools]({s1})

> **Syllabus kit parts utilize design prototypes creation**

---

## 📸 Slide 2: Prototype planning
* **Brainstorming:** Robot application defined requirements list.
* **Drafting:** Pencil sketch layout connection mapping routes.

---

## 📸 Slide 3: Visual Circuit Diagram 🎨
<svg width="450" height="240" viewBox="0 0 450 240" style="display: block; margin: 20px auto; background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 12px; font-family: sans-serif;">
  <rect width="100%" height="100%" fill="#f8fafc" rx="12"/>
  
  <!-- Flow nodes -->
  <g transform="translate(20, 70)">
    <rect x="0" y="10" width="80" height="50" rx="6" fill="#a855f7" stroke="#7e22ce" stroke-width="2"/>
    <text x="40" y="40" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. THINK</text>
  </g>
  <g transform="translate(160, 70)">
    <rect x="0" y="10" width="80" height="50" rx="6" fill="#3b82f6" stroke="#1d4ed8" stroke-width="2"/>
    <text x="40" y="40" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. SKETCH</text>
  </g>
  <g transform="translate(300, 70)">
    <rect x="0" y="10" width="100" height="50" rx="6" fill="#10b981" stroke="#047857" stroke-width="2"/>
    <text x="50" y="40" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. PROTOTYPE</text>
  </g>

  <!-- Connective Arrows -->
  <path d="M 110 105 L 150 105" stroke="#475569" stroke-width="3"/>
  <path d="M 250 105 L 290 105" stroke="#475569" stroke-width="3"/>
  
  {get_hand_svg(350, 40, "Create!")}
</svg>

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 📐 **Step 1:** Apne mind me ek idea sochein (jaise automatic alarm toy ya rotating windmill fan).
* 📝 **Step 2:** Ek sheet par components ko block circles me draw karke connection wires design karein.
* 🛠️ **Step 3:** Kit ke parts combine karke manual structures ko complete push start test karein.

---

## 📸 Slide 5: Student Task — Hands-On Practice
1. **Custom prototype:** Craft sheets motors switches components organize design project check.
2. **❓ Quiz Question:** Ek robot design karne ka first step kya hota hai?
> **Answer:** Drawing plan aur parts requirement structure banana.
"""

    # Session 28: Debugging Day
    elif num == 28:
        s1 = get_base64_image("kit_overview.jpg")
        return f"""# Session 28: Debugging Day 🛠️

**Class 2 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Troubleshooting logic
![Debug setup]({s1})

> **Broken wires faulty joints circuit parameters trace check**

---

## 📸 Slide 2: Fault isolation
* **Checking continuity:** Battery snap connection contacts points check.
* **Visual inspection:** Loose solder joints or component legs touch.

---

## 📸 Slide 3: Visual Circuit Diagram 🎨
<svg width="450" height="240" viewBox="0 0 450 240" style="display: block; margin: 20px auto; background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 12px; font-family: sans-serif;">
  <rect width="100%" height="100%" fill="#f8fafc" rx="12"/>
  
  <rect x="30" y="30" width="390" height="40" fill="#ef4444" rx="4"/>
  <text x="225" y="55" font-size="12" font-weight="bold" fill="#ffffff" text-anchor="middle">🚨 PROBLEM: LED does not light up / buzzer does not ring</text>

  <!-- Checks -->
  <g transform="translate(30, 100)">
    <rect x="0" y="0" width="110" height="60" rx="4" fill="#f59e0b" stroke="#d97706" stroke-width="2"/>
    <text x="55" y="30" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Check 1: Loose Snap</text>
  </g>
  <g transform="translate(170, 100)">
    <rect x="0" y="0" width="110" height="60" rx="4" fill="#f59e0b" stroke="#d97706" stroke-width="2"/>
    <text x="55" y="30" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Check 2: Reversed LED</text>
  </g>
  <g transform="translate(310, 100)">
    <rect x="0" y="0" width="110" height="60" rx="4" fill="#f59e0b" stroke="#d97706" stroke-width="2"/>
    <text x="55" y="30" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Check 3: Broken Wire</text>
  </g>
  
  {get_hand_svg(225, 120, "Fix Faults")}
</svg>

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 🔍 **Step 1:** Agar circuit ON nahi ho raha, toh sabse pehle check karein ki battery snap loose toh nahi hai.
* 🔌 **Step 2:** Check karein ki LED ki lambi leg (+) battery positive se hi judi ho.
* ⚡ **Step 3:** Kisi bhi broken wire ko aapas mein tightly twist karke tape lagayein.

---

## 📸 Slide 5: Student Task — Hands-On Practice
1. **Fault fix challenge:** Pre-messed circuit board errors (loose snap wire, wrong LED legs) check debug fix.
2. **❓ Quiz Question:** Agar switch ON karne par buzzer beeps na ho toh sabse pehle kya check karenge?
> **Answer:** Battery charge aur snaps connections nodes check.
"""

    # Session 29: Innovation Challenge
    elif num == 29:
        s8 = get_base64_image("three_d_pen_filaments.jpg")
        return f"""# Session 29: Innovation Challenge 💡

**Class 2 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Design thinking prototypes
![Innovation check]({s8})

> **Self guided project creation parameters display**

---

## 📸 Slide 2: Iterative building
* **Ideate:** Problem statement solution ideas.
* **Prototype:** Quick building cardboard foam parts wiring check.

---

## 📸 Slide 3: Visual Circuit Diagram 🎨
<svg width="450" height="240" viewBox="0 0 450 240" style="display: block; margin: 20px auto; background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 12px; font-family: sans-serif;">
  <rect width="100%" height="100%" fill="#f8fafc" rx="12"/>
  
  <g transform="translate(40, 50)">
    <rect x="0" y="0" width="100" height="80" rx="6" fill="#3b82f6" stroke="#1d4ed8" stroke-width="2"/>
    <text x="50" y="45" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">1. IDEATE</text>
  </g>
  <g transform="translate(180, 50)">
    <rect x="0" y="0" width="100" height="80" rx="6" fill="#10b981" stroke="#047857" stroke-width="2"/>
    <text x="50" y="45" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">2. PROTOTYPE</text>
  </g>
  <g transform="translate(320, 50)">
    <rect x="0" y="0" width="90" height="80" rx="6" fill="#f43f5e" stroke="#e11d48" stroke-width="2"/>
    <text x="45" y="45" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">3. TEST</text>
  </g>
  
  {get_hand_svg(230, 10, "Brainstorm")}
</svg>

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 📝 **Step 1:** Koi daily problem sochein (jaise study table par andhera ya garmi hona).
* ⚙️ **Step 2:** Apne kit ke parts se us problem ka solution design karein.
* 🛠️ **Step 3:** Project structure ko build karein, wiring check karein aur use real test karke refine karein.

---

## 📸 Slide 5: Student Task — Hands-On Practice
1. **Unique project:** Mentors direction choice prototype model finalize design test output.
2. **❓ Quiz Question:** Trial and error debug kyu zaroori hai?
> **Answer:** Prototype design errors fix karke use refine karne ke liye.
"""

    # Session 30: Robotics Exhibition
    elif num == 30:
        s1 = get_base64_image("kit_overview.jpg")
        return f"""# Session 30: Robotics Exhibition 🏆

**Class 2 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Product presentations
![Exhibition display]({s1})

> **Final working models showcase layout grids celebration**

---

## 📸 Slide 2: Presentation tips
* **Explain working:** Flow diagram details.
* **Answer questions:** Component functions and safety parameters details.

---

## 📸 Slide 3: Visual Circuit Diagram 🎨
<svg width="450" height="240" viewBox="0 0 450 240" style="display: block; margin: 20px auto; background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 12px; font-family: sans-serif;">
  <rect width="100%" height="100%" fill="#f8fafc" rx="12"/>
  
  <g transform="translate(30, 40)">
    <rect x="0" y="20" width="110" height="80" rx="6" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="2"/>
    <text x="55" y="65" font-size="10" font-weight="bold" fill="#1e293b" text-anchor="middle">DISPLAY MODEL</text>
  </g>
  <g transform="translate(170, 40)">
    <rect x="0" y="20" width="110" height="80" rx="6" fill="#3b82f6" stroke="#1d4ed8" stroke-width="2"/>
    <text x="55" y="65" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">EXPLAIN WORK</text>
  </g>
  <g transform="translate(310, 40)">
    <rect x="0" y="20" width="110" height="80" rx="6" fill="#10b981" stroke="#047857" stroke-width="2"/>
    <text x="55" y="65" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">GET BADGES 🏆</text>
  </g>
  
  {get_hand_svg(225, 10, "Present")}
</svg>

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 📊 **Step 1:** Apne project model ke aage ek display sheet lagayein jisme project name likha ho.
* 🗣️ **Step 2:** Aane wale guest ya teachers ko batayein ki aapke project me kaun-kaun se components use hue hain aur unka kya kaam hai.
* 🏃‍♂️ **Step 3:** Project model ka live demonstration run karke unhe dikhayein!

---

## 📸 Slide 5: Student Task — Hands-On Practice
1. **Showcase Model:** Setup product panel display board answer questions guests demo runs.
2. **❓ Quiz Question:** Apne project ko explain karne ke liye main detail kya bolni chahiye?
> **Answer:** Project ka naam, kaam, aur use kiya gaya component parts list.
"""
    return ""
