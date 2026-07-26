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
```mermaid
graph LR
    A["🔋 9V Battery"] -->|🔴 Red Wire (+)| B["💡 LED (Long Leg)"]
    B -->|⚫ Black Wire (-)| C["🔋 9V Battery (-)"]

    style A fill:#f43f5e,stroke:#9f1239,stroke-width:3px,color:#fff
    style B fill:#10b981,stroke:#064e3b,stroke-width:3px,color:#fff
    style C fill:#1e293b,stroke:#0f172a,stroke-width:3px,color:#fff
```

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 🔴 **Red Wire (Positive Connection):** Battery snap ke **Red Wire (+)** ko LED ke **Longe Leg (+)** se direct touch/connect karein.
* ⚫ **Black Wire (Negative Connection):** Battery snap ke **Black Wire (-)** ko LED ke **Short Leg (-)** se connect karein.
* ⚡ **Glow Check:** Jaise hi dono wires sahi se connect honge, electricity ka flow start ho jayega aur LED bright glow karegi!

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
```mermaid
graph LR
    A["🔋 9V Battery (+)"] -->|🔴 Red Wire| B["🔘 Rocker Switch (Pin 1)"]
    B -->|🟡 Yellow/Red Wire| C["💡 LED (Long Leg)"]
    C -->|⚫ Black Wire| D["🔋 9V Battery (-)"]

    style A fill:#f43f5e,stroke:#9f1239,stroke-width:3px,color:#fff
    style B fill:#3b82f6,stroke:#1d4ed8,stroke-width:3px,color:#fff
    style C fill:#10b981,stroke:#064e3b,stroke-width:3px,color:#fff
    style D fill:#1e293b,stroke:#0f172a,stroke-width:3px,color:#fff
```

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 🔴 **Step 1:** Battery snap ke **Red Wire (+)** ko **Rocker Switch** ke Pin 1 par connect karein.
* 🟡 **Step 2:** Rocker Switch ke Pin 2 se ek **extra wire (Yellow/Red)** lekar **LED ke Long Leg (+)** par connect karein.
* ⚫ **Step 3:** Battery snap ke **Black Wire (-)** ko directly **LED ke Short Leg (-)** par lagayein.
* 🔄 **Toggle Check:** Switch ko press (ON) karein — loop close ho jayega aur light jalegi. Switch off karne par path open ho jayega aur light band hogi.

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
```mermaid
graph LR
    A["🔋 9V Battery (+)"] -->|🔴 Red Wire| B["💡 LED 1 (Long Leg)"]
    B -->|🔵 Blue Wire (Neg to Pos)| C["💡 LED 2 (Long Leg)"]
    C -->|⚫ Black Wire| D["🔋 9V Battery (-)"]

    style A fill:#f43f5e,stroke:#9f1239,stroke-width:3px,color:#fff
    style B fill:#10b981,stroke:#064e3b,stroke-width:3px,color:#fff
    style C fill:#a855f7,stroke:#6b21a8,stroke-width:3px,color:#fff
    style D fill:#1e293b,stroke:#0f172a,stroke-width:3px,color:#fff
```

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 🔴 **Step 1:** Battery snap ke **Red Wire (+)** ko **LED 1 के Long Leg (+)** par connect karein.
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
```mermaid
graph TD
    A["🔋 9V Battery (+)"] -->|🔴 Red Wire| B["🔴 Junction Point A"]
    B -->|🔴 Red Wire Branch| C["💡 LED 1 (Long Leg)"]
    B -->|🔴 Red Wire Branch| D["💡 LED 2 (Long Leg)"]
    C -->|⚫ Black Wire| E["⚫ Junction Point B"]
    D -->|⚫ Black Wire| E
    E -->|⚫ Black Wire| F["🔋 9V Battery (-)"]

    style A fill:#f43f5e,stroke:#9f1239,stroke-width:3px,color:#fff
    style B fill:#f97316,stroke:#c2410c,stroke-width:3px,color:#fff
    style C fill:#10b981,stroke:#064e3b,stroke-width:3px,color:#fff
    style D fill:#a855f7,stroke:#6b21a8,stroke-width:3px,color:#fff
    style E fill:#64748b,stroke:#334155,stroke-width:3px,color:#fff
    style F fill:#1e293b,stroke:#0f172a,stroke-width:3px,color:#fff
```

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 🔴 **Step 1:** Dono LEDs ke **Long Legs (+)** ko aapas mein ek joint (Junction Point A) par jodein aur use battery ke **Red Wire (+)** se connect karein.
* ⚫ **Step 2:** Dono LEDs ke **Short Legs (-)** ko dusre joint (Junction Point B) par jodein aur use battery ke **Black Wire (-)** se connect karein.
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
```mermaid
graph LR
    A["🔋 9V Battery (+)"] -->|🔴 Red Wire| B["🔘 Push Button (Pin 1)"]
    B -->|🟡 Yellow Wire (When Pressed)| C["💡 LED (Long Leg)"]
    C -->|⚫ Black Wire| D["🔋 9V Battery (-)"]

    style A fill:#f43f5e,stroke:#9f1239,stroke-width:3px,color:#fff
    style B fill:#3b82f6,stroke:#1d4ed8,stroke-width:3px,color:#fff
    style C fill:#10b981,stroke:#064e3b,stroke-width:3px,color:#fff
    style D fill:#1e293b,stroke:#0f172a,stroke-width:3px,color:#fff
```

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
```mermaid
graph LR
    A["🔋 9V Battery (+)"] -->|🔴 Red Wire| B["🔘 Slide Switch (Pin 1)"]
    B -->|🟡 Yellow Wire| C["💡 Bright Torch LED (+)"]
    C -->|⚫ Black Wire| D["🔋 9V Battery (-)"]

    style A fill:#f43f5e,stroke:#9f1239,stroke-width:3px,color:#fff
    style B fill:#3b82f6,stroke:#1d4ed8,stroke-width:3px,color:#fff
    style C fill:#10b981,stroke:#064e3b,stroke-width:3px,color:#fff
    style D fill:#1e293b,stroke:#0f172a,stroke-width:3px,color:#fff
```

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 🔴 **Step 1:** Battery snap ke **Red Wire (+)** ko **Slide Switch** ke side pin par jodein.
* 🟡 **Step 2:** Switch ke center pin se extra wire lekar **Torch LED ke positive leg (+)** se connect karein.
* ⚫ **Step 3:** Battery snap ke **Black Wire (-)** ko directly **LED ke negative leg (-)** se jodein.
* 🛠️ **Body Assembly:** Cardboard paper roll banakar battery aur switch ko tape se chipkaye.

