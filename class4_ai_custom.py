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
    s1 = get_base64_image("kit_overview.jpg")
    
    if num == 1:
        return f"""# Session 01: Introduction to mBlock 5 Interface 💻

**Class 4 – AI & SOFTWARE TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Welcome to the mBlock Coding Dimension!
![mBlock Coding Lab](https://images.unsplash.com/photo-1516116211223-5c359a36298a?w=800&q=80)

> **Toby the Cyber-Panda ko space dimension se rescue karne ke liye control panels (mBlock 5) chalana seekhna!**

Attention Space Coders! Toby the Cyber-Panda space dimension me navigation grid crash hone ki wajah se phas gaya hai. Use control karne ke liye hume mBlock 5 coding interface ke panels ko aur iske installation process ko master karna hoga. Aaiye is tools ko step-by-step setup aur design karein!
* **Keywords:** `Stage` | `Block Palette` | `Script Area` | `Installation`
* **Session Target:** Install mBlock 5, map the 3 interface zones, and make Toby walk!

---

## 📸 Slide 2: Installing mBlock 5 – Select Your Platform!
<svg width="420" height="200" viewBox="0 0 420 200" style="display:block; margin:15px auto; background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; font-family:sans-serif;">
  <!-- Browser frame mockup -->
  <rect x="10" y="10" width="400" height="180" rx="6" fill="#ffffff" stroke="#cbd5e1" stroke-width="2"/>
  <rect x="10" y="10" width="400" height="25" fill="#f1f5f9" rx="6"/>
  <circle cx="25" cy="22" r="4" fill="#ef4444"/>
  <circle cx="37" cy="22" r="4" fill="#f59e0b"/>
  <circle cx="49" cy="22" r="4" fill="#10b981"/>
  <rect x="70" y="15" width="220" height="14" rx="3" fill="#ffffff" stroke="#cbd5e1"/>
  <text x="80" y="25" font-size="7" fill="#64748b">https://www.mblock.cc/download/</text>

  <!-- Download choices -->
  <g transform="translate(40, 60)">
    <rect x="0" y="0" width="150" height="100" rx="8" fill="#e0f2fe" stroke="#38bdf8" stroke-width="2"/>
    <text x="75" y="30" font-size="10" font-weight="bold" fill="#0369a1" text-anchor="middle">mBlock PC Desktop</text>
    <rect x="25" y="55" width="100" height="25" rx="4" fill="#0ea5e9"/>
    <text x="75" y="71" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">Download (Win/Mac)</text>
  </g>

  <g transform="translate(230, 60)">
    <rect x="0" y="0" width="150" height="100" rx="8" fill="#ecfdf5" stroke="#34d399" stroke-width="2"/>
    <text x="75" y="30" font-size="10" font-weight="bold" fill="#065f46" text-anchor="middle">mBlock Web Editor</text>
    <rect x="25" y="55" width="100" height="25" rx="4" fill="#10b981"/>
    <text x="75" y="71" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">Code in Browser</text>
  </g>
  
  {get_hand_svg(140, 130, "Click Download")}
</svg>

mBlock 5 ko computer me install karne ke liye official download steps:
* **Official URL:** Apne browser par **`www.mblock.cc/download/`** search karein.
* **Option A (Desktop App):** Windows ya Mac setup installers select karke local machine par download start karein.
* **Option B (Web Editor):** Bina install kiye directly chrome browser window par block-code edit run run controls handle karein.

---

## 📸 Slide 3: The Setup Wizard & Installation Wizard
<svg width="420" height="200" viewBox="0 0 420 200" style="display:block; margin:15px auto; background:#f8fafc; border:2px solid #e2e8f0; border-radius:12px; font-family:sans-serif;">
  <!-- Setup progress popup mockup -->
  <rect x="50" y="25" width="320" height="150" rx="8" fill="#ffffff" stroke="#94a3b8" stroke-width="2"/>
  <rect x="50" y="25" width="320" height="20" fill="#3b82f6" rx="8"/>
  <text x="65" y="38" font-size="8" font-weight="bold" fill="#ffffff">mBlock 5 Setup - Installing</text>
  
  <text x="70" y="70" font-size="9" fill="#1e293b">Extracting files and creating shortcuts...</text>
  
  <!-- Loading progress bar -->
  <rect x="70" y="90" width="280" height="20" rx="3" fill="#e2e8f0"/>
  <rect x="70" y="90" width="180" height="20" rx="3" fill="#10b981"/>
  <text x="210" y="103" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">65% Complete</text>
  
  <rect x="235" y="135" width="60" height="22" rx="3" fill="#e2e8f0" stroke="#cbd5e1"/>
  <text x="265" y="148" font-size="8" fill="#475569" text-anchor="middle">Next ></text>
  <rect x="300" y="135" width="60" height="22" rx="3" fill="#cbd5e1"/>
  <text x="330" y="148" font-size="8" fill="#1e293b" text-anchor="middle">Cancel</text>
</svg>

Setup file download karne ke baad local installation path execution instructions:
1. **Open Setup File:** `.exe` installer double-click run karein.
2. **Permission Check:** System prompt popup alerts aane par "Yes / Run" select karein.
3. **Progress Wizard:** Wizard launch hone par storage path choice (e.g. C Drive) confirm karke loading bar complete hone ka wait karein.
4. **Launch:** Desktop short-cut click karke dashboard workspace access karein!

---

## 📸 Slide 4: What is mBlock 5? (The Power of Snapping Blocks)
<svg width="350" height="180" viewBox="0 0 350 180" style="display:block; margin:15px auto; background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; font-family:sans-serif;">
  <!-- Scratch Block 1 -->
  <g transform="translate(100, 30)">
    <path d="M 0 0 L 150 0 L 150 30 L 70 30 L 60 40 L 40 40 L 30 30 L 0 30 Z" fill="#ffab19" stroke="#cf8b17" stroke-width="1.5"/>
    <text x="75" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">when green flag clicked</text>
  </g>
  <!-- Scratch Block 2 -->
  <g transform="translate(100, 70)">
    <path d="M 0 0 L 30 0 L 40 10 L 60 10 L 70 0 L 150 0 L 150 30 L 70 30 L 60 40 L 40 40 L 30 30 L 0 30 Z" fill="#4c97ff" stroke="#3373cc" stroke-width="1.5"/>
    <text x="75" y="18" font-size="10" font-weight="bold" fill="#ffffff" text-anchor="middle">move (10) steps</text>
  </g>
  <!-- Animated Snap Arrows -->
  <path d="M 175 62 L 175 68" fill="none" stroke="#22c55e" stroke-width="3" marker-end="url(#arrow)"/>
  <text x="210" y="65" font-size="8" font-weight="bold" fill="#22c55e">Snap Connect! 🧩</text>
</svg>

mBlock 5 blocks coordinate logic par build hai:
* **Visual Programming:** Hume dynamic lines of code write-down nahi karni padti. Hum building block puzzles ki tarah blocks ko snap connect karte hain instructions create karne ke liye.
* **Blocks Categories:** Har block color-coded hota hai. Jaise:
  - **Event (Yellow):** Codes ko start karne wale triggers (e.g. key pressed).
  - **Motion (Blue):** Wires blocks jo movements coordinates change karte hain.

---

## 📸 Slide 5: The 3 Main Control Zones (Dashboard Overview)
<svg width="400" height="220" viewBox="0 0 400 220" style="display:block; margin:15px auto; background:#1e293b; border:2px solid #38bdf8; border-radius:8px; font-family:sans-serif;">
  <!-- Stage Zone -->
  <g transform="translate(20, 30)">
    <rect x="0" y="0" width="100" height="110" fill="#0f172a" stroke="#475569" stroke-width="1.5"/>
    <circle cx="50" cy="55" r="15" fill="#eab308" fill-opacity="0.2"/>
    <text x="50" y="100" font-size="8" fill="#eab308" text-anchor="middle">STAGE (Toby's View)</text>
  </g>
  
  <!-- Block Palette -->
  <g transform="translate(130, 30)">
    <rect x="0" y="0" width="100" height="150" fill="#334155" stroke="#475569" stroke-width="1.5"/>
    <rect x="10" y="20" width="80" height="20" rx="3" fill="#ffab19"/>
    <rect x="10" y="50" width="80" height="20" rx="3" fill="#4c97ff"/>
    <rect x="10" y="80" width="80" height="20" rx="3" fill="#4cd03b"/>
    <text x="50" y="140" font-size="8" fill="#94a3b8" text-anchor="middle">BLOCK PALETTE</text>
  </g>

  <!-- Script Area -->
  <g transform="translate(240, 30)">
    <rect x="0" y="0" width="140" height="150" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>
    <!-- Stacked blocks -->
    <path d="M 20 20 L 120 20 L 120 40 L 70 40 L 60 45 L 40 45 L 30 40 L 20 40 Z" fill="#ffab19"/>
    <path d="M 20 42 L 30 42 L 40 47 L 60 47 L 70 42 L 120 42 L 120 62 L 70 62 L 60 67 L 40 67 L 30 62 L 20 62 Z" fill="#4c97ff"/>
    <text x="70" y="140" font-size="8" fill="#38bdf8" text-anchor="middle">SCRIPT AREA (Code Workspace)</text>
  </g>
</svg>

Space station cockpit panel divides into 3 key compartments:
1. **The Stage (स्टेज):** Screen ka left-top section jahan Toby code changes execute hote hi live act/run karta hai.
2. **The Block Palette (ब्लॉक टूलकिट):** Center list jisme category wise ready-made blocks range store rehti hai.
3. **The Script Area (कोडिंग एरिया):** Space right side jahan blocks ko assemble aur link karke programs design kiye jate hain.

---

## 📸 Slide 6: Sprites (Actors) vs Devices (Hardware)
<svg width="350" height="180" viewBox="0 0 350 180" style="display:block; margin:15px auto; background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; font-family:sans-serif;">
  <!-- Sprite Section -->
  <g transform="translate(40, 30)">
    <rect x="0" y="0" width="110" height="100" rx="4" fill="#fee2e2" stroke="#fca5a5" stroke-width="2"/>
    <circle cx="55" cy="40" r="18" fill="#ef4444" fill-opacity="0.8"/>
    <text x="55" y="85" font-size="10" font-weight="bold" fill="#b91c1c" text-anchor="middle">Sprite (Toby)</text>
  </g>
  <!-- Device Section -->
  <g transform="translate(200, 30)">
    <rect x="0" y="0" width="110" height="100" rx="4" fill="#e0f2fe" stroke="#7dd3fc" stroke-width="2"/>
    <rect x="25" y="25" width="60" height="35" fill="#0ea5e9" rx="3"/>
    <text x="55" y="85" font-size="10" font-weight="bold" fill="#0369a1" text-anchor="middle">Device (Arduino)</text>
  </g>
</svg>

Dono dynamic categories me difference clear samajhein:
* **Sprites (digital characters):** Virtual actors jo screen stage window ke boundaries me act aur change variables manipulate karte hain (e.g. Toby, balls).
* **Devices (physical components):** External links jo hardware boards and microchips interface command controls detect karte hain (e.g. Arduino UNO, Halocode).

---

## 📸 Slide 7: The Extension Center (AI Superpowers!)
<svg width="350" height="180" viewBox="0 0 350 180" style="display:block; margin:15px auto; background:#f8fafc; border:1px solid #e2e8f0; border-radius:8px; font-family:sans-serif;">
  <rect x="30" y="40" width="130" height="100" rx="6" fill="#f3e8ff" stroke="#c084fc" stroke-width="2"/>
  <circle cx="95" cy="75" r="20" fill="#a855f7"/>
  <text x="95" y="125" font-size="9" font-weight="bold" fill="#6b21a8" text-anchor="middle">AI Cognitive Services</text>

  <rect x="190" y="40" width="130" height="100" rx="6" fill="#ecfdf5" stroke="#34d399" stroke-width="2"/>
  <circle cx="255" cy="75" r="20" fill="#10b981"/>
  <text x="255" y="125" font-size="9" font-weight="bold" fill="#065f46" text-anchor="middle">IoT Cloud Dashboard</text>
  
  {get_hand_svg(165, 80, "Click + Extension")}
</svg>

mBlock interface extensions features expand rules:
* **The + Button:** Left bottom corner side me blue button check tab add libraries configurations.
* **AI Cognitive Services:** Voice, facial recognition, camera scanning, emotional evaluation parameters add locks.
* **IoT (Internet of Things):** Network servers link coordinate systems live data sharing.

---

## 📸 Slide 8: First Script Setup: Walk & Bounce Loop
<svg width="350" height="180" viewBox="0 0 350 180" style="display:block; margin:15px auto; background:#0f172a; border:2px solid #38bdf8; border-radius:8px; font-family:sans-serif;">
  <!-- Stack of blocks represented in vector SVG -->
  <g transform="translate(100, 20)">
    <path d="M 0 0 L 150 0 L 150 25 L 70 25 L 65 30 L 45 30 L 40 25 L 0 25 Z" fill="#ffab19"/>
    <text x="75" y="15" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">when green flag clicked</text>
  </g>
  <g transform="translate(100, 48)">
    <path d="M 0 0 L 40 0 L 45 5 L 65 5 L 70 0 L 150 0 L 150 110 L 70 110 L 65 115 L 45 115 L 40 110 L 0 110 Z" fill="#ffd042" stroke="#d0a030" stroke-width="1"/>
    <text x="35" y="18" font-size="8" font-weight="bold" fill="#ffffff">forever</text>
  </g>
  <!-- Mapped inner blocks of forever -->
  <g transform="translate(120, 75)">
    <path d="M 0 0 L 30 0 L 35 5 L 50 5 L 55 0 L 110 0 L 110 22 L 55 22 L 50 27 L 35 27 L 30 22 L 0 22 Z" fill="#4c97ff"/>
    <text x="55" y="14" font-size="7" font-weight="bold" fill="#ffffff" text-anchor="middle">move (10) steps</text>
  </g>
  <g transform="translate(120, 102)">
    <path d="M 0 0 L 30 0 L 35 5 L 50 5 L 55 0 L 110 0 L 110 22 L 55 22 L 50 27 L 35 27 L 30 22 L 0 22 Z" fill="#4c97ff"/>
    <text x="55" y="14" font-size="7" font-weight="bold" fill="#ffffff" text-anchor="middle">if on edge, bounce</text>
  </g>
</svg>

Astronaut flight checks step by step parameters check:
1. **Yellow trigger:** Drag `when green flag clicked` events block.
2. **Forever loop:** Connect `forever` control block directly below it.
3. **Move block:** Insert `move (10) steps` inside the forever loop brackets.
4. **Boundary guard:** Add `if on edge, bounce` to ensure Toby does not fly away from stage!

---

## 📸 Slide 9: Engaging Lab Task: "The Space Ship Calibration!" 🛸
* **Your Mission:** Calibrate Toby's spaceship control deck!
  1. Open mBlock 5 Web Editor or Desktop App.
  2. **Add a Sprite:** Character list me "Toby" select karein aur load checks ensure.
  3. **Weld the Blocks:** Slide 8 ke stack loop coordinates blocks complete snap lock align structure check.
  4. **Click the green flag:** Run code. Toby will walk back and forth on the stage!
  5. **Load Pen Extension:** Extension page open karke "Pen" add click check. Write blocks stack to draw square lines.

---

## 📸 Slide 10: Flight Check Log Book
Observation logs coordinates sheet check:

| Control Panel Zone | Function | Success Status | Coordinates Range |
| :--- | :--- | :--- | :--- |
| **Stage screen** | Displays Sprite (Toby) movements | ✅ Verified | $X: -240$ to $240$ |
| **Block Palette** | Holds command blocks toolkits | ✅ Verified | Colored Categories |
| **Script area** | Compiled stack logic programs | ✅ Verified | 4 Snapped Blocks |

---

## 📸 Slide 11: Cyber Quiz (Knowledge Check)
* **Q1: mBlock 5 interface me "Script Area" ka main function kya hota hai?**  
  *Answer:* Script area wo workspace/koila hai jahan hum code blocks drag-drop aur links snap lock karke programs build karte hain.
* **Q2: Sprites aur Devices templates mapping loops checks differentiate?**  
  *Answer:* Sprite screen output character data holds (Toby), devices physical hardware chips (Arduino) handles details.
* **Q3: "if on edge, bounce" control block why it's critical loops limits?**  
  *Answer:* Code checks coordinates margins bounds blocks stage boundary loops reset.
"""
    elif num == 2:
        return f"""# Session 02: Sprite Movement & Loops 🌀

**Class 4 – AI & SOFTWARE TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Welcome to the Nebula Disco Zone! 🪩
![Neon Cyber Panda](https://images.unsplash.com/photo-1508700115892-45ecd05ae2ad?w=800&q=80)

> **Toby the Cyber-Panda ko space party me dance karana aur rainbow laser chase script code karna!**

Hey Code Creators! Toby space disco nebula grid me pahunch chuka hai. Use screen par hamare mouse cursor ke peeche-peeche bhagana hai, flashy colors change karwane hain, aur dynamic loops ke through dance trails stamp karwane hain! Aaiye ek interactive mouse follower game code karte hain!
* **Keywords:** `Mouse Chaser` | `Color Effects` | `Stamp Trail` | `Forever Loops`
* **Session Target:** Program Toby to follow the mouse, change rainbow colors, and draw disco stamps.

---

## 📸 Slide 2: The Magic Blocks Toolkit (Toby's Brain Blocks)
<svg width="400" height="200" viewBox="0 0 400 200" style="display:block; margin:15px auto; background:#0f172a; border:2px solid #a855f7; border-radius:10px; font-family:sans-serif;">
  <!-- Point towards mouse-pointer block -->
  <g transform="translate(30, 25)">
    <path d="M 0 0 L 160 0 L 160 30 L 70 30 L 60 40 L 40 40 L 30 30 L 0 30 Z" fill="#4c97ff"/>
    <text x="80" y="18" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">point towards [mouse-pointer v]</text>
  </g>
  <!-- Change color effect block -->
  <g transform="translate(210, 25)">
    <path d="M 0 0 L 160 0 L 160 30 L 70 30 L 60 40 L 40 40 L 30 30 L 0 30 Z" fill="#9966ff"/>
    <text x="80" y="18" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">change [color v] effect by (25)</text>
  </g>
  <!-- Stamp block -->
  <g transform="translate(120, 95)">
    <path d="M 0 0 L 160 0 L 160 30 L 70 30 L 60 40 L 40 40 L 30 30 L 0 30 Z" fill="#00c5bc"/>
    <text x="80" y="18" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">stamp 👣</text>
  </g>
</svg>

Disco party launch karne ke liye hume in **3 smart blocks** ko use karna hoga:
1. **`point towards [mouse-pointer v]` (Blue):** Toby ka nose target hamare mouse pointer direction coordinates par focus kar deta hai.
2. **`change [color v] effect by (25)` (Purple):** Toby ko har cycle me different neon rainbow color shade me transform karta hai.
3. **`stamp` (Teal - Pen Extension):** Toby ki screen footprint copy create karta hai, jisse dynamic painting patterns banaye ja sakein!

---

## 📸 Slide 3: Step-by-Step Code Assembly (The Disco Stack)
<svg width="350" height="220" viewBox="0 0 350 220" style="display:block; margin:15px auto; background:#0f172a; border:2px solid #38bdf8; border-radius:8px; font-family:sans-serif;">
  <!-- Green flag trigger -->
  <g transform="translate(90, 10)">
    <path d="M 0 0 L 170 0 L 170 25 L 70 25 L 65 30 L 45 30 L 40 25 L 0 25 Z" fill="#ffab19"/>
    <text x="85" y="15" font-size="8" font-weight="bold" fill="#ffffff" text-anchor="middle">when green flag clicked</text>
  </g>
  <!-- Forever Bracket -->
  <g transform="translate(90, 38)">
    <path d="M 0 0 L 40 0 L 45 5 L 65 5 L 70 0 L 170 0 L 170 170 L 70 170 L 65 175 L 45 175 L 40 170 L 0 170 Z" fill="#ffd042"/>
    <text x="30" y="15" font-size="8" font-weight="bold" fill="#ffffff">forever</text>
  </g>
  <!-- Point towards mouse-pointer -->
  <g transform="translate(110, 60)">
    <path d="M 0 0 L 30 0 L 35 5 L 50 5 L 55 0 L 140 0 L 140 22 L 55 22 L 50 27 L 35 27 L 30 22 L 0 22 Z" fill="#4c97ff"/>
    <text x="70" y="14" font-size="7" font-weight="bold" fill="#ffffff" text-anchor="middle">point towards [mouse-pointer v]</text>
  </g>
  <!-- move steps -->
  <g transform="translate(110, 85)">
    <path d="M 0 0 L 30 0 L 35 5 L 50 5 L 55 0 L 140 0 L 140 22 L 55 22 L 50 27 L 35 27 L 30 22 L 0 22 Z" fill="#4c97ff"/>
    <text x="70" y="14" font-size="7" font-weight="bold" fill="#ffffff" text-anchor="middle">move (15) steps</text>
  </g>
  <!-- change color effect -->
  <g transform="translate(110, 110)">
    <path d="M 0 0 L 30 0 L 35 5 L 50 5 L 55 0 L 140 0 L 140 22 L 55 22 L 50 27 L 35 27 L 30 22 L 0 22 Z" fill="#9966ff"/>
    <text x="70" y="14" font-size="7" font-weight="bold" fill="#ffffff" text-anchor="middle">change [color v] effect by (15)</text>
  </g>
  <!-- stamp -->
  <g transform="translate(110, 135)">
    <path d="M 0 0 L 30 0 L 35 5 L 50 5 L 55 0 L 140 0 L 140 22 L 55 22 L 50 27 L 35 27 L 30 22 L 0 22 Z" fill="#00c5bc"/>
    <text x="70" y="14" font-size="7" font-weight="bold" fill="#ffffff" text-anchor="middle">stamp</text>
  </g>
</svg>

Let's lock Toby's dance engine instructions step-by-step:
1. **Trigger:** Drag `when green flag clicked` events block.
2. **Loop Bracket:** Connect the `forever` controller block directly below it.
3. **Follow Cursor:** Insert `point towards [mouse-pointer v]` inside the loop.
4. **Chase speed:** Add `move (15) steps` to control his speed.
5. **Color flash:** Add `change [color v] effect by (15)` to loop rainbow lights.
6. **Disco footprints:** Finally, add `stamp` block so he paints the screen!

---

## 📸 Slide 4: Interactive Student Lab Task (Play & Modify!) 🎮
* **Your Mission:** Assemble the code and wave your mouse pointer around the stage screen!
  1. Open mBlock 5 (Web or Desktop).
  2. **Add Pen Extension:** Left bottom corner me **`+ Add Extension`** click karke **`Pen`** toolkit select karein.
  3. **Weld the Blocks:** Drag-drop Slide 3 block stack pattern workspace me.
  4. Click the **Green Flag** and drag your mouse around the Stage! Toby will chase your cursor, flash neon colors, and draw incredible rainbow disco trails!
  
### 🚀 Extreme Hacker Modifications (Try These!):
* **Challenge 1 (Size Warping):** Add `change size by (2)` block inside the loop, aur code ke starting me `set size to (50)%` set karein. Toby cursor chase karte-karte grow karega!
* **Challenge 2 (Clear Screen Button):** Control event setup karein: `when [space key v] pressed` -> `erase all` (from Pen category) tab clean canvas screen instantly!

---

## 📸 Slide 5: Space Pilot's Disco Log Book
Student checks and observation logs:

| Speed Input (steps) | Special Effect Value | Space Key Pressed | Screen Output |
| :--- | :--- | :--- | :--- |
| **5 steps** | color by 10 | space key | Slow rainbow trail, press space to clear |
| **25 steps** | color by 50 | space key | Turbo rainbow chase! Toby runs super fast |
| **15 steps** | **no color/no stamp** | space key | Normal panda walk, no neon lights |

---

## 📸 Slide 6: Command Center Quiz
* **Q1: `point towards [mouse-pointer v]` block ka kya role hai hamare program me?**  
  *Answer:* Wo Toby sprite ko direct alignment directions control points pointer location coordinates matching set rakhta hai.
* **Q2: Pen extension library ka `stamp` block standard drawing line brushes se kaise different hai?**  
  *Answer:* Line drawing continuous lines draw karta hai, jabki `stamp` sprite ki raw image print copies place coordinate stamps drop karta hai.
* **Q3: Space bar click program me `erase all` block execute hone par kya change hota hai?**  
  *Answer:* Stage window screen par bane hue sabhi stamps aur footprints paths clean canvas resets parameters updates handle details.
"""
    elif num == 3:
        return f"""# Session 03: mBlock Event Blocks 🚀

**Class 4 – AI & SOFTWARE TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Welcome to the Laser Cruiser Academy! 🛸
![Space Cruiser Setup](https://images.unsplash.com/photo-1612287230202-1bf1d85d1bdf?w=800&q=80)

> **Toby the Cyber-Panda ke Spaceship ko keyboard arrow keys se steer karna aur mouse click se laser blast trigger code karna!**

Hey Space Pilots! Toby ne asteroid fields me entry le li hai. Debris se bachne aur path clear karne ke liye hume dynamic keyboard controls aur instant mouse click triggers setup karne honge. Aaiye is session me Events trigger programming seekhte hain!
* **Keywords:** `Keyboard Events` | `Mouse Click Triggers` | `Direction Steering` | `Costume Switch`
* **Session Target:** Program a playable Arrow-Key controlled spaceship that plays sound effects on click.

---

## 📸 Slide 2: What is an Event Trigger? (Hat Blocks)
![Big Red Launch Button](https://images.unsplash.com/photo-1596495578065-6e0763fa1178?w=800&q=80)

mBlock me "Event Blocks" (Hat Blocks) specialized triggers hote hain:
* **Passive Listening:** Ye blocks continuous program run nahi karte. Ye background me screen/key signals monitor karte hain aur specific key down hone par hi instant code run trigger karte hain.
* **Arrow Steering:** Har trigger block ke sath hum direction parameters map karte hain taaki ship correct route me move kar sake.

---

## 📸 Slide 3: The 4-Way Steering System (Keyboard Events)
<svg width="420" height="230" viewBox="0 0 420 230" style="display:block; margin:15px auto; background:#0f172a; border:2px solid #38bdf8; border-radius:10px; font-family:sans-serif;">
  <!-- Grid of 4 arrow stacks -->
  
  <!-- UP Arrow Stack (Top Left) -->
  <g transform="translate(15, 15)">
    <!-- Hat Block: when [up arrow] pressed -->
    <path d="M 0 12 C 0 4, 8 0, 20 0 L 160 0 C 170 0, 180 4, 180 12 L 180 25 L 55 25 L 50 30 L 35 30 L 30 25 L 0 25 Z" fill="#ffb000" stroke="#d49200" stroke-width="1.5"/>
    <text x="90" y="16" font-size="7" font-weight="bold" fill="#ffffff" text-anchor="middle">when [up arrow v] key pressed</text>
    
    <!-- Command: point in direction (0) -->
    <g transform="translate(0, 26)">
      <path d="M 0 0 L 30 0 L 35 5 L 50 5 L 55 0 L 180 0 L 180 22 L 55 22 L 50 27 L 35 27 L 30 22 L 0 22 Z" fill="#4c97ff" stroke="#3373cc" stroke-width="1.5"/>
      <text x="90" y="14" font-size="7" font-weight="bold" fill="#ffffff" text-anchor="middle">point in direction (0 v)</text>
    </g>
    
    <!-- Command: move (15) steps -->
    <g transform="translate(0, 49)">
      <path d="M 0 0 L 30 0 L 35 5 L 50 5 L 55 0 L 180 0 L 180 22 L 55 22 L 50 27 L 35 27 L 30 22 L 0 22 Z" fill="#4c97ff" stroke="#3373cc" stroke-width="1.5"/>
      <text x="90" y="14" font-size="7" font-weight="bold" fill="#ffffff" text-anchor="middle">move (15) steps</text>
    </g>
  </g>

  <!-- RIGHT Arrow Stack (Top Right) -->
  <g transform="translate(225, 15)">
    <path d="M 0 12 C 0 4, 8 0, 20 0 L 160 0 C 170 0, 180 4, 180 12 L 180 25 L 55 25 L 50 30 L 35 30 L 30 25 L 0 25 Z" fill="#ffb000" stroke="#d49200" stroke-width="1.5"/>
    <text x="90" y="16" font-size="7" font-weight="bold" fill="#ffffff" text-anchor="middle">when [right arrow v] key pressed</text>
    <g transform="translate(0, 26)">
      <path d="M 0 0 L 30 0 L 35 5 L 50 5 L 55 0 L 180 0 L 180 22 L 55 22 L 50 27 L 35 27 L 30 22 L 0 22 Z" fill="#4c97ff" stroke="#3373cc" stroke-width="1.5"/>
      <text x="90" y="14" font-size="7" font-weight="bold" fill="#ffffff" text-anchor="middle">point in direction (90 v)</text>
    </g>
    <g transform="translate(0, 49)">
      <path d="M 0 0 L 30 0 L 35 5 L 50 5 L 55 0 L 180 0 L 180 22 L 55 22 L 50 27 L 35 27 L 30 22 L 0 22 Z" fill="#4c97ff" stroke="#3373cc" stroke-width="1.5"/>
      <text x="90" y="14" font-size="7" font-weight="bold" fill="#ffffff" text-anchor="middle">move (15) steps</text>
    </g>
  </g>

  <!-- DOWN Arrow Stack (Bottom Left) -->
  <g transform="translate(15, 125)">
    <path d="M 0 12 C 0 4, 8 0, 20 0 L 160 0 C 170 0, 180 4, 180 12 L 180 25 L 55 25 L 50 30 L 35 30 L 30 25 L 0 25 Z" fill="#ffb000" stroke="#d49200" stroke-width="1.5"/>
    <text x="90" y="16" font-size="7" font-weight="bold" fill="#ffffff" text-anchor="middle">when [down arrow v] key pressed</text>
    <g transform="translate(0, 26)">
      <path d="M 0 0 L 30 0 L 35 5 L 50 5 L 55 0 L 180 0 L 180 22 L 55 22 L 50 27 L 35 27 L 30 22 L 0 22 Z" fill="#4c97ff" stroke="#3373cc" stroke-width="1.5"/>
      <text x="90" y="14" font-size="7" font-weight="bold" fill="#ffffff" text-anchor="middle">point in direction (180 v)</text>
    </g>
    <g transform="translate(0, 49)">
      <path d="M 0 0 L 30 0 L 35 5 L 50 5 L 55 0 L 180 0 L 180 22 L 55 22 L 50 27 L 35 27 L 30 22 L 0 22 Z" fill="#4c97ff" stroke="#3373cc" stroke-width="1.5"/>
      <text x="90" y="14" font-size="7" font-weight="bold" fill="#ffffff" text-anchor="middle">move (15) steps</text>
    </g>
  </g>

  <!-- LEFT Arrow Stack (Bottom Right) -->
  <g transform="translate(225, 125)">
    <path d="M 0 12 C 0 4, 8 0, 20 0 L 160 0 C 170 0, 180 4, 180 12 L 180 25 L 55 25 L 50 30 L 35 30 L 30 25 L 0 25 Z" fill="#ffb000" stroke="#d49200" stroke-width="1.5"/>
    <text x="90" y="16" font-size="7" font-weight="bold" fill="#ffffff" text-anchor="middle">when [left arrow v] key pressed</text>
    <g transform="translate(0, 26)">
      <path d="M 0 0 L 30 0 L 35 5 L 50 5 L 55 0 L 180 0 L 180 22 L 55 22 L 50 27 L 35 27 L 30 22 L 0 22 Z" fill="#4c97ff" stroke="#3373cc" stroke-width="1.5"/>
      <text x="90" y="14" font-size="7" font-weight="bold" fill="#ffffff" text-anchor="middle">point in direction (-90 v)</text>
    </g>
    <g transform="translate(0, 49)">
      <path d="M 0 0 L 30 0 L 35 5 L 50 5 L 55 0 L 180 0 L 180 22 L 55 22 L 50 27 L 35 27 L 30 22 L 0 22 Z" fill="#4c97ff" stroke="#3373cc" stroke-width="1.5"/>
      <text x="90" y="14" font-size="7" font-weight="bold" fill="#ffffff" text-anchor="middle">move (15) steps</text>
    </g>
  </g>
</svg>

Steering configurations and direction details:
* **Steer Up (⬆️):** Point in direction `0` sets Toby facing straight up, then moves forward.
* **Steer Right (➡️):** Point in direction `90` sets Toby facing right.
* **Steer Left (⬅️):** Point in direction `-90` sets Toby facing left.
* **Steer Down (⬇️):** Point in direction `180` sets Toby facing straight down.

---

## 📸 Slide 4: Space Laser Blast! (Acoustic Trigger)
![Neon Laser Beam](https://images.unsplash.com/photo-1507608869274-d3177c8bb4c7?w=800&q=80)

<svg width="400" height="180" viewBox="0 0 400 180" style="display:block; margin:15px auto; background:#0f172a; border:2px solid #a855f7; border-radius:10px; font-family:sans-serif;">
  <!-- Clicking sprite trigger -->
  <g transform="translate(100, 20)">
    <!-- Hat: when this sprite clicked -->
    <path d="M 0 12 C 0 4, 8 0, 20 0 L 180 0 C 190 0, 200 4, 200 12 L 200 25 L 55 25 L 50 30 L 35 30 L 30 25 L 0 25 Z" fill="#ffb000" stroke="#d49200" stroke-width="1.5"/>
    <text x="100" y="16" font-size="8.5" font-weight="bold" fill="#ffffff" text-anchor="middle">when this sprite clicked</text>
    
    <!-- Command: start sound [laser1] -->
    <g transform="translate(0, 26)">
      <path d="M 0 0 L 30 0 L 35 5 L 50 5 L 55 0 L 200 0 L 200 22 L 55 22 L 50 27 L 35 27 L 30 22 L 0 22 Z" fill="#cf63cf" stroke="#b356b3" stroke-width="1.5"/>
      <text x="100" y="14" font-size="7.5" font-weight="bold" fill="#ffffff" text-anchor="middle">start sound [laser1 v]</text>
    </g>
    
    <!-- Command: change size by (20) -->
    <g transform="translate(0, 49)">
      <path d="M 0 0 L 30 0 L 35 5 L 50 5 L 55 0 L 200 0 L 200 22 L 55 22 L 50 27 L 35 27 L 30 22 L 0 22 Z" fill="#9966ff" stroke="#8055cc" stroke-width="1.5"/>
      <text x="100" y="14" font-size="7.5" font-weight="bold" fill="#ffffff" text-anchor="middle">change size by (20)</text>
    </g>
    
    <!-- Command: wait 0.1 secs -->
    <g transform="translate(0, 72)">
      <path d="M 0 0 L 30 0 L 35 5 L 50 5 L 55 0 L 200 0 L 200 22 L 55 22 L 50 27 L 35 27 L 30 22 L 0 22 Z" fill="#ffd042" stroke="#d0a030" stroke-width="1.5"/>
      <text x="100" y="14" font-size="7.5" font-weight="bold" fill="#ffffff" text-anchor="middle">wait (0.1) secs</text>
    </g>
    
    <!-- Command: change size by (-20) -->
    <g transform="translate(0, 95)">
      <path d="M 0 0 L 30 0 L 35 5 L 50 5 L 55 0 L 200 0 L 200 22 L 55 22 L 50 27 L 35 27 L 30 22 L 0 22 Z" fill="#9966ff" stroke="#8055cc" stroke-width="1.5"/>
      <text x="100" y="14" font-size="7.5" font-weight="bold" fill="#ffffff" text-anchor="middle">change size by (-20)</text>
    </g>
  </g>
  
  {get_hand_svg(315, 35, "Click Toby")}
</svg>

Mouse clicks trigger space-ship feedback systems:
* **Audio Warning:** Spaceship (Toby) par click target hote hi `start sound [laser1 v]` trigger call sound play karegi.
* **Recoil Feedback:** Laser fire ki feel dene ke liye ship ki size temporarily `change size by (20)` badhegi aur instant recoil loop me `change size by (-20)` normal size reset ho jayegi!

---

## 📸 Slide 5: Interactive Student Lab Task: "The Asteroid Dodger!" 🎮
* **Your Mission:** Code a keyboard-steered cruiser that shoots lasers on click!
  1. Open mBlock 5 editor workspace.
  2. **Select Space Backdrop:** Stage library me se space galaxy background select karein.
  3. **Assemble Steering Triggers:** Slide 3 ke parameters map ke acche se **charo arrow key events** setup aur links connect check karein.
  4. **Assemble Laser Audio:** Slide 4 loop blocks snap connect script design setup.
  5. Run flag. Drive your spaceship around the screen using arrows and click Toby to blast asteroids!
  
### 🚀 Pro-Hacker Enhancements:
* **Turbo Boost:** Event block add karein: `when [space v] key pressed` -> `move (35) steps` to warp-speed dash through asteroids!
* **Alarm Check:** Motion category me add boundaries parameters checking alert sound warnings!

---

## 📸 Slide 6: Space Pilot's Control Room Log Book
Steering values logs:

| Key Input Trigger | Point In Direction | Ship Response | Sound Response |
| :--- | :--- | :--- | :--- |
| **Up Arrow ⬆️** | $0^\circ$ (Up) | Ship moves forward | None |
| **Left Arrow ⬅️** | $-90^\circ$ (Left) | Ship rotates left | None |
| **Mouse Click 🖱️** | No change | Shrinks/grows (recoil effect) | Play Laser sound 🔊 |

---

## 📸 Slide 7: Command Center Quiz
* **Q1: Events triggers coding programs me ordinary loops loops block se kaise different hain?**  
  *Answer:* Loops continuous flow execute karte hain, events passive monitor mode me background rules triggers listen inputs check.
* **Q2: Left arrow steer set limits point direction value mapping check?**  
  *Answer:* Direction should be set to $-90$ degrees coordinate alignments.
* **Q3: Size changes wait parameter mapping target kya show feedback?**  
  *Answer:* Recoil feedback loops checks system. Laser blasts visuals.
"""
    return ""
