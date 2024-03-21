import os
from engi1020.arduino.api import *
from authentication import log_to_file_and_speak
from vosk import Model, KaldiRecognizer
import pyaudio
import numpy as np
model = Model(r"C:\Users\Racool\Downloads\vosk-model-en-us-0.22 (1)\vosk-model-en-us-0.22")


def capture_and_transcribe(listen_duration=4):
    """
    Captures audio for a specified duration, transcribes it, and returns the transcription.

    Args:
        model_path (str): Path to the Vosk model directory.
        listen_duration (int, optional): Duration to listen for in seconds. Defaults to 5.

    Returns:
        str: The transcribed text.
    """
    # Initialize PyAudio
    p = pyaudio.PyAudio()

    # Define audio stream parameters
    format = pyaudio.paInt16
    channels = 1
    rate = 16000
    chunk_duration = 0.2  # Each read length in seconds
    frames_per_buffer = int(rate * chunk_duration)

    # Open the microphone stream
    stream = p.open(format=format,
                    channels=channels,
                    rate=rate,
                    input=True,
                    frames_per_buffer=frames_per_buffer)
    
    log_to_file_and_speak('I am listening')
    stream.start_stream()

    # Create a recognizer with the model
    recognizer = KaldiRecognizer(model, rate)

    # Listen and record for the fixed duration
    num_chunks = int(listen_duration / chunk_duration)
    for _ in range(num_chunks):
        data = stream.read(frames_per_buffer, exception_on_overflow=False)
        recognizer.AcceptWaveform(data)

    # Close the audio stream
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Process and return the captured audio transcription
    result = recognizer.Result()
    return result


def voice_command():
    """
    Processes a spoken command.
    """
    buzzer_stop(5)
    light = (analog_read(6))
    print(light)
    command = capture_and_transcribe()
    command = command[14:-3]

    if command:
        print(f"You said: {command}")  

        if ( "on"in command ) and ("ligth" in command) :
            digital_write(4, True)
            oled_clear()
            oled_print('The light is on!')
            log_to_file_and_speak('The light is on!')

        elif ( "off"in command ) and ("ligth" in command):
            digital_write(4, False)
            oled_clear()
            oled_print('The light is off!')
            log_to_file_and_speak('The light is off!')

        elif "temperature" in command:
            temp = pressure_get_temp()
            oled_clear()
            oled_print(f'Current temp: \n {temp} C')
            log_to_file_and_speak(f'The current temperature is: {temp} Celsious')


        elif "Autonomous" in command:
            temp = pressure_get_temp()
            log_to_file_and_speak('Ok')
            light1 = (analog_read(6))

            if light1 <= 8:
                log_to_file_and_speak(f"the light in the room is currently low, so i will turn on the light")
                            

                digital_write(4, True)
            else:
                log_to_file_and_speak('the ligth in the room is normal')
                digital_write(4, False)
            log_to_file_and_speak(f'The current temperature is: {temp} Celsious')    
            if temp >= 26:
                log_to_file_and_speak('Warning!!! the temperature is too high')
                buzzer_frequency(5, 400)
            

        else:
            log_to_file_and_speak("I am sorry, could you repeat that please")

    else:
        log_to_file_and_speak("No valid command received, please try again.")
