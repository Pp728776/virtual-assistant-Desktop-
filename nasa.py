import requests
import os
from PIL import Image
import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()

Api_key ='ZSrmcZ3Bz2fQNHWmmehTnHYlRpgTQJuuu07K1ENZ'
def NasaNews(Date):
    speak("Extracting Data from Nasa .")
    print("Extracting Data from Nasa .")
    url = "https://api.nasa.gov/planetary/apod?api_key=" + str(Api_key)
    Params = {'date':str(Date)}
    r = requests.get(url,params = Params)
    Data = r.json()

    Info = Data['explanation']
    Title =  Data['title']
    Image_url = Data['url']
    Image_r = requests.get(Image_url)
    FileName = str(Date) + '.jpg'
    print(FileName)
    with open(FileName,'wb') as f:
        f.write(Image_r.content)

    img = Image.open(FileName)
    img.show()
    speak(f"Title: {Title}")
    print(f"Title: {Title}")
    speak(f"According to nasa : {Info}")
    print(f"According to nasa : {Info}")