---

## 📸 Slide 5: Student Task — Hands-On Practice
1. **Torch Assembly:** Apna handheld model assemble karein aur andhere me focus beam test karein.
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
```mermaid
graph LR
    A["🔋 9V Battery (+)"] -->|🔴 Red Wire (+)| B["🔊 Active Buzzer (Long Leg)"]
    B -->|⚫ Black Wire (-)| C["🔋 9V Battery (-)"]

    style A fill:#f43f5e,stroke:#9f1239,stroke-width:3px,color:#fff
    style B fill:#f59e0b,stroke:#b45309,stroke-width:3px,color:#fff
    style C fill:#1e293b,stroke:#0f172a,stroke-width:3px,color:#fff
```

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 🔴 **Red Wire (Buzzer Positive):** Battery snap ke **Red Wire (+)** ko active buzzer ke **Long Leg (+)** se direct touch/connect karein.
* ⚫ **Black Wire (Buzzer Negative):** Battery snap ke **Black Wire (-)** ko active buzzer ke **Short Leg (-)** se connect karein.
* 🔊 **Note:** Correct wire touch karte hi high-pitch warning alarm start ho jayega. Polarity reverse karne par buzzer sound nahi karega.

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
```mermaid
graph LR
    A["🔋 9V Battery (+)"] -->|🔴 Red Wire| B["🔘 Push Button (Pin 1)"]
    B -->|🟡 Yellow Wire| C["🔊 Active Buzzer (+)"]
    C -->|⚫ Black Wire| D["🔋 9V Battery (-)"]

    style A fill:#f43f5e,stroke:#9f1239,stroke-width:3px,color:#fff
    style B fill:#3b82f6,stroke:#1d4ed8,stroke-width:3px,color:#fff
    style C fill:#f59e0b,stroke:#b45309,stroke-width:3px,color:#fff
    style D fill:#1e293b,stroke:#0f172a,stroke-width:3px,color:#fff
```

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
```mermaid
graph LR
    A["🔋 9V Battery (+)"] -->|🔴 Red Wire| B["🔌 Toy DC Motor (Terminal A)"]
    C["🔌 Toy DC Motor (Terminal B)"] -->|⚫ Black Wire| D["🔋 9V Battery (-)"]

    style A fill:#f43f5e,stroke:#9f1239,stroke-width:3px,color:#fff
    style B fill:#64748b,stroke:#334155,stroke-width:3px,color:#fff
    style C fill:#64748b,stroke:#334155,stroke-width:3px,color:#fff
    style D fill:#1e293b,stroke:#0f172a,stroke-width:3px,color:#fff
```

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 🔴 **Step 1:** Battery snap ke **Red Wire (+)** ko DC motor ke pehle terminal (A) se connect karein.
* ⚫ **Step 2:** Battery snap ke **Black Wire (-)** ko DC motor ke dusre terminal (B) se connect karein.
* 🔄 **Polarity Reverse Test:** Wires ko switch (ultea) karein — observe karein ki motor ka rotating shaft ab opposite side ghum raha hai.

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
```mermaid
graph LR
    A["🔋 9V Battery (+)"] -->|🔴 Red Wire| B["🔌 Motor with Fan Propeller (A)"]
    C["🔌 Motor with Fan Propeller (B)"] -->|⚫ Black Wire| D["🔋 9V Battery (-)"]

    style A fill:#f43f5e,stroke:#9f1239,stroke-width:3px,color:#fff
    style B fill:#10b981,stroke:#064e3b,stroke-width:3px,color:#fff
    style C fill:#10b981,stroke:#064e3b,stroke-width:3px,color:#fff
    style D fill:#1e293b,stroke:#0f172a,stroke-width:3px,color:#fff
```

