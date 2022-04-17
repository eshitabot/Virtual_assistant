import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import webbrowser
import os
import smtplib







engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')
engine.setProperty('voices',voices[0].id)

engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',rate-90)






def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def wishMe():
    hour=int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("GOOD MORNING !!!!!!!!!!")
    elif hour>=12 and hour<18:
        speak("GOOD AFTERNOON !!!!!!!!!!!!")
    else:
        speak("GOOD EVENING")
    speak("Hye I am karen  How can i help you")


def takeCommand():
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening!!!!!!!!!!!!!!!!!!!")
        r.pause_threshold=1
        audio = r.listen(source)



    try:
        print("RECOGNISING..")
        query = r.recognize_google(audio,language='en-in')
        print(f"User said:{query}\n")


    except Exception as e:
        print("say that again please")
        return"NONE"
    return query
def sendEmail(to,content):
    server=smtplib.SMTP('smtp,gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('your email', 'password')
    server.sendmail('to whom you want to send mail id',to, content)
    server.close()




if __name__=="__main__":

    wishMe()
    while True:
        query=takeCommand().lower()
        if 'wikipedia' in query:
            speak("searching wikipedia!!!!!!!!")
            query=query.replace("wikipedia"," ")
            results=wikipedia.summary(query,sentences=2)
            speak("according to wikipedia")
            print(results)
            speak(results)
        elif 'open youtube' in query:
            speak("opening youtube just wait")
            webbrowser.open("youtube.com")
        elif 'open facebook' in query:
            speak("opening facebook just wait")
            webbrowser.open("facebook.com")
        elif 'open google' in query:
            speak("opening google please wait ")
            webbrowser.open("google.com")
        elif 'open blogger' in query:
            speak("opening blogger please wait")
            webbrowser.open("blogspot.com")
        elif 'open quora' in query:
            speak("opening quora please wait")
            webbrowser.open("quora.com")
        elif 'open udemy' in query:
            speak("please wait opening udemy")
            webbrowser.open("udemy.com")
        elif 'open stackoverflow' in query:
            speak("opening please wait")
            webbrowser.open("stackoverflow.com")
        elif 'open hackersrank' in query:
            speak("opening please wait")
            webbrowser.open("hackerrank.com")
        elif 'open codechef' in query:
            speak("opening please wait")
            webbrowser.open("codechef.com")
        elif 'open nptel swayam' in query:
            speak("opening please wait")
            webbrowser.open("swayam.gov.in")
        elif 'open jeexams' in query:
            speak("opening please wait!!!!")
            webbrowser.open("jeexams.blogspot.com")
        elif 'play music' in query:
            music_dir='D:\\songs'
            songs=os.listdir(music_dir)
            print("songs")
            os.startfile(os.path.join(music_dir,songs[0]))
        elif 'play movies' in query:
            movie_dir='D:\\movies'
            movies=os.listdir(movie_dir)
            print("movies")
            os.startfile(os.path.join(movie_dir,movies[7]))

        elif 'the time' in query:
            strTime=datetime.datetime.now().strftime("%H;%M;%S")
            speak(f"Sir the time is{strTime}")
        elif 'email to ishita' in query:
            try:
                speak("what should i say")
                content=takeCommand()
                to="email of whom u want to send"
                sendEmail(to,content)
                speak("email has been send")
            except Exception as e:
                print(e)
                speak("sorry i cant do the task")

