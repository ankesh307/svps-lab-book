import os, sys, base64

base_dir = r"C:\Users\ankes\.gemini\antigravity\scratch\curriculum_app\content"

IMG = {
    "robotics": "https://images.unsplash.com/photo-1581092160607-ee22621dd758?w=800&auto=format&fit=crop&q=80",
    "ai": "https://images.unsplash.com/photo-1677442136019-21780efad99a?w=800&auto=format&fit=crop&q=80"
}

# ─────────────────────────────────────────────
#  CURRICULUM blue print definitions (6 classes x 2 tracks x 30 sessions)
# ─────────────────────────────────────────────
CLASSES = ["class2", "class3", "class4", "class5", "class6", "class7"]

# 30 detailed topics per class for Robotics & Hardware Track
ROBOTICS_TOPICS = {
    "class2": [
        (1, "Introduction to Robotics", "Robotics ke basic concepts ko samjho. Robot kya hota hai? Apna dream robot draw karo aur uska naam rakho.", "Introduction|Robotics|Dream Robot"),
        (2, "Kit Components", "Syllabus kit ke sabhi components ko identify karo aur unka basic use aur safety rules samjho.", "Kit Components|Identification|Safety"),
        (3, "Battery Basics", "Power source basics. 9V battery aur snap connector connect karke LED jalana seekho.", "Battery Basics|9V Battery|LED Light"),
        (4, "Open & Closed Circuit", "Current flow loop basics. Rocker switch se LED ON/OFF control circuit banana.", "Open Circuit|Closed Circuit|Rocker Switch"),
        (5, "Series Circuit", "Series connection basics. 2 LEDs ko series me connect karke unki brightness compare karna.", "Series Circuit|LED Brightness|Series Wiring"),
        (6, "Parallel Circuit", "Parallel connection logic. 2 LEDs parallel me connect karke series aur parallel ka difference dekhna.", "Parallel Circuit|Parallel Nodes|Comparison"),
        (7, "Push Button Circuit", "Momentary switch operation. Push button press detect hone par LED jalana seekho.", "Push Button|Momentary Switch|LED Circuit"),
        (8, "Mini Torch Project", "Torch light mechanics. LED, switch aur battery se clean handheld portable torch banana.", "Mini Torch|Switch|LED Design"),
        (9, "Buzzer Introduction", "Acoustic alarm systems. Active buzzer ko check karo aur buzzer sound alarm circuit banana.", "Active Buzzer|Sound Alarm|Acoustics"),
        (10, "Door Bell Project", "Doorbell design logic. Push button aur active buzzer se smart home door bell project build karo.", "Door Bell|Push Button|Buzzer Circuit"),
        (11, "Motor Introduction", "Rotary motion physics. Toy motor ko direct battery source se chala kar RPM speed observe karna.", "Toy Motor|RPM Speed|Rotary Motion"),
        (12, "Propeller Fan", "Aerodynamics check. Motor spindle par plastic propeller mount karke desk utility mini fan banana.", "Propeller Fan|Motor Shaft|Mini Fan"),
        (13, "Gear Motor", "Torque vs speed. High-torque BO gear motor aur simple toy motor ki shaft rotation speed compare karna.", "Gear Motor|BO Motor|Torque vs Speed"),
        (14, "Wheel Motion", "Rolling robot base. Gear motor ke andhar wheel attach karke rolling chassis base move karna.", "Wheel Motion|Robot Base|Rolling Chassis"),
        (15, "Vibration Motor", "Eccentric rotating mass. Coin vibration motor start karke mechanical vibration levels feel karna.", "Vibration Motor|Coin Motor|Vibration Feel"),
        (16, "Dancing Robot", "Eccentric mass dynamics. Vibration motor aur craft materials se vibrot-based dancing toy robot design karna.", "Dancing Robot|Vibrot|Eccentric Mass"),
        (17, "Traffic Signal", "Logic sequencing logic. Red, Yellow, aur Green LEDs use karke manual traffic signal light model banana.", "Traffic Signal|Traffic Light|Red/Yellow/Green"),
        (18, "Emergency Alarm", "Visual-acoustic alert. LED flashes aur buzzer alarm sound ko sync karke emergency indicator system banana.", "Emergency Alarm|LED Flash|Buzzer Alert"),
        (19, "Windmill Project", "Rotary structures. Propeller fan, gear motor aur structure sticks se active rotating windmill model banana.", "Windmill Model|Gear Motor|Rotating Fan"),
        (20, "Robotics Exhibition", "Presentation & communication. Sabhi students class-front par apna final working model aur layout showcase karein.", "Exhibition|Presentation|Showcase Models")
    ],
    "class3": [
        (1, "Tinkercad Navigation", "3D CAD space interface, zoom, pan aur rotate controls ko samjho.", "Tinkercad|CAD Basics|3D Space"),
        (2, "Placing 3D Shapes", "Workplane par basic cubes, cylinders aur spheres place karna seekho.", "Shapes|Workplane|Cubes"),
        (3, "Moving and Scaling", "Objects ko X, Y, Z axes par move aur resize karna seekho.", "Scale|Resize|Move"),
        (4, "Grouping Objects", "Multiple shapes ko group karke complex solids design karo.", "Group|Solid Shapes|CAD"),
        (5, "Creating Holes", "Hole shapes use karke solids ke beech hollow spaces aur grooves banao.", "Holes|Cutouts|Hollow"),
        (6, "Custom Name Plate", "Apne name plate ke base par text blocks design aur align karo.", "Text Block|Name Plate|Alignment"),
        (7, "Designing Toy Wheels", "Gear motors ke liye basic cylindrical toy wheels design karo.", "Wheels|Cylinder|Axle Hole"),
        (8, "Chassis Plate Design", "4-wheel robot chassis ki primary base plate design karo.", "Chassis Plate|Base Plate|Design"),
        (9, "Motor Mounting Slots", "Chassis plate me BO motors fit karne ke slotted holes create karo.", "Mounting Slots|Motor Fit|Slots"),
        (10, "Sensor Bracket CAD", "Ultrasonic sensor ko hold karne ke liye custom bracket layout.", "Sensor Bracket|Ultrasonic|CAD"),
        (11, "3D Pen Welding Plates", "Tinkercad me 2D connector plates print karke 3D pen welds apply karo.", "Hybrid Weld|CAD Plates|3D Pen"),
        (12, "Joint Pin Tolerance", "Moving joints design me exact gaps (0.5mm clearance) setup karo.", "Clearance|Joint Pin|Tolerance"),
        (13, "Exhaust Fan Grill CAD", "Exhaust fan blades ke safety shroud aur grill cover ko model karo.", "Fan Shroud|Safety Grill|Exhaust"),
        (14, "9V Battery Case", "9V battery ko snug fit hold karne wala bracket box design.", "Battery Case|Snug Fit|Holder"),
        (15, "Buzzer Sound Port", "Buzzer enclosure me sound waves propagate karne ke slot ports.", "Sound Port|Buzzer Cover|Acoustics"),
        (16, "Keypad Panel Cover", "4x4 matrix keypad ke boundaries ko secure rakhne ka panel cover.", "Keypad Cover|Matrix Panel|Bezel"),
        (17, "T-Joint Corner Brackets", "T-joint structures reinforcement and stability design.", "T-Joint|Brackets|Reinforcement"),
        (18, "L-Joint Angle Bars", "L-joint structure layout and connection holes mapping.", "L-Joint|Angle Bars|Chassis"),
        (19, "Sensor Shield Shell", "Protective casing layout for ultrasonic sensors.", "Sensor Shield|Enclosure|Safety"),
        (20, "Showcase Exhibition", "Students explain and exhibit their CAD design models.", "Showcase|CAD Models|Exhibition")
    ],
    "class4": [
        (1, "Breadboard Prototyping", "Learn how to plug LEDs and wires into a breadboard without soldering.", "Breadboard|Prototyping|LED Circuits"),
        (2, "Current Flow Loops", "Understand complete loops, series junctions, and resistance path loops.", "Circuits|Loops|Current Flow"),
        (3, "Meet Arduino Uno", "Understand the board layout, power options, and key pin headers.", "Arduino Uno|Board Layout|Headers"),
        (4, "Setup Arduino IDE", "Download, install, and configure the IDE for Arduino development.", "Arduino IDE|Editor Setup|Configuration"),
        (5, "Connecting USB Interface", "Configure COM ports, drivers, and establishing laptop communication.", "USB Interface|COM Ports|Driver"),
        (6, "Blink Built-in LED", "Write first blink sketch modifying delay values in loop().", "Blink Code|Delay|Built-in LED"),
        (7, "Variable Delay Speeds", "Modifying delay parameters to change blink frequencies.", "Delay Speeds|Blink frequency|Sketches"),
        (8, "External LED Circuit", "Connect an LED on a breadboard using a current-limiting resistor.", "External LED|Resistor|Breadboard"),
        (9, "Flashing Alternate LEDs", "Write code to blink two external LEDs alternately.", "Alternate Blink|Two LEDs|Logic Flow"),
        (10, "Digital Input Button", "Read digital status (HIGH/LOW) using a push button.", "Digital Input|Push Button|digitalRead()"),
        (11, "Button Toggle Light", "Toggle LED state with a button press using variables.", "Button Toggle|LED State|State Variable"),
        (12, "Serial Plotter Readings", "Plot incoming sensor values visually in real time.", "Serial Plotter|Sensor Waves|Graph"),
        (13, "Active Buzzer Control", "Control active buzzer alarms using digital pins.", "Active Buzzer|Beeps|Digital Pin"),
        (14, "Laser Diode Setup", "Configure laser transmitter focused alignment logic.", "Laser Module|focused beam|Alignment"),
        (15, "Potentiometer Dial A0", "Read analog voltage from 10K Potentiometer (0-1023).", "Potentiometer|analogRead|A0"),
        (16, "PWM Output Dimming", "Map A0 analog inputs to adjust LED brightness smoothly.", "PWM pin|Dimming|analogWrite"),
        (17, "SG90 Servo Wire Map", "Signal (PWM), power (5V), and ground connection layouts.", "Servo Wiring|SG90|PWM Pin"),
        (18, "Servo Sweep sweep()", "Sweep the servo shaft from 0 to 180 degrees using library commands.", "Servo Sweep|0-180|Angle sweep"),
        (19, "Relay Switch Wiring", "Wiring electromagnetic relay switches safely.", "Relay Coil|Switch Isolation|Wiring"),
        (20, "Showcase Panel Presentation", "Complete Uno based sensor integration model exhibit.", "Exhibition|Sensor Model|Showcase")
    ],
    "class5": [
        (1, "Arduino Uno & Breadboard Prototyping", "Connect power rails, understand digital/analog pins, and build a simple LED circuit on breadboard.", "Arduino Uno|Breadboard|LED Circuit"),
        (2, "LED & Buzzer Alarm Circuit", "Code a blinking LED and buzzer tone to create a security flashing beacon.", "LED Flasher|Buzzer Beeps|Security Beacon"),
        (3, "Button Control Logic (Digital Inputs)", "Read push button state to turn on/off the buzzer or LEDs manually.", "digitalRead()|Push Button|Input Logic"),
        (4, "Potentiometer Dimmer (Analog Input)", "Read a 10K Potentiometer analog value and control the brightness of an LED using PWM.", "Potentiometer|analogRead()|PWM Dimming"),
        (5, "LDR Light Sensor (Smart Street Light)", "Read light levels using LDR and build a smart automatic street light.", "LDR Sensor|analogRead()|Auto Street Light"),
        (6, "Soil Moisture Sensor (Smart Agriculture)", "Calibrate soil moisture threshold and turn on indicator LEDs.", "Soil Moisture|Analog Value|Plant Sensor"),
        (7, "Rain Sensor System (Smart Wiper/Roof)", "Read analog rain sensor values and detect rainfall levels.", "Rain Sensor|analogRead()|Rain Level Map"),
        (8, "IR Obstacle Sensor (Burglar Alarm)", "Use an IR sensor to detect movement and sound a burglar warning alarm.", "IR Sensor|Obstacle Detect|Burglar Alarm"),
        (9, "SG90 Servo Motor (Gate Control)", "Sweep the servo motor and use a button to open/close a garage gate.", "SG90 Servo|Sweep|Gate Control"),
        (10, "5V Relay & Submersible Water Pump", "Connect a relay module to safely switch a 5V water pump on and off.", "Relay Module|5V Water Pump|Submersible Pump"),
        (11, "Automatic Plant Watering System", "Integrate Soil Moisture sensor + Relay + Water Pump to build an automatic plant watering system.", "Automatic Irrigation|Soil Sensor|Water Pump"),
        (12, "LCD1602 Display (I2C)", "Wire the LCD1602 display screen and print 'Hello World' and sensor values.", "LCD1602|I2C Interface|Display Text"),
        (13, "Keypad 4x4 Matrix Interface", "Read keystrokes from a membrane keypad and display them on the serial monitor.", "4x4 Keypad|Matrix Scanner|Keypad Library"),
        (14, "Digital Combination Lock", "Combine Keypad + SG90 Servo + LCD1602 to build a passcode-locked door lock.", "Combination Lock|Keypad Passcode|Servo Lock"),
        (15, "IR Receiver & Remote Control", "Decode signals from an IR remote to switch different LEDs on/off.", "IR Receiver|IR Remote|Signal Decode"),
        (16, "Bluetooth Module (HC-05) Serial Setup", "Establish serial communication between Arduino and a phone via HC-05 bluetooth.", "HC-05 Bluetooth|Serial Communication|Baud Rate 9600"),
        (17, "Bluetooth Controlled Light/Appliance", "Use a phone app to control LEDs and relay via HC-05 bluetooth.", "Bluetooth App|Smart Light|Relay Control"),
        (18, "Laser Module Tripwire Alarm", "Build a security tripwire using a Laser Module pointing at an LDR sensor.", "Laser Module|LDR Tripwire|Laser Security"),
        (19, "DC Motor & Propeller Control", "Speed and direction control of a normal motor + propeller using a potentiometer.", "Normal Motor|Propeller Shaft|Potentiometer Speed"),
        (20, "Class 5 Robotics Showcase Project", "Build and present a custom integrated system combining multiple sensors and actuators.", "Showcase Project|System Design|Exhibition")
    ],
    "class6": [
        (1, "ESP8266 Pin Map & Limits", "NodeMCU V3 3.3V logic level constraints, VCC and GND pins.", "ESP8266|3.3V Logic|NodeMCU"),
        (2, "Uno vs ESP8266 WiFi", "Compare Arduino Uno features with ESP8266 built-in Wi-Fi.", "Uno vs ESP8266|WiFi Board|Features"),
        (3, "Installing ESP8266 Core", "Arduino IDE Additional Boards Manager URL insertion process.", "Board Manager|ESP8266 URL|IDE Setup"),
        (4, "WiFi Library inclusion", "Learn about ESP8266WiFi.h libraries and WiFi modes.", "WiFi Library|Header|WiFi Modes"),
        (5, "Connecting Local WiFi", "WiFi.begin(ssid, password) connection loops status check.", "WiFi.begin()|SSID/PASS|WiFi Loop"),
        (6, "Printing IP Address", "Retrieve the local IP address on serial monitor after connection.", "IP Address|Local IP|Serial Print"),
        (7, "ESP8266WebServer class", "Instantiate server class object, server.on() endpoints.", "ESP8266WebServer|server.on()|HTTP"),
        (8, "HTML response inside C++", "Send complete HTML page templates dynamically from ESP8266.", "HTML Response|C++ Strings|Webpage template"),
        (9, "Web Relay switch logic", "Clicking website button redirects to digital toggle endpoints.", "Web Switch|HTTP Toggle|Relay"),
        (10, "Python Installation", "Download, install, and setup environment variables for Python.", "Python Setup|Path Config|Installation"),
        (11, "Python Print Math input", "Learn simple python math, variables, and output commands.", "Print Math|Python Math|Command line"),
        (12, "Python Conditional statements", "Write if, elif, and else branching logic blocks.", "Conditionals|if-else|Branching"),
        (13, "Python While & For Loops", "Iterate tasks dynamically using loops in Python scripts.", "Loops|while loop|for range"),
        (14, "PySerial Library Setup", "Configure Python script serial bridge links to PC ports.", "PySerial|Serial Connect|Python port"),
        (15, "Read Serial with Python", "Continuously poll and read incoming data on PC COM ports.", "COM Read|Python Serial|COM monitor"),
        (16, "L298N H-Bridge Drive", "Configure high-current H-Bridge drivers for BO motors.", "L298N Driver|H-Bridge|Dual Motors"),
        (17, "ESP8266 Car steering", "Write C++ functions to steer the robot car in multiple directions.", "Car Steering|Drive Functions|C++ code"),
        (18, "HC-SR04 Trigger Echo", "Connect ultrasonic sensors and read raw pulse duration.", "HC-SR04|Trigger Echo|Ultrasonic"),
        (19, "Obstacle Avoider loop", "Implement safety brake thresholds to avoid collision.", "Brake Threshold|Avoid Obstacle|Collisions"),
        (20, "Showcase WiFi Robot Car", "Demonstrate local phone-guided autonomous car over Wi-Fi.", "Showcase|WiFi Car|Demonstration")
    ],
    "class7": [
        (1, "Python Lists & Dicts", "Create and index list arrays and key-value dictionaries.", "Python Lists|Dictionaries|Data Lists"),
        (2, "ThingSpeak Channel API", "Create cloud channel fields and retrieve Write API Keys.", "ThingSpeak|Channel API|Write Key"),
        (3, "ESP8266 HTTPClient", "Write post request data payloads to send values to the cloud.", "HTTPClient|GET/POST|Data payload"),
        (4, "Thingspeak Cloud Update", "Send live sensor logs to visual cloud dashboard channels.", "Cloud update|ThingSpeak|Sensor logs"),
        (5, "IFTTT Webhooks setup", "Create trigger applets for instant email/SMS web notifications.", "IFTTT Webhooks|Applet Trigger|Notifications"),
        (6, "RFID Google Sheets Log", "Log attendance data to cloud sheets directly using scripting.", "RFID Log|Google Sheets|Cloud Attendance"),
        (7, "3D Hinge design logic", "Design mechanical moving joints with standard clearance margins.", "Clearance|Hinge Joint|3D CAD"),
        (8, "Multi-color Bambu Print", "Slicing multi-color models and setting up filament changes.", "Bambu Studio|Multi-color|AMS Setup"),
        (9, "Drone Lift & Aerodynamics", "Understand Lift, Thrust, Weight, and Drag flight aerodynamics.", "Aerodynamics|Drone flight|Forces"),
        (10, "Quad Motor CW/CCW map", "Configure clockwise and counter-clockwise motor distributions.", "Motor mapping|CW/CCW rotation|Propellers"),
        (11, "Flight stabilization IMU", "Reading yaw, pitch, roll angles using internal gyroscopes.", "IMU Sensor|Gyro Pitch|Stabilization"),
        (12, "PID Tuning Algorithm", "Implement Proportional Integral Derivative loops to minimize drift.", "PID Loop|Feedback control|Tuning Algorithm"),
        (13, "ESP-NOW Peer protocol", "Establish connectionless low-latency communication between boards.", "ESP-NOW|Peer connection|Bridge"),
        (14, "ESP-NOW Joystick Remote", "Transmit analog joystick data to control motor steering.", "Joystick remote|Analog read|Transmitter"),
        (15, "Web basic authentication", "Secure server dashboards using base64 header validation.", "Web security|Basic Auth|Passwords"),
        (16, "Warehouse Delivery Bot", "Build line follower/grid tracking transport robot prototypes.", "Delivery Bot|Warehouse transport|Prototype"),
        (17, "Delta Cloud uploading", "Batch transfer local sensor databases to server databases.", "Batch upload|Data transfer|Server logs"),
        (18, "Tilt Glove control logic", "Use gyro sensors to control robotic cars with hand tilts.", "Glove control|MPU6050 gyro|Remote drive"),
        (19, "Python Tkinter GUI setup", "Create desktop control panels with custom buttons.", "Tkinter GUI|Desktop panel|Python buttons"),
        (20, "Showcase autonomous gala", "Demonstrate smart cloud-connected autonomous gimbal systems.", "Showcase Project|Cloud Gimbal|Exhibition")
    ]
}