---

## 📸 Slide 4: Step-by-Step Connection Guide
* ⚙️ **Step 1:** Ek plastic propeller fan ko DC motor ke spindle shaft par gently push karke tightly mount karein.
* 🔴 **Step 2:** Snap ke **Red Wire (+)** aur **Black Wire (-)** ko motor pins par connect karein.
* 💨 **Airflow Direction Check:** Fan ko switch on karke check karein ki hawa front side aa rahi hai ya nahi. Agar hawa piche ja rahi hai, toh motor ke dono wires aapas mein swap karein.

---

## 📸 Slide 5: Student Task — Hands-On Practice
1. **Mini Desk Fan:** Motor and propeller attach karke frame stand build karein aur desk cooling fan test run karein.
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
```mermaid
graph TD
    A["💨 Wind/Air Input"] --> B["🌀 Propeller Fan Blade"]
    B --> C["🔌 Toy Motor Shaft (Generates Voltage)"]
    C -->|🔴 Red Wire| D["💡 LED glows"]
    C -->|⚫ Black Wire| D

    style A fill:#0ea5e9,stroke:#0369a1,stroke-width:3px,color:#fff
    style B fill:#f59e0b,stroke:#b45309,stroke-width:3px,color:#fff
    style C fill:#10b981,stroke:#064e3b,stroke-width:3px,color:#fff
    style D fill:#a855f7,stroke:#6b21a8,stroke-width:3px,color:#fff
```

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 🌀 **Step 1:** Motor ke shaft par propeller lagakar use generator setup mein switch karein.
* 💡 **Step 2:** Motor ke output wires ko directly **LED legs** se connect karein.
* 💨 **Step 3:** Propeller par tez hawa (fan/blow) dalein aur check karein ki generator logic se LED jalti hai ya nahi.
* 📐 **Angle adjustment:** Blades ke bent angle ko modify karke maximum brightness voltage calibration check karein.

---

## 📸 Slide 5: Student Task — Hands-On Practice
1. **Thrust angle check:** Propeller blades ke pitch angle ko manually (slightly) bend karke airflow output pressure test karein aur speed compare karein.
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
```mermaid
graph TD
    A["🔋 9V Battery (+)"] -->|🔴 Red Wire| B["⚙️ BO Gear Motor (Gearbox Inside)"]
    B -->|⚫ Black Wire| C["🔋 9V Battery (-)"]
    B -->|🔧 High Torque| D["🛞 Heavy Robot Wheels Rotate"]

    style A fill:#f43f5e,stroke:#9f1239,stroke-width:3px,color:#fff
    style B fill:#f59e0b,stroke:#b45309,stroke-width:3px,color:#fff
    style C fill:#1e293b,stroke:#0f172a,stroke-width:3px,color:#fff
    style D fill:#10b981,stroke:#064e3b,stroke-width:3px,color:#fff
```

