import os
import base64

def get_base64_image(image_filename):
    image_path = os.path.join("C:/Users/ankes/.gemini/antigravity/scratch/curriculum_app/images", image_filename)
    if os.path.exists(image_path):
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            return f"data:image/png;base64,{encoded_string}"
    return ""

def get_hand_svg(x, y, label="Press/Connect"):
    return f"""
  <g transform="translate({x}, {y})">
    <!-- Click Ripple Animation -->
    <circle cx="0" cy="0" r="12" fill="none" stroke="#ef4444" stroke-width="2">
      <animate attributeName="r" values="6;22" dur="1.2s" repeatCount="indefinite"/>
      <animate attributeName="stroke-opacity" values="1;0" dur="1.2s" repeatCount="indefinite"/>
    </circle>
    <circle cx="0" cy="0" r="5" fill="#ef4444"/>
    <!-- Pointing Hand Vector -->
    <g transform="rotate(-30) translate(-10, -5)">
      <path d="M 0 10 L 0 25 C 0 28, 4 30, 8 30 C 12 30, 14 28, 14 25 L 14 12 C 14 10, 16 9, 17 9 C 19 9, 20 11, 20 12 L 20 18 C 20 19, 22 18, 23 18 C 24 18, 25 19, 25 20 L 25 25 C 25 32, 17 35, 10 35 L 6 35 C 0 35, -5 30, -5 24 L -5 10 C -5 7, -2 5, 0 5 C 2 5, 5 7, 5 10 L 5 18 L 0 18 Z" fill="#ffedd5" stroke="#ea580c" stroke-width="2"/>
    </g>
    <rect x="-35" y="32" width="70" height="15" rx="3" fill="#ef4444"/>
    <text x="0" y="42" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">{label}</text>
  </g>
"""

