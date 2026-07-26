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
        (13, "Wind Power Challenge", "Air thrust alignment. Kis propeller angle aur shape par sabse zyada hawa/thrust milti hai test karna.", "Wind Power|Propeller Angle|Thrust Test"),
        (14, "Gear Motor", "Torque vs speed. High-torque BO gear motor aur simple toy motor ki shaft rotation speed compare karna.", "Gear Motor|BO Motor|Torque vs Speed"),
        (15, "Wheel Motion", "Rolling robot base. Gear motor ke andhar wheel attach karke rolling chassis base move karna.", "Wheel Motion|Robot Base|Rolling Chassis"),
        (16, "Straight Line Challenge", "Axle stability. Robot chassis base ko floor par exact straight line me chalane ki practice aur feedback debug.", "Straight Line|Axle Stability|Robot Alignment"),
        (17, "Distance Challenge", "Linear distance metrics. Robot base ko exact 1 meter tak chalana aur dynamic travel time note karna.", "Distance Challenge|1 Meter Run|Timer Readings"),
        (18, "Speed Challenge", "Battery voltage effects. Alag-alag voltage battery levels me motor speed aur torque characteristics compare karna.", "Speed Challenge|Battery Voltage|Torque Characteristics"),
        (19, "Vibration Motor", "Eccentric rotating mass. Coin vibration motor start karke mechanical vibration levels feel karna.", "Vibration Motor|Coin Motor|Vibration Feel"),
        (20, "Dancing Robot", "Eccentric mass dynamics. Vibration motor aur craft materials se vibrot-based dancing toy robot design karna.", "Dancing Robot|Vibrot|Eccentric Mass"),
        (21, "LED Decoration", "Creative lightning patterns. Multiple multicolor LEDs ko align karke decorative lighting grids draw karna.", "LED Decoration|Multicolor LEDs|Creative Lights"),
        (22, "Traffic Signal", "Logic sequencing logic. Red, Yellow, aur Green LEDs use karke manual traffic signal light model banana.", "Traffic Signal|Traffic Light|Red/Yellow/Green"),
        (23, "Emergency Alarm", "Visual-acoustic alert. LED flashes aur buzzer alarm sound ko sync karke emergency indicator system banana.", "Emergency Alarm|LED Flash|Buzzer Alert"),
        (24, "Windmill Project", "Rotary structures. Propeller fan, gear motor aur structure sticks se active rotating windmill model banana.", "Windmill Model|Gear Motor|Rotating Fan"),
        (25, "Mini Car Model", "BO gear motor, wheels, switch, aur battery module mount karke mechanical moving car build karna.", "Mini Car|Moving Car|BO Motor"),
        (26, "Obstacle Push Car", "Push capacity test. Apni created car par bumper design karke light objects (cardboard scrap) ko push karna.", "Obstacle Push|Bumper Design|Push Capacity"),
        (27, "Creative Robot", "System integration. Syllabus kit ke sabhi elements use karke custom prototype robot board design karna.", "Creative Robot|Prototype|System Integration"),
        (28, "Debugging Day", "Fault isolation logic. Broken wire connections, bad joints, aur low voltage faults ko dhoondh kar fix karna.", "Debugging|Fault Isolation|Troubleshoot"),
        (29, "Innovation Challenge", "Self-guided building. Dadas, mentors ke direction me apni choice ka unique utility electronic project banana.", "Innovation|Self-Guided|Unique Project"),
        (30, "Robotics Exhibition", "Presentation & communication. Sabhi students class-front par apna final working model aur layout showcase karein.", "Exhibition|Presentation|Showcase Models")
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
        (17, "T-Joint Corner Brackets", "Structural frames ko 90 degrees rigid alignment dene wale corners.", "Corner Bracket|T-Joint|Frame"),
        (18, "L-Joint Angle Bars", "Chassis plates aur side panels connect karne wale angle bars.", "Angle Bars|L-Joint|Connection"),
        (19, "Sensor Shield Shell", "Sensitive sensors ko external dust se protect karne ka shell casing.", "Shield Shell|Sensor Cover|Protection"),
        (20, "Wheel Tread Pattern", "Rubber wheels par grip badhane ke liye custom grid treads pattern.", "Treads|Grip Pattern|Tires"),
        (21, "Worm Gear Profile", "BO gear motor output ko torque transfer karne ke teeth curves.", "Gear Teeth|Torque Transfer|Worm Gear"),
        (22, "Pen Holder Arm", "Robot car ke center slot me writing pen clamp karne wala arm.", "Pen Holder|Robot Arm|Clamp"),
        (23, "Rocker Switch Panel Plate", "Multiple rocker switches hold karne wali main front dashboard plate.", "Dashboard Plate|Switch Slots|Panel"),
        (24, "Micro Servo Mount Bracket", "Servo body ko horizontal axis surface par hold karne ka bracket.", "Servo Mount|SG90|Holder"),
        (25, "Hollow Spherical Cap", "Security camera cover ya camera dome cover design logic.", "Camera Dome|Spherical Cap|Hollow"),
        (26, "Fillet and Chamfer Edges", "Edges ko smooth aur impact resistant banane ke fillets parameters.", "Fillets|Chamfers|Smooth Edges"),
        (27, "Importing SVG Designs", "2D vectors ko Tinkercad me extrude karke 3D plates create karo.", "SVG Import|Extrude|2D to 3D"),
        (28, "Exporting STL for 3D Printing", "Designs ko sliced GCODE ke liye STL formatting me export karo.", "STL Export|3D Print file|CAD"),
        (29, "CAD Design Presentation", "Apne Tinkercad virtual models ko rotate aur explode view me demonstrate karo.", "CAD Present|Exploded View|Rotation"),
        (30, "Showcase Exhibition", "Sare digital 3D models ko display screen panel layout me align karo.", "Showcase|Exhibition|3D Screen")
    ],
    "class4": [
        (1, "Breadboard Prototyping", "Breadboard rows, columns aur internal metal strip layout check karo.", "Breadboard|Rows|Metal Strips"),
        (2, "Current Flow Loops", "Resistors ke sath simple current loops create karke breadboard test karo.", "Current Loop|Resistor|Wiring"),
        (3, "Meet Arduino Uno", "Microcontroller pins layout, power terminals aur reset button samjho.", "Arduino Uno|Pins|Reset"),
        (4, "Setup Arduino IDE", "IDE download, port detection aur Uno board configuration test.", "Arduino IDE|COM Port|Uno Setup"),
        (5, "Connecting USB Interface", "B type cable se code upload process aur bootloader signals check.", "USB Upload|Bootloader|B type"),
        (6, "Blink Built-in LED", "Block code editor se Pin 13 LED_BUILTIN ko blink karwao.", "LED_BUILTIN|Blink|Pin 13"),
        (7, "Variable Delay Speeds", "Delay block values modify karke state frequency change karo.", "Delay Block|Frequency|Timing"),
        (8, "External LED Circuit", "Uno Digital outputs se 220 ohm resistor lagakar external LED run karo.", "Digital Output|External LED|220 Ohm"),
        (9, "Flashing Alternate LEDs", "2 LEDs ko opposite cycle timings par alternate code karo.", "Alternate LED|Flashing|Opposite Cycle"),
        (10, "Digital Input Button", "Push button ko digital pin INPUT pullup state me read karo.", "digitalRead|Push Button|INPUT_PULLUP"),
        (11, "Button Toggle Light", "Button press detect karne par LED status toggle function code.", "Toggle Light|Button Press|Logic"),
        (12, "Serial Plotter Readings", "LDR analog readings ko plotter tool par graphical waves me trace karo.", "Serial Plotter|LDR sensor|Graph"),
        (13, "Active Buzzer Control", "Digital output pulse se buzzer beeps sound generate karo.", "Active Buzzer|Beeps|Digital Pin"),
        (14, "Laser Diode Setup", "Laser module current limits aur focused alignment logic setup.", "Laser Module|focused beam|Alignment"),
        (15, "Potentiometer Dial A0", "Potentiometer rotary wiper se 0-1023 analog range read A0.", "Potentiometer|analogRead|A0"),
        (16, "PWM Output Dimming", "Pin A0 values coordinate karke PWM pin LED brightness smoothly map.", "PWM pin|Dimming|analogWrite"),
        (17, "Buzzer Frequency Vary", "Potentiometer values se tone frequency changes observe karo.", "Vary pitch|Buzzer pitch|Tone"),
        (18, "SG90 Servo Wire Map", "Signal (PWM), power (5V) aur ground connections correct check.", "Servo Wiring|SG90|PWM Pin"),
        (19, "Servo Sweep sweep()", "Servo motor shaft ko 0 to 180 degrees code sweep parameter command.", "Servo Sweep|0-180|Angle sweep"),
        (20, "Relay Switch Wiring", "Relay electromagnetic switch isolation coil terminals check.", "Relay Coil|Switch Isolation|Wiring"),
        (21, "Water Pump Relay Control", "Relay ON condition se 5V submersible water pump toggle process.", "Water Pump|Relay Control|5V Pump"),
        (22, "Rain Sensor Analog", "Rain pad corrosion check aur water moisture drop values print.", "Rain Sensor|Moisture Drop|Analog"),
        (23, "Soil Moisture Wet Dry", "Dry soil vs wet soil capacitive resistance values map process.", "Soil Sensor|Capacitive|Resistance"),
        (24, "LCD 1602 I2C Pins", "SDA, SCL, VCC aur GND pins setup with I2C address map.", "I2C LCD|SDA/SCL|Address Map"),
        (25, "Print Custom Text LCD", "setCursor lines command se coordinate system print text.", "LCD Print|setCursor()|Coordinates"),
        (26, "4x4 Matrix Keypad Map", "Row/Column matrix scanner logic aur key character parsing.", "Keypad Matrix|Rows/Cols|Keypress"),
        (27, "Keypad Input to LCD", "Key press values ko dynamic text array ke sath LCD print update.", "Input Map|LCD Update|Keypad"),
        (28, "Buzzer Key Beep", "Every correct keypad input detect par active buzzer beep feedback.", "Key Beep|Acoustic Feedback|Buzzer"),
        (29, "Fault Finding Multimeter", "VCC rails discontinuity aur bad ground connections debug process.", "Discontinuity|Bad Ground|Debug"),
        (30, "Showcase Panel Presentation", "Complete Uno based sensor integration model exhibit karo.", "Exhibition|Sensor Model|Showcase")
    ],
    "class5": [
        (1, "Transition to C++ Text", "Stop using blocks! C++ compiler keywords, braces and comments format.", "C++ Text|Braces|Keywords"),
        (2, "C++ Void Setup & Loop", "void setup() aur void loop() execution blocks and priority flow.", "void setup()|void loop()|Flow"),
        (3, "Syntax Semicolon Debug", "Missing semicolons, typos and variable scope debug techniques.", "Semicolon|Typos|Syntax Error"),
        (4, "Data Type int float bool", "Integer, Float, Boolean variables memory size and limits.", "int|float|bool|Data Types"),
        (5, "String Class Text Data", "Character arrays vs String object functions map process.", "String Class|char array|Text Data"),
        (6, "Local vs Global Scope", "Variables inside function vs global scope memory allocation.", "Global Scope|Local Variable|Memory"),
        (7, "C++ If-Else Conditions", "Comparison operators (==, !=, >, <) logic block executions.", "If-Else|Comparison|Logic Block"),
        (8, "digitalRead C++ Syntax", "digitalRead() returns HIGH or LOW with pullup constraints.", "digitalRead()|INPUT_PULLUP|HIGH/LOW"),
        (9, "analogRead C++ Syntax", "analogRead() function calibration, variables calculation.", "analogRead()|Calibration|Resolution"),
        (10, "C++ For Loop Iterations", "For loop iteration count increments and speed optimization.", "For Loop|Iterations|Speed"),
        (11, "While loop condition", "While condition true execution loops and break commands.", "While Loop|break|Condition true"),
        (12, "Switch Case C++ State", "Switch case structure mapped to multiple choice operations.", "Switch Case|Multiple Choice|States"),
        (13, "Serial Monitor begin()", "Serial.begin(9600) baud rate settings and print logs.", "Serial.begin()|9600 Baud|print()"),
        (14, "C++ Custom Functions", "Functions parameters passing, return types (void, int).", "Custom Functions|Return types|Parameters"),
        (15, "Array storage lists", "Index based array storage lists and matrix arrays.", "Array storage|Index|Matrix"),
        (16, "Header file inclusion", "#include library format and library paths directory.", "#include|Library Paths|Header"),
        (17, "LiquidCrystal_I2C class", "LCD class initialize, print text, cursor update coordinates.", "LiquidCrystal_I2C|lcd.print()|setCursor"),
        (18, "Servo write() function", "Servo class instances attach pin, write angle coordinate.", "Servo.h|attach()|write()"),
        (19, "PWM Analog Output Map", "map() function conversion logic: 0-1023 analog to 0-255 PWM.", "map()|analogWrite()|PWM Dimming"),
        (20, "IR Receiver Decoders", "Decode HEX code patterns from IR remote control devices.", "IRremote.h|HEX Codes|Decoders"),
        (21, "HC-05 Bluetooth C++ RX", "SoftwareSerial communication setup for bluetooth app control.", "HC-05|SoftwareSerial|Bluetooth RX"),
        (22, "Relay Trigger Active LOW", "C++ code active low trigger logic for high voltage safety relays.", "Relay LOW|C++ Trigger|Safety Coil"),
        (23, "Webcam Training AI Model", "Google Teachable Machine classes dataset loading process.", "Teachable Machine|AI Dataset|Webcam"),
        (24, "Image Classifier logic", "Webcam classification threshold logic in computer apps.", "Webcam Classify|Threshold|AI Model"),
        (25, "Hand Gesture Control", "Webcam gesture classes mapped to serial commands output.", "Hand Gestures|Webcam Class|Serial output"),
        (26, "Voice Model Speech API", "Microphone audio signal matching classification states.", "Voice Classify|Speech API|Microphone"),
        (27, "Teachable Machine Output", "API output mapped to local web socket server inputs.", "Teachable API|Web Socket|Local Output"),
        (28, "Serial Port COM Mapping", "Connecting web app commands to specific COM port of Uno.", "COM Port|Web Serial|Uno Match"),
        (29, "Troubleshooting Serial", "COM port locked error, baud rate mismatch fixes.", "COM Locked|Baud Mismatch|Debug"),
        (30, "Showcase presentation", "AI classification + hardware control model live showcase.", "Exhibition|AI Control|Showcase")
    ],
    "class6": [
        (1, "ESP8266 Pin Map Limits", "NodeMCU V3 3.3V logic level constraints, VCC and GND pins.", "ESP8266|3.3V Logic|NodeMCU"),
        (2, "Uno vs ESP8266 WiFi", "Why ESP8266 has built-in WiFi chip and larger flash memory.", "Uno vs ESP8266|Flash memory|WiFi"),
        (3, "Installing ESP8266 Core", "Arduino IDE Additional Boards Manager URL insertion process.", "Board Manager|ESP8266 URL|IDE Setup"),
        (4, "WiFi Library inclusion", "ESP8266WiFi.h library functions and connection modes.", "ESP8266WiFi.h|WiFi Modes|Header"),
        (5, "Connecting Local WiFi", "WiFi.begin(ssid, password) connection loops status check.", "WiFi.begin()|SSID/PASS|WiFi Loop"),
        (6, "Printing IP Address", "WiFi.localIP() output print to Serial Monitor screen.", "localIP()|IP Address|Serial Print"),
        (7, "ESP8266WebServer class", "Instantiate server class object, server.on() endpoints.", "ESP8266WebServer|server.on()|HTTP"),
        (8, "HTML response inside C++", "Serving basic HTML text files as HTTP responses.", "HTML inside C++|HTTP GET|Response"),
        (9, "Web Relay switch logic", "Clicking website button redirects to digital toggle endpoints.", "Web Switch|HTTP Toggle|Relay"),
        (10, "Python Installation", "Python compiler setup path settings, VS Code integration.", "Python Install|VS Code|REPL"),
        (11, "Python Print Math input", "Variables, basic math operations, string manipulation in Python.", "Python Print|Variables|Math"),
        (12, "Python Conditional statements", "if, elif, else indentation logic vs C++ braces.", "Python Indentation|if-elif-else|Logic"),
        (13, "Python While & For Loops", "Infinite loop (while True) and iteration ranges loops.", "while True|for range()|Python Loops"),
        (14, "PySerial Library Setup", "pip install pyserial installation command terminal.", "PySerial|pip install|COM interface"),
        (15, "Read Serial with Python", "Python reading serial input data stream dynamically.", "serial.readline()|Python Serial|Stream"),
        (16, "Bambu Slicer Interface", "Import STL, CAD viewer, camera coordinates controls.", "Bambu Studio|STL Import|CAD Viewer"),
        (17, "Slicing Thickness Density", "Layer height 0.2mm, infill density settings process.", "Layer Height|Infill Density|Slicer"),
        (18, "Gyroid Infill Pattern", "Why gyroid pattern provides high structural strength.", "Gyroid|Structural Strength|Infill"),
        (19, "Generating GCode files", "Exporting sliced models Gcode to SD card for printer.", "GCode Export|SD Card|3D Printing"),
        (20, "L298N H-Bridge Drive", "IN1-4 direction control pins, ENA/B speed pins.", "L298N|IN1-IN4|ENA/ENB"),
        (21, "BO Gear Motor Power Map", "Why L298N needs separate battery power line from board.", "Power Line|Battery Split|L298N"),
        (22, "ESP8266 Car steering", "Differential drive steering logic for left/right turns.", "Differential Drive|Steering|Dual Motor"),
        (23, "HC-SR04 Trigger Echo", "Sound waves transit time duration calculations.", "HC-SR04|TRIG/ECHO|Sound speed"),
        (24, "Ultrasonic Distance math", "Distance = (duration / 2) * 0.0343 speed of sound math.", "Distance math|speed of sound|pulseIn"),
        (25, "Obstacle Avoider loop", "Braking, turning left, checking clear paths logic.", "Obstacle Avoid|Auto Brake|Turn"),
        (26, "SPI Bus RC522 RFID", "MOSI, MISO, SCK and SS pins mapping on ESP8266.", "SPI Bus|RC522 RFID|MOSI/MISO"),
        (27, "Reading RFID card UID", "MFRC522 library read card type, parse Hex UID strings.", "MFRC522|Hex UID|RFID card"),
        (28, "Smart Gate Lock Control", "Matching card UID unlocks Servo gate lock mechanism.", "RFID Gate|Servo Lock|Access Control"),
        (29, "MPU6050 Accelerometer", "I2C SDA/SCL raw acceleration data reading cycles.", "MPU6050|I2C raw data|Accelerometer"),
        (30, "Showcase WiFi Robot Car", "Driving robot car dynamically through phone browser web app.", "Showcase|Web Browser Car|Exhibition")
    ],
    "class7": [
        (1, "Python Lists & Dicts", "Lists manipulation, Dictionary key-value pairs storage.", "Lists|Dicts|Python Data"),
        (2, "ThingSpeak Channel API", "Create channel fields, retrieve Write API key.", "ThingSpeak|Channel API|Write Key"),
        (3, "ESP8266 HTTPClient", "HTTPClient post data payload formatted string URL.", "HTTPClient|GET/POST|Data payload"),
        (4, "Thingspeak Cloud Update", "Sending temperature sensor values every 15 seconds.", "Cloud update|ThingSpeak|Sensor logs"),
        (5, "IFTTT Webhooks setup", "Create event triggers mapped to email notification.", "IFTTT|Webhooks|Email alert"),
        (6, "RFID Google Sheets Log", "RFID swipe sends post request to IFTTT sheets applet.", "RFID Sheets|Google Log|IFTTT Applet"),
        (7, "3D Hinge design logic", "0.5mm clearance gap modeling for moving 3D parts.", "3D Hinge|Clearance|Moving Parts"),
        (8, "Multi-color Bambu Print", "AMS filament loading color settings inside slicer.", "AMS Color|Bambu slicer|Filament change"),
        (9, "Drone Lift & Aerodynamics", "Lift, weight, thrust and drag forces physics.", "Drone Lift|Forces of flight|Physics"),
        (10, "Quad Motor CW/CCW map", "Yaw rotation cancellation torque balancing layout.", "CW/CCW layout|Torque balance|Quadcopter"),
        (11, "Flight stabilization IMU", "MPU6050 feedback filters loops for drone stability.", "Stabilization|MPU6050 feedback|IMU"),
        (12, "PID Tuning Algorithm", "Proportional, Integral and Derivative correction math.", "PID Tuning|Error Correction|Derivative"),
        (13, "Gyro Stabilized Gimbal", "Tilt angle compensation mapping to 2-axis servos.", "Camera Gimbal|2-Axis|Stabilized"),
        (14, "ESP-NOW Peer protocol", "Direct MAC address packet transmission no router.", "ESP-NOW|MAC Address|Peer-to-Peer"),
        (15, "ESP-NOW Joystick Remote", "Joystick analog X/Y data sent to robot receiver.", "Joystick Remote|Transmitter|ESP-NOW"),
        (16, "Web basic authentication", "Adding username password auth header validation.", "Basic Auth|Security Header|Web Server"),
        (17, "Warehouse Delivery Bot", "RFID cards coordinate parsing on floor navigate paths.", "RFID Navigate|Delivery Bot|Warehouse"),
        (18, "Delta Cloud uploading", "Only upload values to cloud if value changes > threshold.", "Delta upload|Bandwidth save|Threshold"),
        (19, "Tilt Glove control logic", "MPU6050 glove sensor readings mapped to car movements.", "Tilt Glove|MPU6050 remote|ESP-NOW"),
        (20, "Python Tkinter GUI setup", "Window layouts, labels, buttons to write serial data.", "Tkinter GUI|Python Buttons|Serial write"),
        (21, "ArduinoOTA Update loop", "Wireless code flashing setup using OTA software port.", "OTA Update|ArduinoOTA|Wireless upload"),
        (22, "ESP8266 Deep Sleep mode", "ESP.deepSleep() wake timer configuration via D0 pin.", "ESP.deepSleep()|Wake Timer|D0 Jumper"),
        (23, "ESP-NOW Mesh routing", "4 nodes passing payload data from station to gateway.", "Mesh network|Mesh routing|ESP-NOW"),
        (24, "Multimeter Fault Finding", "Finding high resistance joints and broken voltage rails.", "Multimeter|Resistance|Voltage drop"),
        (25, "Tinkercad Honeycomb case", "Honeycomb structure print for light weight drone guard.", "Honeycomb|Tinkercad drone|Propeller guard"),
        (26, "OpenCV Image Capture", "pip install opencv-python frame read setup script.", "OpenCV|cv2.VideoCapture|Python Frame"),
        (27, "HSV Color segmentation", "Converting frame to HSV mask values to track color.", "HSV mask|cv2.inRange|Color segment"),
        (28, "Object Contour Tracking", "cv2.findContours, drawing bounding circle coordinates.", "Contours|cv2.findContours|Bounding box"),
        (29, "Haar Cascade Face detect", "Face detection Haar Cascade XML classifier matching loop.", "Haar Cascade|Face detection|XML Classifier"),
        (30, "Showcase autonomous gala", "Presenting Cloud connected AI face tracking camera gimbal.", "Autonomous Gala|Gimbal display|Showcase")
    ]
}