# 30 detailed topics per class for AI & Software Track
AI_TOPICS = {
    "class2": [],
    "class3": [
        (1, "Scratch Stage Grid", "Understanding X-axis (-240 to 240) and Y-axis (-180 to 180).", "Scratch Grid|X-axis|Y-axis"),
        (2, "Move and glide blocks", "Coordinates based motion blocks, sprite speed control.", "Motion Blocks|Sprite Motion|Coordinates"),
        (3, "Sprite costumes switch", "Creating walk animation using loop alternate costumes.", "Costumes|Animation|Sprite Walk"),
        (4, "Forever block repeat", "Creating infinite background running loop process.", "Forever Loop|Repeat|Background"),
        (5, "Keyboard Arrow Event", "Using arrow keys pressed events block direction controls.", "Arrow Keys|Key Pressed|Direction"),
        (6, "Random position glide", "glide to random position block, sky boundary checks.", "glide to|Random Position|Boundary"),
        (7, "Sprite clone block", "Creating 50 star particles clones on screen.", "Cloning|Star Clones|Particles"),
        (8, "Touching Sprite logic", "IF touching apple THEN reset apple, add score.", "Touching Sensor|Collision|Score Add"),
        (9, "Score variable block", "Create variable score, initialize to 0 on start.", "Variables|Score Variable|Set Score"),
        (10, "Broadcast message event", "IF player dies broadcast game_over trigger scenes.", "Broadcast|game_over|Event Trigger"),
        (11, "Scratch Backdrop draw", "Drawing maze path borders, color fill brush tool.", "Backdrop Draw|Maze Path|Brush Tool"),
        (12, "Touching color collision", "IF touching black border return start coordinate.", "Color Collision|Black Border|Start Reset"),
        (13, "Scratch Sound extension", "Play sound file Meow at pitch tone change parameters.", "Play Sound|Meow|Pitch Change"),
        (14, "Looks Ghost transparency", "Changing ghost effect block value transparency level.", "Ghost Effect|Looks Block|Transparency"),
        (15, "Scratch Pen draw tool", "Draw shapes and paths dynamically on screen using pen.", "Pen Extension|Drawing|Canvas"),
        (16, "Ask and wait input", "Reading user input text block save to variable.", "Ask and wait|User Input|Variable Save"),
        (17, "If-else score target", "IF score == 10 THEN next level backdrop switch.", "If-else|Score Target|Backdrop Switch"),
        (18, "Random range pick block", "pick random block logic boundaries selection.", "pick random|Random Range|Boundaries"),
        (19, "Timer countdown block", "Create timer countdown variable decrease count loop.", "Timer|Countdown|Variable Dec"),
        (20, "Showcase exhibition model", "Self running Scratch AI game live showcase presentation.", "Showcase|AI Scratch Game|Exhibition")
    ],
    "class4": [
        (1, "Introduction to mBlock 5 Interface", "Tour the mBlock coding editor, stage, sprites, devices, and extensions.", "mBlock 5|Interface|Extensions"),
        (2, "Sprite Movement & Loops in mBlock", "Make sprites move, bounce, and run in loops using mBlock coding blocks.", "Sprite Motion|Loops|mBlock Coding"),
        (3, "mBlock Event Blocks (Keyboard & Mouse)", "Trigger events to control sprite directions and actions.", "Event Blocks|Keyboard Control|Mouse Events"),
        (4, "mBlock Variables & Score Keeping", "Create variables to track scores, timers, and count loops.", "Variables|Score Keeping|Timer Blocks"),
        (5, "Conditional Logic (If-Then-Else)", "Make smart sprites that react to collisions and color touching.", "If-Then-Else|Collision Sensing|Logic Blocks"),
        (6, "mBlock Broadcast Message Events", "Coordinate communication between multiple sprites.", "Broadcast Message|Sprite Sync|Event Trigger"),
        (7, "mBlock Pen Extension (Drawing Shapes)", "Write block code to draw geometric patterns dynamically.", "Pen Extension|Drawing Patterns|Turtle Art"),
        (8, "Cognitive Services (Speech to Text)", "Use mBlock's AI Cognitive Services to recognize voice commands.", "Speech to Text|Cognitive Services|AI Voice"),
        (9, "Cognitive Services (Text to Speech)", "Make your sprite read out loud in different accents and voices.", "Text to Speech|Auditory Output|Speech Generation"),
        (10, "Smart Translation extension in mBlock", "Translate speech to multiple languages using translation block logic.", "Translation Extension|Multi-Language|Smart Blocks"),
        (11, "mBlock Face Recognition AI", "Detect faces, age, and emotions using webcam cognitive blocks.", "Face Detection|Age Predict|Emotion AI"),
        (12, "Teachable Machine Extension in mBlock", "Train and upload an image classification model to control sprites.", "Teachable Machine|Image Dataset|Webcam Control"),
        (13, "mBlock Hand Gesture Controller", "Use webcam gesture recognition to control sprite coordinates.", "Hand Gestures|Webcam Tracker|Coord Control"),
        (14, "Cognitive Services (Emotion Detection)", "Change sprite costumes based on student's detected emotion (Happy/Sad).", "Emotion Detection|Sprite Costumes|Interactive AI"),
        (15, "mBlock Climate & Weather Extension", "Fetch live real-time city temperature and weather data using cloud blocks.", "Weather API|Cloud Data|Climate Blocks"),
        (16, "mBlock IoT (Internet of Things) basics", "Send messages to a local digital cloud board dashboard.", "IoT Basics|Cloud Message|Digital Dashboard"),
        (17, "Data Visualization in mBlock", "Create live line graphs and bar charts plotting cloud variables.", "Data Visuals|Line Graph|Bar Chart"),
        (18, "mBlock Game: The AI Shield Catcher", "Create a game where player catches falling space rocks using head movements!", "AI Game|Webcam Shield|Head Tracker"),
        (19, "Debugging block code errors in mBlock", "Troubleshooting loops, broken conditions, and API loading issues.", "Debug Blocks|Bugs Fix|Troubleshooting"),
        (20, "Showcase AI mBlock Project", "Present your custom mBlock AI game/model to the class.", "Showcase|AI mBlock Game|Exhibition")
    ],
    "class5": [
        (1, "Transition to Text Coding (C++ in Arduino IDE)", "Compare visual blocks vs text-based syntax, semicolon rules, and brace matching.", "C++ Text|Semicolon Rule|Syntax Intro"),
        (2, "C++ Variables and Data Types", "Learn how to declare int, float, char, and bool variables for sensor data.", "Variables|int|float|bool|char"),
        (3, "C++ Setup & Loop Functions", "Deep dive into how setup() runs once for configuration and loop() runs infinitely.", "void setup()|void loop()|Execution Flow"),
        (4, "C++ Conditional Statements (If-Else)", "Use logic operators (==, !=, <, >, &&, ||) to make decisions based on inputs.", "If-Else|Logic Operators|Comparison Math"),
        (5, "C++ Loops (For & While)", "Write loops to repeat actions, blink LEDs multiple times, or print counting variables.", "For Loop|While Loop|Repeat Logic"),
        (6, "C++ Functions & Parameter Passing", "Write custom reusable functions to handle sensor reads or alerts.", "Custom Functions|Parameters|Return Types"),
        (7, "C++ Arrays & Keypad Mapping", "Understand arrays and how they are used to map rows and columns of a 4x4 keypad matrix.", "C++ Arrays|Keypad Mapping|Memory Indexes"),
        (8, "String Manipulation & LCD Formatting", "Parse text strings and print them with custom formatting on an LCD1602 screen.", "String Class|LCD Formatting|sprintf()"),
        (9, "Serial Port Communication (Debugging)", "Use Serial.begin(), Serial.print() and Serial.read() to send/receive data to PC.", "Serial.begin()|Serial.print()|Debugging Logs"),
        (10, "Arduino Serial API with Python", "Write a Python script using PySerial to read Arduino sensor data in real-time.", "PySerial|Python COM Port|Serial Read"),
        (11, "Data Logging to Excel/CSV", "Save sensor readings (temperature, soil moisture) from Arduino directly to Excel/CSV using Python.", "Data Logger|Python csv|Excel logs"),
        (12, "Teachable Machine Image Classification", "Train a custom computer vision model on Google Teachable Machine.", "Teachable Machine|Image Dataset|Model Training"),
        (13, "Webcam Gesture Controller", "Map webcam gesture classifications in Python to control sprites or media.", "Webcam Gestures|Python OpenCV|Sprite Control"),
        (14, "PySerial Hand Gesture to Arduino", "Send webcam gesture commands from Python via Serial to control Arduino LEDs/Motors.", "PySerial COM|Webcam Control|Hardware Trigger"),
        (15, "Speech Recognition in Python (Voice Commands)", "Use Python speech-to-text to recognize voice commands.", "SpeechToText|Python Voice|Voice Parser"),
        (16, "Voice Controlled Arduino Hardware", "Send voice command strings from Python to Arduino to toggle the relay/pump.", "Voice Control|Relay Switch|Arduino Serial"),
        (17, "Wokwi/Tinkercad Arduino Simulation", "Simulate complex hardware circuits online to test code before uploading.", "Online Simulation|Tinkercad Circuits|Wokwi Debug"),
        (18, "Debugging Code Compilation Errors", "Identify common syntax errors, missing library errors, and COM port locks.", "Compiler Errors|Syntax Fix|COM Port Lock"),
        (19, "Object Detection with Python OpenCV", "Setup simple color-tracking or face-tracking in Python.", "OpenCV|Object Tracking|Color Mask"),
        (20, "Class 5 AI & Software Showcase", "Present a hybrid Python-Arduino project (e.g. voice-controlled fan or face-tracking alarm).", "Showcase Project|Python-Arduino Hybrid|Exhibition")
    ],
    "class6": [
        (1, "Python installation setup", "Download and install Python, configuring PATH variables.", "Python Setup|Path Config|Environment"),
        (2, "Python basic math print", "Perform simple calculations and print formatted text strings.", "Print Math|Python Math|Console"),
        (3, "Python Indentation syntax", "Understand code blocks indentation, loops scope guidelines.", "Indentation|Blocks|Syntax errors"),
        (4, "Python Loops iterations", "Write loops repeating actions, counters parameters tracking.", "Loops|while loop|for range"),
        (5, "PySerial COM connection", "Establishing communication links from Python scripts to COM ports.", "PySerial|Serial Connect|Port Config"),
        (6, "Bambu Studio CAD import", "STL orientation scaling parameters inside slicer.", "Bambu Studio|STL scaling|Slicer config"),
        (7, "Slicing layer config", "0.2mm parameters setting layer width calculations.", "Layer width|Slicing parameters|Config"),
        (8, "Gyroid infill structure", "Infill pattern strength density comparisons tests.", "Gyroid infill|Strength test|Density check"),
        (9, "GCode file parameters", "Gcode commands syntax check coordinate mapping.", "Gcode parameters|Syntax check|Coordinates"),
        (10, "L298N Speed map logic", "PWM outputs mapping motors speed curves.", "L298N speed|PWM outputs|Motor speed"),
        (11, "HC-SR04 sonar transit", "Sonar wave pulse duration measurements parameters check.", "HC-SR04|Pulse width|Transit time"),
        (12, "Distance alert threshold", "Map sensor distance values to coordinate alert alerts.", "Distance alert|Threshold|Logic control"),
        (13, "Obstacle check logic", "IF obstacle detected THEN stop motors, reverse steering.", "Obstacle avoid|Brake logic|Car driving"),
        (14, "SPI interface setup", "Serial Peripheral Interface MISO/MOSI wiring structures.", "SPI bus|Interface pins|MISO/MOSI"),
        (15, "RFID authentication C++", "Validate card UID against stored access registers.", "RFID validation|UID scan|C++ authorization"),
        (16, "MPU6050 I2C registers", "Reading raw linear acceleration and angular velocity registers.", "MPU6050|I2C registers|Raw values"),
        (17, "Angle mathematical mapping", "Calculating tilt degrees using basic trigonometrical math.", "Angle math|Trigonometry|Tilt calculation"),
        (18, "Tinkercad structural design", "Design robust brackets for mounting components on the car.", "Chassis mount|Bracket CAD|Structure"),
        (19, "Matplotlib live graphs", "Plot live sensor data over time inside Python canvas.", "Matplotlib|Live graph|Sensor plot"),
        (20, "Showcase exhibition model", "Demonstrate phone web-server car control with graph overlays.", "Showcase|Telemetry Car|Presentation")
    ],
    "class7": [
        (1, "Python Lists structures", "Store datasets in ordered list containers.", "Python Lists|Arrays|Data structures"),
        (2, "ThingSpeak JSON parsing", "Fetch and extract status logs from JSON API responses.", "JSON API|ThingSpeak read|JSON parsing"),
        (3, "ThingSpeak fields update", "Send numeric inputs to dedicated fields on cloud channels.", "ThingSpeak write|Fields update|Cloud API"),
        (4, "IFTTT email webhooks", "Map webhook requests to trigger immediate email dispatches.", "IFTTT Webhooks|Email trigger|Applet"),
        (5, "RFID Google Sheets log", "Log visitor name details into sheets rows via HTTP triggers.", "RFID Cloud sheet|Attendance log|App Script"),
        (6, "Moving parts clearance", "Setting exact tolerances for clean mechanical rotations.", "Clearance gap|3D print fit|Hinge CAD"),
        (7, "Bambu AMS multicolor select", "Instruct Bambu printer to alternate between colors dynamically.", "Bambu AMS|Multicolor|Filament swap"),
        (8, "Drone flight forces", "Learn the balance between Lift, Weight, Thrust, and Drag.", "Flight physics|Lift forces|Drone balance"),
        (9, "Drone torque cancellation", "Map clockwise and counter-clockwise propeller forces.", "Torque cancellation|CW/CCW map|Drone rotor"),
        (10, "IMU roll pitch angles", "Convert accelerometer raw values to angular coordinates.", "IMU coordinates|Roll/Pitch angles|Math map"),
        (11, "PID stabilization loop", "minimizing drone shaking errors using feedback gains.", "PID Feedback|Stabilization|Error minimize"),
        (12, "Camera Gimbal servos map", "Mount camera systems and balance horizon tilts using servos.", "Gimbal servo|Horizon balance|MPU6050 lock"),
        (13, "ESP-NOW remote setup", "Establishing direct peer links between control transmitters.", "ESP-NOW remote|Transceiver link|Latency"),
        (14, "Basic Auth verification", "Checking client base64 auth headers to allow server access.", "Basic Auth|Base64 login|HTTP security"),
        (15, "RFID coordinate tracking", "Scanning tags to trigger localized delivery route points.", "RFID navigation|Tracking tag|Delivery path"),
        (16, "OpenCV Video Capture", "Write Python codes to open webcams and display video frames.", "OpenCV|VideoCapture|Python frame"),
        (17, "HSV segmentation mask", "Filter pixels by color thresholds to detect target objects.", "HSV filter|Color mask|cv2.inRange()"),
        (18, "Contour tracking math", "Finding outline coordinate loops and drawing bounding shapes.", "Contours|cv2.findContours|Center coordinate"),
        (19, "Face detection Haar Cascade", "Use Haar Cascade models to recognize frontal face regions.", "Face detection|Haar Cascade|XML Classifier"),
        (20, "Showcase exhibition model", "Present cloud-connected face-tracking camera gimbals.", "Showcase Project|AI Gimbal|Exhibition")
    ]
}

