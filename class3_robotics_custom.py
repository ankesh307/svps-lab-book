# Class 3 Robotics Custom Override Content - Fully Fleshed Sessions 1-10 Masterpieces
import os
import base64

def get_base64_image(image_filename):
    image_path = os.path.join(r"C:\Users\ankes\.gemini\antigravity\scratch\curriculum_app\images", image_filename)
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
    # Mapping table: new index -> original index
    mapping = {
        1: 1, # Revision
        2: 2, # Component Expert
        3: 3, # Battery & Power
        4: 4, # Circuit Troubleshooting
        5: 5, # Series vs Parallel LEDs
        6: 6, # Two-Switch Circuit
        7: 7, # Emergency Light
        8: 8, # Decorative Lighting
        9: 9, # Advanced Buzzer
        10: 10, # Quiz + Practical Test
        11: 11, # Motor Performance (originally 11)
        12: 12, # Propeller Engineering (originally 12)
        13: 14, # Gear Motor Load Test (originally 14)
        14: 15, # Better Car Design (originally 15)
        15: 16, # Straight Driving Challenge (originally 16)
        16: 18, # Speed Challenge (originally 18)
        17: 20, # Robot Delivery Challenge (originally 20)
        18: 22, # Smart Traffic Signal (originally 22)
        19: 28, # 3D Pen Engineering (originally 28)
        20: 30, # Robotics Exhibition (originally 30)
    }
    mapped_num = mapping.get(num)
    if not mapped_num:
        return ""
    num = mapped_num

    s1 = get_base64_image("kit_overview.jpg")
    s2 = get_base64_image("battery_snap.jpg")
    s5 = get_base64_image("leds_buzzer.jpg")
    s7 = get_base64_image("switches_buttons.jpg")
    s8 = get_base64_image("three_d_pen_filaments.jpg")
    
    # SESSION 1: ROBOTICS REVISION & CHALLENGE (12 Slides)
    if num == 1:
        return f"""# Session 01: Robotics Revision & Challenge 🤖

**Class 3 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Welcome to Class 3 Robotics & Revision Goals
![Electronics Lab](https://images.unsplash.com/photo-1507413245164-6160d8298b31?w=800&q=80)

> **Class 2 ke electronics aur control concepts ko advanced detail ke sath revise karna**

Robotics ke automatic systems ko build karne se pehle hume manually wired circuits ke electrical paths aur control points ko master karna hoga. Aaj hum kit ke components ko revision challenge ke through connect aur test karenge.
* **Keywords:** `Conductors` | `Insulators` | `Polarity` | `Continuity`
* **Session Target:** Master closed-loop circuit assembly with a switch, an LED, and a buzzer.

---

## 📸 Slide 2: The Atomic Science of Electricity (Conductors)
<svg width="350" height="180" viewBox="0 0 350 180" style="display:block; margin:15px auto; background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; font-family:sans-serif;">
  <g transform="translate(100, 90)">
    <circle cx="0" cy="0" r="22" fill="#ea580c" opacity="0.8"/>
    <text x="0" y="4" font-size="9" fill="#ffffff" font-weight="bold" text-anchor="middle">Nucleus</text>
    <circle cx="0" cy="0" r="50" fill="none" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,4"/>
    <circle cx="50" cy="0" r="5" fill="#0ea5e9"/>
    <text x="50" y="-8" font-size="8" fill="#0ea5e9" font-weight="bold" text-anchor="middle">Free Electron</text>
  </g>
  <g transform="translate(250, 90)">
    <circle cx="0" cy="0" r="22" fill="#ea580c" opacity="0.8"/>
    <text x="0" y="4" font-size="9" fill="#ffffff" font-weight="bold" text-anchor="middle">Nucleus</text>
    <circle cx="0" cy="0" r="50" fill="none" stroke="#94a3b8" stroke-width="1.5" stroke-dasharray="4,4"/>
  </g>
  <path d="M 155 85 Q 175 70 195 85" fill="none" stroke="#0ea5e9" stroke-width="2.5" stroke-dasharray="4,2"/>
  <text x="175" y="60" font-size="8" fill="#0ea5e9" font-weight="bold" text-anchor="middle">Electron Hop ⚡</text>
</svg>

Electricity hamare wires me kaise behti hai? Aaiye atomic level par iske flow logic ko samajhte hain:
* **Copper Atomic Structure:** Copper (तांबा) ek metal hai jiske outer orbit me electrons loosely bound hote hain. Jab voltage apply kiya jata, toh yeh free electrons ek atom se dusre atom par push hote hain.
* **Electron Flow:** Electrons positive potential (+) ki taraf attraction ke chalte travel karte hain. Isi flow rate ko hum electrical current kehte hain.

---

## 📸 Slide 3: Insulators & Safety Wires Coating
<svg width="350" height="180" viewBox="0 0 350 180" style="display:block; margin:15px auto; background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; font-family:sans-serif;">
  <rect x="50" y="40" width="250" height="100" rx="10" fill="#ef4444" fill-opacity="0.1" stroke="#ef4444" stroke-width="2"/>
  <rect x="50" y="70" width="250" height="40" fill="#ea580c" stroke="#c2410c" stroke-width="2"/>
  <text x="175" y="94" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">Copper Core (Conductor)</text>
  <text x="175" y="55" font-size="10" font-weight="bold" fill="#b91c1c" text-anchor="middle">Plastic Shield (Insulator)</text>
</svg>

* **Insulator Logic:** Plastic, rubber aur glass ke atoms me electrons tightly bound hote hain, jiski wajah se yeh current ko pass hone se block karte hain.
* **Safety Sheath:** Hamare snap connectors aur jumpers ke upar colored plastic covering hoti hai taaki:
  1. Hum safe rahein aur electric shock na lage.
  2. Red (+) aur Black (-) bare wires touch hokar short circuit na karein.

---

## 📸 Slide 4: Power Source — 9V Battery & Chemical Reaction
<svg width="350" height="180" viewBox="0 0 350 180" style="display:block; margin:15px auto; background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; font-family:sans-serif;">
  <rect x="100" y="20" width="150" height="140" rx="8" fill="#1e293b" stroke="#0f172a" stroke-width="2"/>
  <line x1="175" y1="20" x2="175" y2="160" stroke="#475569" stroke-width="2" stroke-dasharray="4,4"/>
  <text x="135" y="85" font-size="28" font-weight="bold" fill="#ef4444" text-anchor="middle">+</text>
  <text x="135" y="115" font-size="8" fill="#94a3b8" text-anchor="middle">Anode (+)</text>
  <text x="215" y="85" font-size="28" font-weight="bold" fill="#3b82f6" text-anchor="middle">-</text>
  <text x="215" y="115" font-size="8" fill="#94a3b8" text-anchor="middle">Cathode (-)</text>
  <text x="175" y="150" font-size="9" fill="#10b981" font-weight="bold" text-anchor="middle">Chemical Cell</text>
</svg>

* **Inside the Battery:** 9V battery ke andar chemicals reacting states electrons force create karti hain. Negative terminal par extra electrons accumulate hote hain aur positive terminal par electrons ki shortage hoti hai.
* **Voltage (Electrical Pressure):** 9 Volts ka chemical force electrons ko push karta hai.
* **Polarized snap connectors:**
  * **🔴 Red terminal snap (+):** Power output terminal.
  * **⚫ Black terminal snap (-):** Return path/Ground terminal.

---

## 📸 Slide 5: Control Gates — Slide Switch Mechanics
<svg width="350" height="180" viewBox="0 0 350 180" style="display:block; margin:15px auto; background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; font-family:sans-serif;">
  <rect x="120" y="20" width="110" height="40" rx="4" fill="#475569"/>
  <rect x="140" y="60" width="70" height="15" fill="#f59e0b" rx="2"/>
  <rect x="110" y="110" width="15" height="40" fill="#94a3b8"/>
  <rect x="165" y="110" width="15" height="40" fill="#94a3b8"/>
  <rect x="220" y="110" width="15" height="40" fill="#94a3b8"/>
  <text x="117" y="165" font-size="8" fill="#475569" text-anchor="middle">Pin 1 (In)</text>
  <text x="172" y="165" font-size="8" fill="#475569" text-anchor="middle">Pin 2 (Out)</text>
  <text x="227" y="165" font-size="8" fill="#475569" text-anchor="middle">Pin 3 (NC)</text>
  <path d="M 140 70 L 205 70" fill="none" stroke="#10b981" stroke-width="3"/>
  <text x="172" y="92" font-size="8" font-weight="bold" fill="#10b981" text-anchor="middle">ON Bridge</text>
</svg>

Slide switch latching mechanism par kaise control rules execute karta hai?
* **Solder tabs (Pins):** Switch ke niche 3 metal pins hote hain:
  * **Pin 1 (Left):** Connects to battery Positive red wire snap. (Current Input).
  * **Pin 2 (Center):** Connects to LED Anode (+) long leg. (Current Controlled Output).
  * **Pin 3 (Right):** NC (Not Connected) state.
* **The Bridge:** Slide switch ko slide karne par internal metal plate Pin 1 aur Pin 2 ko bridge karti hai, loop complete ho jata hai (ON).

---

## 📸 Slide 6: Visual Indicators — LED Anatomy & Diodes
<svg width="350" height="180" viewBox="0 0 350 180" style="display:block; margin:15px auto; background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; font-family:sans-serif;">
  <path d="M 130 130 Q 130 30 175 30 Q 220 30 220 130 Z" fill="#10b981" fill-opacity="0.1" stroke="#10b981" stroke-width="2"/>
  <line x1="155" y1="90" x2="155" y2="170" stroke="#ea580c" stroke-width="3" stroke-linecap="round"/>
  <line x1="195" y1="100" x2="195" y2="155" stroke="#3b82f6" stroke-width="3" stroke-linecap="round"/>
  <text x="145" y="165" font-size="8" fill="#ea580c" font-weight="bold" text-anchor="middle">Long Leg (+)</text>
  <text x="215" y="150" font-size="8" fill="#3b82f6" font-weight="bold" text-anchor="middle">Short Leg (-)</text>
  <path d="M 190 100 L 200 90 L 195 90 Z" fill="#cbd5e1"/>
  <circle cx="195" cy="88" r="3" fill="#ef4444"/>
</svg>

LED simple indicator nahi balki semiconductor diode logic hai:
* **Unidirectional flow:** Current ko Anode (+) se Cathode (-) ki taraf hi flow hone deta hai. Reverse direction flow block kar deta hai.
* **Terminal checks:**
  * **Long Lead (Anode / +):** Connect to Switch Pin 2.
  * **Short Lead (Cathode / -):** Connect to Buzzer positive leg.

---

## 📸 Slide 7: Sound Alerts — Piezoelectric Buzzers
<svg width="350" height="180" viewBox="0 0 350 180" style="display:block; margin:15px auto; background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; font-family:sans-serif;">
  <circle cx="175" cy="90" r="50" fill="#1e293b" stroke="#0f172a" stroke-width="3"/>
  <circle cx="175" cy="90" r="12" fill="#0f172a"/>
  <path d="M 240 70 Q 260 90 240 110" fill="none" stroke="#ef4444" stroke-width="3" stroke-linecap="round"/>
  <path d="M 255 60 Q 285 90 255 120" fill="none" stroke="#ef4444" stroke-width="3" stroke-opacity="0.6" stroke-linecap="round"/>
  <text x="175" y="155" font-size="10" font-weight="bold" fill="#1e293b" text-anchor="middle">Piezo Crystal</text>
</svg>

* **Vibrating Disk:** Buzzer ke andar dynamic piezo crystal plate hoti hai jo voltage changes hone par oscillate karti hai aur sharp acoustic beep generate karti hai.
* **Polarity Rules:** Active buzzer polarity sensitive hota hai. Iski long leg (+) positive side aur short leg (-) negative black wire side connect honi chahiye.

---

## 📸 Slide 8: Interactive Wiring Map (Master SVG) 🎨
<svg width="450" height="250" viewBox="0 0 450 250" style="display: block; margin: 20px auto; background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 12px; font-family: sans-serif;">
  <defs>
    <pattern id="grid_master" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#f1f5f9" stroke-width="1"/>
    </pattern>
  </defs>
  <rect width="100%" height="100%" fill="url(#grid_master)" rx="12"/>
  
  <!-- 9V Battery -->
  <g transform="translate(20, 50)">
    <rect x="0" y="20" width="70" height="110" rx="6" fill="#1e293b" stroke="#0f172a" stroke-width="3"/>
    <rect x="15" y="8" width="15" height="12" fill="#94a3b8"/>
    <rect x="40" y="8" width="15" height="12" fill="#cbd5e1"/>
    <text x="35" y="85" font-size="11" font-weight="bold" fill="#ffffff" text-anchor="middle">9V BATT</text>
    <circle cx="22" cy="42" r="7" fill="#ef4444"/>
    <text x="22" y="46" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">+</text>
    <circle cx="48" cy="42" r="7" fill="#3b82f6"/>
    <text x="48" y="46" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">-</text>
  </g>

  <!-- Slide Switch with labeled pins -->
  <g transform="translate(140, 50)">
    <rect x="0" y="20" width="90" height="50" rx="4" fill="#475569" stroke="#334155" stroke-width="2"/>
    <rect x="35" y="10" width="20" height="10" fill="#e2e8f0"/>
    <circle cx="20" cy="85" r="5" fill="#cbd5e1"/>
    <circle cx="45" cy="85" r="5" fill="#cbd5e1"/>
    <circle cx="70" cy="85" r="5" fill="#cbd5e1"/>
    <text x="20" y="98" font-size="7" fill="#475569" text-anchor="middle">Pin 1 (In)</text>
    <text x="45" y="98" font-size="7" fill="#475569" text-anchor="middle">Pin 2 (Out)</text>
    <text x="70" y="98" font-size="7" fill="#475569" text-anchor="middle">Pin 3 (NC)</text>
  </g>

  <!-- LED with legs -->
  <g transform="translate(260, 50)">
    <line x1="20" y1="80" x2="20" y2="130" stroke="#ef4444" stroke-width="3"/>
    <line x1="40" y1="80" x2="40" y2="115" stroke="#3b82f6" stroke-width="3"/>
    <path d="M 10 70 Q 10 20 30 20 Q 50 20 50 70 Z" fill="#10b981" fill-opacity="0.8" stroke="#047857" stroke-width="2"/>
    <circle cx="20" cy="135" r="5" fill="#ef4444"/>
    <circle cx="40" cy="120" r="5" fill="#3b82f6"/>
    <text x="30" y="50" font-size="9" font-weight="bold" fill="#047857" text-anchor="middle">LED</text>
  </g>

  <!-- Buzzer -->
  <g transform="translate(350, 50)">
    <circle cx="30" cy="50" r="22" fill="#000000" stroke="#334155" stroke-width="3"/>
    <line x1="20" y1="72" x2="20" y2="120" stroke="#ef4444" stroke-width="3"/>
    <line x1="40" y1="72" x2="40" y2="105" stroke="#3b82f6" stroke-width="3"/>
    <circle cx="20" cy="125" r="5" fill="#ef4444"/>
    <circle cx="40" cy="110" r="5" fill="#3b82f6"/>
    <text x="30" y="15" font-size="9" font-weight="bold" fill="#0f172a" text-anchor="middle">BUZZER</text>
  </g>

  <!-- Connections -->
  <path d="M 42 50 L 42 25 L 160 25 L 160 50" fill="none" stroke="#ef4444" stroke-width="3" stroke-linecap="round"/>
  <rect x="55" y="16" width="90" height="12" fill="#ef4444" rx="2"/>
  <text x="100" y="24" font-size="6.5" font-weight="bold" fill="#ffffff" text-anchor="middle">🔴 Red Wire: 9V Power In</text>

  <path d="M 185 50 L 185 25 L 280 25 L 280 50" fill="none" stroke="#eab308" stroke-width="3" stroke-linecap="round"/>
  <rect x="195" y="16" width="80" height="12" fill="#eab308" rx="2"/>
  <text x="235" y="24" font-size="6.5" font-weight="bold" fill="#1e293b" text-anchor="middle">🟡 Yellow: Switch to LED Anode</text>

  <path d="M 300 50 L 300 25 L 370 25 L 370 50" fill="none" stroke="#3b82f6" stroke-width="3" stroke-linecap="round"/>
  <path d="M 68 50 L 68 180 L 390 180 L 390 50" fill="none" stroke="#1e293b" stroke-width="3" stroke-linecap="round"/>
  <rect x="180" y="174" width="110" height="12" fill="#1e293b" rx="2"/>
  <text x="235" y="182" font-size="6.5" font-weight="bold" fill="#ffffff" text-anchor="middle">⚫ Black Wire: Ground Return Loop</text>

  {get_hand_svg(185, 95, "Pin 2 Output")}
</svg>

---

## 📸 Slide 9: Step-by-Step Connection Instructions
![Assembly Action](https://images.unsplash.com/photo-1581092160607-ee22621dd758?w=800&q=80)

* **[ ] Step 1:** Connect the battery snap connector to the 9V battery terminals.
* **[ ] Step 2:** Connect the snap **Red Wire (+)** to **Slide Switch Pin 1 (Leftmost input)**.
  * *Why:* Power source voltage switch gate tak lane ke liye.
* **[ ] Step 3:** Connect a **Yellow wire** from **Slide Switch Pin 2 (Center output)** to **LED Long leg (+)**.
  * *Why:* Slide toggle control loop state LED tak link karne ke liye.
* **[ ] Step 4:** Connect a **Blue wire** from **LED Short leg (-)** to **Buzzer Long leg (+)**.
  * *Why:* Series circuit chain complete karne ke liye.
* **[ ] Step 5:** Connect the **Buzzer Short leg (-)** to the snap **Black wire (-)**.
  * *Why:* Loop return ground line se complete karne ke liye.

---

## 📸 Slide 10: Troubleshooting Scenarios
![Troubleshooting inspecting](https://images.unsplash.com/photo-1581092335397-9583fe92d232?w=800&q=80)

* **Scenario 1: No sound, no light when switch is slid to ON.**
  * *Fix:* Switch pins check karein, wires rightmost Pin 3 (NC) me toh nahi hain? Shift wire to Pin 2 (Center).
* **Scenario 2: Buzzer rings, but LED remains OFF.**
  * *Fix:* LED is reversed! Flip the LED legs so the long leg (+) is connected to the yellow wire from the switch output.
* **Scenario 3: Wires aapas me directly touch ho gaye aur battery gets warm.**
  * *Fix:* Short circuit! Red and black wires are touching directly. Disconnect the snap connector immediately and inspect nodes.

---

## 📸 Slide 11: Student Workbook Log & Exercise
![Student Writing Log](https://images.unsplash.com/photo-1456513080510-7bf3a84b82f8?w=800&q=80)

Apni workbook copy me observations data record table sketch karein:
* Table headings: Switch state, LED status (ON/OFF), Buzzer sound (Yes/No), Loop logic (Open/Closed).
* **Sketch Challenge:** Draw a schematic diagram showing two LEDs in a series chain loop controlled by a slide switch.

---

## 📸 Slide 12: Concept Assessment Quiz
![Quiz Paper](https://images.unsplash.com/photo-1434030216411-0b793f4b4173?w=800&q=80)

* **Q1: Slide Switch ke Pin 2 ko switch circuit me output terminal kyu joda jata hai?**  
  *Answer:* Slider move karne par internally metal strip Pin 1 aur Pin 2 ke gap bridge contact close karti hai.
* **Q2: Diode components reverse connections blocking logic details?**  
  *Answer:* Semiconductor barrier reverse current limits check infinite resistance state badhata hai.
* **Q3: Short loop configurations parameters battery heating kyu cause karte hain?**  
  *Answer:* Zero load parameters current output surge power limit increase heat generate.
"""

    # SESSION 2: COMPONENT EXPERT (Fully Detailed Overhaul - 11 Slides)
    elif num == 2:
        return f"""# Session 02: Component Expert 🕵️

**Class 3 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Component Expert Intro
![Lab Equipment](https://images.unsplash.com/photo-1581092160607-ee22621dd758?w=800&q=80)

> **Junior Maker Kit ke har component ke internal technical properties, limits aur safety margins ko master karna**

Robotics projects build karte time components ke behavior, voltage thresholds aur limits ki absolute clarity hona zaroori hai. Aaiye in specs ko scientifically samajhte hain!
* **Keywords:** `Specs Sheet` | `Torque Limits` | `Voltage Thresholds` | `Current Bounds`
* **Session Goal:** Understand operational limits of battery, motors, LEDs, buzzers, and 3D pen.

---

## 📸 Slide 2: Power Specs — 9V Battery Discharge Curve
<svg width="350" height="180" viewBox="0 0 350 180" style="display:block; margin:15px auto; background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; font-family:sans-serif;">
  <line x1="50" y1="140" x2="300" y2="140" stroke="#1e293b" stroke-width="2"/>
  <line x1="50" y1="20" x2="50" y2="140" stroke="#1e293b" stroke-width="2"/>
  <text x="35" y="25" font-size="8" fill="#475569" font-weight="bold">9V</text>
  <text x="35" y="70" font-size="8" fill="#475569" font-weight="bold">6V</text>
  <text x="35" y="140" font-size="8" fill="#475569" font-weight="bold">0V</text>
  <path d="M 50 25 Q 150 40 200 70 T 300 135" fill="none" stroke="#ef4444" stroke-width="3"/>
  <text x="175" y="160" font-size="8" fill="#475569" font-weight="bold" text-anchor="middle">Usage Time ➔</text>
  <line x1="50" y1="70" x2="300" y2="70" stroke="#eab308" stroke-dasharray="3,3"/>
  <rect x="210" y="75" width="80" height="12" fill="#fee2e2" rx="2"/>
  <text x="250" y="83" font-size="6.5" font-weight="bold" fill="#ef4444" text-anchor="middle">Drop Zone (Motors Slow)</text>
</svg>

9V Dry Cell battery continuous use hone par kaise behavior change karti hai?
* **Voltage Drain Curve:** Battery full charge par exactly 9.0V supply karti hai. But heavy motors use karne par voltage gradual decline (discharge) hota hai.
* **The 6.0V Threshold:** Jab battery voltage 6.0V se niche drop ho jata hai, tab components coordinate malfunction start karte hain:
  1. Gear motors start spinning too slow.
  2. Active buzzers make clicking or weak low-pitch tones.
  3. LEDs become very dim.

---

## 📸 Slide 3: Actuator Specs — BO Gear Motor Torque & Gear Train
<svg width="350" height="180" viewBox="0 0 350 180" style="display:block; margin:15px auto; background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; font-family:sans-serif;">
  <circle cx="120" cy="90" r="18" fill="none" stroke="#475569" stroke-width="3" stroke-dasharray="4,2"/>
  <circle cx="120" cy="90" r="6" fill="#475569"/>
  <circle cx="170" cy="90" r="36" fill="none" stroke="#f59e0b" stroke-width="3" stroke-dasharray="6,3"/>
  <circle cx="170" cy="90" r="8" fill="#f59e0b"/>
  <path d="M 115 65 A 25 25 0 0 1 135 65" fill="none" stroke="#475569" stroke-width="2" marker-end="url(#arrow)"/>
  <path d="M 160 45 A 50 50 0 0 0 200 45" fill="none" stroke="#f59e0b" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="145" y="150" font-size="9" font-weight="bold" fill="#1e293b" text-anchor="middle">Gear Reduction Ratio: 1:48</text>
</svg>

BO (Battery Operated) Gear Motor high load carriage kyu pull kar pati hai?
* **Internal Gear Reduction:** Motor ke metal casing ke andar total 4 plastic spur gears hote hain. Yeh gear train high rotation inputs ko reduce karke torque (spindle turning force) ko multiply karta hai.
* **Parameters Limits:**
  * **Ratio:** 1:48 reduction. (Motor shaft spins 48 times for 1 axle rotation).
  * **Safe Axle Load:** Up to 500 grams (0.5 kg). Isse zyada load par motor stall/lock ho jati hai.

---

## 📸 Slide 4: Thrust Specs — DC Toy Motor RPM vs Air Thrust
<svg width="350" height="180" viewBox="0 0 350 180" style="display:block; margin:15px auto; background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; font-family:sans-serif;">
  <rect x="110" y="60" width="100" height="60" rx="6" fill="#cbd5e1" stroke="#94a3b8" stroke-width="2"/>
  <line x1="210" y1="90" x2="250" y2="90" stroke="#94a3b8" stroke-width="4"/>
  <circle cx="230" cy="90" r="15" fill="none" stroke="#0ea5e9" stroke-width="1.5" stroke-dasharray="4,4"/>
  <circle cx="230" cy="90" r="22" fill="none" stroke="#0ea5e9" stroke-opacity="0.5" stroke-width="1.5" stroke-dasharray="4,4"/>
  <text x="160" y="94" font-size="10" font-weight="bold" fill="#1e293b" text-anchor="middle">Direct Drive</text>
  <text x="160" y="145" font-size="9" font-weight="bold" fill="#0284c7" text-anchor="middle">High Speed (10,000+ RPM) / Low Torque</text>
</svg>

Toy DC Motor and propeller blades assembly kyu different physics follow karte hain?
* **Direct Drive:** Gear motor ke contrary, isme koi internal gear speed reduction nahi hoti. Axle directly internal motor coils electromagnetic spin se connect rehta hai.
* **RPM limits:** 9V supply par direct running speed **10,000+ Rotations Per Minute** reach kar jati hai.
* **Air Displacement (Thrust):** Is spindle par propeller attach karne par blades high velocity air stream push generate karti hain jo propulsion generate karti hai.

---

## 📸 Slide 5: Output Specs — LED Forward Current Limits
<svg width="350" height="180" viewBox="0 0 350 180" style="display:block; margin:15px auto; background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; font-family:sans-serif;">
  <path d="M 120 100 L 120 40 L 160 70 Z" fill="#10b981" stroke="#047857" stroke-width="2"/>
  <line x1="160" y1="40" x2="160" y2="100" stroke="#047857" stroke-width="3"/>
  <line x1="100" y1="70" x2="180" y2="70" stroke="#047857" stroke-width="2"/>
  <path d="M 220 70 L 290 70" fill="none" stroke="#ef4444" stroke-width="3" marker-end="url(#arrow)"/>
  <text x="255" y="60" font-size="8" font-weight="bold" fill="#ef4444" text-anchor="middle">Max current: 20mA</text>
  <text x="175" y="140" font-size="9" fill="#475569" font-weight="bold" text-anchor="middle">Forward Voltage (Vf): 2.0V - 3.0V</text>
</svg>

LED ke current consumption levels kyu strictly limited hain?
* **Forward Current (If):** LED chip ka maximum safe current carrying capacity **20mA (Milli-Amperes)** hota hai.
* **Direct Power Hazard:** 9V battery snap ko directly LED legs par lagane se dynamic current 100mA+ overflow kar jata hai, jo LED ke fine internal wire links melt block kar deta hai.
* **Resistor/Load Series Connection:** Isiliye multi-LED grids ya warning systems series me wire connect karne par current levels divide rehte hain aur LED safe glow karti hai.

---

## 📸 Slide 6: Audio Specs — Active Buzzer decibel levels
<svg width="350" height="180" viewBox="0 0 350 180" style="display:block; margin:15px auto; background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; font-family:sans-serif;">
  <rect x="50" y="70" width="250" height="20" rx="4" fill="#e2e8f0"/>
  <rect x="50" y="70" width="200" height="20" rx="4" fill="#3b82f6"/>
  <line x1="100" y1="70" x2="100" y2="90" stroke="#1e293b" stroke-width="1.5"/>
  <line x1="200" y1="70" x2="200" y2="90" stroke="#1e293b" stroke-width="1.5"/>
  <text x="100" y="60" font-size="8" fill="#475569" text-anchor="middle">30dB (Whisper)</text>
  <text x="200" y="60" font-size="8" fill="#ef4444" font-weight="bold" text-anchor="middle">85dB (Buzzer Alert)</text>
  <text x="250" y="105" font-size="8" fill="#ef4444" font-weight="bold" text-anchor="middle">Piezo Alarm Limits</text>
</svg>

Active buzzer alert levels safe sound standard logic parameters check:
* **Decibel Output:** Supplies **85 decibels (dB)** at a distance of 10cm. (Normal human voice levels se high alerts).
* **Piezo Resonance:** Built-in internal oscillator circuit fixed frequency tone wave emit karta hai.
* **Usage warning:** Continuous close distance buzzer sounds ears safety bounds limits test coordinates check.

---

## 📸 Slide 7: Motion Specs — Coin Motor Eccentric Mass Dynamics
<svg width="350" height="180" viewBox="0 0 350 180" style="display:block; margin:15px auto; background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; font-family:sans-serif;">
  <circle cx="175" cy="90" r="50" fill="#cbd5e1" stroke="#94a3b8" stroke-width="3"/>
  <path d="M 175 90 L 210 65 A 40 40 0 0 1 210 115 Z" fill="#475569" stroke="#1e293b" stroke-width="2"/>
  <circle cx="175" cy="90" r="6" fill="#1e293b"/>
  <path d="M 215 50 Q 235 90 215 130" fill="none" stroke="#ef4444" stroke-width="2" stroke-dasharray="3,3"/>
  <text x="175" y="160" font-size="9" font-weight="bold" fill="#1e293b" text-anchor="middle">Asymmetric Rotating Weight (ERM)</text>
</svg>

Vibration Coin Motor silent mechanical oscillations kaise emit karti hai?
* **Eccentric Rotating Mass (ERM):** Motor shaft par ek asymmetric (आधा कटा हुआ) copper load mount hota hai.
* **Unbalanced Spin:** Jab motor high-speed speed bounds par spin karti hai, toh imbalance weight rotating axis shifting vibration waves emit karta hai.
* **Operational Limits:** Safe operating voltage range is 1.5V - 3.7V. Direct 9V battery voltage se connection components burn damages levels.

---

## 📸 Slide 8: Latching Switches vs Momentary Buttons
<svg width="350" height="180" viewBox="0 0 350 180" style="display:block; margin:15px auto; background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; font-family:sans-serif;">
  <g transform="translate(40, 40)">
    <rect x="0" y="10" width="110" height="50" rx="4" fill="#cbd5e1" stroke="#94a3b8" stroke-width="2"/>
    <rect x="45" y="0" width="20" height="10" fill="#3b82f6"/>
    <text x="55" y="80" font-size="10" font-weight="bold" fill="#1e293b" text-anchor="middle">Latching Switch</text>
    <text x="55" y="95" font-size="8" fill="#475569" text-anchor="middle">ON state permanent</text>
  </g>
  <g transform="translate(200, 40)">
    <rect x="0" y="10" width="110" height="50" rx="4" fill="#cbd5e1" stroke="#94a3b8" stroke-width="2"/>
    <circle cx="55" cy="15" r="12" fill="#ef4444"/>
    <text x="55" y="80" font-size="10" font-weight="bold" fill="#1e293b" text-anchor="middle">Momentary Button</text>
    <text x="55" y="95" font-size="8" fill="#475569" text-anchor="middle">ON only when pressed</text>
  </g>
</svg>

Switches mechanical connection states loops:
* **Latching Slide Switch:** State changes slider move coordinate lock permanent.
* **Momentary Push Button:** internal springs buttons pressure return systems. finger press tab tak loop ON.

---

## 📸 Slide 9: 3D Pen Nozzle Thermal Safety Limits
<svg width="350" height="180" viewBox="0 0 350 180" style="display:block; margin:15px auto; background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; font-family:sans-serif;">
  <polygon points="120,40 230,40 175,130" fill="#475569"/>
  <circle cx="175" cy="130" r="14" fill="#ef4444" fill-opacity="0.2"/>
  <circle cx="175" cy="130" r="6" fill="#ef4444"/>
  <rect x="200" y="110" width="80" height="15" fill="#ef4444" rx="2"/>
  <text x="240" y="121" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">HOT NOZZLE (190°C)</text>
</svg>

3D Pen filament extrusion parameters safety guides:
* **Extrusion Temperature:** PLA requires **190°C (Celsius)** nozzle heat. Nozzle metal tip ko touch karne par thermal burns hazard ho sakta hai.
* **Cooling phase:** Melted plastic 3-5 seconds me solidify ho jata hai, jisse structures build and join kiye jate hain.

---

## 📸 Slide 10: Step-by-Step Component Test Guide
* 🔴 **Step 1:** Mount a wheel on the BO Gear motor spindle axle shaft.
* 🔋 **Step 2:** Connect the 9V battery snap terminals.
* 🔴 **Step 3:** Touch the positive Red wire of the snap to the gear motor positive pin, and Black wire to the negative pin.
* 👆 **Step 4:** Try to stop the spinning wheel using your finger. Note down the high resistive force (Torque).
* 🌀 **Step 5:** Repeat the test with the Toy DC motor (High speed, stops instantly with a light touch).

---

## 📸 Slide 11: Component Expert Quiz
* **Q1: BO Gear motor me internal gears lagane se axle torque kyu multiply hota hai?**  
  *Answer:* Gear reduction ratio (1:48) speed ko drop karke mechanical force/torque output ko proportional badha deta hai.
* **Q2: Active buzzer aur passive buzzer me functional difference kya hai?**  
  *Answer:* Active buzzer has built-in oscillator (beeps on DC power), while passive buzzer requires input frequency signals to sound.
* **Q3: 3D Pen brackets templates designing clearance limits kyu zaroori?**  
  *Answer:* Secure fitting, tight grips loops align parameters checks.
"""

    # SESSION 3: BATTERY & POWER (Premium Overhaul with Interactive Lab Tasks - 9 Slides)
    elif num == 3:
        return f"""# Session 03: Battery & Power 🔋

**Class 3 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Battery & Power Intro
![Battery Power](https://images.unsplash.com/photo-1626252301306-444f6f874fde?w=800&q=80)

> **Voltage pressure, polarity management aur dangerous short-circuit loops se safety rules seekhna**

Robotic circuits build karte time voltage rules aur short circuit hazards ki absolute understanding hona sabse pehle zaroori hai. Aaiye is session ke physics rules ko step-by-step master karein!
* **Keywords:** `Voltage Pressure` | `Short Circuit` | `DC Polarity` | `Safe Loop`
* **Session Target:** Build a loop safely, identify short-circuits, and complete the "Current Detective" puzzle.

---

## 📸 Slide 2: Polarity Principles & Direction of Flow
<svg width="350" height="180" viewBox="0 0 350 180" style="display:block; margin:15px auto; background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; font-family:sans-serif;">
  <rect x="20" y="50" width="60" height="90" rx="4" fill="#1e293b"/>
  <circle cx="20" cy="70" r="15" fill="#ef4444" fill-opacity="0.1"/>
  <path d="M 50 60 L 290 60 L 290 120 L 50 120" fill="none" stroke="#ea580c" stroke-width="3" stroke-linecap="round"/>
  <path d="M 170 60 L 180 60" fill="none" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow)"/>
  <path d="M 180 120 L 170 120" fill="none" stroke="#1e293b" stroke-width="2" marker-end="url(#arrow)"/>
  <text x="170" y="50" font-size="8" font-weight="bold" fill="#ea580c" text-anchor="middle">Conventional Current Flow (➕ to ➖)</text>
  <text x="170" y="140" font-size="8" font-weight="bold" fill="#0284c7" text-anchor="middle">Actual Electron Flow (➖ to ➕)</text>
</svg>

DC (Direct Current) networks me electricity hamesha rules follow karti hai:
* **Polarity Rules:** DC loops me positive (+ Red) aur negative (- Black) terminals strictly defined hote hain.
* **Direct current direction:** Physics theory ke mutabik electric current hamesha battery positive (+) pole se start hokar negative (-) pole ki taraf flow karta hai.

---

## 📸 Slide 3: Inside the Carbon-Zinc Chemical Cell
<svg width="350" height="180" viewBox="0 0 350 180" style="display:block; margin:15px auto; background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; font-family:sans-serif;">
  <rect x="130" y="30" width="90" height="120" rx="8" fill="#e2e8f0" stroke="#475569" stroke-width="2"/>
  <rect x="170" y="15" width="10" height="15" fill="#1e293b"/>
  <line x1="175" y1="30" x2="175" y2="150" stroke="#ea580c" stroke-width="8" stroke-linecap="round"/>
  <text x="175" y="100" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">Carbon Rod (+)</text>
  <text x="260" y="90" font-size="8" font-weight="bold" fill="#475569" text-anchor="middle">Chemical Paste</text>
  <path d="M 230 90 L 205 90" fill="none" stroke="#475569" stroke-width="1.5" marker-end="url(#arrow)"/>
</svg>

Battery electrical energy kaise produce karti hai?
* **Chemical Energy Conversion:** Battery ke andar ek **Carbon Rod** (positive) aur surrounding **Zinc casing** (negative) ke beech chemical paste reaction chalti hai.
* **Potential Pressure:** Potential chemical pressure negative terminal par electrons jama karti hai jo electrical force generate karta hai.

---

## 📸 Slide 4: Short Circuit Danger (Thermal Hazard)
<svg width="350" height="180" viewBox="0 0 350 180" style="display:block; margin:15px auto; background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; font-family:sans-serif;">
  <rect x="60" y="50" width="60" height="90" rx="4" fill="#1e293b"/>
  <path d="M 90 60 L 260 60 L 260 120 L 90 120" fill="none" stroke="#ef4444" stroke-width="4"/>
  <path d="M 175 90 L 165 75 L 185 75 Z" fill="#eab308" stroke="#ca8a04"/>
  <circle cx="175" cy="85" r="15" fill="#ef4444" fill-opacity="0.2"/>
  <text x="175" y="150" font-size="10" font-weight="bold" fill="#ef4444" text-anchor="middle">⚠️ DANGER: SHORT CIRCUIT!</text>
</svg>

Agar battery loops directly contact me aa jayein toh kya hota hai?
* **Zero Resistance (R = 0):** Agar battery (+) aur (-) wires bina LED/Buzzer load ke directly touch ho jayein, toh circuit resistance zero ho jata hai.
* **Thermal Explosion Hazard:** Unlimited current flows ke chalte battery chemical cells boil hone lagte hain, wires melt ho sakte hain aur dynamic spark hazards hote hain.

---

## 📸 Slide 5: Safe Loops vs Short Loops (Visual Guide)
<svg width="350" height="180" viewBox="0 0 350 180" style="display:block; margin:15px auto; background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; font-family:sans-serif;">
  <g transform="translate(10, 20)">
    <rect x="10" y="20" width="140" height="110" rx="4" fill="#e2e8f0"/>
    <text x="80" y="40" font-size="9" font-weight="bold" fill="#15803d" text-anchor="middle">✅ SAFE CLOSED LOOP</text>
    <rect x="50" y="70" width="60" height="20" fill="#10b981" rx="2"/>
    <text x="80" y="83" font-size="8" fill="#ffffff" font-weight="bold" text-anchor="middle">LOAD (LED)</text>
  </g>
  <g transform="translate(180, 20)">
    <rect x="10" y="20" width="140" height="110" rx="4" fill="#fee2e2"/>
    <text x="80" y="40" font-size="9" font-weight="bold" fill="#b91c1c" text-anchor="middle">❌ DANGEROUS SHORT</text>
    <line x1="30" y1="80" x2="130" y2="80" stroke="#ef4444" stroke-width="4"/>
    <text x="80" y="95" font-size="7" fill="#b91c1c" font-weight="bold" text-anchor="middle">Direct wire link!</text>
  </g>
</svg>

Dono circuits loops configurations limits check:
* **Safe Closed Loop:** Current limit checks ke liye loop me load (LED/Motor) lagana zaroori hai jo current flow rate ko switch scale limits me rakhta hai.
* **Short Circuit:** Bina resistance load ke direct current return system battery damage aur hazards generate karta hai.

---

## 📸 Slide 6: Step-by-Step Safe Connection Guide
* **[ ] Step 1:** Sabhi output components (LED, switch, buzzer) ko pehle wire loops me connect karein.
* **[ ] Step 2:** Wires connections and polarities ko visually cross-check karein.
* **[ ] Step 3 (Crucial Rule):** Battery snap connector ko **sabse aakhir me (last)** battery terminals par lagayein.
* **[ ] Step 4:** Agar battery snap lagate hi components bypass sound alert ya hot spots thermal heat de, toh snap ko immediately pull off karein.

---

## 📸 Slide 7: Interactive Lab Task: "The Current Detective" 🔍
<svg width="350" height="180" viewBox="0 0 350 180" style="display:block; margin:15px auto; background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; font-family:sans-serif;">
  <circle cx="150" cy="80" r="30" fill="none" stroke="#3b82f6" stroke-width="4"/>
  <line x1="172" y1="102" x2="210" y2="140" stroke="#3b82f6" stroke-width="6" stroke-linecap="round"/>
  <line x1="130" y1="80" x2="170" y2="80" stroke="#ef4444" stroke-width="3"/>
  <text x="150" y="160" font-size="10" font-weight="bold" fill="#1e293b" text-anchor="middle">Find the Hidden Short Circuit!</text>
</svg>

Aaiye ek puzzle game khelte hain!
* **Task Goal:** Teacher aapko 3 card boards denge jisme circuits wire loops bane hain.
  * **Card A:** Switch directly battery positive aur negative ko short kar raha hai.
  * **Card B:** LED ke cathode and anode aapas me short-wired hain.
  * **Card C:** Correct Series Alarm Loop.
* **Your Action:** Apne notebook logs par detect karein ki kis card me **Short Circuit** hai aur use fix karein!

---

## 📸 Slide 8: Student Lab Log & Observations
Apni copy me niche di gayi values aur results log karein:

| Circuit Card Tested | Visual Status (OK / short) | Corrective Action | Heat Level (Normal / Hot) |
| :--- | :--- | :--- | :--- |
| Card Board A | Short Circuit detected | Remove direct switch ground link | Warm |
| Card Board B | Short Loop LED pins | Separate positive and negative nodes | Normal |
| Card Board C | Safe Closed Loop | None (Alert active) | Normal |

---

## 📸 Slide 9: Battery Safety Quiz
* **Q1: Battery snap ko hamesha wiring complete hone ke baad aakhir me kyu lagate hain?**  
  *Answer:* Taaki kisi bhi wiring mistake ya loose contact se hone wale short circuit ko power dene se pehle hi check kiya ja sake.
* **Q2: Carbon-zinc dry cells electrical power kaise construct krte hain?**  
  *Answer:* Chemical paste reactions voltage potential differences coordinates dynamic current electron generation loops.
* **Q3: Resistor or loads values loops current variables control kyu krti hain?**  
  *Answer:* Resistors current flow streams limits coordinate ohm's law safety parameter criteria details locks.
"""

    # SESSION 4: CIRCUIT TROUBLESHOOTING (Premium Overhaul with Debugging Tasks - 9 Slides)
    elif num == 4:
        return f"""# Session 04: Circuit Troubleshooting 🔍

**Class 3 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Troubleshooting Intro
![Diagnostics Work](https://images.unsplash.com/photo-1581092335397-9583fe92d232?w=800&q=80)

> **Circuits me loose contacts, reversed components legs aur low voltage blocks ko locate aur debug karna**

Engineering networks me troubleshooting sabse critical skill hai. Aaj hum real technicians ki tarah circuit faults ko systematically isolate aur repair karna seekhenge!
* **Keywords:** `Fault Isolation` | `Continuity Check` | `Bypass Test` | `Polarity Swap`
* **Session Target:** Debug 3 broken robot circuits and fill out the repair logs.

---

## 📸 Slide 2: The Core Rule: Fault Isolation
<svg width="350" height="180" viewBox="0 0 350 180" style="display:block; margin:15px auto; background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; font-family:sans-serif;">
  <line x1="50" y1="90" x2="300" y2="90" stroke="#94a3b8" stroke-width="3"/>
  <circle cx="80" cy="90" r="10" fill="#3b82f6"/>
  <text x="80" y="115" font-size="8" font-weight="bold" fill="#3b82f6" text-anchor="middle">Node A (Power)</text>
  <circle cx="175" cy="90" r="10" fill="#ef4444"/>
  <text x="175" y="115" font-size="8" font-weight="bold" fill="#ef4444" text-anchor="middle">Node B (Switch)</text>
  <circle cx="270" cy="90" r="10" fill="#3b82f6"/>
  <text x="270" y="115" font-size="8" font-weight="bold" fill="#3b82f6" text-anchor="middle">Node C (Load)</text>
  <line x1="170" y1="80" x2="180" y2="100" stroke="#ef4444" stroke-width="3"/>
</svg>

Fault isolation ka matlab hai circuit ko step-by-step points me split karke testing karna:
* **Divide-and-Conquer:** Agar poora system band hai, toh directly check karein:
  1. Kya source power de raha hai? (Node A)
  2. Kya trigger connector output signal generate kar raha hai? (Node B)
  3. Kya target component intact aur secure hai? (Node C)

---

## 📸 Slide 3: Visual Inspection Checklist
<svg width="350" height="180" viewBox="0 0 350 180" style="display:block; margin:15px auto; background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; font-family:sans-serif;">
  <path d="M 50 90 L 300 90" stroke="#475569" stroke-width="2"/>
  <line x1="150" y1="90" x2="160" y2="90" stroke="none"/>
  <circle cx="150" cy="90" r="25" fill="none" stroke="#ef4444" stroke-width="3"/>
  <text x="150" y="130" font-size="8" font-weight="bold" fill="#ef4444" text-anchor="middle">Loose contact point detected!</text>
</svg>

Debugging start karne se pehle physical connections ki checking karein:
* **Loose contacts:** Twist joints properly tightly locked nahi hain, jiski wajah se loop break ho jata hai.
* **Bare wire crossings:** Do safety coated wires peel off hokar bare surfaces touch kar rahi hain (Direct Short route risk).
* **Open Solder Tabs:** Slide switch pins se wires physical displacement block checks parameters.

---

## 📸 Slide 4: Switch Bypass Test (No-Tools Debugging)
<svg width="350" height="180" viewBox="0 0 350 180" style="display:block; margin:15px auto; background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; font-family:sans-serif;">
  <rect x="130" y="70" width="80" height="40" rx="4" fill="#ef4444" fill-opacity="0.1" stroke="#ef4444" stroke-width="2"/>
  <text x="170" y="93" font-size="9" font-weight="bold" fill="#ef4444" text-anchor="middle">FAULTY SW</text>
  <path d="M 90 90 Q 170 30 250 90" fill="none" stroke="#22c55e" stroke-width="3" stroke-dasharray="4,2"/>
  <text x="170" y="45" font-size="8" font-weight="bold" fill="#22c55e" text-anchor="middle">Bypass Jumper Wire (Checks OK)</text>
</svg>

Agar switch toggle karne par bhi system dead rehti hai:
* **Bypass Method:** Ek direct jumper wire battery snap positive (+) se direct LED anode terminal par touch karein.
* **Diagnosis:** Agar bypass lagate hi LED glow kar jaye, toh confirm ho jata hai ki switch internally kharab hai ya contacts tab block open hain.

---

## 📸 Slide 5: Polarity Swap Diagnostics
<svg width="350" height="180" viewBox="0 0 350 180" style="display:block; margin:15px auto; background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; font-family:sans-serif;">
  <line x1="175" y1="30" x2="175" y2="150" stroke="#ef4444" stroke-width="3"/>
  <path d="M 120 90 L 220 90" fill="none" stroke="#ef4444" stroke-width="3" marker-end="url(#arrow)"/>
  <text x="175" y="20" font-size="10" font-weight="bold" fill="#ef4444" text-anchor="middle">BLOCK: REVERSED DIODE</text>
  <text x="175" y="165" font-size="8" fill="#475569" text-anchor="middle">Current cannot cross the semiconductor barrier</text>
</svg>

LED aur Buzzers ko trace karke polarity evaluate karein:
* **Symptom:** LED and buzzer silent. But battery output OK hai.
* **Why it happens:** Semiconductors elements negative terminals blocks and reverse bias configuration me standard current values infinite impedance resistance generate kar blocks details loops trace.

---

## 📸 Slide 6: Diagnostic Check Sequence (Flow Guide)
* 👆 **Step A:** Check power loops (feel the battery). Agar warm hai, disconnect instantly (Short circuit warning!).
* 🔘 **Step B:** Switch positions checks. Check switch solder pin configurations.
* 💡 **Step C:** Flip component legs. Anode/Cathode terminals swap verify steps check.

---

## 📸 Slide 7: Engaging Lab Task: "The Broken Robot Factory" 🛠️
<svg width="350" height="180" viewBox="0 0 350 180" style="display:block; margin:15px auto; background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; font-family:sans-serif;">
  <rect x="140" y="40" width="70" height="70" rx="8" fill="#cbd5e1" stroke="#94a3b8" stroke-width="2"/>
  <circle cx="160" cy="65" r="5" fill="#ef4444"/>
  <circle cx="190" cy="65" r="5" fill="#ef4444"/>
  <path d="M 160 90 Q 175 100 190 90" fill="none" stroke="#ef4444" stroke-width="2"/>
  <path d="M 110 130 L 240 130" stroke="#f59e0b" stroke-width="4" stroke-linecap="round"/>
  <text x="175" y="160" font-size="9" font-weight="bold" fill="#f59e0b" text-anchor="middle">Repair Station: 3 Faulty Systems</text>
</svg>

Aaiye repair workshop factory open karte hain!
* **Your Mission:** Teacher ne tables par 3 broken robotic circuits arrange kiye hain:
  * **Robot 1 (LED dark):** Fault check logic (LED long leg is wired backwards).
  * **Robot 2 (Motor spin speed extremely slow):** Fault check logic (Low battery cells voltage).
  * **Robot 3 (Buzzer silent ticking sound):** Fault check logic (Loose ground wire snaps).
* **Action:** Har robot fault write down karein, resolve actions apply karein aur circuit repair log parameters mark karein!

---

## 📸 Slide 8: Technician's Repair Log Table
Apni notebook me repair results log karein:

| System ID | Error Symptom | Isolated Fault | Action Taken | Status |
| :--- | :--- | :--- | :--- | :--- |
| Robot 1 | LED completely OFF | LED legs reversed | Swapped anode and cathode leads | ✅ REPAIRED |
| Robot 2 | Motor spins too slow | Drained 9V battery | Replaced with fresh battery cells | ✅ REPAIRED |
| Robot 3 | Buzzer clicks only | Loose ground wire snap | Tightened twist joints loop | ✅ REPAIRED |

---

## 📸 Slide 9: Troubleshooting Master Quiz
* **Q1: Jumper bypass test karne par LED glow ho gayi. Fault kis component me hai?**  
  *Answer:* Fault switch me hai ya switch terminals ke wire joints me loose contacts hain.
* **Q2: Diode semiconductor block layers reverse current block kyu krti hain?**  
  *Answer:* Crystal depletion boundaries charges swap limits check block parameters blocks.
* **Q3: Short circuits detect hote hi snap quickly pull kyu krte hain?**  
  *Answer:* Thermal battery fire damages prevent properties safety targets locks.
"""

    # SESSION 5: SERIES VS PARALLEL LEDS (Space Explorer Theme - 9 Slides Masterpiece)
    elif num == 5:
        return f"""# Session 05: Space Cockpit Light Grid! 🚀

**Class 3 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Mission Briefing: Starship Light Crisis!
![Spaceship Cockpit](https://images.unsplash.com/photo-1506703719100-a0f3a48c0f86?w=800&q=80)

> **Space Explorer Roy ke spaceship cockpit indicators ko series vs parallel layout me wire karke rescue mission complete karna**

Attention Space Explorers! Space Voyager Roy ka starship orbit me meteor belt se crash ho gaya hai. Cabin generator power drop ho rahi hai, aur indicator panels band hain. Hamare paas sirf 2 LEDs aur ek 9V backup power source bacha hai. Aaiye indicators ko wire karne ke sabse best circuits seekhein!
* **Keywords:** `Series Weak Chain` | `Parallel Star Grid` | `Voltage Split` | `Rescue Mode`
* **Mission Goal:** Wire cabin indicator grids in series and parallel, and solve the "Meteor Strike" failure simulation.

---

## 📸 Slide 2: The Series Loop (The Weak Chain Indicator)
<svg width="350" height="180" viewBox="0 0 350 180" style="display:block; margin:15px auto; background:#0f172a; border:2px solid #ef4444; border-radius:8px; font-family:sans-serif;">
  <circle cx="50" cy="40" r="1" fill="#ffffff"/>
  <circle cx="280" cy="30" r="1.5" fill="#ffffff"/>
  <circle cx="150" cy="140" r="1" fill="#ffffff"/>
  <g transform="translate(100, 90)">
    <circle cx="0" cy="0" r="15" fill="#eab308" fill-opacity="0.3"/>
    <path d="M -10 10 Q -10 -15 0 -15 Q 10 -15 10 10 Z" fill="#facc15" fill-opacity="0.5"/>
    <text x="0" y="28" font-size="7" fill="#cbd5e1" text-anchor="middle">Dim Light 1</text>
  </g>
  <g transform="translate(220, 90)">
    <circle cx="0" cy="0" r="15" fill="#eab308" fill-opacity="0.3"/>
    <path d="M -10 10 Q -10 -15 0 -15 Q 10 -15 10 10 Z" fill="#facc15" fill-opacity="0.5"/>
    <text x="0" y="28" font-size="7" fill="#cbd5e1" text-anchor="middle">Dim Light 2</text>
  </g>
  <path d="M 40 90 L 85 90 M 115 90 L 205 90 M 235 90 L 300 90" fill="none" stroke="#ef4444" stroke-width="2"/>
  <text x="160" y="40" font-size="9" font-weight="bold" fill="#ef4444" text-anchor="middle">Single Path: Voltage divides (4.5V each)</text>
</svg>

Series wiring starship systems me sabse weak connection chain hoti hai:
* **Single Path Control:** Current positive terminal se nikalkar pehle LED 1, fir LED 2 se hote hue ek hi patli road par behta hai.
* **Dim Dashboard Glow:** 9V backup pressure split ho jata hai (dono LEDs ko 4.5V each milta hai), jisse lights bilkul dim glow karti hain.
* **The Cabin Hazard:** Agar cockpit me se ek bhi indicator damage/unplug ho jaye, toh poora path break ho jata hai aur baki saari panel lights band ho jati hain!

---

## 📸 Slide 3: The Parallel Grid (The Star Power Channels)
<svg width="350" height="180" viewBox="0 0 350 180" style="display:block; margin:15px auto; background:#0f172a; border:2px solid #22c55e; border-radius:8px; font-family:sans-serif;">
  <circle cx="40" cy="30" r="1.5" fill="#ffffff"/>
  <circle cx="310" cy="130" r="1" fill="#ffffff"/>
  <g transform="translate(160, 55)">
    <circle cx="0" cy="0" r="18" fill="#eab308" fill-opacity="0.7"/>
    <circle cx="0" cy="0" r="28" fill="#eab308" fill-opacity="0.2"/>
    <path d="M -10 10 Q -10 -15 0 -15 Q 10 -15 10 10 Z" fill="#facc15"/>
  </g>
  <g transform="translate(160, 125)">
    <circle cx="0" cy="0" r="18" fill="#eab308" fill-opacity="0.7"/>
    <circle cx="0" cy="0" r="28" fill="#eab308" fill-opacity="0.2"/>
    <path d="M -10 10 Q -10 -15 0 -15 Q 10 -15 10 10 Z" fill="#facc15"/>
  </g>
  <text x="260" y="95" font-size="9" font-weight="bold" fill="#22c55e" text-anchor="middle">Equal 9V Pressure!</text>
</svg>

Parallel Grid starship indicators ko hamesha running aur shining rakhta hai:
* **Branching Lanes:** Current ke paas dono indicator lights ke liye alag-alag lanes (branches) hoti hain.
* **Maximum Dashboard Brightness:** Dono LEDs ko direct battery se full 9V electrical pressure milta hai, jisse dono super bright glow karti hain.
* **Meteor Shield Protection:** Agar space dust/meteor strike se ek branch link break bhi ho jaye, tab bhi dusri branch completely safe aur glowing chalti rehti hai!

---

## 📸 Slide 4: Space Metrics comparison
Aaiye dono power loops ki features sheet check karein:

| Metric Indicator | Series Cabin Chain | Parallel Star Grid |
| :--- | :--- | :--- |
| **Number of Paths** | Only 1 path | Multiple branches (2 paths) |
| **Voltage Pressure** | Splits up (Dull indicators) | Maximum 9V (Super Bright) |
| **One Bulb Fails?** | All dashboard goes dark ❌ | Other indicator stays ON! ✅ |
| **Starship Usage** | Warning alarm chain | Main cabin emergency cockpit panels |

---

## 📸 Slide 5: Master Space Schematic (High-Fidelity Wiring) 🎨
<svg width="450" height="250" viewBox="0 0 450 250" style="display: block; margin: 20px auto; background: #0f172a; border: 2px solid #38bdf8; border-radius: 12px; font-family: sans-serif;">
  <defs>
    <pattern id="space_grid" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#1e293b" stroke-width="1"/>
    </pattern>
  </defs>
  <rect width="100%" height="100%" fill="url(#space_grid)" rx="12"/>

  <!-- Battery -->
  <g transform="translate(15, 60)">
    <rect x="0" y="20" width="70" height="110" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="35" y="85" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">9V POWER</text>
    <circle cx="22" cy="42" r="7" fill="#ef4444"/>
    <text x="22" y="46" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">+</text>
    <circle cx="48" cy="42" r="7" fill="#3b82f6"/>
    <text x="48" y="46" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">-</text>
  </g>

  <!-- Parallel Branch Grid node layout -->
  <g transform="translate(180, 40)">
    <rect x="0" y="10" width="80" height="30" rx="4" fill="#1e293b" stroke="#eab308" stroke-width="2"/>
    <text x="40" y="28" font-size="8" font-weight="bold" fill="#eab308" text-anchor="middle">INDICATOR 1</text>
  </g>
  <g transform="translate(180, 130)">
    <rect x="0" y="10" width="80" height="30" rx="4" fill="#1e293b" stroke="#eab308" stroke-width="2"/>
    <text x="40" y="28" font-size="8" font-weight="bold" fill="#eab308" text-anchor="middle">INDICATOR 2</text>
  </g>

  <!-- Parallel nodes wires red branching paths -->
  <path d="M 37 60 L 37 30 L 140 30 L 140 25 M 140 25 L 180 25 M 140 25 L 140 145 L 180 145" fill="none" stroke="#ef4444" stroke-width="3" stroke-linecap="round"/>
  <rect x="50" y="15" width="80" height="12" fill="#ef4444" rx="2"/>
  <text x="90" y="23" font-size="6.5" font-weight="bold" fill="#ffffff" text-anchor="middle">🔴 Red: Branch 1 & 2 In</text>

  <!-- Return paths -->
  <path d="M 260 25 L 300 25 L 300 145 M 260 145 L 300 145 M 300 80 L 300 190 L 63 190 L 63 170" fill="none" stroke="#3b82f6" stroke-width="3" stroke-linecap="round"/>
  <rect x="150" y="184" width="100" height="12" fill="#3b82f6" rx="2"/>
  <text x="200" y="192" font-size="6.5" font-weight="bold" fill="#ffffff" text-anchor="middle">🔵 Blue/Black: Main Ground Return</text>

  {get_hand_svg(130, 85, "Parallel Node")}
</svg>

---

## 📸 Slide 6: Starship Assembly Steps
* 🛠️ **Step 1:** Battery snap connector attach karein, snaps secure ensure check.
* 🔗 **Step 2 (Series Circuit):** Red wire snap to LED 1 Anode (+) long leg. LED 1 short leg directly wire connect to LED 2 Anode (+). LED 2 short leg return path snap Black wire (-) twist lock.
* 🔀 **Step 3 (Parallel Circuit):** Red snap wire (+) output ko split jumper nodes se link karke dono LEDs long legs (+) par jodein. Cathodes (-) lines ko combine karke directly ground black snap wire se close down connection path.

---

## 📸 Slide 7: Engaging Lab Task: "Starship Cockpit Power Mission!" 🛸
<svg width="350" height="180" viewBox="0 0 350 180" style="display:block; margin:15px auto; background:#0f172a; border:2px solid #f59e0b; border-radius:8px; font-family:sans-serif;">
  <path d="M 175 30 L 210 90 L 140 90 Z" fill="#38bdf8" stroke="#0284c7" stroke-width="2"/>
  <rect x="155" y="90" width="40" height="40" fill="#e2e8f0"/>
  <path d="M 160 130 Q 175 160 190 130 Z" fill="#ef4444"/>
  <circle cx="175" cy="70" r="8" fill="#eab308"/>
  <text x="175" y="12" font-size="9" font-weight="bold" fill="#38bdf8" text-anchor="middle">Starship Rescue: Simulating Meteor strike</text>
</svg>

Explorer limits testing rules:
1. **Task A (Build Warp Drive):** 2 LEDs ko Series Layout me connect karein. Dono lights glow dim yellow.
2. **Task B (The Meteor Strike Simulation):** Wires connect chalte time sudden **LED 1 ko socket/jumper wire se disconnect** kar dein. Observe karein ki LED 2 ke indicator par kya effect padta hai.
3. **Task C (Build Main Cabin Grid):** Dono LEDs ko Parallel Layout me re-wire karein. Open one LED branch aur check karein - dusri LED light shining safe levels check.

---

## 📸 Slide 8: Space Explorer's Flight Log Book
Apni Starship Log Book me observations records sheet mark down karein:

| Circuit Layout | Meteor Strike target | Active indicator status | Cabin Status (Safe/Danger) |
| :--- | :--- | :--- | :--- |
| **Series Warp Grid** | LED 1 removed | LED 2 goes dark instantly ❌ | **DANGER DARK** |
| **Parallel Star Grid** | LED 1 removed | LED 2 continues shining bright! ✅ | **MISSION SAFE** |

---

## 📸 Slide 9: Cosmic Assessment Quiz
* **Q1: Series circuit indicator panel space exploration ships me use kyu nahi kiya jata?**  
  *Answer:* Kyunki agar ek bhi control indicator breakdown ho jaye, toh safety warning system complete loop shutdown collapse ho jata hai.
* **Q2: Parallel loops check voltage values constant kyu rehti hain?**  
  *Answer:* Har branch loop directly battery output node references lines parallel touch check bounds complete channels.
* **Q3: Spaceship indicator cells load series battery drain speed kya hai?**  
  *Answer:* Parallel networks resistance low hone se current draw rate badhta hai aur battery energy dynamic consume handles details limits checks.
"""

    # SESSION 6: TWO-SWITCH CIRCUIT (Castle Gate OR Logic - 9 Slides Masterpiece)
    elif num == 6:
        return f"""# Session 06: Castle Gate Security Lock! 🏰

**Class 3 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Welcome to the Castle Security Mission!
![Castle Gate](https://images.unsplash.com/photo-1599707367072-cd6ada2bc375?w=800&q=80)

> **2 switches ko parallel layout me wire karke castle gate locks system control karna (Logical OR Gate)**

Princess Aria ke castle ki protection warning grid damage ho gayi hai! Security criteria ye hai ki agar **guard bahar se switch dabaye YA Princess andar se switch dabaye**, toh castle gate ka lock active (Green LED ON) ho jana chahiye. Aaiye is logical controller system ko wire karein!
* **Keywords:** `Logical OR Gate` | `Parallel Switches` | `Security Grid` | `Dual Control`
* **Mission Goal:** Build an OR logic gate using parallel switches to control the castle gate status.

---

## 📸 Slide 2: Logical OR Gate Principles
<svg width="350" height="180" viewBox="0 0 350 180" style="display:block; margin:15px auto; background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; font-family:sans-serif;">
  <!-- OR Logic Gate Symbol -->
  <path d="M 100 40 Q 140 40 170 90 Q 140 140 100 140 Q 130 90 100 40 Z" fill="#3b82f6" fill-opacity="0.2" stroke="#2563eb" stroke-width="3"/>
  <!-- Inputs -->
  <line x1="50" y1="65" x2="115" y2="65" stroke="#1e293b" stroke-width="2"/>
  <line x1="50" y1="115" x2="115" y2="115" stroke="#1e293b" stroke-width="2"/>
  <!-- Output -->
  <line x1="170" y1="90" x2="240" y2="90" stroke="#1e293b" stroke-width="2"/>
  <text x="75" y="55" font-size="8" font-weight="bold" fill="#1e293b">Guard SW A</text>
  <text x="75" y="105" font-size="8" font-weight="bold" fill="#1e293b">Princess SW B</text>
  <text x="210" y="80" font-size="8" font-weight="bold" fill="#10b981">Gate Lock (ON)</text>
</svg>

Logic controllers systems inputs signals read karte hain:
* **OR Logic Definition:** Agar kisi bhi route ka input signal **ON (True)** hota hai, toh final output hamesha active **ON (True)** ho jata hai.
* **Parallel routing:** Switches ko aapas me side-by-side (parallel) lagane se current ko flow karne ke liye do alternate roads mil jati hain.

---

## 📸 Slide 3: Staircase Wiring (Real-World Application)
* **Double Switches:** Gharo me staircase lights is logic par kaam karti hain.
* **Logical Convenience:** Stair ke ground floor par laga switch YA top floor par laga switch, dono me se koi bhi lights ON/OFF toggle kar sakta hai.

---

## 📸 Slide 4: High-Fidelity Castle Gate SVG Schematic 🎨
<svg width="450" height="250" viewBox="0 0 450 250" style="display: block; margin: 20px auto; background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 12px; font-family: sans-serif;">
  <defs>
    <pattern id="grid_castle" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#f1f5f9" stroke-width="1"/>
    </pattern>
  </defs>
  <rect width="100%" height="100%" fill="url(#grid_castle)" rx="12"/>
  
  <!-- Castle Wall mockups -->
  <rect x="0" y="0" width="30" height="250" fill="#94a3b8"/>
  <rect x="420" y="0" width="30" height="250" fill="#94a3b8"/>
  
  <!-- Switch A (Guard) -->
  <g transform="translate(120, 30)">
    <rect x="0" y="10" width="80" height="45" rx="4" fill="#3b82f6" stroke="#1d4ed8" stroke-width="2"/>
    <text x="40" y="35" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Guard SW A</text>
  </g>
  <!-- Switch B (Princess) -->
  <g transform="translate(120, 130)">
    <rect x="0" y="10" width="80" height="45" rx="4" fill="#3b82f6" stroke="#1d4ed8" stroke-width="2"/>
    <text x="40" y="35" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">Princess SW B</text>
  </g>
  
  <!-- LED Output -->
  <g transform="translate(300, 80)">
    <path d="M 10 70 Q 10 20 30 20 Q 50 20 50 70 Z" fill="#10b981" fill-opacity="0.8" stroke="#047857" stroke-width="2"/>
    <text x="30" y="90" font-size="9" font-weight="bold" fill="#047857" text-anchor="middle">GATE OPEN</text>
  </g>

  <!-- Power Battery -->
  <g transform="translate(45, 80)">
    <rect x="0" y="10" width="50" height="80" rx="4" fill="#1e293b"/>
    <text x="25" y="55" font-size="9" font-weight="bold" fill="#ffffff" text-anchor="middle">9V</text>
  </g>

  <!-- Wires -->
  <path d="M 70 80 L 70 55 L 120 55" fill="none" stroke="#ef4444" stroke-width="3"/>
  <path d="M 70 55 L 70 155 L 120 155" fill="none" stroke="#ef4444" stroke-width="3"/>
  <path d="M 200 55 L 320 55 L 320 80" fill="none" stroke="#eab308" stroke-width="3"/>
  <path d="M 200 155 L 320 155 L 320 80" fill="none" stroke="#eab308" stroke-width="3"/>
  <path d="M 95 125 L 340 125 M 340 125 L 340 150 M 95 90 L 95 125" fill="none" stroke="#3b82f6" stroke-width="3"/>
  
  {get_hand_svg(160, 45, "Press SW A")}
</svg>

---

## 📸 Slide 5: Step-by-Step Connection Guide
* 📦 **Step 1:** Prepare your desk: Place 9V battery, snap, 2 slide switches, green LED, and jumper wires.
* 🔴 **Step 2 (Parallel Input splitting):** Connect battery snap **Red Wire (+)** to **both Switch A (Pin 1) AND Switch B (Pin 1)**.
* 🟡 **Step 3 (Parallel Output bridging):** Connect Switch A (Pin 2) center output AND Switch B (Pin 2) center output together to the **LED Long Leg (+)**.
* ⚫ **Step 4 (Common Return):** Connect the **LED Short Leg (-)** directly back to the battery snap **Black Wire (-)**.

---

## 📸 Slide 6: Engaging Lab Task: "The Twin-Switch Lock System" 🔑
* **Task Goal:** Guard Room and Princess Room setups ko wire mesh board par assemble karein.
* **The Mission Actions:**
  1. Dono switches ko OFF rakhein. LED is OFF.
  2. Guard SW A ko ON slide karein (Switch B is OFF). Check: Castle Gate opens?
  3. SW A ko OFF karke Princess SW B ko ON karein. Check: Gate status?
  4. Dono switches ko ek sath ON slide karein. Gate lock remains open?
* **Write results:** Apne security manual logs card par data verify karein.

---

## 📸 Slide 7: Security Guard's Logic Log
Princess Castle security logic status table logs card:

| Guard Switch A | Princess Switch B | Gate LED Status (ON/OFF) | Lock State (Secure/Open) |
| :--- | :--- | :--- | :--- |
| **OFF** (0) | **OFF** (0) | OFF | **SECURE** 🔒 |
| **ON** (1) | **OFF** (0) | ON (Glows Green) | **GATE OPEN** 🔓 |
| **OFF** (0) | **ON** (1) | ON (Glows Green) | **GATE OPEN** 🔓 |
| **ON** (1) | **ON** (1) | ON (Glows Green) | **GATE OPEN** 🔓 |

---

## 📸 Slide 8: Concept Assessment Quiz
* **Q1: Castle Security system me parallel switches lagane ka main reason kya hai?**  
  *Answer:* Taaki current flow hone ke liye do alag pathways (choices) generate ho sakein aur koi bhi ek switch bridge line loop complete kar sake.
* **Q2: Agar switches series me lagaye jayein toh logic gate kya banega?**  
  *Answer:* Tab logical AND Gate banega (Gate kholne ke liye dono switches ko ek sath dabana padega).
* **Q3: Staircase wiring loops dual operations parameters logic checks?**  
  *Answer:* Alternate switch states mapping current flow returns loops trace checks.
"""

    # SESSION 7: EMERGENCY LIGHT (Dark Mine Reflector - 9 Slides Masterpiece)
    elif num == 7:
        return f"""# Session 07: Dark Mine Explorer! 💎

**Class 3 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Welcome to the Mine Rescue Mission!
![Dark Mine](https://images.unsplash.com/photo-1507608869274-d3177c8bb4c7?w=800&q=80)

> **High-brightness LED, slide switch aur custom foil reflector cone se dynamic light beams expand karna**

Deep Mine Explorer Roy gufa ke sabse andhere hisse me diamond hunt par ja raha hai. Use ek aisi backup light chahiye jo continuous chalu rahe bina kisi button ko hold kiye, aur uska spotlight wide angle area cover kare. Aaiye Miner's Torch build karein!
* **Keywords:** `Latching Switch` | `Spotlight Cone` | `Reflector` | `Lux Diffusion`
* **Mission Goal:** Build a latching emergency torch and design a foil reflector cone to focus light beam distance.

---

## 📸 Slide 2: Latching Switch vs Momentary Button
<svg width="350" height="180" viewBox="0 0 350 180" style="display:block; margin:15px auto; background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; font-family:sans-serif;">
  <rect x="30" y="50" width="120" height="60" rx="4" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="2"/>
  <rect x="180" y="50" width="120" height="60" rx="4" fill="#fee2e2" stroke="#fca5a5" stroke-width="2"/>
  <text x="90" y="85" font-size="10" font-weight="bold" fill="#475569" text-anchor="middle">Latching Switch</text>
  <text x="90" y="130" font-size="8" fill="#475569" text-anchor="middle">(ON State Locked) 🔒</text>
  <text x="240" y="85" font-size="10" font-weight="bold" fill="#b91c1c" text-anchor="middle">Momentary Button</text>
  <text x="240" y="130" font-size="8" fill="#b91c1c" text-anchor="middle">(Release turns OFF) ⏳</text>
</svg>

Miner's torch ke liye hum slide switch kyu select karte hain:
* **Latching Action:** Slide switch positions ko latch (lock) kar deta hai. Explorer Roy ko tunnel me chaltay time continuous button hold nahi karna padta.
* **Momentary buttons danger:** Push buttons ko continuous finger pressure chahiye hota hai, jo explorer's grip ko fatigue detail warnings handles.

---

## 📸 Slide 3: Light Diffusion & Reflector Theory
<svg width="350" height="180" viewBox="0 0 350 180" style="display:block; margin:15px auto; background:#0f172a; border:1px solid #eab308; border-radius:8px; font-family:sans-serif;">
  <!-- LED bulb emitting light beams through a reflector cone -->
  <polygon points="120,90 260,30 260,150" fill="#fef08a" fill-opacity="0.3"/>
  <!-- Reflector lines -->
  <line x1="120" y1="70" x2="200" y2="40" stroke="#cbd5e1" stroke-width="4"/>
  <line x1="120" y1="110" x2="200" y2="140" stroke="#cbd5e1" stroke-width="4"/>
  <circle cx="110" cy="90" r="10" fill="#facc15"/>
  <text x="220" y="95" font-size="10" font-weight="bold" fill="#facc15" text-anchor="middle">Focused Beam</text>
</svg>

Spotlight cones engineering mechanics analyze check:
* **LED straight angle:** Standard LEDs light wave beams ko narrow straight lines me shoot karti hain.
* **Foil Reflector Cone:** Silver/aluminum foil reflection surfaces scattered light rays ko bounce back karke forward trajectory spotlight me project karti hain, jisse illumination span badh jata hai.

---

## 📸 Slide 4: High-Fidelity Miner's Torch SVG Schematic 🎨
<svg width="450" height="250" viewBox="0 0 450 250" style="display: block; margin: 20px auto; background: #0f172a; border: 2px solid #e2e8f0; border-radius: 12px; font-family: sans-serif;">
  <defs>
    <pattern id="grid_mine" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#1e293b" stroke-width="1"/>
    </pattern>
  </defs>
  <rect width="100%" height="100%" fill="url(#grid_mine)" rx="12"/>
  
  <!-- 9V Battery -->
  <g transform="translate(30, 60)">
    <rect x="0" y="20" width="70" height="110" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="35" y="85" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">9V BATT</text>
  </g>

  <!-- Slide switch -->
  <g transform="translate(160, 60)">
    <rect x="0" y="20" width="80" height="50" rx="4" fill="#475569" stroke="#94a3b8" stroke-width="2"/>
    <text x="40" y="50" font-size="8" fill="#ffffff" text-anchor="middle">EMG SW</text>
  </g>

  <!-- LED with Cone reflector mockup -->
  <g transform="translate(300, 60)">
    <polygon points="10,45 60,10 60,80" fill="#cbd5e1" stroke="#94a3b8" stroke-width="2"/>
    <circle cx="20" cy="45" r="10" fill="#facc15"/>
    <!-- Yellow illumination beam -->
    <path d="M 60 10 L 130 0 L 130 90 L 60 80 Z" fill="#fef08a" fill-opacity="0.3"/>
    <text x="95" y="50" font-size="8" fill="#fef08a" font-weight="bold" text-anchor="middle">BEAM</text>
  </g>

  <!-- Wires connections -->
  <path d="M 50 60 L 50 30 L 180 30 L 180 60" fill="none" stroke="#ef4444" stroke-width="3" stroke-linecap="round"/>
  <path d="M 220 60 L 220 30 L 310 30 L 310 60" fill="none" stroke="#eab308" stroke-width="3" stroke-linecap="round"/>
  <path d="M 70 60 L 70 190 L 330 190 L 330 120" fill="none" stroke="#3b82f6" stroke-width="3" stroke-linecap="round"/>
  
  {get_hand_svg(200, 85, "Slide ON")}
</svg>

---

## 📸 Slide 5: Step-by-Step Torch Assembly
* 🔴 **Step 1:** Battery snap connector Red wire (+) ko slide switch Pin 1 se connect karein.
* 🟡 **Step 2:** Slide switch Pin 2 (Center common) se Yellow wire lekar LED positive long leg (+) par jodein.
* ⚫ **Step 3:** LED negative short leg (-) line to battery snap Black wire (-) ground twisted connector loops lock.
* 📦 **Step 4 (The Reflector Weld):** Stencil paper sheet ko cone shape cup me roll karein. Foil sheet wrap parameters check. Fit the LED inside the small tip of the cone.

---

## 📸 Slide 6: Engaging Lab Task: "Build the Miner's Torch!" 🔦
* **Your Mission:** Dark mine cockpit panel rescue light assemble parameters checks:
  1. Assembly complete karke slide switch slide RIGHT (ON) state click check. LED glows.
  2. Without reflector: LED light beams straight wall par project karein. Measure light spot circle diameter (cm).
  3. With reflector: Foil cone mounts karein aur same spot distance check coordinate. Spot circles broad spreads parameter analyze loops check.
* **Log entries:** Write details on miner flight book.

---

## 📸 Slide 7: Miner's Illumination Log
Explorer Roy miner's dashboard observation specs details:

| Setup Configuration | Spot Circle Diameter (cm) | Light Spread (Narrow/Broad) | Visibility Area |
| :--- | :--- | :--- | :--- |
| **Only LED Bulb** | Approx 10 cm | Narrow spot beam | Focuses only at 1 point |
| **LED + Foil Reflector** | Approx 35 cm | Broad ambient light | Spreads all over the floor ✅ |

---

## 📸 Slide 8: Concept Assessment Quiz
* **Q1: Miner's backup loop light connections latching switch check optimization?**  
  *Answer:* Latching switch stays permanently locked in ON state, ensuring hands-free operation.
* **Q2: Foil papers light ray reflection laws check parameters kyu optimize krte hain?**  
  *Answer:* Shiny aluminum surfaces ray scattering drops bounce straight lines expand distance.
* **Q3: Direct LEDs circuits load resistor or safety loops trace checks?**  
  *Answer:* Current limits check ensures LEDs do not burn out under load conditions.
"""

    # SESSION 8: DECORATIVE LIGHTING (Alien Egg Cover - 9 Slides Masterpiece)
    elif num == 8:
        return f"""# Session 08: The Glowing Alien Egg! ✍️

**Class 3 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Welcome to the Space Egg Containment Mission!
![Alien Space Egg](https://images.unsplash.com/photo-1615715757401-f30e7b27b912?w=800&q=80)

> **3D Pen welds templates aur semi-transparent PLA mesh frames se sharp LED lights diffuse aur design karna**

Explorers, we have found a rare glowing Alien Egg in deep space! But the egg's radiation light is too sharp (raw LED glare). We need to build a custom mesh container cover using a 3D Pen that diffuses the sharp light rays into a soft, glowing ambient lamp shade. Aaiye design starts karein!
* **Keywords:** `3D Pen Nozzle` | `PLA Polymer` | `Refraction` | `Light Diffusion`
* **Mission Goal:** Weld a custom 3D mesh lamp shade cover to diffuse sharp LED beams.

---

## 📸 Slide 2: 3D Pen Nozzle Thermal Safety Limits
<svg width="350" height="180" viewBox="0 0 350 180" style="display:block; margin:15px auto; background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; font-family:sans-serif;">
  <!-- Pen nozzle design hot zones -->
  <polygon points="130,30 220,30 175,120" fill="#475569" stroke="#334155" stroke-width="2"/>
  <path d="M 170 120 L 180 120 L 175 140 Z" fill="#ef4444"/>
  <circle cx="175" cy="140" r="10" fill="#ef4444" fill-opacity="0.2"/>
  <text x="175" y="165" font-size="9" font-weight="bold" fill="#ef4444" text-anchor="middle">⚠️ CAUTION: HOT TIP (190°C)</text>
</svg>

3D pen weld techniques run karte time safety rules strict parameters check:
* **High-temperature tip:** 3D pen print tip extruder internally **190°C (Celsius)** touch parameters. Bare skin contact burns hazards create block check.
* **PLA filament melt points:** Solid plastic filament feed tip passing melt flow parameters check.

---

## 📸 Slide 3: Light Diffusion & Refraction Theory
<svg width="350" height="180" viewBox="0 0 350 180" style="display:block; margin:15px auto; background:#0f172a; border:1px solid #a855f7; border-radius:8px; font-family:sans-serif;">
  <!-- Sharp rays vs Scattered diffused rays -->
  <line x1="30" y1="90" x2="150" y2="90" stroke="#facc15" stroke-width="4"/>
  <!-- Mesh block -->
  <rect x="150" y="50" width="15" height="80" fill="#a855f7" rx="2"/>
  <!-- scattered rays -->
  <line x1="165" y1="90" x2="260" y2="40" stroke="#facc15" stroke-width="2" stroke-dasharray="3,1"/>
  <line x1="165" y1="90" x2="260" y2="90" stroke="#facc15" stroke-width="2" stroke-dasharray="3,1"/>
  <line x1="165" y1="90" x2="260" y2="140" stroke="#facc15" stroke-width="2" stroke-dasharray="3,1"/>
  <text x="90" y="80" font-size="8" fill="#cbd5e1" text-anchor="middle">Sharp Glare</text>
  <text x="210" y="70" font-size="8" fill="#a855f7" text-anchor="middle">Soft Diffusion</text>
</svg>

Lamp shade diffusion filters check:
* **The Mesh barrier:** Jab sharp LED beams semi-transparent PLA wireframe layers se takrati hain, toh light rays multiple angles par bend (refract) ho jati hain.
* **Ambient Glow:** Yeh bending action sharp spot light beam to visual soft ambient distribution glow me translate check coordinates.

---

## 📸 Slide 4: High-Fidelity Alien Egg Lamp SVG Schematic 🎨
<svg width="450" height="250" viewBox="0 0 450 250" style="display: block; margin: 20px auto; background: #0f172a; border: 2px solid #a855f7; border-radius: 12px; font-family: sans-serif;">
  <defs>
    <pattern id="grid_space_egg" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#1e293b" stroke-width="1"/>
    </pattern>
  </defs>
  <rect width="100%" height="100%" fill="url(#grid_space_egg)" rx="12"/>
  
  <!-- LED Base -->
  <g transform="translate(185, 80)">
    <rect x="15" y="60" width="50" height="60" rx="4" fill="#e2e8f0" stroke="#cbd5e1" stroke-width="2"/>
    <circle cx="40" cy="40" r="22" fill="#facc15" fill-opacity="0.8"/>
    
    <!-- 3D Pen Mesh Egg Shell -->
    <path d="M 5 60 Q 5 0 40 0 Q 75 0 75 60 Z" fill="none" stroke="#a855f7" stroke-width="3" stroke-dasharray="5,5"/>
    <path d="M 15 60 Q 15 15 40 15 Q 65 15 65 60 Z" fill="none" stroke="#d8b4fe" stroke-width="2" stroke-dasharray="4,4"/>
    
    <text x="40" y="140" font-size="10" font-weight="bold" fill="#d8b4fe" text-anchor="middle">Mesh Diffuser Shell</text>
  </g>
  
  {get_hand_svg(200, 20, "Weld PLA Joints")}
</svg>

---

## 📸 Slide 5: Drawing & Welding Steps
* 📝 **Step 1:** Drawing templates paper sheet par cross-lines oval pattern sketch draw.
* ✍️ **Step 2:** 3D pen parameters configure karein (PLA mode, 190°C nozzle heat).
* 🖋️ **Step 3:** Paper stencil path trace loops line par extrusion start lines weld. Wait for 5 seconds to cool.
* 📦 **Step 4:** Solid shapes sheet parameters roll loops curve brackets form. Wrap over your LED case, seal nodes.

---

## 📸 Slide 6: Engaging Lab Task: "Weld the Alien Egg Case!" 🥚
* **Your Mission:** Solid brackets shells structural design parameters check:
  1. Paper sheet template paths outline trace locks.
  2. 3D pen custom mesh grid designs structures weld (Green or Yellow PLA filaments best transparency).
  3. LED circuit complete slide SW RIGHT (ON) state test.
  4. LED bulb head par welded mesh cap slide coordinate structure cover check. Spot light glare soft glowing change check.
* **Log observations:** Explorer log card status.

---

## 📸 Slide 7: Alien Egg Containment Log
Observation dashboard:

| Setup Test Node | Light Intensity (Sharp / Soft) | Ray Pattern (Straight / Scattered) | Eye Comfort (Low / High) |
| :--- | :--- | :--- | :--- |
| **Bare LED Lamp** | Sharp Glare (Chundh) | Straight focused rays | Low comfort (painful) |
| **LED + Welded Egg Case** | Soft Ambient Glow | Scattered 3D mesh patterns | High comfort (Premium) ✅ |

---

## 📸 Slide 8: Concept Assessment Quiz
* **Q1: 3D pen printing tip metal head ko skin touch kyu lock restrictions?**  
  *Answer:* Nozzle operating thermal limit is 190°C, which can cause severe skin burns.
* **Q2: PLA plastics cooling freeze time checks logic?**  
  *Answer:* Hot extruded liquid plastic solidifying time limits check (solid in 3-5 seconds).
* **Q3: Light diffusers properties sharp rays scatter kyu coordinate krte hain?**  
  *Answer:* Refraction bends direction lines, distributing the glare evenly across the room.
"""

    # SESSION 9: ADVANCED BUZZER (Bank Vault Alarm - 9 Slides Masterpiece)
    elif num == 9:
        return f"""# Session 09: Bank Vault Tripwire! 🔊

**Class 3 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Welcome to the Bank Heist Mission!
![Bank Vault](https://images.unsplash.com/photo-1563986768609-322da13575f3?w=800&q=80)

> **Active buzzer sirens aur mechanical door-tripwire switch loops design karke intruder alerts alarm build karna**

The Diamond Bank is under threat! Intruder alert system construct parameter check logic: hume vault gate ke edge par ek automatic tripwire safety loop switch banana hai. Jaise hi intruder vault ka darwaza open kare, alarm immediately go off ho jaye!
* **Keywords:** `Burglar Siren` | `Tripwire Switch` | `Active buzzer` | `Security Loop`
* **Mission Goal:** Build a door-triggered tripwire security loop to sound a loud alert buzzer.

---

## 📸 Slide 2: Active Buzzer Internal Mechanics
<svg width="350" height="180" viewBox="0 0 350 180" style="display:block; margin:15px auto; background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; font-family:sans-serif;">
  <circle cx="100" cy="90" r="30" fill="#1e293b"/>
  <rect x="150" y="80" width="120" height="20" fill="#3b82f6" rx="2"/>
  <text x="100" y="93" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">Oscillator</text>
  <text x="210" y="92" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">Piezo Disk Vibrates</text>
</svg>

Active buzzer sirens check limits parameters:
* **Built-in Oscillator:** Is alarm device ke shell case ke andar automatic signal oscillator circuit lagaya jata hai.
* **Direct Voltage trigger:** Ise operate karne ke liye kisi external frequency codes signal ki need nahi hoti. Direct 9V supply receive hote hi instant output alarm generate beeps coordinates.

---

## 📸 Slide 3: Mechanical Tripwire Switch logic
<svg width="350" height="180" viewBox="0 0 350 180" style="display:block; margin:15px auto; background:#0f172a; border:2px solid #ef4444; border-radius:8px; font-family:sans-serif;">
  <!-- Door frame and contact switch -->
  <rect x="50" y="30" width="80" height="120" fill="#475569"/>
  <!-- open door swing -->
  <polygon points="130,30 200,10 200,130 130,150" fill="#ef4444" fill-opacity="0.3" stroke="#ef4444" stroke-width="2"/>
  <circle cx="130" cy="90" r="10" fill="#eab308"/>
  <text x="130" y="165" font-size="9" font-weight="bold" fill="#ef4444" text-anchor="middle">Door Opens ➔ Switch Releases 🔊</text>
</svg>

Burglar alarm loop trigger nodes details check:
* **Normally Closed status:** Jab lock door close rehta hai, switch pressed and circuit open/NC line checks.
* **Door Swing alert:** Door open hotay hi mechanical pull trigger releases switch contacts, closing the alarm signal path.

---

## 📸 Slide 4: High-Fidelity Vault Alarm SVG Schematic 🎨
<svg width="450" height="250" viewBox="0 0 450 250" style="display: block; margin: 20px auto; background: #0f172a; border: 2px solid #ef4444; border-radius: 12px; font-family: sans-serif;">
  <defs>
    <pattern id="grid_vault" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#1e293b" stroke-width="1"/>
    </pattern>
  </defs>
  <rect width="100%" height="100%" fill="url(#grid_vault)" rx="12"/>
  
  <!-- 9V Battery -->
  <g transform="translate(30, 60)">
    <rect x="0" y="20" width="70" height="110" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
    <text x="35" y="85" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">9V BATT</text>
  </g>

  <!-- Door contact switch mockup -->
  <g transform="translate(160, 60)">
    <rect x="0" y="20" width="90" height="50" rx="6" fill="#cbd5e1" stroke="#94a3b8" stroke-width="2"/>
    <circle cx="45" cy="45" r="12" fill="#ef4444"/>
    <text x="45" y="15" font-size="8" fill="#ef4444" font-weight="bold" text-anchor="middle">VAULT DOOR SW</text>
  </g>

  <!-- Siren Buzzer -->
  <g transform="translate(320, 60)">
    <circle cx="40" cy="50" r="25" fill="#000000" stroke="#334155" stroke-width="3"/>
    <text x="40" y="15" font-size="9" fill="#ef4444" font-weight="bold" text-anchor="middle">SIREN BUZZER</text>
    <!-- Sparks -->
    <path d="M 75 25 L 85 10 L 65 10 Z" fill="#eab308"/>
  </g>

  <!-- Connections -->
  <path d="M 50 60 L 50 30 L 175 30 L 175 60" fill="none" stroke="#ef4444" stroke-width="3" stroke-linecap="round"/>
  <path d="M 235 60 L 235 30 L 360 30 L 360 60" fill="none" stroke="#eab308" stroke-width="3" stroke-linecap="round"/>
  <path d="M 70 60 L 70 195 L 360 195 L 360 110" fill="none" stroke="#3b82f6" stroke-width="3" stroke-linecap="round"/>
  
  {get_hand_svg(200, 85, "Open Door")}
</svg>

---

## 📸 Slide 5: Step-by-Step Security Loop Assembly
* 🔴 **Step 1:** Red wire battery positive connection to door alarm switch.
* 🟡 **Step 2:** Switch output yellow wire to active alarm buzzer positive leg (+).
* ⚫ **Step 3:** Buzzer negative return leg directly battery black snap wire negative.
* 🚪 **Step 4:** Cardboard box frame door design mounting switches.

---

## 📸 Slide 6: Engaging Lab Task: "Trap the Vault Thief!" 🚨
* **Your Mission:** Bank Security Vault prototype safety grid assemble check parameters:
  1. Cardboard vault door prototype frames align switches brackets design locks.
  2. Series buzzer circuit connections setup complete.
  3. Close the door: Latch switch is pressed. Alarm stays silent.
  4. Open the door (Intruder attack!): Latch switch releases contact point. Alarm sounds! LOUD Beeping warning active status checks.
* **Log response time:** Explorer logs card.

---

## 📸 Slide 7: Security Vault Log
Observation chart:

| Vault Door State | Switch Terminal Condition | Buzzer Sound Output | Threat Status |
| :--- | :--- | :--- | :--- |
| **Closed** | Pressed (Open Loop NC) | Silent | **VAULT SECURE** 🔒 |
| **Opened (Thief!)** | Released (Closed Loop ON) | Loud Siren Beep! 🔊 | **INTRUSION DETECTED** 🚨 |

---

## 📸 Slide 8: Concept Assessment Quiz
* **Q1: Active warning buzzer negative terminal checks reverse current levels blocks?**  
  *Answer:* Yes, built-in piezoelectric diode paths wrong polarity current blocks.
* **Q2: Burglar alarms loop switch latching mechanisms kyu optimize checks?**  
  *Answer:* Reliable triggers are critical to ensure instantaneous alarms.
* **Q3: Tripwire sensors safety gates structures loops trace checks?**  
  *Answer:* Closed loops path configuration ensures constant security.
"""

    # SESSION 10: QUIZ + PRACTICAL TEST (Astronaut Space Flight Test - 9 Slides Masterpiece)
    elif num == 10:
        return f"""# Session 10: Rocket Launch Flight Check! 🏆

**Class 3 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Welcome to Mission Control!
![Rocket Launch](https://images.unsplash.com/photo-1541185933-ef5d8ed016c2?w=800&q=80)

> **10-minute astronaut circuit check speed tests, logic grids assembly aur final assessments**

Attention Astronauts! Rocket launch countdown has started. We have exactly 10 minutes to verify all electronic cockpit control loops. If our checks fail, the starship launch is aborted. Aaiye speed check diagnostics start karein!
* **Keywords:** `Countdown Timer` | `Series-Parallel Grid` | `Diagnostics Check` | `Launch Ready`
* **Session Target:** Build a multi-load control circuit in under 10 minutes to verify flight check ready.

---

## 📸 Slide 2: 10-Minute Countdown Guidelines
* **The Constraint:** Complete the flight board wiring grid (1 battery, 1 switch, 1 LED, 1 buzzer in parallel branch setup).
* **Speed & Accuracy:** Connections must be correct, zero short-circuit threats, and clean routing nodes.

---

## 📸 Slide 3: Flight Board Wiring Checklist
* [ ] Battery checks: Voltage pressure is above 6.0V warning limit.
* [ ] Switch Pin 1: Power input Red snap wire connected.
* [ ] Switch Pin 2: Branch split node to LED and Buzzer positive legs.
* [ ] Return ground: Common return Black wire snap connected.

---

## 📸 Slide 4: Countdown Gauge Dashboard Panel SVG 🎨
<svg width="450" height="250" viewBox="0 0 450 250" style="display: block; margin: 20px auto; background: #0f172a; border: 2px solid #f59e0b; border-radius: 12px; font-family: sans-serif;">
  <defs>
    <pattern id="grid_timer" width="20" height="20" patternUnits="userSpaceOnUse">
      <path d="M 20 0 L 0 0 0 20" fill="none" stroke="#1e293b" stroke-width="1"/>
    </pattern>
  </defs>
  <rect width="100%" height="100%" fill="url(#grid_timer)" rx="12"/>
  
  <!-- timer board -->
  <g transform="translate(125, 45)">
    <rect x="0" y="10" width="200" height="90" rx="8" fill="#1e293b" stroke="#eab308" stroke-width="3"/>
    <text x="100" y="55" font-size="28" font-weight="bold" fill="#ef4444" text-anchor="middle">10:00</text>
    <text x="100" y="80" font-size="12" fill="#cbd5e1" text-anchor="middle">COUNTDOWN LAUNCH</text>
  </g>
  
  <!-- Gauges -->
  <circle cx="60" cy="190" r="30" fill="#1e293b" stroke="#22c55e" stroke-width="2"/>
  <text x="60" y="193" font-size="8" fill="#ffffff" text-anchor="middle">Power OK</text>

  <circle cx="390" cy="190" r="30" fill="#1e293b" stroke="#ef4444" stroke-width="2"/>
  <text x="390" y="193" font-size="8" fill="#ffffff" text-anchor="middle">Time limit</text>
  
  {get_hand_svg(225, 145, "Ignition ON")}
</svg>

---

## 📸 Slide 5: Step-by-Step Test Sequence
* ⏰ **Step 1:** Start the timer countdown.
* 🔌 **Step 2:** Layout snap, switches, LEDs, and buzzers.
* 🔴 **Step 3:** Wire switch series logic positive connections.
* ⚫ **Step 4:** Finish negative ground returns.

---

## 📸 Slide 6: Student Task: Finish and evaluate
* **Student Activity:** Astronaut flight check panel wiring testing. Record speed time scores on review card sheet.

---

## 📸 Slide 7: Astronaut Flight Check Log
Observation logger:

| Flight Test Run | Wiring Time (Min:Sec) | Polarity Status (OK / Fault) | Rocket Status |
| :--- | :--- | :--- | :--- |
| **Launch Run A** | 04:35 mins | OK | **READY FOR IGNITION** 🚀 |
| **Launch Run B** | 07:12 mins | Fault (LED reversed) | **LAUNCH ABORTED (Debug)** 🛑 |

---

## 📸 Slide 8: Practical Test Quiz
* **Q1: Rocket cockpit indicator safety checks zero short warning parameters?**  
  *Answer:* Short circuit damages prevent checks prioritizing flight safety checks.
* **Q2: Circuit checks diagnostic flow sequence parameters check limits?**  
  *Answer:* Step by step validations verify loops connection values before launch.
"""

    # FALLBACK / PREVIEW TEMPLATE FOR SESSIONS 11-30
    else:
        return f"""# Session {num:02d}: Class 3 Robotics Content Preview 🤖

**Class 3 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Welcome & Setup
![Setup]({s1})

> **Detailed content slide deck is currently loading for this session**

This slide deck is being prepared one-by-one to maintain highest visual and content detailing.
* **Keywords:** `Robotics` | `Engineering` | `Class 3`
* **Session number:** {num}

---

## 📸 Slide 2: Conceptual Details
Detailed explanation of this session's concepts will be loaded here.

---

## 📸 Slide 3: Visual Circuit Placeholder
<svg width="450" height="240" viewBox="0 0 450 240" style="display: block; margin: 20px auto; background: #f8fafc; border: 2px solid #e2e8f0; border-radius: 12px; font-family: sans-serif;">
  <rect width="100%" height="100%" fill="#f8fafc" rx="12"/>
  <text x="225" y="120" font-size="14" font-weight="bold" fill="#64748b" text-anchor="middle">Visual Diagram Pending Overhaul</text>
</svg>
"""
    return ""
