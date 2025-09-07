import pyttsx3
def speak_text(text):
    engine = pyttsx3.init()
    engine.say("start")    
    engine.say(text)
    engine.runAndWait()
def announcement(train_number,from_station,to_station,dicplat_no_o,lug):
    if(lug==1):
        if train_number and from_station and to_station:
            text = (f"Attention please. Train number {train_number}, {from_station} Express "
                f"from {from_station}  to {to_station}, is arriving shortly on platform number {dicplat_no_o}. "
                f"Passengers are requested to stand behind the yellow line and mind the gap. Thank you.")
            speak_text(text)
    elif(lug==2):
        if train_number and from_station and to_station:
            text = (f"कृपया ध्यान दें। ट्रेन नंबर {train_number}, {from_station} एक्सप्रेस "
                f"{from_station} से {to_station} जा रही है, जो कुछ ही समय में प्लेटफॉर्म नंबर {dicplat_no_o} पर आने वाली है। "
                f"कृपया पीली रेखा के पीछे खड़े रहें और सावधानी बरतें। धन्यवाद।")
            speak_text(text)
    else:
        print("Not abale to speak")
        print("Invalid input. Please check your indices.")
'''def main():
    dicnum = {1: 123, 2: 321, 3: 456, 4: 654}
    dic1 = {1: "Ahmedabad", 2: "Baroda"}
    dic2 = {1: "Surat", 2: "Rajkot"}
    dicplat={1:1,2:2,3:3,4:4}
    num = int(input("Enter train index (1 to 4): "))
    dic1_from = int(input("Enter 'from' location index (1 or 2): "))
    dic2_to = int(input("Enter 'to' location index (1 or 2): "))
    dicplat_no=int(input("Enter platform number(1 to 4):"))
    lug=int(input("Enter lunguage:"))
    train_number = dicnum.get(num)
    from_station = dic1.get(dic1_from)
    to_station = dic2.get(dic2_to)
    dicplat_no_o=dicplat.get(dicplat_no)
    announcement(train_number,from_station,to_station,dicplat_no_o,lug)
main()
'''
def main():
    dicnum = {1: 123, 2: 321, 3: 456, 4: 654}
    dic1 = {'ahm': "Ahmedabad", 'bar': "Baroda"}
    dic2 = {'sur': "Surat", 'raj': "Rajkot"}
    dicplat = {1: 1, 2: 2, 3: 3, 4: 4}

    try:
        num = int(input("Enter train index (1 to 4): "))
        dic1_from = input("Enter 'from' station code (e.g., ahm, bar): ").lower()
        dic2_to = input("Enter 'to' station code (e.g., sur, raj): ").lower()
        dicplat_no = int(input("Enter platform number (1 to 4): "))
        lug = int(input("Enter luggage count: "))

        train_number = dicnum.get(num, "Unknown Train")
        from_station = dic1.get(dic1_from, "Unknown Station")
        to_station = dic2.get(dic2_to, "Unknown Station")
        platform_number = dicplat.get(dicplat_no, "Unknown Platform")

        announcement(train_number, from_station, to_station, platform_number, lug)
    except:
        pass
main()

