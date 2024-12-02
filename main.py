import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
import datetime
import wikipedia
import google.generativeai as genai
import re
import warnings
warnings.simplefilter("ignore")

recognizer = sr.Recognizer()
engine = pyttsx3.init()
speed = engine.setProperty('rate', 170) # Set the speed of the engine
gemini_api_key = "Your_Api_Key"  # Replace with your actual Google API key
generation_config ={"temperature": 0.5}

running = True

def speak(text):
    engine.say(text)
    engine.runAndWait()

def aiProcess(command):
    genai.configure(api_key=gemini_api_key)
    model=genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    system_instruction="You are a virtual assistant named Jarvis, designed to assist users with a wide range of tasks, including answering questions and performing general-purpose actions similar to Alexa and Google Assistant. Your responses should be clear, concise, and helpful, adapting to the user's needs while maintaining a friendly and professional tone.")
    response = model.generate_content(command)
    cleaned_text = re.sub(r'\*+', '', response.text)

    return cleaned_text

def get_weather(city):
    # Get weather data from OpenWeatherMap API
    api_key = "You_Api_Key" # Replace with your actual OpenWeatherMap API Key
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        # Extract relevant information from the JSON object
        temp = round(data['main']['temp'])
        feels_like_temp = round(data['main']['feels_like'])
        description_weather=data["weather"][0]["description"]

         # Speak out the weather information for the given city
        speak(f"The current temperature in {city} is {temp} degrees Celsius, but it feels like {feels_like_temp} degrees Celsius. The sky is currently described as {description_weather}.")
    else:
        speak("Sorry, I could not retrieve weather information for that city.")

def processCommand(c):
    global running
    if "open google" in c.lower():
        webbrowser.open("https://www.google.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://www.youtube.com")
    elif "open facebook" in c.lower():
        webbrowser.open("https://www.facebook.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://www.linkedin.com")
    elif "open tiktok" in c.lower():
        webbrowser.open("https://www.tiktok.com")
    elif "open twitter" in c.lower():
        webbrowser.open("https://www.twitter.com")
    # If another website then it will open the url:
    elif "open" in c.lower():
        website = c.lower().split(" ")[1]
        webbrowser.open(f"https://www.{website}.com")

    elif c.lower().startswith("play"):
        song = c.lower()[len("play "):].strip()  # Check for any extra spaces
        print("Extracted song name:", song)  # Add this line for debugging
        link = musicLibrary.music.get(song)
        if link:
            webbrowser.open(link)
        else:
            print("Song not found in the music library")

    elif "time" in c.lower():
        now = datetime.datetime.now()
        current_time = now.strftime("%I:%M:%S %p")
        speak(f"The time is {current_time}")

    elif "wikipedia" in c.lower():
        speak("What do you want to search on Wikipedia?")
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
            search_query = recognizer.recognize_google(audio)
            try:
                summary = wikipedia.summary(search_query, sentences=2)
                speak(summary)
            except wikipedia.exceptions.DisambiguationError as e:
                speak("There are multiple results for this query. Please be more specific.")
            except wikipedia.exceptions.PageError:
                speak("The page does not exist on wikipedia")
            except Exception as e:
                speak("An error occurred while searching Wikipedia.")

    elif "weather" in c.lower():
        speak("Which city do you want the weather for?")
        with sr.Microphone() as source:
             audio = recognizer.listen(source)
             city = recognizer.recognize_google(audio)
             get_weather(city)

    elif "search on google" in c.lower():
        speak("What do you want to search on Google?")
        with sr.Microphone() as source:
             audio = recognizer.listen(source)
             search_query = recognizer.recognize_google(audio)
             url = "https://www.google.com/search?q={}".format(search_query.replace(' ', '+'))
             webbrowser.get().open(url)
    
    elif "search on youtube" in c.lower():
        speak("What do you want to search on YouTube?")
        with sr.Microphone() as source:
            audio = recognizer.listen(source)
            search_query = recognizer.recognize_google(audio)
            url = "https://www.youtube.com/results?search_query={}".format(search_query.replace(' ', '+')).lower()
            webbrowser.get().open(url)

    elif "exit" in c.lower():
        speak("Goodbye!")
        running = False

    else:
        # Let gemini handle the request:
        output = aiProcess(c)
        speak(output)


if __name__ == "__main__":
    speak("Initializing Jarvis......")
    while running:
        # Listen for the wake word "Jarvis"
        # obtain audio from the microphone
        r = sr.Recognizer()
        
        print("Recognizing...")
        try:
            with sr.Microphone() as source:
                print("Listening for wake word...")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Yes, how can I help you?")
                # Listen for command:
                with sr.Microphone() as source:
                    print("Listening for command...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)

                    processCommand(command)
        except Exception as e:
            print("Error; {0}".format(e))
        except KeyboardInterrupt as k:
            print( "Keyboard Interrupted")
            running = False