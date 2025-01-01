import speech_recognition as sr
import pyttsx3
import pywhatkit
import wikipedia
import datetime
import pyautogui
import smtplib
from email.message import EmailMessage
import time

# Initialize the speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 0.9)

def speak(text):
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen_command():
    """Listen for a voice command and return the recognized text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"User said: {command}")
            return command
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            return ""

def wake_Jarvis():
    """Wait for the wake-up call: 'jarvis'."""
    while True:
        print("Waiting for wake-up call...")
        command = listen_command()
        if "jarvis" in command:
            speak("Yes sir.")
            return

def send_email(to_email, subject, body):
    """Send an email using Gmail SMTP."""
    your_email = "your_email@gmail.com"
    your_app_password = "your_app_password"

    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = your_email
    msg['To'] = to_email
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(your_email, your_app_password)
            server.send_message(msg)
        speak("Email has been sent successfully.")
    except Exception as e:
        speak(f"Failed to send the email. {e}")

def search_wikipedia(query):
    """Search Wikipedia."""
    speak(f"Searching Wikipedia for {query}")
    results = wikipedia.summary(query, sentences=2)
    speak(results)

def main():
    """Main function to run Jarvis"""
    while True:
        wake_Jarvis()  # Wait for "Jarvis" to be called
        while True:
            command = listen_command()

            if not command:
                break

            # Process the recognized command
            if "play" in command:
                song = command.replace("play", "").strip()
                speak(f"Playing {song} on YouTube")
                pywhatkit.playonyt(song)

            elif "search wikipedia" in command:
                speak("What do you want to search on Wikipedia?")
                search_query = listen_command()
                if search_query:
                    search_wikipedia(search_query)

            elif "send email" in command:
                speak("Who is the recipient?")
                recipient = input("Enter recipient email: ")
                speak("What is the subject?")
                subject = listen_command()
                speak("What should be the body of the email?")
                body = listen_command()
                send_email(recipient, subject, body)

            elif "screenshot" in command:
                screenshot = pyautogui.screenshot()
                file_name = f"screenshot_{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}.png"
                screenshot.save(file_name)
                speak("Screenshot taken and saved.")
            elif "what is" in command:
                query = command.replace("what is", "").strip()
                speak(f"Searching Wikipedia for {query}")
                results = wikipedia.summary(query, sentences=2)
                speak(results)

            elif "who is" in command:
                query = command.replace("who is", "").strip()
                speak(f"Searching Wikipedia for {query}")
                results = wikipedia.summary(query, sentences=2)
                speak(results)

            elif "where is" in command:
                query = command.replace("where is", "").strip()
                speak(f"Searching Wikipedia for {query}")
                results = wikipedia.summary(query, sentences=2)
                speak(results)

            elif "open" in command:
                open_app = command.replace("open", "").strip()
                open_app(open_app)

            elif "close" in command:
                app_name = command.replace("close", "").strip()
                close_app(app_name)

            elif "remember" in command:
                key = command.replace("remember", "").strip()
                speak("What should I remember?")
                value = listen_command()
                remember_memory(key, value)

            elif "time" in command:
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                speak(f"The current time is {current_time}")

            elif "date" in command:
                current_date = datetime.datetime.now().strftime("%B %d, %Y")
                speak(f"The current date is {current_date}")

            elif "joke" in command:
                joke = pywhatkit.joke()
                speak(joke)

            elif "news" in command:
                news = pywhatkit.news()
                speak(news)

            

            elif "open" in command:
                app_name = command.replace("open", "").strip()
                open_app(app_name)

            elif "close" in command:
                app_name = command.replace("close", "").strip()
                close_app(app_name)

            elif "remember" in command:
                key = command.replace("remember", "").strip()
                speak("What should I remember?")
                value = listen_command()
                remember_memory(key, value)

            elif "recall" in command:
                key = command.replace("recall", "").strip()
                value = recall_memory(key)
                speak(f"You asked me to remember {key}. The answer is {value}")

            elif "calculate" in command:
                expression = command.replace("calculate", "").strip()
                result = eval(expression)
                speak(f"The result is {result}")

            elif "translate" in command:
                text = command.replace("translate", "").strip()
                translated_text = translate(text)
                speak(translated_text)
            elif "alarm" in command:
                time_str = command.replace("alarm", "").strip()
                set_alarm(time_str)

            elif "check social media" in command:
                check_social_media()

            elif "Article" in command:
                article = command.replace("Article", "").strip()
                speak(f"Searching for {article} on Wikipedia")
                search_wikipedia(article)

            elif "search" in command:
                query = command.replace("search", "").strip()
                speak(f"Searching for {query} on YouTube")
                pywhatkit.playonyt(query)

            elif "ChatGpt" in command:
                prompt = command.replace("ChatGpt", "").strip()
                answer = chatgpt(prompt)
                speak(answer)

            elif "exit" in command or "stop" in command:
                speak("Goodbye, sir!")
                return  # Exit the entire program

            speak("Waiting for your next command.")
            break  # Stop listening until "Jarvis" is called again

if __name__ == "__main__":
    main()