---

## 📸 Slide 4: Step-by-Step Connection Guide
* ⚙️ **Step 1:** Gear motor ke terminals par battery snap ke **Red (+)** aur **Black (-)** wires attach karein.
* 🌀 **Step 2:** Motor ke rotating axle (spindle shaft) par directly finger se pressure banayein.
* 💡 **Observe:** Gear ratio reduction ki wajah se motor ki rotation power (torque) itni zyaada hogi ki ise haath se rokna impossible ho jayega. normal toy motor turant ruk jati hai.

---

## 📸 Slide 5: Student Task — Hands-On Practice
1. **Torque Resistance Test:** Dono motors chalakar shaft ko finger tip se rokhne ka pressure compare karein. Gear motor ko stop karna lagbhag impossible hoga!
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
```mermaid
graph LR
    A["🔋 9V Battery (+)"] -->|🔴 Red Wire| B["⚙️ BO Gear Motor Axle"]
    B -->|🔒 Solid Axle Lock| C["🛞 Toy Rubber Wheel"]
    D["🔋 9V Battery (-)"] -->|⚫ Black Wire| B

    style A fill:#f43f5e,stroke:#9f1239,stroke-width:3px,color:#fff
    style B fill:#f59e0b,stroke:#b45309,stroke-width:3px,color:#fff
    style C fill:#10b981,stroke:#064e3b,stroke-width:3px,color:#fff
    style D fill:#1e293b,stroke:#0f172a,stroke-width:3px,color:#fff
```

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
```mermaid
graph TD
    A["🔋 9V Battery Source"] -->|🔴 Parallel Red Wire| B["⚙️ Left Motor (D-shaft)"]
    A -->|🔴 Parallel Red Wire| C["⚙️ Right Motor (D-shaft)"]
    B -->|🛞 Left Wheel| D["🏃‍♂️ Linear Straight Motion"]
    C -->|🛞 Right Wheel| D

    style A fill:#f43f5e,stroke:#9f1239,stroke-width:3px,color:#fff
    style B fill:#f59e0b,stroke:#b45309,stroke-width:3px,color:#fff
    style C fill:#f59e0b,stroke:#b45309,stroke-width:3px,color:#fff
    style D fill:#10b981,stroke:#064e3b,stroke-width:3px,color:#fff
```

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 🔴 **Step 1:** Dono gear motors ko parallel connection mein wire karein taaki dono ko barabar power mile.
* 🛞 **Step 2:** Robot chassis ke dono side ke wheels ko exact center parallel direction mein scale se align karein.
* 🏃‍♂️ **Step 3:** Floor par 1-meter straight line draw karein aur robot ko us par run karke directional error adjust karein.

---

## 📸 Slide 5: Student Task — Hands-On Practice
1. **Straight Line Run:** Robot car chassis floor line par straight chala kar deviations note karein aur structure adjustment se straight route tune karein.
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
```mermaid
graph LR
    A["🏁 Start Line (0 meters)"] -->|🏃‍♂️ Robot base travels| B["🏁 Finish Line (1 meter)"]
    C["⏱️ Timer Starts"] -->|Record duration| D["⏱️ Timer Stops"]

    style A fill:#f43f5e,stroke:#9f1239,stroke-width:3px,color:#fff
    style B fill:#10b981,stroke:#064e3b,stroke-width:3px,color:#fff
    style C fill:#f59e0b,stroke:#b45309,stroke-width:3px,color:#fff
    style D fill:#64748b,stroke:#334155,stroke-width:3px,color:#fff
```

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 📐 **Step 1:** Floor par exactly 1 meter (100 cm) ki target line trace/draw karein.
* ⏱️ **Step 2:** Robot car ko start line par place karein aur switch ON karte hi stopwatch start karein.
* 🏁 **Step 3:** Robot ke target line cross karte hi timer stop karein aur use time log book/sheet me record karein.

---

