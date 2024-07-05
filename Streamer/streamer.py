from tkinter import *
import speech_recognition as sr
import pyttsx3 as tts

root = Tk()
root.title("Streamer")
icon = PhotoImage(file="img/8103873.png")
root.iconphoto(True, icon)
root.geometry("500x500")
root.resizable(False,False)

text_box = Text(root, height = 5, width = 52, font=("Helvetica", 10))
text_box.pack()

# Function to listen and recognize the voice
def start_speech():
    # Initiate the recognizer
    reco = sr.Recognizer()
    
    with sr.Microphone() as source:
        # let the recognizer adjust the energy threshold based on the surrounding noise level
        reco.adjust_for_ambient_noise(source, duration=0.2)
        # takes the original voice
        print("Speak, am listening")
        audio = reco.listen(source, timeout=10)
        print("Processing")

        # use Google Web Speech API to convert the audio to text
        text = reco.recognize_google(audio).lower()
        if text is not None:
            print(f"Did you say: {text}")
            text_box.insert("1.0", text)
        else: 
            print("There is somthing wrong")
        
# Function to convert the recognized text to speech
def convert_speech():
    # Initialize the engine
    engine = tts.init()
    input = text_box.get("1.0", END)    
    engine.say(input)
    engine.runAndWait()
    # to delete
    text_box.delete(0, END)

def quit_speech():
    root.destroy() 

speak_button = Button(root, text="Start", command= start_speech)
speak_button.pack(pady=10)

convert_button = Button(root, text="Convert", command= convert_speech)
convert_button.pack(pady=10)

quit_button = Button(root, text="Quit", command= quit_speech)
quit_button.pack(pady=10)

root.mainloop()