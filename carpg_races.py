import carpg
import carpgmenu
import carpg_autoshop
import random

class Race:
    # A class that grants the race functionality
    def __init__(self, totaltime):
        self.totaltime = totaltime

    def racestart(self):
        # Start of the race
        if carpg.current == '':
            print("You don't have a car to race with\n")
            carpgmenu.acmenu.main()
        else:
            print ("START!\n")
            self.corner1()

    def corner1(self):
        # Corner 1 data
        response = input("You accelerate through the starting line. There is an easy left corner approaching. Take it fast (risky) or slow (safe)?\n")
        risky_corner = random.randint(1, 6)
        if response == 'safe':
            self.totaltime += 1
            self.corner2()
        elif response == 'risky':
            if risky_corner == 6:
                self.crash()
            else:
                self.totaltime -= 1
                self.corner2()
        else:
            print("Invalid input\n")
            self.corner1()

    def corner2(self):
        # Corner 2 data
        response = input("You exit turn 1. There is a medium right corner approaching. Take it fast (risky) or slow (safe)?\n")
        risky_corner = random.randint(1, 6)
        if response == 'safe':
            self.totaltime += 1
            self.corner3()
        elif response == 'risky':
            if risky_corner == 5 or 6:
                self.crash()
            else:
                self.totaltime -= 1
                self.corner3()
        else:
            print("Invalid input\n")
            self.corner2()

    def corner3(self):
        # Corner 3 data
        response = input("You exit turn 2. There is a 90 degree left corner approaching. Take it fast (risky) or slow (safe)?\n")
        risky_corner = random.randint(1, 6)
        if response == 'safe':
            self.totaltime += 1
            self.corner4()
        elif response == 'risky':
            if risky_corner == 4 or 5 or 6:
                self.crash()
            else:
                self.totaltime -= 1
                self.corner4()
        else:
            print("Invalid input\n")
            self.corner3()

    def corner4(self):
        # Corner 4 data
        response = input("You exit turn 3. There is fast left corner approaching. Take it fast (risky) or slow (safe)?\n")
        risky_corner = random.randint(1, 6)
        if response == 'safe':
            self.totaltime += 1
            self.corner5()
        elif response == 'risky':
            if risky_corner == 6:
                self.crash()
            else:
                self.totaltime -= 1
                self.corner5()
        else:
            print("Invalid input\n")
            self.corner4()

    def corner5(self):
        # Corner 5 data
        response = input("You exit turn 4. There is a narrow hairpin right corner approaching. Take it fast (risky) or slow (safe)?\n")
        risky_corner = random.randint(1, 6)
        if response == 'safe':
            self.totaltime += 1
            self.race_end()
        elif response == 'risky':
            if risky_corner == 3 or 4 or 5 or 6:
                self.crash()
            else:
                self.totaltime -= 1
                self.race_end()
        else:
            print("Invalid input\n")
            self.corner5()

    def race_end(self):
        # End of race data, payments, etc.
        print(f"Your time was {self.totaltime} seconds.\n")
        placement = 1
        opponent1time = random.randint(57, 59)
        opponent2time = random.randint(59, 62)
        if opponent1time <= self.totaltime:
            placement += 1
        elif opponent2time <= self.totaltime:
            placement += 1
        if placement == 1:
            print("You placed 1st. You recieved 1000 Credits.\n")
            carpg_autoshop.shop.playercr += 1000
            carpgmenu.acmenu.main()
        elif placement == 2:
            print("You placed 2nd. You recieved 500 Credits.\n")
            carpg_autoshop.shop.playercr += 500
            carpgmenu.acmenu.main()
        elif placement == 3:
            print("You placed 3rd. You recieved 250 Credits.\n")
            carpg_autoshop.shop.playercr += 250
            carpgmenu.acmenu.main()

    def crash(self):
        # Crash data
        print("You crashed. You recieve a DNF and your car is totalled. You must pay 250 Credits in repairs.\n")
        carpg_autoshop.shop.playercr -= 250
        carpgmenu.acmenu.main()

# Initial race times based on PR of current vehicle
pr20 = Race(60)
pr22 = Race(59.5)
pr24 = Race(59)
pr26 = Race(58.5)
pr28 = Race(58)
pr30 = Race(57.5)
    