## 📸 Slide 5: Student Task — Hands-On Practice
1. **Timer Run:** Robot base coordinate path runtime check stop-watch se trace karein aur time notes update sheet check karein.
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
```mermaid
graph TD
    A["🔋 3V AA Batteries"] -->|Low Voltage| B["🔌 DC Motor spins SLOW"]
    C["🔋 9V Battery Source"] -->|High Voltage| D["🔌 DC Motor spins FAST"]

    style A fill:#64748b,stroke:#334155,stroke-width:3px,color:#fff
    style B fill:#f59e0b,stroke:#b45309,stroke-width:3px,color:#fff
    style C fill:#f43f5e,stroke:#9f1239,stroke-width:3px,color:#fff
    style D fill:#10b981,stroke:#064e3b,stroke-width:3px,color:#fff
```

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
```mermaid
graph LR
    A["🔋 3V Battery"] -->|🔴 Red Wire (+)| B["📳 Coin Vibration Motor (Internal Off-center Weight)"]
    B -->|🔵 Blue Wire (-)| C["🔋 3V Battery (-)"]

    style A fill:#f43f5e,stroke:#9f1239,stroke-width:3px,color:#fff
    style B fill:#10b981,stroke:#064e3b,stroke-width:3px,color:#fff
    style C fill:#1e293b,stroke:#0f172a,stroke-width:3px,color:#fff
```

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 🔴 **Step 1:** Coin vibration motor ke Red (+) wire ko battery positive se connect karein.
* 🔵 **Step 2:** Motor ke Blue/Black (-) wire ko battery negative se connect karein.
* 📳 **Observe:** Jab internal asymmetrical load high speed par rotate hota hai, toh structural vibrations paida hoti hain jise aap fingertip par feel kar sakte hain.

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
```mermaid
graph TD
    A["📳 Vibration Coin Motor"] -->|Stick with Tape| B["📦 Lightweight Cardboard Body"]
    B -->|Vibration energy transfers| C["🪥 Flexible Legs / Toothbrush Bristles"]
    C -->|Random sliding motion| D["🕺 Robot Dances on table!"]

    style A fill:#10b981,stroke:#064e3b,stroke-width:3px,color:#fff
    style B fill:#f59e0b,stroke:#b45309,stroke-width:3px,color:#fff
    style C fill:#3b82f6,stroke:#1d4ed8,stroke-width:3px,color:#fff
    style D fill:#a855f7,stroke:#6b21a8,stroke-width:3px,color:#fff
```

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 📦 **Step 1:** Cardboard or paper use karke ek chota lightweight design model banayein.
* 📳 **Step 2:** Vibration motor ko tape se cardboard body ke exact center (Center of Mass) par mount karein.
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
```mermaid
graph TD
    A["🔋 9V Battery (+)"] -->|🔴 Common Positive Rail| B["💡 LED 1 (Red)"]
    A -->|🔴 Common Positive Rail| C["💡 LED 2 (Green)"]
    A -->|🔴 Common Positive Rail| D["💡 LED 3 (Yellow)"]
    B -->|⚫ Common Ground| E["🔋 9V Battery (-)"]
    C -->|⚫ Common Ground| E
    D -->|⚫ Common Ground| E

    style A fill:#f43f5e,stroke:#9f1239,stroke-width:3px,color:#fff
    style B fill:#ef4444,stroke:#991b1b,stroke-width:3px,color:#fff
    style C fill:#10b981,stroke:#064e3b,stroke-width:3px,color:#fff
    style D fill:#f59e0b,stroke:#b45309,stroke-width:3px,color:#fff
    style E fill:#1e293b,stroke:#0f172a,stroke-width:3px,color:#fff
```

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 🎨 **Step 1:** Cardboard template par star ya home shape draw karke LEDs ke liye small holes karein.
* 🔴 **Step 2:** Sabhi LEDs ke positive nodes (+) ko aapas mein ek standard wire (parallel) se link karein.
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
```mermaid
graph TD
    A["🔋 9V Battery (+)"] --> B["🔘 Red Switch"]
    A --> C["🔘 Yellow Switch"]
    A --> D["🔘 Green Switch"]
    B -->|ON| E["🔴 RED LED (Stop)"]
    C -->|ON| F["🟡 YELLOW LED (Ready)"]
    D -->|ON| G["🟢 GREEN LED (Go)"]
    E --> H["⚫ Battery (-) Node"]
    F --> H
    G --> H

    style A fill:#f43f5e,stroke:#9f1239,stroke-width:3px,color:#fff
    style B fill:#ef4444,stroke:#991b1b,stroke-width:3px,color:#fff
    style C fill:#f59e0b,stroke:#b45309,stroke-width:3px,color:#fff
    style D fill:#10b981,stroke:#064e3b,stroke-width:3px,color:#fff
    style E fill:#ef4444,stroke:#991b1b,stroke-width:3px,color:#fff
    style F fill:#f59e0b,stroke:#b45309,stroke-width:3px,color:#fff
    style G fill:#10b981,stroke:#064e3b,stroke-width:3px,color:#fff
    style H fill:#1e293b,stroke:#0f172a,stroke-width:3px,color:#fff
```

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 🚥 **Step 1:** Cardboard pole par sequence wise **RED**, **YELLOW**, aur **GREEN** LEDs place karein.
* 🔘 **Step 2:** Har LED ke series path mein ek dedicated slide/rocker switch wire karein.
* 🔌 **Step 3:** Sabhi switches ko battery (+) aur sabhi LEDs ke common negative nodes ko battery (-) se jodein. Switch toggle karke traffic state changes model karein.

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
```mermaid
graph TD
    A["🔋 9V Battery (+)"] --> B["🔘 Push Button / Switch"]
    B -->|🔴 Trigger Alert| C["🔴 Split Node"]
    C -->|🔴 Positive Branch| D["💡 RED Alert LED"]
    C -->|🔴 Positive Branch| E["🔊 Sound Buzzer"]
    D --> F["⚫ Common Battery (-)"]
    E --> F

    style A fill:#f43f5e,stroke:#9f1239,stroke-width:3px,color:#fff
    style B fill:#3b82f6,stroke:#1d4ed8,stroke-width:3px,color:#fff
    style C fill:#f97316,stroke:#c2410c,stroke-width:3px,color:#fff
    style D fill:#ef4444,stroke:#991b1b,stroke-width:3px,color:#fff
    style E fill:#f59e0b,stroke:#b45309,stroke-width:3px,color:#fff
    style F fill:#1e293b,stroke:#0f172a,stroke-width:3px,color:#fff
```

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 🔴 **Step 1:** Battery snap ke **Red Wire (+)** ko main control switch ke pin 1 par jodein.
* 🔌 **Step 2:** Switch ke Pin 2 se wire lekar use parallel lines mein divide karein (Red LED + active buzzer).
* ⚫ **Step 3:** LED aur buzzer ke **negative legs (-)** ko battery snap ke **Black Wire (-)** se jodein. Jaise hi button dabayein, tab siren sound aur flashing light dono chalu honge!

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
```mermaid
graph LR
    A["🔋 9V Battery (+)"] -->|🔴 Red Wire| B["🔘 ON/OFF Slide Switch"]
    B -->|🔴 Switch Output| C["🔌 Toy DC Motor (Tower Top)"]
    C -->|⚫ Black Wire| D["🔋 9V Battery (-)"]
    C -->|🌀 Axle spin| E["💨 Rotating Windmill Fan"]

    style A fill:#f43f5e,stroke:#9f1239,stroke-width:3px,color:#fff
    style B fill:#3b82f6,stroke:#1d4ed8,stroke-width:3px,color:#fff
    style C fill:#10b981,stroke:#064e3b,stroke-width:3px,color:#fff
    style D fill:#1e293b,stroke:#0f172a,stroke-width:3px,color:#fff
    style E fill:#0ea5e9,stroke:#0369a1,stroke-width:3px,color:#fff
```

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
```mermaid
graph TD
    A["🔋 9V Battery (+)"] -->|🔴 Red Wire| B["🔘 Main Slide Switch"]
    B -->|🔴 Active Loop| C["🔴 Split Node"]
    C -->|🔴 Positive wire| D["⚙️ Left BO Motor"]
    C -->|🔴 Positive wire| E["⚙️ Right BO Motor"]
    D --> F["⚫ Common Battery (-)"]
    E --> F

    style A fill:#f43f5e,stroke:#9f1239,stroke-width:3px,color:#fff
    style B fill:#3b82f6,stroke:#1d4ed8,stroke-width:3px,color:#fff
    style C fill:#f97316,stroke:#c2410c,stroke-width:3px,color:#fff
    style D fill:#f59e0b,stroke:#b45309,stroke-width:3px,color:#fff
    style E fill:#f59e0b,stroke:#b45309,stroke-width:3px,color:#fff
    style F fill:#1e293b,stroke:#0f172a,stroke-width:3px,color:#fff
```

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
```mermaid
graph TD
    A["🛡️ Heavy Cardboard Bumper"] -->|Glued tightly to| B["🚗 Mini Car Base Chassis"]
    B -->|High torque BO motors| C["🛞 High Grip Rubber Wheels"]
    C -->|Pushes forward| D["📦 Light Boxes / Obstacles pushed away"]

    style A fill:#64748b,stroke:#334155,stroke-width:3px,color:#fff
    style B fill:#f59e0b,stroke:#b45309,stroke-width:3px,color:#fff
    style C fill:#10b981,stroke:#064e3b,stroke-width:3px,color:#fff
    style D fill:#a855f7,stroke:#6b21a8,stroke-width:3px,color:#fff
```

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 🛡️ **Step 1:** Ek flat rectangular cardboard sheet ko front bumper bumper box ki tarah design karein.
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
```mermaid
graph TD
    A["🎨 Student Creative Idea"] --> B["✏️ Sketch Plan on paper"]
    B -->|Select Components| C["📦 Assemble using 3D Pen + Battery Snap"]
    C --> D["🤖 Working Creative Model!"]

    style A fill:#a855f7,stroke:#6b21a8,stroke-width:3px,color:#fff
    style B fill:#3b82f6,stroke:#1d4ed8,stroke-width:3px,color:#fff
    style C fill:#10b981,stroke:#064e3b,stroke-width:3px,color:#fff
    style D fill:#f43f5e,stroke:#9f1239,stroke-width:3px,color:#fff
```

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 📐 **Step 1:** Apne mind me ek idea sochein (jaise automatic alarm toy ya rotating windmill fan).
* 📝 **Step 2:** Ek sheet par components ko block circles me draw karke connection wires design karein.
* 🛠️ **Step 3:** Kit ke parameters combine karke manual structures ko complete push start test karein.

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
```mermaid
graph TD
    A["⚠️ Alarm doesn't ring / LED doesn't glow"] --> B["🕵️ Check 1: Is wire broken?"]
    A --> C["🕵️ Check 2: Are LED legs reversed?"]
    A --> D["🕵️ Check 3: Is battery snap loose?"]
    B -->|Fix| E["✅ Circuit Works!"]
    C -->|Fix| E
    D -->|Fix| E

    style A fill:#ef4444,stroke:#991b1b,stroke-width:3px,color:#fff
    style B fill:#f59e0b,stroke:#b45309,stroke-width:3px,color:#fff
    style C fill:#f59e0b,stroke:#b45309,stroke-width:3px,color:#fff
    style D fill:#f59e0b,stroke:#b45309,stroke-width:3px,color:#fff
    style E fill:#10b981,stroke:#064e3b,stroke-width:3px,color:#fff
```

