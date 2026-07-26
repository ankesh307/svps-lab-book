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

## 📸 Slide 3: Circuit Diagram
```mermaid
graph LR
    A[Battery Positive RED] --> B[Resistor + LED Positive]
    C[LED Negative] --> D[Battery Negative BLACK]
```

---

## 📸 Slide 4: Connection Rules
1. Battery Snap connector ko battery pins par tight secure karein.
2. Snap ke Red wire (+) ko LED ki lambi leg (+) se connect karein.
3. Snap ke Black wire (-) ko LED ki chhoti leg (-) se connect karein (series me 220 Ohm resistor ke sath).

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

## 📸 Slide 3: Circuit Diagram
```mermaid
graph LR
    A[Battery Snap RED] --> B[Rocker Switch Terminal 1]
    B -->|Switch ON| C[Rocker Switch Terminal 2]
    C --> D[LED Positive]
    E[LED Negative] --> F[Battery Snap BLACK]
```

---

## 📸 Slide 4: Connection Guide
1. Snap Red wire ko Rocker switch ke kisi ek pin par connect karein.
2. Switch ke dusre pin se ek jumper wire lekar LED Positive (+) leg par dalein.
3. Snap Black wire ko directly LED Negative (-) leg par connect karein.

---

## 📸 Slide 5: Student Task — Hands-On Practice
![LED Toggle]({s5})

1. **ON/OFF Switch Loop:** Rocker switch ko series path me wire karein aur button toggle karke LED ON/OFF setup demonstrate karein.
2. **❓ Quiz Question:** Open circuit me current flow hota hai ya nahi?
> **Answer:** Nahi, open circuit me path break hone ki wajah se current flow nahi hota.
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

## 📸 Slide 3: Circuit Diagram
```mermaid
graph LR
    A[Battery RED] --> B[LED 1 Positive]
    B -->|Negative to Positive| C[LED 2 Positive]
    C -->|LED 2 Negative| D[Battery BLACK]
```

---

## 📸 Slide 4: Connection Rules
1. LED 1 ke negative (-) pin ko LED 2 ke positive (+) pin se direct connect karein.
2. Battery snap Red wire ko LED 1 ke positive (+) pin par lagayein.
3. Battery snap Black wire ko LED 2 ke negative (-) pin par lagayein.

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

## 📸 Slide 3: Circuit Diagram
```mermaid
graph TD
    A[Battery RED] --> B[Split Node A]
    B --> C[LED 1 Positive]
    B --> D[LED 2 Positive]
    C --> E[Split Node B]
    D --> E
    E --> F[Battery BLACK]
```

---

## 📸 Slide 4: Connection Rules
1. Dono LEDs ke positive (+) legs ko ek hi node (Red wire) me connect karein.
2. Dono LEDs ke negative (-) legs ko battery negative node (Black wire) se connect karein.

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
* **Button terminals:** Tactile switch ke 4 pins hote hain, jisme opposite pins key press karne par close hotey hain.

---

## 📸 Slide 3: Circuit Diagram
```mermaid
graph LR
    A[Battery RED] --> B[Tactile Button Pin 1]
    B -->|Press Button| C[Tactile Button Pin 2]
    C --> D[LED Positive]
    E[LED Negative] --> F[Battery BLACK]
```

---

## 📸 Slide 4: Connection Guide
1. Battery snap Red wire ko push button ke input pin par connect karein.
2. Push button ke output pin se jumper wire LED positive par lagayein.
3. Snap Black wire ko LED negative node par lock karein.

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
* **Cardboard body:** Chassis structure jo battery aur wires ko andar safely hold karega.
* **Focussed light:** Bright LED reflector jo clear beam light dega.
* **Control button:** Rocker switch loop ON/OFF karne ke liye.

---

## 📸 Slide 3: Assembly Diagram
```mermaid
graph TD
    A[Wrap components in paper sleeve] --> B[Connect Switch in series with LED]
    B --> C[Fix LED at top of tube]
    C --> D[Stick Switch on tube surface]
```

---

## 📸 Slide 4: Connection Guide
1. Battery, switch aur LED ka standard closed loop series connection complete karein.
2. Cardboard sheet ko roll karke tube shape banayein.
3. Wires ko secure tap lagakar casing tube ke andar dalein.

---

## 📸 Slide 5: Student Task — Hands-On Practice
1. **Torch Assembly:** Apna handheld model assemble karein aur andhere me focus beam test karein.
2. **❓ Quiz Question:** Torch me component parts kis direction me judtey hain?
3. **Answer:** Series circuit chain direction me.
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

## 📸 Slide 3: Circuit Diagram
```mermaid
graph LR
    A[Battery RED] --> B[Active Buzzer Positive Pin]
    C[Active Buzzer Negative Pin] --> D[Battery BLACK]
```

---

## 📸 Slide 4: Connection Guide
1. Buzzer ke positive leg (+) ko battery snap ke Red wire se jodhein.
2. Buzzer ke negative leg (-) ko snap ke Black wire se direct touch karein.

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

## 📸 Slide 3: Circuit Diagram
```mermaid
graph LR
    A[Battery RED] --> B[Push Button Pin 1]
    B -->|Press Bell| C[Push Button Pin 2]
    C --> D[Active Buzzer Positive]
    E[Active Buzzer Negative] --> F[Battery BLACK]
```

---

## 📸 Slide 4: Assembly Guide
1. Board par push button aur active buzzer mount karein.
2. Series connection path setup karke loop finalize karein.

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

## 📸 Slide 3: Wiring Loop
```mermaid
graph LR
    A[Battery Snap RED] --> B[Motor Terminal A]
    C[Battery Snap BLACK] --> D[Motor Terminal B]
```

---

## 📸 Slide 4: Student Task — Hands-On Practice
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

## 📸 Slide 3: Fan Assembly
```mermaid
graph TD
    A[Mount motor vertically in holder] --> B[Connect Snap wires to motor pins]
    B --> C[Push propeller onto motor shaft gently]
    C --> D[Turn on switch to test airflow]
```

---

## 📸 Slide 4: Student Task — Hands-On Practice
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

## 📸 Slide 3: Student Task — Hands-On Practice
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

## 📸 Slide 3: Student Task — Hands-On Practice
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

## 📸 Slide 3: Student Task — Hands-On Practice
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

## 📸 Slide 3: Student Task — Hands-On Practice
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

## 📸 Slide 3: Student Task — Hands-On Practice
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

## 📸 Slide 3: Student Task — Hands-On Practice
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

## 📸 Slide 3: Student Task — Hands-On Practice
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

## 📸 Slide 3: Student Task — Hands-On Practice
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

## 📸 Slide 3: Student Task — Hands-On Practice
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

## 📸 Slide 3: Student Task — Hands-On Practice
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

## 📸 Slide 3: Student Task — Hands-On Practice
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

## 📸 Slide 3: Student Task — Hands-On Practice
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

## 📸 Slide 3: Student Task — Hands-On Practice
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

## 📸 Slide 3: Student Task — Hands-On Practice
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

## 📸 Slide 3: Student Task — Hands-On Practice
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

## 📸 Slide 3: Student Task — Hands-On Practice
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

## 📸 Slide 3: Student Task — Hands-On Practice
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

## 📸 Slide 3: Student Task — Hands-On Practice
1. **Showcase Model:** Setup product panel display board answer questions guests demo runs.
2. **❓ Quiz Question:** Apne project ko explain karne ke liye main detail kya bolni chahiye?
> **Answer:** Project ka naam, kaam, aur use kiya gaya component parts list.
"""
    return ""