def get_custom_session(num):
    if num == 1:
        return f"""# Session 01: Arduino Uno & Breadboard Prototyping 🔌

**Class 5 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Welcome to the Hardware Lab! 🛠️
![Arduino & Breadboard Lab](https://images.unsplash.com/photo-1553406830-ef2513669743?w=800&q=80)

> **Arduino Uno (Brain) aur Solderless Breadboard (Playground) ke coordinate connections seekhna aur apna pehla manual circuit design karna!**

Hey young engineers! Aaj se hum advanced physical computing and hardware programming ki series start kar rahe hain. 
Is session me hum seekhenge:
* **Microcontroller board** kya hota hai.
* **Breadboard** circuits ko solder kiye bina kaise design karte hain.
* Safe power distribution and first live circuit building blocks.

---

## 📸 Slide 2: Meet the Brain: Arduino Uno Anatomy
<svg width="420" height="240" viewBox="0 0 420 240" style="display:block; margin:15px auto; background:#0f172a; border:2px solid #38bdf8; border-radius:10px; font-family:sans-serif;">
  <!-- Arduino Board Body -->
  <rect x="50" y="30" width="300" height="180" rx="10" fill="#005f73" stroke="#0096c7" stroke-width="3"/>
  <rect x="65" y="25" width="270" height="190" rx="6" fill="#0077b6" opacity="0.15"/>

  <!-- USB Connector -->
  <rect x="25" y="55" width="45" height="35" rx="3" fill="#cbd5e1" stroke="#94a3b8" stroke-width="2"/>
  <text x="47" y="77" font-size="7" fill="#475569" font-weight="bold">USB</text>

  <!-- Power Jack -->
  <rect x="40" y="140" width="40" height="45" rx="3" fill="#1e293b" stroke="#0f172a" stroke-width="2"/>
  <text x="60" y="167" font-size="7" fill="#94a3b8" font-weight="bold">DC IN</text>

  <!-- ATmega328P Chip -->
  <rect x="170" y="110" width="130" height="30" rx="2" fill="#1e293b" stroke="#334155" stroke-width="2"/>
  <line x1="180" y1="110" x2="180" y2="105" stroke="#94a3b8" stroke-width="1.5"/>
  <line x1="200" y1="110" x2="200" y2="105" stroke="#94a3b8" stroke-width="1.5"/>
  <line x1="220" y1="110" x2="220" y2="105" stroke="#94a3b8" stroke-width="1.5"/>
  <line x1="240" y1="110" x2="240" y2="105" stroke="#94a3b8" stroke-width="1.5"/>
  <line x1="260" y1="110" x2="260" y2="105" stroke="#94a3b8" stroke-width="1.5"/>
  <line x1="280" y1="110" x2="280" y2="105" stroke="#94a3b8" stroke-width="1.5"/>
  <line x1="180" y1="140" x2="180" y2="145" stroke="#94a3b8" stroke-width="1.5"/>
  <line x1="200" y1="140" x2="200" y2="145" stroke="#94a3b8" stroke-width="1.5"/>
  <line x1="220" y1="140" x2="220" y2="145" stroke="#94a3b8" stroke-width="1.5"/>
  <line x1="240" y1="140" x2="240" y2="145" stroke="#94a3b8" stroke-width="1.5"/>
  <line x1="260" y1="140" x2="260" y2="145" stroke="#94a3b8" stroke-width="1.5"/>
  <line x1="280" y1="140" x2="280" y2="145" stroke="#94a3b8" stroke-width="1.5"/>
  <text x="235" y="129" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">ATmega328P (CPU)</text>

  <!-- Headers -->
  <!-- Digital pins header -->
  <rect x="130" y="38" width="180" height="12" rx="2" fill="#1e293b"/>
  <text x="220" y="47" font-size="7.5" fill="#f8fafc" text-anchor="middle">DIGITAL (PINS 0 - 13)</text>

  <!-- Power pins header -->
  <rect x="130" y="190" width="80" height="12" rx="2" fill="#1e293b"/>
  <text x="170" y="199" font-size="7" fill="#f8fafc" text-anchor="middle">POWER (5V, GND)</text>

  <!-- Analog pins header -->
  <rect x="230" y="190" width="80" height="12" rx="2" fill="#1e293b"/>
  <text x="270" y="199" font-size="7" fill="#f8fafc" text-anchor="middle">ANALOG IN (A0 - A5)</text>

  <!-- Labels -->
  <text x="330" y="222" font-size="8" fill="#e2e8f0" font-weight="bold">UNO R3</text>
</svg>

Arduino Uno Board ke core components:
* **Microcontroller (ATmega328P):** Ye board ka main storage aur brain processor hai jo user code instructions save and execute karta hai.
* **USB Interface Port:** Arduino ko programmer software/computer power feed source se link and upload channel code.
* **Digital Input/Output Pins:** High (5V) ya Low (0V) signal commands send/read process systems.
* **Analog Input Pins (A0-A5):** Potentiometer ya sensors se continuously variable signals metrics read.

---

## 📸 Slide 3: Meet the Playground: Solderless Breadboard
<svg width="420" height="200" viewBox="0 0 420 200" style="display:block; margin:15px auto; background:#0f172a; border:2px solid #ef4444; border-radius:10px; font-family:sans-serif;">
  <!-- Breadboard Base -->
  <rect x="40" y="30" width="340" height="140" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
  
  <!-- Outer power rails -->
  <!-- Positive red rail -->
  <line x1="50" y1="42" x2="370" y2="42" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="2 4"/>
  <text x="35" y="45" font-size="9" fill="#ef4444" font-weight="bold">+</text>
  
  <!-- Negative blue rail -->
  <line x1="50" y1="52" x2="370" y2="52" stroke="#3b82f6" stroke-width="1.5" stroke-dasharray="2 4"/>
  <text x="35" y="55" font-size="9" fill="#3b82f6" font-weight="bold">-</text>

  <!-- Center divider (Insulation trench) -->
  <rect x="40" y="96" width="340" height="8" fill="#e2e8f0"/>
  <text x="210" y="103" font-size="6" fill="#64748b" text-anchor="middle">CENTER TRENCH (ISOLATION ZONE)</text>

  <!-- Component Terminal rows columns holes grids -->
  <!-- Row group A (top rows) -->
  <g fill="#475569">
    <circle cx="60" cy="70" r="1.5"/><circle cx="80" cy="70" r="1.5"/><circle cx="100" cy="70" r="1.5"/><circle cx="120" cy="70" r="1.5"/>
    <circle cx="60" cy="78" r="1.5"/><circle cx="80" cy="78" r="1.5"/><circle cx="100" cy="78" r="1.5"/><circle cx="120" cy="78" r="1.5"/>
    <circle cx="60" cy="86" r="1.5"/><circle cx="80" cy="86" r="1.5"/><circle cx="100" cy="86" r="1.5"/><circle cx="120" cy="86" r="1.5"/>
    
    <circle cx="300" cy="70" r="1.5"/><circle cx="320" cy="70" r="1.5"/><circle cx="340" cy="70" r="1.5"/><circle cx="360" cy="70" r="1.5"/>
    <circle cx="300" cy="78" r="1.5"/><circle cx="320" cy="78" r="1.5"/><circle cx="340" cy="78" r="1.5"/><circle cx="360" cy="78" r="1.5"/>
    <circle cx="300" cy="86" r="1.5"/><circle cx="320" cy="86" r="1.5"/><circle cx="340" cy="86" r="1.5"/><circle cx="360" cy="86" r="1.5"/>
  </g>

  <!-- Row group B (bottom rows) -->
  <g fill="#475569">
    <circle cx="60" cy="114" r="1.5"/><circle cx="80" cy="114" r="1.5"/><circle cx="100" cy="114" r="1.5"/><circle cx="120" cy="114" r="1.5"/>
    <circle cx="60" cy="122" r="1.5"/><circle cx="80" cy="122" r="1.5"/><circle cx="100" cy="122" r="1.5"/><circle cx="120" cy="122" r="1.5"/>
    <circle cx="60" cy="130" r="1.5"/><circle cx="80" cy="130" r="1.5"/><circle cx="100" cy="130" r="1.5"/><circle cx="120" cy="130" r="1.5"/>
    
    <circle cx="300" cy="114" r="1.5"/><circle cx="320" cy="114" r="1.5"/><circle cx="340" cy="114" r="1.5"/><circle cx="360" cy="114" r="1.5"/>
    <circle cx="300" cy="122" r="1.5"/><circle cx="320" cy="122" r="1.5"/><circle cx="340" cy="122" r="1.5"/><circle cx="360" cy="122" r="1.5"/>
    <circle cx="300" cy="130" r="1.5"/><circle cx="320" cy="130" r="1.5"/><circle cx="340" cy="130" r="1.5"/><circle cx="360" cy="130" r="1.5"/>
  </g>

  <!-- Bottom power rails -->
  <line x1="50" y1="150" x2="370" y2="150" stroke="#ef4444" stroke-width="1.5" stroke-dasharray="2 4"/>
  <line x1="50" y1="160" x2="370" y2="160" stroke="#3b82f6" stroke-width="1.5" stroke-dasharray="2 4"/>

  <!-- Vertical highlight loops representing internal connections -->
  <rect x="76" y="65" width="8" height="26" rx="2" fill="none" stroke="#22c55e" stroke-width="1.5" stroke-dasharray="1 1"/>
  <text x="80" y="59" font-size="5" fill="#22c55e" font-weight="bold" text-anchor="middle">Row Connect</text>
  
  <text x="210" y="180" font-size="8.5" fill="#0f172a" font-weight="bold" text-anchor="middle">Horizontal Power Rails | Vertical Component Lanes</text>
</svg>

Solderless Breadboard ka internal structure:
* **Power Rails (+ and -):** Top and bottom lines horizontally connected hot tracks (red line runs positive supply, blue line runs negative ground).
* **Terminal Lanes (vertical rows):** Middle part ki columns vertical lanes connected rehti hain (e.g. Pin A, B, C, D, E internally connected line segments).
* **Center trench:** Separates column groups. This protects IC legs from shorting, allowing pins separation.

---

## 📸 Slide 4: Connecting the Power Rails (Power Bridge)
<svg width="420" height="220" viewBox="0 0 420 220" style="display:block; margin:15px auto; background:#0f172a; border:2px solid #22c55e; border-radius:10px; font-family:sans-serif;">
  <!-- Arduino schematic outline -->
  <g transform="translate(10, 40)">
    <rect x="0" y="0" width="130" height="120" rx="5" fill="#005f73" stroke="#0096c7" stroke-width="2"/>
    <text x="65" y="20" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Arduino Uno</text>
    
    <!-- Red Terminal 5V Pin -->
    <circle cx="110" cy="50" r="5" fill="#ef4444"/>
    <text x="95" y="53" font-size="8" font-weight="bold" fill="#ffffff">5V</text>
    
    <!-- Black Terminal GND Pin -->
    <circle cx="110" cy="80" r="5" fill="#3b82f6"/>
    <text x="95" y="83" font-size="8" font-weight="bold" fill="#ffffff">GND</text>
  </g>

  <!-- Breadboard schematic outline -->
  <g transform="translate(200, 30)">
    <rect x="0" y="0" width="200" height="140" rx="5" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
    <text x="100" y="18" font-size="9" fill="#1e293b" font-weight="bold" text-anchor="middle">Breadboard Base</text>
    
    <!-- Power rails lanes representation -->
    <line x1="10" y1="40" x2="190" y2="40" stroke="#ef4444" stroke-width="3"/>
    <text x="100" y="37" font-size="6.5" fill="#ef4444" font-weight="bold" text-anchor="middle">+ Positive Red Rail</text>
    
    <line x1="10" y1="110" x2="190" y2="110" stroke="#3b82f6" stroke-width="3"/>
    <text x="100" y="125" font-size="6.5" fill="#3b82f6" font-weight="bold" text-anchor="middle">- Negative Ground Rail</text>
  </g>

  <!-- Wires connections path -->
  <!-- Positive red wire -->
  <path d="M 120 90 C 140 90, 160 70, 210 70" fill="none" stroke="#ef4444" stroke-width="3" stroke-linecap="round"/>
  <circle cx="210" cy="70" r="4" fill="#ef4444"/>
  
  <!-- Negative blue wire -->
  <path d="M 120 120 C 140 120, 160 140, 210 140" fill="none" stroke="#3b82f6" stroke-width="3" stroke-linecap="round"/>
  <circle cx="210" cy="140" r="4" fill="#3b82f6"/>
</svg>

Power bridge connect karne ka tarika:
1. **Red Jumper Wire:** Connect one end to Arduino **5V Pin** and second end to Breadboard **Red Rail (+)**.
2. **Black/Blue Jumper Wire:** Connect one end to Arduino **GND Pin** and second end to Breadboard **Blue/Black Rail (-)**.
3. Ab humare pooray breadboard rails me positive 5V supply line active ho chuki hai!

---

## 📸 Slide 5: Build Your First Circuit: Live LED! 💡
<svg width="420" height="220" viewBox="0 0 420 220" style="display:block; margin:15px auto; background:#0f172a; border:2px solid #f59e0b; border-radius:10px; font-family:sans-serif;">
  <!-- Breadboard layout background -->
  <rect x="80" y="20" width="260" height="180" rx="8" fill="#f8fafc" stroke="#cbd5e1" stroke-width="2"/>
  
  <!-- Positive (+) Rail -->
  <line x1="90" y1="35" x2="330" y2="35" stroke="#ef4444" stroke-width="2"/>
  <!-- Negative (-) Rail -->
  <line x1="90" y1="185" x2="330" y2="185" stroke="#3b82f6" stroke-width="2"/>

  <!-- Resistor component -->
  <!-- Left pin connect to Positive rail -->
  <circle cx="150" cy="35" r="3.5" fill="#f59e0b"/>
  <!-- Right pin connects to component lane row 5 -->
  <circle cx="180" cy="80" r="3.5" fill="#f59e0b"/>
  <path d="M 150 35 L 150 60 L 160 60 L 163 55 L 167 65 L 171 55 L 175 65 L 180 60 L 180 80" fill="none" stroke="#a855f7" stroke-width="2"/>
  <text x="195" y="60" font-size="6" fill="#a855f7" font-weight="bold">220Ω Resistor</text>

  <!-- LED component -->
  <!-- Anode (long leg) connects to same vertical lane (row 5) -->
  <circle cx="180" cy="80" r="4.5" fill="#22c55e"/>
  <!-- Cathode (short leg) connects to negative rail directly -->
  <path d="M 180 80 L 180 130 C 180 160, 220 185, 220 185" fill="none" stroke="#ef4444" stroke-width="2"/>
  <circle cx="220" cy="185" r="4" fill="#3b82f6"/>
  
  <!-- LED bulb shape -->
  <circle cx="180" cy="115" r="14" fill="#ef4444" opacity="0.8"/>
  <path d="M 172 125 L 188 125 L 185 132 L 175 132 Z" fill="#94a3b8"/>
  <text x="180" y="118" font-size="6.5" font-weight="bold" fill="#ffffff" text-anchor="middle">LED</text>
  
  <!-- Glow rays -->
  <line x1="160" y1="115" x2="150" y2="115" stroke="#f59e0b" stroke-width="1.5"/>
  <line x1="200" y1="115" x2="210" y2="115" stroke="#f59e0b" stroke-width="1.5"/>
  <line x1="180" y1="95" x2="180" y2="85" stroke="#f59e0b" stroke-width="1.5"/>

  {get_hand_svg(150, 35, "Bridge +")}
</svg>

Live LED loop connection guidelines:
1. **Resistor (220Ω):** Connect one leg of the resistor to the **Red positive rail (+)** and the second leg to any middle component pin lane (e.g. Lane 10).
2. **LED Long Leg (+):** Place it into the **same vertical lane** where the resistor's second leg is connected (Lane 10).
3. **LED Short Leg (-):** Insert it directly into the **Blue negative rail (-)**.
4. **Result:** Current flows from 5V (+) -> Resistor -> LED (produces glow) -> Ground (-). We have a successful closed loop circuit!

---

## 📸 Slide 6: Student Action Plan: Let's Build! 🎮
* **Your Mission: Assemble your first breadboard LED glowing circuit!**
  1. Open your physical Tier 2 kit bag.
  2. Find these components: **Arduino Uno board, Solderless Breadboard, Red LED, 220Ω Resistor, and Jumper Wires**.
  3. Connect the **Power Bridge** from Arduino (5V and GND) to the breadboard side rails.
  4. Carefully insert the **220Ω Resistor** between the positive rail (+) and the vertical component lane.
  5. Align the **LED legs**: Anode (long leg) inside the resistor lane and Cathode (short leg) inside the negative ground rail.
  6. Connect Arduino Uno to power using the USB cable. Watch your LED light up immediately!
  
> [!WARNING]
> **Resistor Alert:** Kabhi bhi LED ko directly 5V power supply se bina Resistor ke connect mat karein, warna excess electrical current se LED instantly burn out/damage ho sakti hai!

---

## 📸 Slide 7: Pilot Quiz & Knowledge Check
* **Q1: Breadboard positive and negative rails ko internally kaise check karein?**  
  *Answer:* Power rails horizontally end-to-end connected hoti hain, isliye kisi bhi ek hole me connect kiya gaya switch pooray rail column path par power supply distribute kar deta hai.
* **Q2: Resistor logic control value target circuit me kya function play karta hai?**  
  *Answer:* Current limit control function. Resistor electricity flow voltage reduce karta hai taaki digital actuators safely operate ho sakein.
* **Q3: Long leg check value cathode or anode parameters state?**  
  *Answer:* Long leg humesha Anode (+) positive direction link indicate karti hai aur short leg Cathode (-) ground connection indicate karti hai.
"""
    return ""
