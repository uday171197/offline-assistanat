import speech_recognition as sr

def SpeakText(command):
    """This is a function that convert the text to speech .

    Parameters
    ----------
    command : str
        This is the response text that we want to convert text to speech.

    Returns
    -------
    type
        Description of returned object.

    """
    # Initialize the engine
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait()

def main():
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            #wait for a second to let the recognizer adjust the
            #energy threshold based on the surrounding noise level
            r.adjust_for_ambient_noise(source)
            print("Say Something")
            SpeakText("Say Something")
            #listens for the user's input
            audio = r.listen(source)
            try:
#                 text = r.recognize_google_cloud(audio)
                text = r.recognize_google(audio)
                print ("you said: " + text )
                SpeakText("you said: " + text)
                if text == 'what is your name':
                # The text that you want to convert to audio
                    mytext = 'My name is Uday'
                    SpeakText(mytext)
                    print(mytext)
                    break
                if text == 'hello':
                # The text that you want to convert to audio
                    mytext = 'hello sir'
                    SpeakText(mytext)
                    print(mytext)
                    break
                if text == 'how are you':
                # The text that you want to convert to audio
                    mytext = 'i am fine'
                    SpeakText(mytext)
                    print(mytext)
                    break
            #error occurs when google could not understand what was said

            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")


if __name__ == '__main__':
    main()