def get_topic_image(title, tags):
    title_lower = title.lower()
    tags_lower = [t.lower() for t in tags]
    
    if any(k in title_lower or any(k in tg for tg in tags_lower) for k in ["esp8266", "nodemcu"]):
        return "https://images.unsplash.com/photo-1555664424-778a1e5e1b48?w=800&auto=format&fit=crop&q=80"
    if any(k in title_lower or any(k in tg for tg in tags_lower) for k in ["arduino", "uno", "breadboard"]):
        return "https://images.unsplash.com/photo-1553406830-ef2513677491?w=800&auto=format&fit=crop&q=80"
    if any(k in title_lower or any(k in tg for tg in tags_lower) for k in ["3d pen", "craft"]):
        return "https://images.unsplash.com/photo-1615663245857-ac93bb7c39e7?w=800&auto=format&fit=crop&q=80"
    if any(k in title_lower or any(k in tg for tg in tags_lower) for k in ["tinkercad", "cad", "design", "3d print", "clearance", "slicer"]):
        return "https://images.unsplash.com/photo-1581092162384-8987c1d64718?w=800&auto=format&fit=crop&q=80"
    if any(k in title_lower or any(k in tg for tg in tags_lower) for k in ["drone", "flight", "quadcopter"]):
        return "https://images.unsplash.com/photo-1508614589041-895b88991e3e?w=800&auto=format&fit=crop&q=80"
    if any(k in title_lower or any(k in tg for tg in tags_lower) for k in ["motor", "servo", "relay", "pump"]):
        return "https://images.unsplash.com/photo-1518770660439-4636190af475?w=800&auto=format&fit=crop&q=80"
    if any(k in title_lower or any(k in tg for tg in tags_lower) for k in ["led", "blink", "light", "display", "lcd"]):
        return "https://images.unsplash.com/photo-1565814636199-ae8133055c1c?w=800&auto=format&fit=crop&q=80"
    if any(k in title_lower or any(k in tg for tg in tags_lower) for k in ["sensor", "ldr", "dht11", "ultrasonic", "sonar", "rain", "soil", "mpu6050", "gyro"]):
        return "https://images.unsplash.com/photo-1517055720413-77a282b11dd9?w=800&auto=format&fit=crop&q=80"
    if any(k in title_lower or any(k in tg for tg in tags_lower) for k in ["python", "code", "programming", "serial", "matplotlib"]):
        return "https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?w=800&auto=format&fit=crop&q=80"
    if any(k in title_lower or any(k in tg for tg in tags_lower) for k in ["scratch", "block", "sprite"]):
        return "https://images.unsplash.com/photo-1516116211223-5c359a36298a?w=800&auto=format&fit=crop&q=80"
    if any(k in title_lower or any(k in tg for tg in tags_lower) for k in ["ai", "teachable", "classification", "gesture", "vision", "opencv", "face", "tracking"]):
        return "https://images.unsplash.com/photo-1620712943543-bcc4688e7485?w=800&auto=format&fit=crop&q=80"
    if any(k in title_lower or any(k in tg for tg in tags_lower) for k in ["cloud", "thingspeak", "ifttt", "wifi", "internet", "web"]):
        return "https://images.unsplash.com/photo-1451187580459-43490279c0fa?w=800&auto=format&fit=crop&q=80"
        
    return "https://images.unsplash.com/photo-1581092160607-ee22621dd758?w=800&auto=format&fit=crop&q=80"

