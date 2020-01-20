import carpgmenu
import carpg

# A list of all parts available for purchase and install
partslist = [
    'Engine - $12,000',
    'Transmission - $6000',
    'Brakes - $2000',
    'Exhaust - $500',
    'Suspension - $1000'
    ] 

# A list of all vehicles available for purchase
shopcarslist = [
    '1994 Mazda Miata R - $5100',
    '1991 Honda CRX SI - $6160',
    '2019 Volkswagen Golf GTI - $28,040'
    ]

class Shop:
    # A class which adds the shop functionality of the program
    def __init__(self, playercr):
        self.playercr = playercr
    def cars_shop(self):
        # Function which lets the user purchase additional vehicles
        for shopcar in shopcarslist:
            print(shopcar)
        response = input("Which car would you like to purchase? (input car name, lower case with spaces)\n")
        if response == '1994 mazda miata r':
            # Mazda Miata R
            response = input("Are you sure you would like to buy this car? (yes/no)\n")
            if response == 'yes':
                if self.playercr >= 5100:
                    self.playercr -= 5100
                    carpgmenu.carlist.append('1994 Mazda Miata R')
                    shopcarslist.remove('1994 Mazda Miata R - $5100')
                    print("You've successfully purchased a 1994 Mazda Miata R\n")
                    self.cars_shop()
                else:
                    print("You do not have enough money\n")
                    self.cars_shop()
            elif response == 'no':
                self.cars_shop()
        elif response == '1991 honda crx si':
            # Honda CRX SI
            response = input("Are you sure you would like to buy this car? (yes/no)\n")
            if response == 'yes':
                if self.playercr >= 6160:
                    self.playercr -= 6160
                    carpgmenu.carlist.append('1991 Honda CRX SI')
                    shopcarslist.remove('1991 Honda CRX SI - $6160')
                    print("You've successfully purchased a 1991 Honda CRX SI\n")
                    self.cars_shop()
                else:
                    print("You do not have enough money\n")
                    self.cars_shop()
            elif response == 'no':
                self.cars_shop()
        elif response == '2019 volkswagen golf gti':
            # VW Golf GTI
            response = input("Are you sure you would like to buy this car? (yes/no)\n")
            if response == 'yes':
                if self.playercr >= 28040:
                    self.playercr -= 28040
                    carpgmenu.carlist.append('2019 Volkswagen Golf GTI')
                    shopcarslist.remove('2019 Volkswagen Golf GTI - $28,040')
                    print("You've successfully purchased a 2019 Volkswagen Golf GTI\n")
                    self.cars_shop()
                else:
                    print("You do not have enough money\n")
                    self.cars_shop()
            elif response == 'no':
                self.cars_shop()
        elif response == 'back':
            carpgmenu.acmenu.autoshop()
        else:
            print("Invalid input\n")
            self.cars_shop()

    def parts_install(self):
        # Function which allows the user to purchase parts for their car(s)
        for part in partslist:
            print(part)
        response = input("Select which part you would like to purchase and install. (lowercase)\n")
        if response == 'engine':
            # Engine upgrade
            response = input("Are you sure you want to purchase and install this part? (yes/no)\n")
            if response == 'yes':
                if shop.playercr >= 12000:
                    partslist.remove('Engine - $12,000')
                    carpg.current.hrspr += 50
                    carpg.current.pr += 8
                    print("Part successfully installed.\n")
                    shop.playercr -= 12000
                    self.parts_install()
                else:
                    print("You don't have enough money\n")
                    self.parts_install()
            elif response == 'no':
                self.parts_install()
            else:
                print("Invalid input.\n")
                self.parts_install()
        elif response == 'transmission':
            # Transmission upgrade
            response = input("Are you sure you want to purchase and install this part? (yes/no)\n")
            if response == 'yes':
                if shop.playercr >= 6000:
                    partslist.remove('Transmission - $6000')
                    carpg.current.pr += 4
                    shop.playercr -= 6000
                    print("Part successfully installed.\n")
                    self.parts_install()
                else:
                    print("You don't have enough money\n")
                    self.parts_install()
            elif response == 'no':
                self.parts_install()
            else:
                print("Invalid input.\n")
                self.parts_install()
        elif response == 'brakes':
            # Brakes upgrade
            response = input("Are you sure you want to purchase and install this part? (yes/no)\n")
            if response == 'yes':
                if shop.playercr >= 2000:
                    partslist.remove('Brakes - $2000')
                    shop.playercr -= 2000
                    carpg.current.pr += 2
                    print("Part successfully installed.\n")
                    self.parts_install()
                else:
                    print("You don't have enough money\n")
                    self.parts_install()
            elif response == 'no':
                self.parts_install()
            else:
                print("Invalid input.\n")
                self.parts_install()
        elif response == 'exhaust':
            # Exhaust upgrade
            response = input("Are you sure you want to purchase and install this part? (yes/no)\n")
            if response == 'yes':
                if shop.playercr >= 500:
                    partslist.remove('Exhaust - $500')
                    shop.playercr -= 500
                    carpg.current.hrspr += 5
                    carpg.current.pr += 1
                    print("Part successfully installed.\n")
                    self.parts_install()
                else:
                    print("You don't have enough money\n")
                    self.parts_install()
            elif response == 'no':
                self.parts_install()
            else:
                print("Invalid input.\n")
                self.parts_install()
        elif response == 'suspension':
            # Suspension upgrade
            response = input("Are you sure you want to purchase and install this part? (yes/no)\n")
            if response == 'yes':
                if shop.playercr >= 1000:
                    partslist.remove('Suspension - $1000')
                    shop.playercr -= 1000
                    carpg.current.pr += 2
                    print("Part successfully installed.\n")
                    self.parts_install()
                else:
                    print("You don't have enough money\n")
                    self.parts_install()
            elif response == 'no':
                self.parts_install()
            else:
                print("Invalid input.\n")
                self.parts_install()
        elif response == 'back':
            carpgmenu.acmenu.autoshop()
        else:
            print("Invalid input.\n")
            self.parts_install()

shop = Shop(6000)
            
            
        
