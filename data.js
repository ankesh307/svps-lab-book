const curriculumData = {
    "ai-software": {
        "tier1": {
            "title": "Tier 1: Junior Makers (AI & Software)",
            "kit": "📦 No physical kit required for this section, mostly digital tools and Tinkercad.",
            "modules": [
                {
                    "title": "Module 1: 3D Design (Days 1-6)",
                    "days": [
                        { day: 1, type: "Fundamental", title: "Intro to Dimensions & 3D Pen Safety", desc: "Understand 2D vs 3D shapes. Learn the safety rules for using a 3D pen, handling the hot tip, and loading PLA filament." },
                        { day: 2, type: "Fundamental", title: "3D Pen Mechanics (Tracing & Welding)", desc: "Practice tracing 2D stencils and learn how to weld pieces together to make simple 3D objects." },
                        { day: 3, type: "Fundamental", title: "Digital 3D Tinkercad Intro", desc: "Introduction to the digital workspace. Learn about the X, Y, and Z planes and how to place basic solid blocks." },
                        { day: 4, type: "Project", title: "3D Pen Build (Custom Keychain)", desc: "Design and physically draw a custom keychain using the 3D pen and colorful PLA filaments." },
                        { day: 5, type: "Project", title: "Tinkercad Build (Smart House)", desc: "Apply Tinkercad skills to digitally design a Smart House featuring multiple rooms and a roof." },
                        { day: 6, type: "Test", title: "Design Review & Class Presentation", desc: "Present the physical keychain and the digital Smart House to the class. Explain the design choices." }
                    ]
                },
                {
                    "title": "Module 2: AI Tools (Days 7-12)",
                    "days": [
                        { day: 7, type: "Fundamental", title: "AI Text & Image Generation", desc: "Introduction to prompting. Learn how to ask AI chatbots questions and generate custom images using text prompts." },
                        { day: 8, type: "Fundamental", title: "AI Video Tools", desc: "Learn how to convert generated AI images into short, moving video clips using basic AI video generators." },
                        { day: 9, type: "Fundamental", title: "AI Web & PPT Outlines", desc: "Discover how AI can help structure ideas and instantly generate outlines for presentations." },
                        { day: 10, type: "Project", title: "Media Generator (Storyboard)", desc: "Use AI image tools to create a sequence of images that tell a story, assembling them into a storyboard." },
                        { day: 11, type: "Project", title: "Pitch Deck (5-Slide PPT)", desc: "Use AI to generate a 5-slide presentation and a simple landing page concept for a new idea." },
                        { day: 12, type: "Test", title: "AI Showcase & Presentation", desc: "Showcase the AI-generated storyboard and pitch deck to the class." }
                    ]
                },
                {
                    "title": "Module 3: Coding (Days 13-18)",
                    "days": [
                        { day: 13, type: "Fundamental", title: "HTML Basics (Writing Tags)", desc: "Learn the structure of the web. Write basic HTML tags (headings, paragraphs) to structure a simple page." },
                        { day: 14, type: "Fundamental", title: "Logic Basics", desc: "Introduction to computational thinking using loops and visual logic blocks." },
                        { day: 15, type: "Fundamental", title: "Python Basics", desc: "Learn about variables (storing data) and perform simple mathematical operations in Python." },
                        { day: 16, type: "Project", title: "Personal Profile", desc: "Code a custom, one-page HTML website showcasing personal hobbies and interests." },
                        { day: 17, type: "Project", title: "Logic Game", desc: "Build a simple text-based game or calculator using Python logic and math." },
                        { day: 18, type: "Test", title: "Code Review", desc: "Live debugging test where students must find and fix deliberate errors in a piece of code." }
                    ]
                }
            ]
        },
        "tier2": {
            "title": "Tier 2: Smart Coders (AI & Software)",
            "kit": "📦 No physical kit required, PC/Laptop with Tinkercad, Python IDE, and Web Browser.",
            "modules": [
                {
                    "title": "Module 1: 3D Design (Days 1-6)",
                    "days": [
                        { day: 1, type: "Fundamental", title: "Tinkercad Navigation", desc: "Master the Tinkercad interface and the X/Y/Z workplane for precise 3D modeling." },
                        { day: 2, type: "Fundamental", title: "Placing & Sizing Solid Blocks", desc: "Learn exact dimensional sizing and aligning of basic solid shapes." },
                        { day: 3, type: "Fundamental", title: "Grouping & Hole Features", desc: "Combine multiple shapes and use 'Hole' shapes to carve out complex details." },
                        { day: 4, type: "Project", title: "Tinkercad Build (Digital Smart House)", desc: "Design an advanced Smart House with hollowed-out rooms, furniture, and proper scaling." },
                        { day: 5, type: "Project", title: "3D Arduino Case Design", desc: "Design a custom protective case for the Arduino Uno board, ensuring ports are accessible." },
                        { day: 6, type: "Test", title: "Design Review & Class Presentation", desc: "Present the Smart House and Arduino Case. Review sizing constraints and design efficiency." }
                    ]
                },
                {
                    "title": "Module 2: AI Tools (Days 7-12)",
                    "days": [
                        { day: 7, type: "Fundamental", title: "AI Text & Image Generation", desc: "Advanced prompt engineering for specific art styles and detailed text responses." },
                        { day: 8, type: "Fundamental", title: "AI Video Exploring", desc: "Explore AI tools that create dynamic video sequences and learn how to write prompts for motion." },
                        { day: 9, type: "Fundamental", title: "AI Web & PPT Outlining", desc: "Use AI to brainstorm tech startup ideas and structure professional presentation outlines." },
                        { day: 10, type: "Project", title: "Media Generator (Storyboard)", desc: "Create a detailed AI storyboard featuring consistent characters and environments." },
                        { day: 11, type: "Project", title: "Pitch Deck (Tech Startup)", desc: "Generate a professional slide deck for a mock tech startup, focusing on problem and solution." },
                        { day: 12, type: "Test", title: "AI Showcase & Presentation", desc: "Pitch the tech startup idea using the generated AI media and slides." }
                    ]
                },
                {
                    "title": "Module 3: Coding (Days 13-18)",
                    "days": [
                        { day: 13, type: "Fundamental", title: "HTML Basics (Webpage structures)", desc: "Build multi-section webpages using HTML5 semantic tags and structure." },
                        { day: 14, type: "Fundamental", title: "C++ Logic (Arduino Prep)", desc: "Introduction to C++ syntax, focusing on setup(), loop(), and the importance of semicolons." },
                        { day: 15, type: "Fundamental", title: "Python Power", desc: "Deep dive into Python variables, data types, and complex mathematical logic." },
                        { day: 16, type: "Project", title: "Personal Profile (Custom HTML)", desc: "Code a fully structured, stylish HTML personal portfolio website." },
                        { day: 17, type: "Project", title: "Logic Game (Python Calculator)", desc: "Program an interactive text-based calculator in Python that takes user input." },
                        { day: 18, type: "Test", title: "Code Review", desc: "Examine broken Python and HTML code, identify bugs, and fix them live." }
                    ]
                }
            ]
        },
        "tier3": {
            "title": "Tier 3: Tech Pros (AI & Software)",
            "kit": "📦 Requires PC/Laptop with Python IDE and Bambu Studio Slicer software.",
            "modules": [
                {
                    "title": "Module 1: 3D Design (Days 1-6)",
                    "days": [
                        { day: 1, type: "Fundamental", title: "Digital 3D Tinkercad Navigation", desc: "Advanced modeling techniques and rapid prototyping workflows in Tinkercad." },
                        { day: 2, type: "Fundamental", title: "Bambu Slicer Software Intro", desc: "Import 3D models into the slicer, understand the build plate, and prepare for printing." },
                        { day: 3, type: "Fundamental", title: "Slicing Settings", desc: "Learn about layer height, supports, and infill patterns (e.g., Gyroid Infill) for strength." },
                        { day: 4, type: "Project", title: "3D Print a Bracket", desc: "Design a custom mount for the Ultrasonic sensor and prepare it for printing." },
                        { day: 5, type: "Project", title: "3D Moving Parts", desc: "Design Print-in-Place hinges, learning about gaps and tolerances in 3D printing." },
                        { day: 6, type: "Test", title: "Design Review & Slicing Presentation", desc: "Present the 3D designs and explain the chosen slicing settings for optimal printing." }
                    ]
                },
                {
                    "title": "Module 2: AI Tools (Days 7-12)",
                    "days": [
                        { day: 7, type: "Fundamental", title: "AI Text & Image Generation", desc: "Master complex prompt chains to generate highly specific technical documentation and assets." },
                        { day: 8, type: "Fundamental", title: "AI Video Tools", desc: "Generate high-quality video demonstrations or concept trailers using AI tools." },
                        { day: 9, type: "Fundamental", title: "AI Web & PPT Generation", desc: "Automate the creation of full website copy and professional investor pitch decks." },
                        { day: 10, type: "Project", title: "Media Generator Storyboard", desc: "Produce a cinematic AI storyboard for an advanced robotics product concept." },
                        { day: 11, type: "Project", title: "Pitch Deck (Landing Page & PPT)", desc: "Develop a complete pitch deck and a functional landing page layout for a product launch." },
                        { day: 12, type: "Test", title: "AI Showcase", desc: "Deliver a professional pitch using all AI-generated assets." }
                    ]
                },
                {
                    "title": "Module 3: Coding (Days 13-18)",
                    "days": [
                        { day: 13, type: "Fundamental", title: "Python Basics (Loops & Conditionals)", desc: "Master 'While True' loops, and complex 'If-Elif-Else' decision trees in Python." },
                        { day: 14, type: "Fundamental", title: "Python Lists & Dictionaries", desc: "Learn how to store, retrieve, and manipulate collections of data efficiently." },
                        { day: 15, type: "Fundamental", title: "C++ Local Web Server HTML", desc: "Learn how to write HTML code inside C++ strings to serve webpages from microcontrollers." },
                        { day: 16, type: "Project", title: "Password Protected Webpage", desc: "Build a secure local webpage that requires a password login using Python or C++ logic." },
                        { day: 17, type: "Project", title: "Python Live Graph", desc: "Write a script to visualize simulated sensor data dynamically on a live graph." },
                        { day: 18, type: "Test", title: "Code Review", desc: "Live debugging of complex algorithms and web server code." }
                    ]
                }
            ]
        }
    },
    "robotics-hardware": {
        "tier1": {
            "title": "Tier 1: Junior Makers (Robotics & Hardware)",
            "kit": "📦 TIER 1 KIT: 9V Battery & Snap, Gear Motor, Toy Motor + Propeller, LEDs, Buzzer, Vibration Motor, Switches, Cardboard Mounts.",
            "modules": [
                {
                    "title": "Module 4: Robotics (Days 19-24)",
                    "days": [
                        { day: 19, type: "Fundamental", title: "Battery Magic & Circuit Path", desc: "Learn how electricity flows. Build a basic circuit to light up Multicolor LEDs using a 9V battery." },
                        { day: 20, type: "Fundamental", title: "Power Test", desc: "Compare the speed and torque of a Normal Toy Motor versus a Gear Motor." },
                        { day: 21, type: "Fundamental", title: "Switch Control", desc: "Learn how to open and close circuits using Rocker Switches and Push Buttons." },
                        { day: 22, type: "Project", title: "Bristlebot Construction", desc: "Build a tiny crawling robot using a Vibration Coin Motor and craft materials." },
                        { day: 23, type: "Project", title: "Air Thrust Car", desc: "Construct a vehicle powered by the wind thrust from a Fan Motor and Propeller." },
                        { day: 24, type: "Test", title: "Robotics Race", desc: "Test and race the Air Thrust Cars on a physical track to see whose is fastest." }
                    ]
                },
                {
                    "title": "Module 5: IoT / Automation (Days 25-30)",
                    "days": [
                        { day: 25, type: "Fundamental", title: "Conductor Test & Wire Resistance", desc: "Test different materials to see what conducts electricity and learn about resistance." },
                        { day: 26, type: "Fundamental", title: "Series & Parallel Wiring", desc: "Wire multiple LEDs in series and parallel to see how it affects brightness." },
                        { day: 27, type: "Fundamental", title: "AND / OR Logic Game", desc: "Use manual push buttons to create physical AND/OR logic gates." },
                        { day: 28, type: "Project", title: "Doorbell Alarm", desc: "Build a security box featuring a push-button triggered Active Buzzer." },
                        { day: 29, type: "Project", title: "Smart Home Craft", desc: "Construct a cardboard house with hidden LED wiring and a roof exhaust fan." },
                        { day: 30, type: "Test", title: "Grand Bootcamp Gala", desc: "Final showcase event presenting the Smart Home models and Robotics cars." }
                    ]
                }
            ]
        },
        "tier2": {
            "title": "Tier 2: Smart Coders (Robotics & Hardware)",
            "kit": "📦 TIER 2 KIT: Arduino Uno, Breadboard, Jumper Wires, Potentiometer, Bluetooth HC-05, Sensors (IR, Rain, LDR, Soil, Receiver), Keypad, LCD1602, Relay, Pump, Servo, Motor.",
            "modules": [
                {
                    "title": "Module 4: Robotics (Days 19-24)",
                    "days": [
                        { day: 19, type: "Fundamental", title: "Meet Arduino & Breadboard", desc: "Learn the Arduino pins and how to prototype circuits using a solderless breadboard." },
                        { day: 20, type: "Fundamental", title: "Servo Motor & Potentiometer", desc: "Control the precise angle of an SG90 Servo Motor using a 10K Potentiometer dial." },
                        { day: 21, type: "Fundamental", title: "Sensor Arsenal", desc: "Learn how to read analog/digital data from LDR (Light) and IR (Obstacle) sensors." },
                        { day: 22, type: "Project", title: "Auto Street Light", desc: "Program the Arduino to automatically turn on LEDs when the LDR detects darkness." },
                        { day: 23, type: "Project", title: "Laser Tripwire Alarm", desc: "Build an invisible security system using a Laser Module, LDR, and a loud Buzzer." },
                        { day: 24, type: "Test", title: "Robotics Circuit Presentation", desc: "Explain the wiring, logic, and code behind the built robotics circuits." }
                    ]
                },
                {
                    "title": "Module 5: IoT / Automation (Days 25-30)",
                    "days": [
                        { day: 25, type: "Fundamental", title: "I2C Protocol & LCD1602", desc: "Wire and program an LCD screen using I2C to display text and sensor data." },
                        { day: 26, type: "Fundamental", title: "Bluetooth (HC-05) App Linking", desc: "Connect the HC-05 module and link it to a smartphone app to send/receive commands." },
                        { day: 27, type: "Fundamental", title: "5V Relay Switch", desc: "Learn how to safely control high-power devices using a low-power Arduino signal." },
                        { day: 28, type: "Project", title: "Bluetooth Smart Fan", desc: "Build a fan (Normal Motor + Relay) that can be turned on/off wirelessly via a phone app." },
                        { day: 29, type: "Project", title: "Auto Plant Watering", desc: "Combine a Soil Moisture Sensor and 5V Water Pump to automatically hydrate a plant." },
                        { day: 30, type: "Test", title: "Mega Smart Home Show", desc: "Final presentation of all integrated smart automation and IoT projects." }
                    ]
                }
            ]
        },
        "tier3": {
            "title": "Tier 3: Tech Pros (Robotics & Hardware)",
            "kit": "📦 TIER 3 KIT: ESP8266 (Wi-Fi), Sensors (Ultrasonic, DHT11, MPU6050), RFID RC522, L298N Driver, Robot Car Chassis, Servo.",
            "modules": [
                {
                    "title": "Module 4: Robotics (Days 19-24)",
                    "days": [
                        { day: 19, type: "Fundamental", title: "Meet ESP8266 & 3.3V Limits", desc: "Introduction to the Wi-Fi enabled ESP8266 board and understanding 3.3V power logic." },
                        { day: 20, type: "Fundamental", title: "L298N High-Power Motor Driver", desc: "Learn how to wire battery power to the L298N driver to control heavy BO motors." },
                        { day: 21, type: "Fundamental", title: "Ultrasonic Radar & Distance Math", desc: "Trigger sound waves and calculate the time-of-flight to measure distance accurately." },
                        { day: 22, type: "Project", title: "C++ Car Code", desc: "Write modular C++ functions (forward, backward, left, right) to control the car chassis." },
                        { day: 23, type: "Project", title: "Obstacle Avoider Car", desc: "Integrate the Ultrasonic sensor so the car automatically brakes and turns at 20cm." },
                        { day: 24, type: "Test", title: "Robotics Race", desc: "Test the autonomous obstacle avoider cars on a physical track with hurdles." }
                    ]
                },
                {
                    "title": "Module 5: IoT / Automation (Days 25-30)",
                    "days": [
                        { day: 25, type: "Fundamental", title: "Connect ESP8266 to Wi-Fi", desc: "Write C++ code to connect the board to a local network and ping its IP address." },
                        { day: 26, type: "Fundamental", title: "Cloud API & ThingSpeak", desc: "Set up an IoT cloud platform (ThingSpeak) and generate API keys for data transmission." },
                        { day: 27, type: "Fundamental", title: "SPI Wiring & RFID Scanner", desc: "Learn the SPI communication protocol to wire and read RFID cards using the RC522 module." },
                        { day: 28, type: "Project", title: "Weather Webpage", desc: "Read Temp/Humidity from the DHT11 and send the live data to the cloud dashboard." },
                        { day: 29, type: "Project", title: "RFID Online Attendance", desc: "Scan student ID cards and automatically log the attendance data to Google Sheets via API." },
                        { day: 30, type: "Test", title: "Final Grand Gala", desc: "Massive showcase combining the autonomous vehicles and cloud-connected IoT systems." }
                    ]
                }
            ]
        }
    }
};
