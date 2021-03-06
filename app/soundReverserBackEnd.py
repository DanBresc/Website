import pyaudio
import wave
import time
from flask import render_template, flash, redirect
import os.path

def reverseSound(seconds):
    
    chunk = 1024 # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16 bits per sample
    channels = 2
    fs = 44100  # Record at 44100 samples per second
    
    #path = os.path.join("static", "WaveFiles")
    
    #filename = os.path.join(path, "output.wav")
    path0 = os.path.join("app","Static")
    path1 = os.path.join(path0,"WaveFiles")
    filename = os.path.join(path1,"output.wav")
    
    #filename = "output.wav" THIS WORKED DON"T SCREW IT YET
    
    p = pyaudio.PyAudio()  # Create an interface to PortAudio

    

    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    frames_per_buffer=chunk,
                    input=True)

    frames = []  # Initialize array to store frames

    # Store data in chunks for 3 seconds
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.insert(0,data)

    # Stop and close the stream 
    stream.stop_stream()
    stream.close()
    # Terminate the PortAudio interface
    p.terminate()

   

    # Save the recorded data as a WAV file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()


def playSound():
    #Play the Sound
    # Set chunk size of 1024 samples per data frame
    chunk = 1024  
    path0 = os.path.join("app","Static")
    path1 = os.path.join(path0,"WaveFiles")
    filename = os.path.join(path1,"output.wav")
    
    # Open the sound file 
    wf = wave.open(filename, 'rb')

    # Create an interface to PortAudio
    p = pyaudio.PyAudio()

    # Open a .Stream object to write the WAV file to
    # 'output = True' indicates that the sound will be played rather than recorded
    stream = p.open(format = p.get_format_from_width(wf.getsampwidth()),
                    channels = wf.getnchannels(),
                    rate = wf.getframerate(),
                    output = True)

    # Read data in chunks
    data = wf.readframes(chunk)


    
    # Play the sound by writing the audio data to the stream
    
    while data:
        stream.write(data)
        data = wf.readframes(chunk)
        
    # Close and terminate the stream
    stream.close()
    p.terminate()
    