# 30 detailed topics per class for AI & Software Track
AI_TOPICS = {
    "class2": [
        (1, "Algorithmic thinking", "Task steps ko sequence list form me define karna.", "Algorithm|Sequence|Task Steps"),
        (2, "Binary logic values", "True (1) vs False (0) basic logic states.", "Binary|True/False|Logic States"),
        (3, "AND gate condition", "Dono conditions satisfy hone par hi output trigger.", "AND gate|Conditions|Output"),
        (4, "OR gate condition", "Kisi bhi ek condition check true output trigger.", "OR gate|Condition check|Trigger"),
        (5, "NOT logic invert", "Input signals state ko reverse/invert karna.", "NOT gate|Invert|Logic State"),
        (6, "Algorithmic flowcharts", "Shapes standard representation (Start, Process, End).", "Flowcharts|Start/Process/End|Shapes"),
        (7, "Pattern Recognition", "Repeating sequences patterns identify karna shapes me.", "Pattern Recognition|Sequences|Shapes"),
        (8, "Classification datasets", "Objects features mapping classification rules.", "Classification|Features|Datasets"),
        (9, "Data input sorting", "Items ascending descending values sorting rules.", "Sorting|Data Input|Rules"),
        (10, "Conditional loops", "If condition holds repeat process logic loops.", "Conditional loops|Repeat|Logic"),
        (11, "Sensor value logic", "Value > Threshold check digital condition mapping.", "Sensor logic|Threshold|Condition"),
        (12, "Logic decision trees", "Root node, branches, decision endpoints mapping.", "Decision Tree|Branches|Endpoints"),
        (13, "Algorithmic loops count", "Fixed iteration loops vs condition loop structures.", "Loops count|Iterations|Structure"),
        (14, "Input data arrays", "Storing multiple names in ordered list array.", "Arrays|Lists|Data Storage"),
        (15, "Logic gates mapping", "AND, OR, NOT operations combined logic outputs.", "Combined Logic|Logic Gates|Truth Table"),
        (16, "Teachable machine dataset", "Webcam dataset loading categories labels.", "Teachable Machine|Dataset|Webcam Labels"),
        (17, "Image classification model", "Training classification classes webcam threshold.", "Classification|Webcam Class|Threshold"),
        (18, "Hand Gesture mappings", "Left, Right hand states mapping serial commands.", "Hand Gestures|Serial Maps|Classification"),
        (19, "Voice activation setup", "Speech API audio waveform matching states.", "Voice Match|Speech API|Waveform"),
        (20, "Object recognition box", "Object bounding coordinates box detection logic.", "Bounding Box|Object Detection|Webcam"),
        (21, "Speech translation API", "Converting sound speech text outputs dynamically.", "Speech API|Text Output|Translation"),
        (22, "Teachable API web app", "Web app connection key validation test parameters.", "Teachable API|Web Key|Connection"),
        (23, "Serial Port Uno match", "Local server connection COM port mapping logic.", "COM Port|Web Serial|Uno Link"),
        (24, "Troubleshooting ports", "Locked port errors, wrong baud rate mapping fixes.", "COM Locked|Baud Mismatch|Debug"),
        (25, "Custom logic functions", "Defining clean logic commands output modular functions.", "Modular Logic|Custom functions|Clean Code"),
        (26, "Loop speed optimization", "C++ code delay timing checks for smooth UI.", "Delay Timing|C++ Code|Optimization"),
        (27, "Sensor data plotter", "Live LDR values wave tracking plotter tool.", "LDR Plotter|Live waves|Serial Monitor"),
        (28, "Switch Case state map", "Keypad input key mapping switch case structures.", "Keypad Map|Switch Case|Input Parse"),
        (29, "Fault Finding debugger", "Syntax compile error check console output reading.", "Compile Error|Syntax Check|Console Logs"),
        (30, "Showcase exhibition model", "Self running AI classification logic display.", "Showcase|AI Display|Exhibition")
    ],
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
        (15, "Scratch Pen draw tool", "Drawing lines dynamically on cat movements shapes.", "Pen Tool|Drawing Lines|Shapes"),
        (16, "Ask and wait input", "Reading user input text block save to variable.", "Ask and wait|User Input|Variable Save"),
        (17, "If-else score target", "IF score == 10 THEN next level backdrop switch.", "If-else|Score Target|Backdrop Switch"),
        (18, "Random range pick block", "pick random block logic boundaries selection.", "pick random|Random Range|Boundaries"),
        (19, "Timer countdown block", "Create timer countdown variable decrease count loop.", "Timer|Countdown|Variable Dec"),
        (20, "Hide and show blocks", "Using hide/show blocks on broadcast triggers events.", "Hide/Show|Broadcast Trigger|Events"),
        (21, "Algorithm Flowchart plan", "Draw Scratch game pseudocode logic on paper first.", "Pseudocode|Flowchart|Game Plan"),
        (22, "Variables arrays list", "Create Scratch list array, insert values strings.", "Scratch List|Array Insert|Strings"),
        (23, "Teachable machine dataset", "Train webcam dataset categories labels Scratch.", "Teachable Machine|Dataset|Webcam Labels"),
        (24, "Image classification model", "Training classification classes webcam threshold.", "Classification|Webcam Class|Threshold"),
        (25, "Hand Gesture mappings", "Left, Right hand states mapping Scratch sprite.", "Hand Gestures|Sprite Control|Classification"),
        (26, "Voice activation setup", "Speech API audio waveform matching Scratch controls.", "Voice Match|Speech API|Waveform"),
        (27, "Object recognition box", "Object bounding coordinates box detection logic.", "Bounding Box|Object Detection|Webcam"),
        (28, "Teachable API block", "Load Teachable Machine model extension key validation.", "Teachable API|Extension Key|Model Load"),
        (29, "Fault Finding debugger", "Broken blocks loop checks, logic sequence debugger.", "Debug Blocks|Loop Check|Logic debugger"),
        (30, "Showcase exhibition model", "Self running Scratch AI game live showcase presentation.", "Showcase|AI Scratch Game|Exhibition")
    ],
    "class4": [
        (1, "Blink logic frequency", "delay() block map calculation for millisecond frequency.", "Blink Logic|delay()|Frequency"),
        (2, "Speed control variables", "Delay variable mapping logic parameter changes Uno.", "Delay Variable|Speed control|Uno"),
        (3, "Traffic light logic", "Red Yellow Green LED sequence timing map control.", "Traffic Light|Sequence Logic|Timing Map"),
        (4, "Button digital status", "Parsing digitalRead HIGH/LOW status to serial monitor.", "digitalRead HIGH/LOW|Serial logs|Button Status"),
        (5, "Button toggle state", "Toggle logic state mapping IF button active ON/OFF.", "Toggle State|Button active|Logic"),
        (6, "Potentiometer map calculation", "0-1023 analog range mapping analogWrite 0-255 PWM.", "analogRead 0-1023|analogWrite 0-255|map()"),
        (7, "LDR light threshold", "LDR dark detection parameter threshold level setups.", "LDR threshold|Dark detect|Parameter"),
        (8, "Auto street light logic", "IF LDR < 300 THEN LED HIGH else LED LOW.", "Auto light|LDR 300|LED HIGH/LOW"),
        (9, "Buzzer pitch notesHz", "tone() frequency parameter notes scale map Hz.", "tone()|Buzzer pitch|Hz Notes scale"),
        (10, "Servo sweep speed loop", "Delay iteration steps calibration angle mapping.", "Servo sweep|Delay iteration|Angle map"),
        (11, "Rain sensor threshold", "Water drops levels check output alerts threshold.", "Rain threshold|Water drop alert|Sensor"),
        (12, "Soil moisture range map", "Calibrating dry soil vs wet soil percentage logic.", "Soil dry/wet|Calibration|Percentage map"),
        (13, "I2C LCD coordinate print", "setCursor column row character display coordinate.", "LCD coordinates|setCursor|Column/Row"),
        (14, "Keypad character matrix", "Mapping matrix intersections to ASCII char outputs.", "Keypad matrix|ASCII char|Intersections"),
        (15, "Troubleshooting Uno compiler", "COM port lock fix, board parameter settings check.", "COM lock|Uno compiler|Bugs fix"),
        (16, "Teachable machine dataset", "Webcam dataset loading categories labels.", "Teachable Machine|Dataset|Webcam Labels"),
        (17, "Image classification model", "Training classification classes webcam threshold.", "Classification|Webcam Class|Threshold"),
        (18, "Hand Gesture mappings", "Left, Right hand states mapping serial commands.", "Hand Gestures|Serial Maps|Classification"),
        (19, "Voice activation setup", "Speech API audio waveform matching states.", "Voice Match|Speech API|Waveform"),
        (20, "Object recognition box", "Object bounding coordinates box detection logic.", "Bounding Box|Object Detection|Webcam"),
        (21, "Speech translation API", "Converting sound speech text outputs dynamically.", "Speech API|Text Output|Translation"),
        (22, "Teachable API web app", "Web app connection key validation test parameters.", "Teachable API|Web Key|Connection"),
        (23, "Serial Port Uno match", "Local server connection COM port mapping logic.", "COM Port|Web Serial|Uno Link"),
        (24, "Troubleshooting ports", "Locked port errors, wrong baud rate mapping fixes.", "COM Locked|Baud Mismatch|Debug"),
        (25, "Custom logic functions", "Defining clean logic commands output modular functions.", "Modular Logic|Custom functions|Clean Code"),
        (26, "Loop speed optimization", "C++ code delay timing checks for smooth UI.", "Delay Timing|C++ Code|Optimization"),
        (27, "Sensor data plotter", "Live LDR values wave tracking plotter tool.", "LDR Plotter|Live waves|Serial Monitor"),
        (28, "Switch Case state map", "Keypad input key mapping switch case structures.", "Keypad Map|Switch Case|Input Parse"),
        (29, "Fault Finding debugger", "Syntax compile error check console output reading.", "Compile Error|Syntax Check|Console Logs"),
        (30, "Showcase exhibition model", "Self running AI classification logic display.", "Showcase|AI Display|Exhibition")
    ],
    "class5": [
        (1, "C++ compiler setup", "MinGW compilation setup, command line GCC runs.", "MinGW compiler|GCC command|Compilation"),
        (2, "C++ standard syntax", "main() function return types, scope variables print.", "main() function|Return|Variables"),
        (3, "Variables scope limits", "int float string boolean variables size allocation.", "int/float/string|Memory allocate|Variables"),
        (4, "C++ logic operators", "AND (&&), OR (||), NOT (!) C++ boolean expressions.", "&& Logic||| Logic|! Logic"),
        (5, "Nested If-Else conditions", "Nested branch logic operations tree diagram flow.", "Nested If-Else|Branch logic|Tree diagram"),
        (6, "Baud rate calculations", "Bits per second transit timings parameters monitor.", "Baud rate|Bits per second|Monitor"),
        (7, "For Loop incremental", "Index increment counters, memory optimization logic.", "For loop|Index count|Memory optimize"),
        (8, "While Loop exit logic", "break statement loops exit checks conditions.", "While exit|break|Loops check"),
        (9, "C++ Custom Header files", "Creating custom library header files definitions.", "Header files|Custom Library|Definitions"),
        (10, "Arrays memory map", "Index mapping memory offset arrays structures.", "Arrays memory|Offset index|Structures"),
        (11, "String functions C++", "length() find() substring() string parser functions.", "length()|find()|substring()|String"),
        (12, "Function parameter pass", "Call by value vs call by reference memory paths.", "Call by value|Call by reference|Memory"),
        (13, "Teachable Machine model", "Exporting model file metadata JSON load process.", "Teachable Machine|JSON load|Metadata"),
        (14, "Web socket server app", "Connecting Python web sockets to local port server.", "Python Web sockets|Port Server|Connection"),
        (15, "Hand gestures API map", "Webcam gesture class string sent to serial COM.", "Webcam gestures|String COM|Serial output"),
        (16, "Voice Model Speech to text", "SpeechRecognition module parsing sound waves text.", "SpeechRecognition|Text parse|Sound waves"),
        (17, "Audio classification model", "Audios waveforms feature matching thresholds.", "Audio Classify|Waveform feature|Threshold"),
        (18, "Troubleshooting COM port", "Access denied Serial port lock bypass script.", "Access Denied|Port Lock|Bypass Script"),
        (19, "Custom C++ libraries", "Uno import library directory structure check.", "Library directory|Import check|Uno lib"),
        (20, "Sensor data plotter", "Live LDR values wave tracking plotter tool.", "LDR Plotter|Live waves|Serial Monitor"),
        (21, "Switch Case state map", "Keypad input key mapping switch case structures.", "Keypad Map|Switch Case|Input Parse"),
        (22, "Fault Finding debugger", "Syntax compile error check console output reading.", "Compile Error|Syntax Check|Console Logs"),
        (23, "Teachable machine dataset", "Webcam dataset loading categories labels.", "Teachable Machine|Dataset|Webcam Labels"),
        (24, "Image classification model", "Training classification classes webcam threshold.", "Classification|Webcam Class|Threshold"),
        (25, "Hand Gesture mappings", "Left, Right hand states mapping serial commands.", "Hand Gestures|Serial Maps|Classification"),
        (26, "Voice activation setup", "Speech API audio waveform matching states.", "Voice Match|Speech API|Waveform"),
        (27, "Object recognition box", "Object bounding coordinates box detection logic.", "Bounding Box|Object Detection|Webcam"),
        (28, "Teachable API web app", "Web app connection key validation test parameters.", "Teachable API|Web Key|Connection"),
        (29, "Serial Port Uno match", "Local server connection COM port mapping logic.", "COM Port|Web Serial|Uno Link"),
        (30, "Showcase exhibition model", "Self running AI classification logic display.", "Showcase|AI Display|Exhibition")
    ],
    "class6": [
        (1, "Python installation setup", "pip packages managers, environment variables config.", "Python setup|pip packages|Variables config"),
        (2, "Python basic math print", "Basic operators string print formats logic.", "Math print|Operators|String format"),
        (3, "Python Indentation syntax", "Indentation blocks checks logic errors fixes.", "Python Indentation|Blocks check|Bugs fix"),
        (4, "Python Loops iterations", "for range loops, conditional while loop logic.", "for range|while loop|Python Loops"),
        (5, "PySerial COM connection", "Serial port initialization python loop read.", "PySerial|Port initialize|Read loop"),
        (6, "Bambu Studio CAD import", "STL orientation scaling parameters inside slicer.", "Bambu Studio|STL scaling|Slicer config"),
        (7, "Slicing layer config", "0.2mm parameters setting layer width calculations.", "Layer width|Slicing parameters|Config"),
        (8, "Gyroid infill structure", "Infill pattern strength density comparisons tests.", "Gyroid infill|Strength test|Density check"),
        (9, "GCode file parameters", "Gcode commands syntax check coordinate mapping.", "Gcode parameters|Syntax check|Coordinates"),
        (10, "L298N Speed map logic", "PWM outputs mapping motors speed curves.", "L298N speed|PWM outputs|Motor speed"),
        (11, "HC-SR04 sonar transit", "Sonar speed duration math time calculation.", "HC-SR04 sonar|Sound speed|Transit time"),
        (12, "Distance alert threshold", "IF distance < 20cm brake command serial trigger.", "Distance alert|20cm Brake|Serial trigger"),
        (13, "Obstacle check logic", "Check left path vs check right path decisions.", "Path check|Brake/Turn|Decisions"),
        (14, "SPI interface setup", "MFRC522 libraries address setups registers.", "MFRC522|SPI interface|Address setup"),
        (15, "RFID authentication C++", "HEX UID compare statement access credentials code.", "RFID Auth|HEX UID|Access credentials"),
        (16, "MPU6050 I2C registers", "Read MPU6050 accel values address register loops.", "I2C read|MPU6050 register|Accel values"),
        (17, "Angle mathematical mapping", "Gyro raw values mapped degree conversion logic.", "Angle map|Gyro degrees|Conversion logic"),
        (18, "Tinkercad structural design", "Creating brackets STL file export Tinkercad.", "Tinkercad bracket|STL export|CAD design"),
        (19, "Matplotlib live graphs", "Real-time plotter line graphs data visualization.", "Matplotlib|Live graph|Plotter line"),
        (20, "Sensor data plotter", "Live LDR values wave tracking plotter tool.", "LDR Plotter|Live waves|Serial Monitor"),
        (21, "Switch Case state map", "Keypad input key mapping switch case structures.", "Keypad Map|Switch Case|Input Parse"),
        (22, "Fault Finding debugger", "Syntax compile error check console output reading.", "Compile Error|Syntax Check|Console Logs"),
        (23, "Teachable machine dataset", "Webcam dataset loading categories labels.", "Teachable Machine|Dataset|Webcam Labels"),
        (24, "Image classification model", "Training classification classes webcam threshold.", "Classification|Webcam Class|Threshold"),
        (25, "Hand Gesture mappings", "Left, Right hand states mapping serial commands.", "Hand Gestures|Serial Maps|Classification"),
        (26, "Voice activation setup", "Speech API audio waveform matching states.", "Voice Match|Speech API|Waveform"),
        (27, "Object recognition box", "Object bounding coordinates box detection logic.", "Bounding Box|Object Detection|Webcam"),
        (28, "Teachable API web app", "Web app connection key validation test parameters.", "Teachable API|Web Key|Connection"),
        (29, "Serial Port Uno match", "Local server connection COM port mapping logic.", "COM Port|Web Serial|Uno Link"),
        (30, "Showcase exhibition model", "Self running AI classification logic display.", "Showcase|AI Display|Exhibition")
    ],
    "class7": [
        (1, "Python Lists structures", "Array storage appending lists indexes sorting.", "Lists append|Sorting|Index array"),
        (2, "ThingSpeak JSON parsing", "GET request return fields JSON parser values.", "ThingSpeak JSON|GET request|Field parsing"),
        (3, "ThingSpeak fields update", "Data update payload formatting parameters logs.", "Data update|ThingSpeak logs|Parameters"),
        (4, "IFTTT email webhooks", "Event name payload triggers notifications alert.", "IFTTT email|Webhooks|Trigger alert"),
        (5, "RFID Google Sheets log", "Google Script triggers Google Sheets logging data.", "Google Script|Sheets log|RFID log"),
        (6, "Moving parts clearance", "0.5mm clearance gap slicer boundary setup.", "Clearance gap|3D print hinge|Slicer setup"),
        (7, "Bambu AMS multicolor select", "Bambu Studio paint tool color fill STL.", "Bambu AMS|Paint tool|Slicer colors"),
        (8, "Drone flight forces", "Forces balance equations roll pitch yaw parameters.", "Quadcopter forces|Roll/Pitch/Yaw|Balance"),
        (9, "Drone torque cancellation", "Quadcopter motors placement stability loops.", "Quadcopter stability|Torque cancel|Motor layout"),
        (10, "IMU roll pitch angles", "MPU6050 angle tilt mapping stabilizer logic.", "Roll/Pitch angles|MPU6050 tilt|Stabilizer"),
        (11, "PID stabilization loop", "Proportional Integral Derivative correction calculation.", "PID stabilize|Derivative correction|Math"),
        (12, "Camera Gimbal servos map", "Tilt angles values sent to Servos active map.", "Gimbal Servos|Tilt map|2-Axis"),
        (13, "ESP-NOW remote setup", "MAC address target peer configurations setup.", "ESP-NOW MAC|Peer config|Remote setup"),
        (14, "Basic Auth verification", "Basic Authentication header check web server.", "Basic Auth|Security Header|Web Server"),
        (15, "RFID coordinate tracking", "RFID card index positions coordinate grid maps.", "RFID grid|Coordinate tracking|Index check"),
        (16, "OpenCV Video Capture", "Frame capture loop scale resize python OpenCV.", "cv2.VideoCapture|OpenCV Frame|Python loop"),
        (17, "HSV segmentation mask", "HSV scale ranges limits color tracking mask.", "HSV scale|Color mask|cv2.inRange"),
        (18, "Contour tracking math", "Moments parsing center coordinates X/Y math.", "Contour center|cv2.moments|X/Y coordinates"),
        (19, "Face detection Haar Cascade", "CascadeClassifier XML matching loop bounding box.", "Haar Cascade|Face detection|Bounding box"),
        (20, "Sensor data plotter", "Live LDR values wave tracking plotter tool.", "LDR Plotter|Live waves|Serial Monitor"),
        (21, "Switch Case state map", "Keypad input key mapping switch case structures.", "Keypad Map|Switch Case|Input Parse"),
        (22, "Fault Finding debugger", "Syntax compile error check console output reading.", "Compile Error|Syntax Check|Console Logs"),
        (23, "Teachable machine dataset", "Webcam dataset loading categories labels.", "Teachable Machine|Dataset|Webcam Labels"),
        (24, "Image classification model", "Training classification classes webcam threshold.", "Classification|Webcam Class|Threshold"),
        (25, "Hand Gesture mappings", "Left, Right hand states mapping serial commands.", "Hand Gestures|Serial Maps|Classification"),
        (26, "Voice activation setup", "Speech API audio waveform matching states.", "Voice Match|Speech API|Waveform"),
        (27, "Object recognition box", "Object bounding coordinates box detection logic.", "Bounding Box|Object Detection|Webcam"),
        (28, "Teachable API web app", "Web app connection key validation test parameters.", "Teachable API|Web Key|Connection"),
        (29, "Serial Port Uno match", "Local server connection COM port mapping logic.", "COM Port|Web Serial|Uno Link"),
        (30, "Showcase exhibition model", "Self running AI classification logic display.", "Showcase|AI Display|Exhibition")
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
