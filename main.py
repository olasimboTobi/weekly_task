from data import FORMAT,resources
import sys
logo = '''
 ______      _            _                ______              _     _             
(_____ \    (_)      _   (_)              |  ___ \            | |   (_)            
 _____) )___ _ ____ | |_  _ ____   ____   | | _ | | ____  ____| | _  _ ____   ____ 
|  ____/ ___) |  _ \|  _)| |  _ \ / _  |  | || || |/ _  |/ ___) || \| |  _ \ / _  )
| |   | |   | | | | | |__| | | | ( ( | |  | || || ( ( | ( (___| | | | | | | ( (/ / 
|_|   |_|   |_|_| |_|\___)_|_| |_|\_|| |  |_||_||_|\_||_|\____)_| |_|_|_| |_|\____)
                                 (_____|                                           

'''
print(logo)

class Printer:
    def __init__(self):
        self.price_coloured = FORMAT["coloured"]["price"]
        self.price_grayscale = FORMAT["greyscale"]["price"]
        self.coloured_per_paper= FORMAT["coloured"]['materials']['paper']
        self.grayscale_per_paper= FORMAT["greyscale"]['materials']['paper']
        self.coloured_per_ink = FORMAT["coloured"]['materials']['ink']
        self.grayscale_per_ink =FORMAT["greyscale"]['materials']['ink']
        self.ink_available = resources["ink"]
        self.paper_available = resources["paper"]
        self.input_amount = 0
        self.amount = 0
        self.num_of_pages = 0
        self.profit = 0
        self.Biyar = 5
        self.Faiba = 10
        self.Muri =20
        self.Wazobia = 50
        self.Wazobia_notes=0
        self.Muri_notes=0
        self.Biyar_notes = 0
        self.Faiba_notes= 0
        self.mode = "ON"
        self.format1 = ""


    def mode1(self): 
        try:
            confirm1 = input("Do you want to switch-off the printer? (yes or no): ").lower()

            if confirm1 == 'yes':
                exit('Thank you')
            elif confirm1 == 'no':
                self.input_format()
            else:
                raise Exception
        except Exception:
            print('Invalid input,try again')
            self.mode1()



    def report_print(self):
        print(f" \n\'''resources\n paper:{self.paper_available}pc\n ink:{self.ink_available}ml\n profit:#{self.profit}\n \''' ")      
        self.input_format()

    def print_user(self):
        print(f"Here is your Project and thanks you for using our services")
        self.input_format()

    def check_transaction(self, input_amount):
        print(self.num_of_pages)
        if self.format1 == "coloured":
            self.amount = (self.num_of_pages * self.price_coloured)
            print(self.price_coloured)
            print(self.amount)
            if self.amount == input_amount:
                self.paper_available = (self.paper_available - self.num_of_pages)
                self.ink_available = (self.ink_available - (self.coloured_per_ink * self.num_of_pages))
                self.profit +=  self.amount
                #print user's job
            elif self.amount > input_amount:
                print("Sorry that's not enough money. Money refunded")
                # restart
                self.input_format()

            elif self.amount < input_amount:
                # give change
                print(f"Here is { input_amount - self.amount} Naira in change")
                # process resources
                self.paper_available = (self.paper_available - self.num_of_pages)
                self.ink_available = (self.ink_available - (self.coloured_per_ink * self.num_of_pages))
                self.profit +=  self.amount
                #print user's job


        elif self.format1 == "grayscale":
            print(self.num_of_pages)
            self.amount = (self.num_of_pages * self.price_grayscale)

            if self.amount > input_amount:
                return("Sorry that's not enough money. Money refunded")
                # restart
                self.input_format()
            elif self.amount == input_amount:
                self.paper_available = (self.paper_available - self.num_of_pages)
                self.ink_available = (self.ink_available - (self.coloured_per_ink * self.num_of_pages))
                self.profit +=  self.amount
                 #print user's job

            elif self.amount < input_amount:
                # give change
                print(f"Here is {input_amount - self.amount} Naira in change")
                # process resources
                self.paper_available = (self.paper_available - self.num_of_pages)
                self.ink_available = (self.ink_available - (self.coloured_per_ink * self.num_of_pages))
                self.profit +=  self.amount 
                 #print user's job

    def street_notes(self):
        # while True:
        try:
            input_note = input("""Enter 1 for Biyar (#5); \nEnter 2 for Faiba (#10); \nEnter 3 for Muri(#20); \nEnter 4 for Wazobia(#50)\nEnter 5 When you are Done.:
            \n """ ).strip()
            if input_note in ['1','2','3','4','5']:
                if input_note == '1':
                    num_of_biyar = input('Enter the number of Biyar(#5): ')
                    self.Biyar_notes += int(num_of_biyar)
                    self.street_notes()
                elif input_note == '2':
                    num_of_fabia = input('Enter the number of Fabia(#10): ')
                    self.Faiba_notes += int(num_of_fabia)
                    self.street_notes()
                elif input_note == '3':
                    num_of_muri = input('Enter the number of Muri(#20): ')
                    self.Muri_notes += int(num_of_muri)
                    self.street_notes()
                elif input_note == '4':
                    num_of_wazobia = input('Enter the number of Wazobia(#50): ')
                    self.Wazobia_notes += int(num_of_wazobia)
                    self.street_notes()
                elif input_note == '5':
                    input_amount = (self.Biyar_notes * self.Biyar) + (self.Faiba_notes * self.Faiba)+(self.Muri_notes * self.Muri)+(self.Wazobia_notes *self.Wazobia)
                    total_num_of_Biyar = self.Biyar_notes * self.Biyar 
                    total_num_of_Faiba = self.Faiba_notes * self.Faiba
                    total_num_of_Muri = self.Muri_notes * self.Muri
                    total_num_of_Wazobia = self.Wazobia_notes * self.Wazobia
                    print(f"We have :\n{total_num_of_Biyar} Biyar\n{total_num_of_Faiba} Faiba\n{total_num_of_Muri} Muri\n{total_num_of_Wazobia} Wazobia") 
                    self.check_transaction(input_amount)   
            
            else:
                raise Exception("Invalid Option")
        except ValueError:
            print("Input must be a number")
            self.street_notes()
        except Exception as err:
            print(str(err))
            self.street_notes()                   
    def confirm_amount_process(self):
        if self.format1 == "coloured":
            self.amount += self.num_of_pages * self.price_coloured
        elif self.format1 == "grayscale":
            self.amount += self.num_of_pages * self.price_grayscale
        print(f"Your price is #{self.amount}")
    def process_price(self):
        self.confirm_amount_process()
        self.street_notes()

    def confirm_sufficient_resources(self):
        try:
            self.num_of_pages = int(input("Enter the number of pages: "))
            if isinstance(self.num_of_pages,int):
                pass
        except Exception:
            print(f"Please, enter a whole number1")
            self.confirm_sufficient_resources()
        
        if self.format1 == "coloured":
            if (self.paper_available < self.num_of_pages):
                return "Sorry there is not enough paper"
            if self.ink_available < (self.coloured_per_ink * self.num_of_pages):
                return "Sorry there is not enough ink"
        elif self.format1 == "grayscale":
            if (self.paper_available < self.num_of_pages):
                return "Sorry there is not enough paper"
            if self.ink_available < (self.grayscale_per_ink * self.num_of_pages):
                return "Sorry there is not enough ink" 
    def check_resources(self):  
        self.confirm_sufficient_resources() 
    def check_initial(self):
        print(f" \n\'''resources\n paper:{self.paper_available}pc\n ink:{self.ink_available}ml\n profit:#{self.profit}\n \''' ")
        self.input_format()
   
    def input_format(self):
        user_prompt = input("What do you want to do?1)check 2)Print 3)Mode 4)Report: ").lower()
        try:
            if user_prompt == "check" or user_prompt =="print" or user_prompt=="mode" or user_prompt=="report":
                if user_prompt == "print":
                    while True:
                        try:
                            self.format1 = input('What format would you like? ( coloured or grayscale ): ').lower() #############
                            print(self.format1)
                            if self.format1 == 'coloured' or self.format1 =='grayscale':
                                self.check_resources() 
                                self.process_price()    
                                self.print_user()        
                            else:
                                print(f"Enter either coloured or grayscale")
                                break
                                
                        except:
                            exit()
                    else:
                         exit()

                elif user_prompt == "mode":
                    self.mode1()
                elif user_prompt == "report":
                    self.report_print()
                elif user_prompt == "check":
                    self.check_initial()
            else:
                print(f"Please enter the right option")
                self.input_format()
        except:
            # print(f"Thanks for using our service")
            exit()




user = Printer()
user.input_format()
                   
    
        
    
              
              
    
    
        
    
    
    
        
    
        
    