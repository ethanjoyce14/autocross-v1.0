import carpg
import carpg_races
import carpg_autoshop

# Main menu options
mainmenu = [
    'Race',
    'Garage',
    'Autoshop',
    'Quit']

# List of currently available cars
carlist = [
    '2002 Honda Civic SI'
    ]

# List of currently available tracks
tracklist = [
    'Parking Lot'
    ]

# List of autoshop functionalities
options = [
    'Cars',
    'Parts'
    ]

class Menu:
    # Class which grants a main menu functionality
    def __init__(self, enable):

        self.enable = enable

    def main(self):
        # Main menu data
        print(f"\nAUTOCROSS:\n")
        
        for index, value in enumerate(mainmenu, 1):
            print("\t{}. {}".format(index, value))
        
        response = input("\nInput a number to select.\n")
        
        if response == '1':
            print("Race menu has been selected.\n")
            self.race()
        
        elif response == '2':
            print("Garage has been selected.\n")
            self.garage()
        
        elif response == '3':
            print("Autoshop has been selected.\n")
            self.autoshop()
        
        elif response == '4':
            quit()
        
        else:
            print("I didn't understand that.\n")
            self.main()


    def garage(self):
        # Garage menu data, vehicle selection
        print("GARAGE:\n")

        for car in carlist:
            print(car)
        
        response = input("\nWhich car would you like to drive? (inputs must be lowercase, with spaces)\n")
        
        if response == '2002 honda civic si':
            carpg.current = carpg.honda_civic_si_2002
            print(carpg.current.carstats())
            self.main()

        elif response == '1994 mazda miata r':
            if '1994 Mazda Miata R' in carlist:
                carpg.current = carpg.mazda_miata_r_1994
                print(carpg.current.carstats())
                self.main()
            else:
                print("You do not have this car yet\n")
                self.garage()
        
        elif response == '1991 honda crx si':
            if '1991 Honda CRX SI' in carlist:
                carpg.current = carpg.honda_crx_si_1991
                print(carpg.current.carstats())
                self.main()
            else:
                print("You do not have this car yet\n")
                self.garage()
        
        elif response == '2019 volkswagen golf gti':
            if '2019 Volkswagen Golf GTI' in carlist:
                carpg.current = carpg.volkswagen_golf_gti_2019
                print(carpg.current.carstats())
                self.main()
            else:
                print("You do not have this car yet\n")
                self.garage()
        elif response == 'back':
            self.main()
        else:
            print("I didn't understand that.\n")
            self.garage()

    def race(self):
        # Race menu data leading to race start
        print("TRACKS:\n")
        
        for index, value in enumerate(tracklist, 1):
            print("\t{}. {}".format(index, value))
        
        response = input("\nPlease select a track (input number)\n")
        
        if response == '1':
            if carpg.current.pr == 20 or 21:
                carpg_races.pr20.racestart()
            elif carpg.current.pr == 22 or 23:
                carpg_races.pr22.racestart()
            elif carpg.current.pr == 24 or 25:
                carpg_races.pr24.racestart()
            elif carpg.current.pr == 26 or 27:
                carpg_races.pr26.racestart()
            elif carpg.current.pr == 28 or 29:
                carpg_races.pr28.racestart()
            else:
                carpg_races.pr30.racestart()
        elif response == 'back':
            self.main()

        else:
            print("I didn't understand that\n")
            self.race()

    def autoshop(self):
        # Autoshop menu data, current Credits, options leading to auto shops
        print("AUTOSHOP:\n")
        print(f"You currently have {carpg_autoshop.shop.playercr} Credits. You are currently driving your {carpg.current.cardesc()}.\n")
        for index, value in enumerate(options, 1):
            print("\t{}. {}".format(index, value))
        response = input("Which menu would you like to access?\n")
        if response == '1':
            carpg_autoshop.shop.cars_shop()
        elif response == '2':
            carpg_autoshop.shop.parts_install()
        elif response == 'back':
            self.main()
        else:
            print("Invalid input\n")
            self.autoshop()

acmenu = Menu(1)