---

## 📸 Slide 4: Step-by-Step Connection Guide
* 🔍 **Step 1:** Agar circuit ON nahi ho raha, toh sabse pehle check karein ki battery snap loose toh nahi hai.
* 🔌 **Step 2:** Check karein ki LED ki lambi leg (+) battery positive se hi judi ho.
* ⚡ **Step 3:** Kisi bhi broken wire ko aapas mein tightly twist karke tape lagayein taaki current leak na ho.

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
```mermaid
graph TD
    A["💡 Problem: Need a cooling fan"] --> B["✏️ Ideate: Pocket Fan using toy motor"]
    B --> C["🛠️ Prototype: Cardboard tube + fan blades"]
    C --> D["🚀 Test & Refine for stable airflow"]

    style A fill:#a855f7,stroke:#6b21a8,stroke-width:3px,color:#fff
    style B fill:#3b82f6,stroke:#1d4ed8,stroke-width:3px,color:#fff
    style C fill:#10b981,stroke:#064e3b,stroke-width:3px,color:#fff
    style D fill:#f43f5e,stroke:#9f1239,stroke-width:3px,color:#fff
```

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
```mermaid
graph TD
    A["🔬 Final Prototype Ready"] --> B["📊 Display Board/Poster Setup"]
    B --> C["🗣️ Present to Judges (Name, Work, Parts)"]
    C --> D["🏆 Get Congratulations & Badges!"]

    style A fill:#10b981,stroke:#064e3b,stroke-width:3px,color:#fff
    style B fill:#3b82f6,stroke:#1d4ed8,stroke-width:3px,color:#fff
    style C fill:#f59e0b,stroke:#b45309,stroke-width:3px,color:#fff
    style D fill:#a855f7,stroke:#6b21a8,stroke-width:3px,color:#fff
```

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
