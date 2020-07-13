import speech_recognition as sr 
from gtts import gTTS
import sqlite3
import os
import pandas as pd
from sqlalchemy import create_engine
import os

# os.chdir('')
def create_db(db_name):
    db = sqlite3.connect(db_name,timeout=100)
    c= db.cursor()
    try:
        data = pd.read_excel('database_excel.xlsx')
        try:
            c.execute('''CREATE TABLE response_table({} text primary key asc,{} text)'''.format(data.columns[0],data.columns[1]))
        except:
            print('data base is already exist')
        data_list = [tuple(data.iloc[x,:]) for x in range(len(data))]
        for i in data_list:
            try:
                c.execute("insert into response_table values (?,?)",i)
            except:
                print('response is already exist')
        db.commit()
        c.close()
        engine = create_engine('sqlite:///database.db')
        return True,engine
    except  Exception  as ex:
        print(ex)
        return False,' '
        
        
    
def fetc_data(text,engine):
    read_data = pd.read_sql('select Response from response_table where Input == "{}"'.format(text),engine)
    if len(read_data == 1):
        return True,read_data.Response.values[0]
    else:
        return False,0

def SpeakText(command):    
    # Initialize the engine 
    engine = pyttsx3.init() 
    engine.say(command)  
    engine.runAndWait()

def main():
    db_name = 'database.db'
    print('database create')
    db_flag,engine = create_db(db_name)
    
    while db_flag:
        
        r = sr.Recognizer() 
        with sr.Microphone() as source: 
        #wait for a second to let the recognizer adjust the  
        #energy threshold based on the surrounding noise level 
            r.adjust_for_ambient_noise(source) 
            print("Say Something")
            #listens for the user's input 
            audio = r.listen(source) 

            try: 
                text = r.recognize_google(audio)
                print ("you said: " + text )
                find_flag,mytext = fetc_data(text,engine) 
                if find_flag:
                    SpeakText(mytext)
                    print(mytext)
                    
                else:
                    print ("There is no response for this in '{}' database : ".format(text))
                break

            #error occurs when google could not understand what was said 

            except sr.UnknownValueError: 
                print("Google Speech Recognition could not understand audio, say again")
            

    else:
        print('error while creating databse')
        
if __name__ == '__main__':
    main()
        