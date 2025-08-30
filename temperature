import requests
import pyttsx3

def speak_text(text,city):
    engine = pyttsx3.init()
    
    engine.say(f"You Enter{city} Temperature is")
    engine.say(text)
    engine.say("Degrees Celsius")
    engine.runAndWait()
    
def main():
    api_key = "ee537900e6312a194b4175aa6e96262f"  
    city = input("Enter the name of the city\n")
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()   
        print(data)  
        a=int(round(data["main"]["temp"]))
        speak_text(a,city)
        
        if "main" in data:
            print("Temperature:",a , "°C")
        else:
            print("No 'main' key found in response")
    else:
        print("Error fetching data:", response.status_code, response.text)
        
main()
