# Tankbot

This repository contains Python code for controlling a Raspberry Pi-based tank-style robot, built using the DFROBOT Devastator Tank Mobile Robot Platform. The bot is controlled via keyboard inputs, and can be expanded to include sensors, a camera, and remote API control.

## Table of Contents
1. [Features](#features)  
2. [Hardware Requirements](#hardware-requirements)  
3. [Software Setup](#software-setup)  
4. [Wiring Diagram](#wiring-diagram)  
5. [Usage](#usage)  
6. [Expansion Ideas](#expansion-ideas)  
7. [License](#license)

---

## Features

- **Simple Movement Controls**: Forward, reverse, left, right, and stop.  
- **Fun Routines**: Quick “Yes”, “No”, and “Welcome” dance sequences.  
- **Keyboard Control**: Use the `keyboard` library to issue commands via arrow keys or hotkeys.  
- **Recording & Playback**: Record a sequence of movement commands and replay them at will.  
- **Modular Design**: `tankbot.py`/`tankboy.py` handles GPIO pins and motor logic, while `bot.py` manages user input and the main loop.

---

## Hardware Requirements

- **Raspberry Pi** (tested on Pi 3/4)  
- **DFROBOT Devastator Tank Chassis** (or similar tank-style platform)  
- **Motor Driver** (e.g., L298N or equivalent)  
- **DC Gear Motors** (included with many tank chassis kits)  
- **Power Source(s)** for the Pi (5V) and for the motors (often 7–12V, depending on your driver)  
- **Jumper Wires** (male-female, female-female)  
- **Optional**: Protective case for the Pi, additional sensors, camera module, etc.

---

## Software Setup

1. **Install RPi.GPIO and keyboard libraries**  
   ```bash
   sudo apt-get update && sudo apt-get upgrade -y
   sudo pip3 install RPi.GPIO
   sudo pip3 install keyboard
   ```
2. **Clone or download this repository**  
   ```bash
   git clone https://github.com/grizzlypeaksoftware/tankbot.git
   cd tankbot
   ```
3. **Check Python version**  
   - This code is designed for Python 3.  
   - On most Raspberry Pi OS setups, `python3` will be the default interpreter.

---

## Wiring Diagram

Below is an overview of the GPIO pin assignments and connections (BOARD mode). Adjust if needed:

| Pi Pin (BOARD) | Connected To       | Role                       |
|----------------|--------------------|----------------------------|
| 3              | Motor Driver IN1   | Left motor direction       |
| 5              | Motor Driver IN2   | Left motor direction       |
| 16             | Motor Driver IN3   | Right motor direction      |
| 18             | Motor Driver IN4   | Right motor direction      |
| 2 (5V)         | Motor Driver 5V    | (if required by driver)    |
| 6 (GND)        | Motor Driver GND   | Common ground              |

The motor outputs on your driver (often labeled OUT1/OUT2 for Motor A, and OUT3/OUT4 for Motor B) should be wired to the left and right motors, respectively. Ensure the motor driver has a suitable external power supply (often 7–12V, depending on the motors).

---

## Usage

1. **Power Up**  
   - Power on the Raspberry Pi and the motor driver’s power supply.  
2. **Run the Code**  
   ```bash
   cd /path/to/tankbot
   python3 bot.py
   ```
   - The bot will perform a quick “welcome” movement test and then wait for keyboard input.

3. **Keyboard Controls**  
   - **Arrow Keys**: Move forward, backward, left, right.  
   - **s**: Stop the bot.  
   - **1**: Perform a “No” shake routine.  
   - **2**: Perform a “Yes” nod routine.  
   - **3**: Replay the “Welcome” routine.  
   - **F1**: Start recording your key inputs.  
   - **F2**: Stop recording and immediately replay the recorded sequence.  
   - **q**: Quit the program.  

4. **Recording & Playback**  
   - Press **F1** to start recording a series of movements. Press **F2** to end the recording and automatically replay those moves. Press **F2** again without a new recording to replay the same sequence.

5. **Shut Down / Cleanup**  
   - Once you exit the program, `GPIO.cleanup()` is automatically called in the code (see `tankbot.Close()`). This releases the GPIO pins and prevents stray signals.

---

## Expansion Ideas

- **Camera Vision**: Integrate a Pi Camera or USB webcam for FPV (First-Person View) control or computer vision projects.  
- **Remote API**: Create a small Flask or FastAPI server to control the tankbot from a web dashboard or mobile app.  
- **Autonomous Navigation**: Add ultrasonic or infrared sensors for obstacle detection and pathfinding.  
- **Speech Control**: Integrate libraries like `speech_recognition` to add voice commands.  

Feel free to share your additions and experiments so others can learn from and enjoy your creativity!

---

## License

This project is open-source. Feel free to modify and distribute your versions of the code. If you share it publicly, a small shout-out or acknowledgment is always appreciated!

---

**Happy building and coding!** If you have any questions, issues, or feature requests, please open an issue or contact [Shane Larson](https://github.com/grizzlypeaksoftware). Remember to keep experimenting and having fun—Tankbot is just the start of your journey into DIY robotics.