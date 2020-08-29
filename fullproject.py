# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 21:21:27 2020

@author: SREERAM S
"""

from flask import Flask

from googletrans import Translator
import speech_recognition as sr 
import pyttsx3

from textblob import TextBlob
import emoji
import nltk

nltk.download('punkt')
app = Flask(__name__)

p = -1
q = -0.5
r = 0
s =  0.8
t = 1

@app.route('/') 

def hack():
    
    r = sr.Recognizer()
    command = None
    engine = pyttsx3.init()
    engine.say(command)
    engine.runAndWait() 
    while(1):  
        
        try: 
            
            with sr.Microphone() as source2:
                 r.adjust_for_ambient_noise(source2, duration=0.2) 
                 audio2 = r.listen(source2) 
                 
                 MyText = r.recognize_google(audio2)
                 MyText = MyText.lower() 
                 
                 print("Did you say "+MyText) 
                 SpeakText(MyText) 
                 translator = Translator()
                 test = translator.translate(MyText)
                 print(test)
                 
                 y = test
                 sen = TextBlob(y)
                 x = sen.sentiment.polarity
                 x = float(x)
                 print(x)
                 
                 print("\n")
                 if x<q and x>=p:
                     print("Worst")
                     print(emoji.emojize(":angry_face:"))
                 elif x>=q and x<r:
                    print("Not Satisfactory")
                    print(emoji.emojize(":face_with_steam_from_nose:"))
                 elif x==r:
                    print("Moderate")
                    print(emoji.emojize(":neutral_face:"))
                 elif x>r and x<=s:
                    print("Satisfactory")
                    print(emoji.emojize(":slightly_smiling_face:"))
                 elif x>s and x<=t:
                    print("Good and Happy")
                    print(emoji.emojize(":beaming_face_with_smiling_eyes:"))
                
                 res = len(y.split())
                 print("\n")
                 print("total No. of words:\n",str(res))
                 print("The Word Counts:\n",sen.word_counts)
                 print("The words are :\n",sen.words)
                 print("The Sentences are :\n",sen.sentences)
            
        except sr.RequestError as e: 
            print("Could not request results; {0}".format(e))
            
        except sr.UnknownValueError:
            print("unknown error occured") 
                
    return render_template("hackindex.html")
    

if __name__ == '__main__': 
   app.run(debug = True) 
    
    