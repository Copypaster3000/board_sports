#front.py

#This class will be the only class that interacts with users

import surf_report
import snow_report
import kite_report
import skate_report

class front():

    #gets session time window from user and returns it
    def get_session(self):
        time = []

        print("Hello, welcome to the board sports bot!\n")
        print("This program tells you the best board sport to do today for someone living in Portland, Oregon.\n")
        print("It compares conditions for surfing, snowboarding, kiteboarding, and skateboarding.\n")
        print("This program will ask you what time you'r interested in doing sports today and then tell you what sport is best for that time period based on the conditions.")
        print("Use integers to represent the hours of the day. For example if you want to start your session at 3:00 pm enter '15'.\n")
        print("First enter the time you would like your session to start then the time you would like to end your session.")
        time.append(self.get_time())
        time.append(self.get_time())
        print("\nYou entered that you're interested in a session from ", time[0], " to ", time[1])

        return time
    
    def get_time(self):
        while True: #loops until user enters acceptable data
            try:
                num = int(input("Type in the integer then press the enter key: "))
                
                if 0 <= num <= 24:
                    return num
                else:
                    print("Please enter an integer between 0 and 24.")

            except ValueError:
                print("Invalid entry, please enter an integer.")


    def return_surf_score(self, time):
        surf_object = surf_report.surf_report()

        return surf_object.return_surf_score(time) #Returns surf rating


    def return_snow_score(self, time):
        snow_object = snow_report.snow_report()

        return snow_object.return_snow_score(time)


    def return_kite_score(self, time):
        kite_object = kite_report.kite_report()
        
        return kite_object.return_kite_score(time)


    def return_skate_score(self, time):
        skate_object = skate_report.skate_report()

        return skate_object.return_skate_score(time)


    #Returns the sport in text that has the highest score
    def highest_score(self, surf_score, snow_score, kite_score, skate_score):
        highest_score = -100
        sport = ""

        if surf_score > highest_score:
            highest_score = surf_score
            sport = "surfing at Indian Beach, OR"
        if snow_score > highest_score:
            highest_score = snow_score
            sport = "snowboarding at Mt.Hood Meadows, OR"
        if kite_score > highest_score:
            highest_score = kite_score
            sport = "kiteboarding at Hood River, OR"
        if skate_score > highest_score:
            highest_score = skate_score
            sport = "skateboarding in Portland, OR"

        return sport