def get_base64_image(image_filename):
    image_path = os.path.join(r"C:\Users\ankes\.gemini\antigravity\scratch\curriculum_app\images", image_filename)
    if os.path.exists(image_path):
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
            return f"data:image/png;base64,{encoded_string}"
    return ""

def generate_session_file(class_key, track, num, title, desc, tags_str):
    # Intercept custom content for Class 2 Robotics Session 1 (Intro to Robotics)
    if class_key == "class2" and track == "robotics" and num == 1:
        s1 = get_base64_image("slide_1.png")
        s2 = get_base64_image("slide_2.png")
        s3 = get_base64_image("slide_3.png")
        s4 = get_base64_image("slide_4.png")
        
        return f"""# Session 01: Introduction to Robotics 🤖

**Class 2 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Introduction to Robotics
![Introduction to Robotics]({s1})

> **Grade 2 ke chhote makers ke liye — Robot kya hota hai aur unke features ka introductory session**

---

## 📸 Slide 2: What is a Robot?
![What is a Robot?]({s2})

### 🤖 A Machine With a Job
Robot ek machine hai jo apna kaam khud se (ya humans ke instructions se) kar sakti hai!

### 🛠️ Built by Humans
Robots ko humans banate hain taaki woh humare mushkil kamo ko aasan bana sakein — jaise factories, homes aur space mein!

### 🧠 They Move & Think!
Robots move kar sakte hain, bol sakte hain, weight lift kar sakte hain, aur unke andar ke mini-computers (Brain) se soch bhi sakte hain!

---

## 📸 Slide 3: Parts of a Robot
![Parts of a Robot?]({s3})

* **🧠 Brain (CPU):** Tells the robot what to do! (Jaise hamara dimaag hume guidance deta hai)
* **👀 Sensors:** Help the robot see, hear & feel! (Jaise hamari eyes, ears, aur skin)
* **💪 Actuators:** Help the robot move & pick things up! (Jaise hamare muscles aur joints)
* **🔋 Power Source:** Gives the robot energy to work! (Jaise hamara food/khana)
* **🎮 Controller:** We use it to give the robot instructions! (Jaise a remote control)

---

## 📸 Slide 4: What Can Robots Do?
![What Can Robots Do?]({s4})

* **🏥 Help Doctors:** Robots help doctors in hospitals during surgeries!
* **🚗 Build Cars:** Robots build cars in factories without ever getting tired!
* **🌕 Explore Space:** NASA's Rover robot explores Mars — all the way from Earth!
* **🏠 Clean Our Homes:** The Roomba vacuum robot keeps our floors clean all by itself!
* **🧸 Play With Us!:** Toy robots can dance, sing, and talk — how cool is that?!

---

## Student Task — Hands-On Practice
1. **Robot Definition:** Apne simple words me batao, robot kya hota hai aur woh hamari kaise help karta hai?
2. **Draw Your Dream Robot:** Ek drawing sheet par apna manpasand (Dream) Robot draw karo! 
   - Uska ek pyara sa naam rakho.
   - Uske parts (Brain, Eye sensors, Muscle arms) ko label karo.
3. **❓ Bonus Activity:** Agar ek robot ko window saaf karne ka job diya jaye, toh use kaun-kaun se components (Brain, Sensors, Battery) chahiye honge? Class me discuss karo!
"""

    # Intercept custom content for Class 2 Robotics Session 2 (Kit Components)
    if class_key == "class2" and track == "robotics" and num == 2:
        s1 = get_base64_image("kit_overview.jpg")
        s2 = get_base64_image("battery_snap.jpg")
        s3 = get_base64_image("gear_motor_wheels.jpg")
        s4 = get_base64_image("toy_motor_propeller.jpg")
        s5 = get_base64_image("leds_buzzer.jpg")
        s6 = get_base64_image("vibration_coin_motor.jpg")
        s7 = get_base64_image("switches_buttons.jpg")
        s8 = get_base64_image("three_d_pen_filaments.jpg")
        
        return f"""# Session 02: Kit Components 📦

**Class 2 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

---

## 📸 Slide 1: Junior Maker Kit Overview
![Kit Overview]({s1})

> **Grade 2 STEM Kit Components Introduction**
>
> Is session me hum Junior Maker Kit ke sabhi components, unke naam aur basic uses ke baare mein seekhenge!

---

## 📸 Slide 2: Power — 9V Battery & Snap Connector
![9V Battery & Snap Connector]({s2})

### 🔋 9V Battery
* **Naam:** 9V Alkaline/Carbon-Zinc Battery.
* **Use:** Humare circuits aur motors ko electric power (energy) dene ke liye!
* **Safety Rule:** Dono terminals (+ aur -) ko directly wire se connect mat karein, varna battery garam hokar kharab ho sakti hai.

### 🔌 Snap Connector
* **Naam:** 9V Battery Snap Connector.
* **Use:** Battery se current ko wires ke through LED aur switches tak safely pahunchane ke liye!

---

## 📸 Slide 3: Actuators — 1 BO Gear Motor & 2 Rubber Wheels
![BO Gear Motor & Wheels]({s3})

### ⚙️ BO Gear Motor
* **Naam:** Battery-Operated (BO) Gear Motor.
* **Use:** Iske andar special gears hote hain jo motor ki speed ko kam aur power (torque) ko zyada karte hain taaki robot heavy weight push kar sake!

### 🛞 Rubber Wheels
* **Naam:** Rubber Grip Toy Wheels (2 units).
* **Use:** Gear motor ke spindle par lagakar robot chassis ko surface par smooth movements/rolling dene ke liye!

---

## 📸 Slide 4: Thrust — 1 Normal Toy DC Motor & Propeller
![Toy Motor & Propeller]({s4})

### 🌀 Normal Toy DC Motor
* **Naam:** Toy DC Motor (High RPM).
* **Use:** Ye motor bina gear ke bahut fast ghumti hai!
* **Application:** Iska use hum mini fan, thrust car aur wind generator banane me karte hain.

### 💨 Propeller (Fan Blades)
* **Naam:** Plastic Propeller.
* **Use:** Toy motor ke metal axle par fit karke high-speed air flow (hawa/thrust) generate karne ke liye!

---

## 📸 Slide 5: Outputs — Multicolor LEDs & Active Buzzer
![LEDs & Active Buzzer]({s5})

### 💡 Multicolor LEDs
* **Naam:** Light Emitting Diodes (Multicolor Pack).
* **Use:** Jab isme se current flow hota hai, ye glow karti hai (lights up)! Red, Green aur Yellow LEDs se signal aur decor model bante hain.

### 🔊 Active Buzzer
* **Naam:** 5V Active Sound Buzzer.
* **Use:** Circuits me sound indicator ya warning alarm dene ke liye (jaise doorbell ya security alarms).

---

## 📸 Slide 6: Motion — Vibration Coin Motor
![Vibration Coin Motor]({s6})

### 📳 Vibration Coin Motor
* **Naam:** Flat Coin Vibration Motor.
* **Use:** Chhoti flat coin shape motor jisme ek asymmetric load ghumta hai aur mechanical vibration levels generate karta hai (jaise mobile phone ka silent mode vibration).
* **Application:** Iska use hum vibrot bugs aur creative dancing toys banane me karte hain.

---

## 📸 Slide 7: Control — Rocker Switches & Push Buttons
![Switches & Buttons]({s7})

### 🔘 Rocker Switch
* **Naam:** SPST Rocker Switch.
* **Use:** Circuit loop ko permanently ON ya OFF rakhne ke liye switch positions.

### 🔴 Tactile Push Buttons
* **Naam:** Momentary Push Button.
* **Use:** Jab tak hum button press karte hain, tab tak circuit close rehta hai (jaise doorbell switch).

---

## 📸 Slide 8: Craft — 3D Pen & PLA Plastic Filaments
![3D Pen & Filaments]({s8})

### ✍️ 3D Printing Pen
* **Naam:** Low-temperature 3D Pen.
* **Use:** Melting plastic nozzle se hawa me 3D model, structures, aur wheels-holders draw/weld karne ke liye!

### 🧵 PLA Plastic Filaments
* **Naam:** Polylactic Acid (PLA) Filaments.
* **Use:** 3D pen ka "ink" jise melt karke plastic models banaye jate hain.

---

## Student Task — Hands-On Practice
1. **Component Match Game:** Apni table par rakhe sabhi components ko unke sahi naam ke sath align karo.
2. **First Circuit connection:** 9V battery aur snap connector lekar directly ek LED ko connect karo (make sure correct legs connection).
3. **Switch Integration:** Us loop ke beech me rocker switch lagakar LED ko manually ON/OFF karne ki practice karo!
"""

    # Intercept custom content for Class 2 Robotics Sessions 3-30
    if class_key == "class2" and track == "robotics" and num >= 3:
        try:
            import class2_robotics_custom as c2rc
            res = c2rc.get_custom_session(num)
            if res: return res
        except Exception as e:
            print(f"Error loading custom content for Session {num}: {e}")

    # Intercept custom content for Class 5 Robotics Sessions
    if class_key == "class5" and track == "robotics":
        try:
            import class5_robotics_custom as c5rc
            res = c5rc.get_custom_session(num)
            if res: return res
        except Exception as e:
            print(f"Error loading custom content for Class 5 Robotics Session {num}: {e}")

    # Intercept custom NodeMCU detailed content for Class 6 Robotics Session 1
    if class_key == "class6" and track == "robotics" and num == 1:
        return """# Session 01: ESP8266 Pin Map & Limits

**Class 6 – ROBOTICS TRACK**  
Tier Curriculum | Connect Shiksha

![ESP8266 NodeMCU](https://images.unsplash.com/photo-1555664424-778a1e5e1b48?w=800&auto=format&fit=crop&q=80)

> **Session 01** | 80 Minutes | ROBOTICS Track
>
> **Beginners ke liye — GPIO, Power, ADC, aur Communication Pins ka complete guide**

---

## Class Schedule (80 Minutes)

| Time | Activity | Focus |
|:---|:---|:---|
| **0-20 min** | Theory | NodeMCU ESP8266 specs, hardware overview, and pin map |
| **20-65 min** | Practical Lab | Component wiring & ESP8266 safety bounds |
| **65-75 min** | Debug & Fix | Boot restriction troubleshooting & limits check |
| **75-80 min** | Quick Quiz | Hands-on practice assessment & task check |

**Keywords:** `ESP8266` | `NodeMCU` | `Pinout Map` | `Boot State` | `ADC A0`

---

## Theory (20 Minutes)

### 1. ESP8266 (NodeMCU) Kya Hai?
* **All-in-One Board:** Microcontroller + built-in Wi-Fi ek hi compact board mein — sab kuch ek jagah!
* **USB se Program Karo:** Directly USB cable se upload karo — koi extra adapter ya programmer nahi chahiye.
* **IoT ka Sabse Sasta Option:** IoT projects ke liye sabse popular aur budget-friendly development board.

### 2. ESP8266 Key Specifications (Hardware Overview)

| Feature | Detail |
|:---|:---|
| **Processor** | Tensilica L106, 80 MHz |
| **Wi-Fi** | 802.11 b/g/n (2.4 GHz) |
| **GPIO Pins** | 11 usable (D0–D10) |
| **Flash Memory** | 4 MB |
| **SRAM** | 80 KB |
| **Operating Voltage** | 3.3V (USB = 5V tolerant) |

### 3. NodeMCU Pin Map – D-Pins to GPIO
> [!IMPORTANT]
> Har D-pin ka ek corresponding GPIO number hota hai. Yeh mapping yaad rakhna bahut zaroori hai!

| D-Pin | GPIO | Function / Note | Boot Restriction |
|:---|:---|:---|:---|
| **D0** | GPIO16 | Deep sleep wake pin — No Interrupt / No PWM | — |
| **D1** | GPIO5 | I²C SCL (default) | — |
| **D2** | GPIO4 | I²C SDA (default) | — |
| **D3** | GPIO0 | Flash button | **HIGH hona chahiye** |
| **D4** | GPIO2 | Onboard Blue LED (active LOW) | **HIGH hona chahiye** |
| **D5** | GPIO14 | SPI SCK | — |
| **D6** | GPIO12 | SPI MISO | — |
| **D7** | GPIO13 | SPI MOSI | — |
| **D8** | GPIO15 | SPI CS | **LOW hona chahiye** |

### 4. ⚠️ Pin Limits — Ye Galtiyan Mat Karo!
* **D0 (GPIO16) Bahut Limited Hai:** Interrupt, PWM, I2C, ya Open-drain — kuch bhi nahi chalta. Sirf basic digital read/write ke liye use karein.
* **D3, D4, D8 Boot State Critical:** Boot ke time inhe galat state mein rakha to board start hi nahi hoga! Always double-check pull-up/pull-down connections.
* **3.3V Logic Only — 5V Mat Lagao!** GPIO pins pe directly 5V lagane se board permanently kharab ho sakta hai ⚡.
* **A0 (ADC) — Max 1.0V Input:** NodeMCU chip internally 0-1.0V support karti hai. A0 pin pe directly 3.3V se zyada voltage mat lagayein, voltage divider sirf board ke andar standard inputs ke liye hai.

### 5. ADC Pin – A0 ka Sahi Use
* **Resolution:** 10-bit → `0` se `1023` tak values milti hain.
* **Input Range:** Board pe voltage divider hai jo 0–3.3V ko internally 0–1V mein convert karta hai.
* **Common Use Cases:** Potentiometer (volume knob jaisi), LDR (light sensor), Soil Moisture Sensor.

### 6. Communication Pins – UART, I2C, SPI
NodeMCU teen tarah ke communication protocols support karta hai:
* **UART (Serial):** `D9 → RX (GPIO3)`, `D10 → TX (GPIO1)`. PC se data send/receive aur debugging ke liye.
* **I2C:** `D1 → SCL (GPIO5)`, `D2 → SDA (GPIO4)`. OLED displays, BMP280 pressure sensors ke liye.
* **SPI:** `D5 → SCK`, `D6 → MISO`, `D7 → MOSI`, `D8 → CS`. Displays aur SD card readers ke liye.

---

## Practical Lab (45 Minutes)

### Step 1: Component Identification & Connections
Yahan kuch commonly used sensors aur unke connections diye gaye hain:

* **LED (with resistor):** LED positive leg → `D0 (GPIO16)`, negative leg → `GND` (220Ω resistor in series).
* **Push Button:** Button terminal 1 → `D1 (GPIO5)`, terminal 2 → `GND` (use internal pull-up resistor).
* **Buzzer:** Buzzer Positive → `D2 (GPIO4)`, Negative → `GND`.
* **Relay Module:** IN → `D3 (GPIO0)`, VCC → `3.3V`, GND → `GND`.
* **DHT11 Temp/Humidity:** Data → `D4 (GPIO2)`, VCC → `3.3V`, GND → `GND`.
* **Ultrasonic HC-SR04:** Trig → `D5 (GPIO14)`, Echo → `D6 (GPIO12)`, VCC → `3.3V/5V`, GND → `GND`.

### Step 2: Breadboard Wiring Guide — Step-by-Step
```mermaid
graph TD
    A["Step 1: Seat NodeMCU straddling the center gap of the breadboard"] --> B["Step 2: Connect NodeMCU 3.3V and GND pins to Power Rails (+ and -)"]
    B --> C["Step 3: Wire LED with 220 Ohm series resistor to GPIO D0"]
    C --> D["Step 4: Add Push Button to D1 with GND path"]
```

### Step 3: Write Code
Here is the basic code to read the LDR sensor on A0 and print it to the Serial Monitor:

```cpp
void setup() {
    Serial.begin(115200); // Start serial communication at 115200 baud
}

void loop() {
    int sensorValue = analogRead(A0); // Read the analog value on A0
    Serial.print("LDR Analog Value: ");
    Serial.println(sensorValue);      // Print value to serial monitor
    delay(500);                       // Wait for 500ms
}
```

---

## Troubleshooting Guide

| Problem | Solution |
|:---|:---|
| **NodeMCU won't boot / Blue LED constant ON** | Check D3/D4 state (must be HIGH) and D8 state (must be LOW at boot). Disconnect connections to these pins and try re-booting. |
| **Garbled / Junk text on Serial Monitor** | Change the Serial Monitor baud rate in Arduino IDE to match `115200` (baud rate defined in `Serial.begin`). |
| **A0 sensor value always 1023** | Check if the sensor input is exceeding 3.3V, or check if the VCC pin of the sensor is correctly connected to 3.3V. |

---

## Student Task — Hands-On Practice

1. **Pin Diagram Draw Karo:** NodeMCU ka pin diagram draw karo aur har D-pin ke saath uska GPIO number aur function likho.
2. **D0 vs D4 Comparison Table:** D0 aur D4 ke limitations ek table mein side-by-side compare karo — kya support hai, kya nahi.
3. **LDR + A0 Project:** A0 pin pe LDR sensor connect karo. Arduino IDE mein code likho aur Serial Monitor mein analog value print karo.
4. **❓ Bonus Question:** Batao — D3 ko boot ke time HIGH kyun rakhna padta hai? Agar LOW ho to kya hoga?

---

## Sources
* [NodeMCU ESP8266: Pinout, Specs, and Common Issues](https://connect-shiksha-guide.netlify.app/2-months-robotics-iot/)
* [ESP8266 NodeMCU V2 - Circuitrocks Documentations](https://connect-shiksha-guide.netlify.app/2-months-robotics-iot/)
* [gpio - NodeMCU Documentation](https://connect-shiksha-guide.netlify.app/2-months-robotics-iot/)
"""

    cls_title = f"Class {class_key.replace('class', '')}"
    tag_list = tags_str.split("|")
    tag_items = "\n".join([f"- `{t}`" for t in tag_list])

    # Dynamic image links based on class & track
    img_url = get_topic_image(title, tag_list)

    # C++ boilerplate code or Python boilerplate depending on class/track
    code_lang = "cpp"
    code_content = ""
    if track == "robotics":
        if class_key in ["class2", "class3"]:
            code_lang = "text"
            code_content = "// No programming needed. Focus on craft, circuits, or Tinkercad 3D CAD modeling!"
        elif class_key == "class4":
            code_content = """// Arduino Block-to-Text Code
void setup() {
    pinMode(13, OUTPUT);
}

void loop() {
    digitalWrite(13, HIGH);
    delay(1000);
    digitalWrite(13, LOW);
    delay(1000);
}"""
        elif class_key == "class5":
            code_content = """// C++ Arduino Code
#include <Servo.h>
Servo myServo;

void setup() {
    Serial.begin(9600);
    myServo.attach(9);
    pinMode(13, OUTPUT);
}

void loop() {
    myServo.write(90);
    digitalWrite(13, HIGH);
    delay(1000);
}"""
        else: # class 6 & 7
            code_content = """// NodeMCU ESP8266 Wi-Fi Robot Code
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
}"""
    else: # AI track
        if class_key == "class2":
            code_lang = "text"
            code_content = "// No screen programming needed. Focus on logic, flowcharts, and paper computational games!"
        elif class_key == "class3":
            code_lang = "scratch"
            code_content = """when green flag clicked
forever
    move (10) steps
    if on edge, bounce
end"""
        elif class_key == "class4":
            code_content = """// C++ Logic Controls
void setup() {
    pinMode(2, INPUT_PULLUP);
    pinMode(13, OUTPUT);
}

void loop() {
    if(digitalRead(2) == LOW) {
        digitalWrite(13, HIGH);
    } else {
        digitalWrite(13, LOW);
    }
}"""
        elif class_key == "class5":
            code_content = """// C++ Corgi API Parsing Logic
#include <Arduino.h>
void setup() {
    Serial.begin(9600);
}
void loop() {
    if(Serial.available() > 0) {
        String gesture = Serial.readStringUntil('\\n');
        if(gesture == "hand_up") {
            // Turn on LED
        }
    }
}"""
        else: # class 6 & 7 Python
            code_lang = "python"
            code_content = """# Python OpenCV AI Tracking Script
import cv2
import serial

ser = serial.Serial('COM3', 9600)
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    # Apply color masking or face detection
    # Send control values to Serial COM
    ser.write(b'MOVE_LEFT\\n')
    cv2.imshow('AI Frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break"""

    return f"""# Session {num:02d}: {title}

**{cls_title} – {track.upper()} TRACK**  
Tier Curriculum | Connect Shiksha

![{title}]({img_url})

> **Session {num:02d}** | 80 Minutes | {track.upper()} Track

---

## Class Schedule (80 Minutes)

| Time | Activity | Focus |
|:---|:---|:---|
| **0-20 min** | Theory | {desc[:60]}... |
| **20-65 min** | Practical Lab | Hands-on building and testing |
| **65-75 min** | Debug & Fix | Troubleshoot and improve |
| **75-80 min** | Quick Quiz | 3-question knowledge check |

**Keywords:** {' | '.join(['`' + t + '`' for t in tag_list])}

---

## Theory (20 Minutes)

### Core Concept
{desc}

### Component Specifications
* **Key Device:** {title}
* **Usage Parameter:** {' / '.join(tag_list)}

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

```{code_lang}
{code_content}
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

**Q2.** What is the purpose of `{tag_list[0]}`?
> Answer: It acts as the key parameter for control and calibration in today's setup.

**Q3.** Name a real-world application of this session's project.
> Answer: Smart automation, aerospace tracking, or local control grids.
"""

# Generate the files
total_generated = 0
for class_key in CLASSES:
    # 1. Robotics
    robotics_dir = os.path.join(base_dir, class_key, "robotics")
    os.makedirs(robotics_dir, exist_ok=True)
    for (num, title, desc, tags) in ROBOTICS_TOPICS[class_key]:
        content = generate_session_file(class_key, "robotics", num, title, desc, tags)
        filename = f"session{num:02d}.md"
        with open(os.path.join(robotics_dir, filename), "w", encoding="utf-8") as f:
            f.write(content)
        total_generated += 1

    # 2. AI
    ai_dir = os.path.join(base_dir, class_key, "ai")
    os.makedirs(ai_dir, exist_ok=True)
    for (num, title, desc, tags) in AI_TOPICS[class_key]:
        content = generate_session_file(class_key, "ai", num, title, desc, tags)
        filename = f"session{num:02d}.md"
        with open(os.path.join(ai_dir, filename), "w", encoding="utf-8") as f:
            f.write(content)
        total_generated += 1

print(f"Successfully generated {total_generated} session files across 6 classes!")
