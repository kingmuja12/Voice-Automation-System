# Voice Automation System

Welcome to the Voice Automation System repository! This project aims to develop a voice-activated home automation system using Python, Tkinter for GUI, and Arduino for hardware interaction.

## Overview

The Voice Automation System enables users to control various home appliances and devices using voice commands. The system consists of three main components:

1. **Graphical User Interface (GUI)**: Provides a user-friendly interface for authentication and initiating voice commands.
2. **Authentication Module**: Manages user authentication and user history storage.
3. **Voice Control Module**: Recognizes voice commands, processes them, and interacts with Arduino hardware components.

## Key Features

- **User Authentication**: Secure authentication mechanism with hashed passwords and user history storage.
- **Voice Command Recognition**: Integration with the Vosk library for accurate voice transcription and command processing.
- **Arduino Integration**: Control of lights, temperature retrieval, and automation tasks based on predefined conditions using Arduino sensors and actuators.

## Getting Started

To get started with the Voice Automation System, follow these steps:

1. Clone the repository to your local machine.
2. Install the required Python libraries listed in `requirements.txt`.
3. Ensure you have the necessary hardware components, including an Arduino board, sensors, and actuators.
4. Run the `GUI.py` script to start the graphical user interface.
5. Enter your credentials to authenticate and initiate voice commands.

## File Structure

The repository is organized as follows:

- **GUI.py**: Main script for the graphical user interface setup and interaction.
- **authentication.py**: Handles user authentication and user history management.
- **voice_control.py**: Implements voice command recognition and interaction with Arduino hardware.
- **requirements.txt**: Contains a list of required Python libraries.

## Testing

The system has undergone extensive testing to ensure its stability and reliability. Test scenarios include:

- Correct and incorrect user authentication.
- Voice command recognition and execution.
- Integration with Arduino hardware components.
- Error handling and user feedback mechanisms.


## Contributors

- Abdulwaheed Abdulmujeeb - Developed voice_control.py and Authentication.py.
- Mohammed Saad Shaikh - Organized the codebase and created GUI.py.

  
Feel free to explore the repository and contribute to enhancing the Voice Automation System! If you have any questions or suggestions, please don't hesitate to reach out.

