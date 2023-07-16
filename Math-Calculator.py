from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import os

class mainControls():

    def __init__(self, master):
        
        #This list will be used to see if the widgets have been setup for that menu item. True means it has been setuped, False means it has not be setup.
        self.setup = {"fraction": False, "precent": False, "decimal": False} #index 0 is for fraction, index 1 is for precent, and index 2 is for decimal.

        self.functionName = "" #This will keep track of what function is being used

        #This is where we will set the style for the widgets. 
        self.style = ttk.Style()

        #This will set the main output and input labels
        self.style.configure('MainLabels.TLabel', foreground = 'white', background = '#002953', font = ('Courier New', 20, 'bold')) 

        #This will set the calculate button.
        self.style.configure('FucntionButton.TButton', foreground = 'black', background = 'white', font = ('Courier New', 13, 'bold'))
        
        #This will be used to set the labels that tell the user where to input their number. Like Enter Numerator, Enter Denominator, Enter Precent and Enter Decimal. 
        self.style.configure('IndecatorLabel.TLabel', font = ('Courier New', 14))

        #Used for the button frame.
        self.style.configure('ButtonFrame.TFrame', background = '#002953')

        #Call the classes that have the calculations
        self.Simplifing = Simplifying() 
        self.Fraction = Fraction()
        self.Precent = Precent()
        self.Decimal = Decimal()
        
        
        #This section is for properly setting up the cascade menus
        #This will be the menu bar.
        self.menuBar = Menu(master)


        #The fraction menu item and all of it's commands.
        self.fraction = Menu(self.menuBar)
        self.fraction.add_command(label = 'Simplifying Fractions', command = lambda : self.fractionSetup(1))
        self.fraction.add_separator()
        self.fraction.add_command(label = 'Fraction to Precent', command = lambda : self.fractionSetup(2))
        self.fraction.add_separator()
        self.fraction.add_command(label = 'Fraction to Decimal', command = lambda : self.fractionSetup(3))
        
        #The precent menu item and all of it's commands.
        self.precent = Menu(self.menuBar)
        self.precent.add_command(label = 'Precent to Fraction', command = lambda: self.precentSetup(0))
        self.precent.add_separator()
        self.precent.add_command(label = 'Precent to Decimal', command = lambda: self.precentSetup(1))
        
        #The decimal menu item and all of it's commands.
        self.decimal = Menu(self.menuBar)
        self.decimal.add_command(label = 'Decimal to Fraction', command = lambda: self.decimalSetup(0))
        self.decimal.add_separator()
        self.decimal.add_command(label = 'Decimal to Precent', command = lambda: self.decimalSetup(1))


        #Displaying the menu items.
        self.menuBar.add_cascade(menu = self.fraction, label = 'Fraction')
        self.menuBar.add_cascade(menu = self.precent, label = 'Precent')
        self.menuBar.add_cascade(menu = self.decimal, label = 'Decimal')
        
        master.config(menu = self.menuBar)


        #Input label
        ttk.Label(master, text = 'Input', style = 'MainLabels.TLabel', justify = CENTER).grid(row = 0, column = 0)
        
        #Output Label
        ttk.Label(master, text = 'Output', style = 'MainLabels.TLabel', justify = CENTER).grid(row = 0, column = 1)

        #Frame for the user input
        self.inputFrame = ttk.Frame(master, height = 500, width = 700, relief = 'solid')
        self.inputFrame.grid(row = 1, column = 0, sticky = 'w')
        
        #Frame for the output
        self.outputFrame = ttk.Frame(master, height = 500, width = 700, relief = 'solid')
        self.outputFrame.grid(row = 1, column = 1, sticky = 's')
        
        #Frame that will hold the export and the clear output button.
        self.buttonFrame = ttk.Frame(master,style = 'ButtonFrame.TFrame', height = 200, width = 600)
        self.buttonFrame.grid(row = 2, column = 1)


        #The text widget used for desplaying the calculation answers.
        self.output = Text(self.outputFrame, width = 85, height = 31, state = 'disable')    
        self.output.grid(row = 0, column = 0)

        #The scroll bar for the text widget
        self.scrollBar = ttk.Scrollbar(self.outputFrame, orient = VERTICAL, command = self.output.yview)
        self.scrollBar.grid(row = 0, column = 1, sticky = 'ns')
        self.output.config(yscrollcommand = self.scrollBar.set)


        #Calculate button
        ttk.Button(master, text = 'Calculate', style = 'FucntionButton.TButton', command = self.calculate).grid(row = 2, column = 0, pady = 60, ipadx = 10, ipady = 10)

        #Export button
        ttk.Button(self.buttonFrame, text = 'Export', style = 'FucntionButton.TButton', command = self.export).grid(row = 0, column = 0, padx = 100, ipadx = 10, ipady = 10)

        #Clear output button
        ttk.Button(self.buttonFrame, text = 'Clear Output', style = 'FucntionButton.TButton', command = self.clearOutput).grid(row = 0, column = 1, padx = 100, ipadx = 10, ipady = 10)

        

    def destroyWidgets(self): #Used to destroy the widgets in the user input frame but doesn't destroy the frame itself.
        for widgets in self.inputFrame.place_slaves():
            widgets.destroy()



    def fractionSetup(self, funcNum): #funcNum is used to get the funciton numeber
        #The number that comes from funcNum will be the index number for this list. 
        self.titleName = ['Arithmatic', 'Simplifying Fractions', 'Converting Fraction to Precent', 'Converting Fraction to Decimal']
        self.currentName = self.titleName[funcNum] #This will store the current title
        
        
        if self.setup["fraction"] == False: #This will create the setup for precent only if the setup hasn't been already setup.
            
            #Destroy the widgets that are in the input frame.
            self.destroyWidgets()

            #This will tell the user what funciton they are on.
            self.title = ttk.Label(self.inputFrame, text = f'{self.titleName[funcNum]}', font = ('Courier New', 16, 'bold'), justify = CENTER)
            self.title.place(relx = 0.5, y = 20, anchor = CENTER)
            

            self.functionName = f"{self.titleName[funcNum]}" #Store the name of the function the user is using currently.  



            #Label that will tell them where to input the numerator.
            self.enterLabel1 = ttk.Label(self.inputFrame, text = 'Enter Numerator: ', style = 'IndecatorLabel.TLabel', justify = LEFT)
            self.enterLabel1.place(x = 20, y = 160)

            #Label that will tell them where to input the denominator.
            self.enterLabel2 = ttk.Label(self.inputFrame, text = 'Enter Denominator:', style = 'IndecatorLabel.TLabel', justify = LEFT)
            self.enterLabel2.place(x = 20, y = 300)


            #This entry widget will take the users numerator input. "nume" is the short for numerator
            self.numeInput = ttk.Entry(self.inputFrame, font = ('Courier New', 13), justify = CENTER)
            self.numeInput.place(x = 240, y = 160, width = 100, height = 30)

            #This will represent the line between the numerator and denominator.
            self.lineLabel = ttk.Label(self.inputFrame, text = '_____________', font =  ('Courier New', 14, 'bold'), justify = CENTER)
            self.lineLabel.place(x = 220, y = 220)


            #This entry widget will take the users denominator. "deno" is short for denominator
            self.denoInput = ttk.Entry(self.inputFrame, font = ('Courier New', 13), justify = CENTER)
            self.denoInput.place(x = 240, y = 300, width = 100, height = 30)


            #This is the text telling the user to only input whole numbers for the numerator. 
            self.warning = ttk.Label(self.inputFrame, text = '(Enter whole numbers only)', font = ('Courier New', 9), justify = LEFT)
            self.warning.place(x = 410, y = 165)

            #This is the text telling the user to only input whole numbers for the denominator. 
            self.warning2 = ttk.Label(self.inputFrame, text = '(Enter whole numbers only)', font = ('Courier New', 9), justify = LEFT)
            self.warning2.place(x = 410, y = 305)


            #Change the value to true to signal that it has been setup and set the other values to false meaning that they will have to be setup.
            self.setup["fraction"] = True
            self.setup["precent"] = False
            self.setup["decimal"] = False

        

        if self.titleName[funcNum] == self.currentName:
            self.title.destroy()

            #This will tell the user what funciton they are on.
            self.title = ttk.Label(self.inputFrame, text = f'{self.titleName[funcNum]}', font = ('Courier New', 16, 'bold'), justify = CENTER)
            self.title.place(relx = 0.5, y = 15, anchor = CENTER)

            self.functionName = f"{self.titleName[funcNum]}" #Pass in what function is currently being used.  

    

    def precentSetup(self,funcNum): #funcNum is used to get the funciton numeber
        #p will be but infront of the names so it will be defined as a different variable
        #The number that comes from funcNum will be the index number for this list.
        self.pTitleName = ['Precent to Fraction', 'Precent to Decimal']
        self.pCurrentName = self.pTitleName[funcNum] #This will store the current title

        if self.setup['precent'] == False: #This will create the setup for precent only if the setup hasn't been already setup.
            
            #Destroy the widgets in the widgets in the input frame.
            self.destroyWidgets()

            #The title telling what function they are using.
            self.pTitle = ttk.Label(self.inputFrame, text = f'{self.pTitleName[funcNum]}', font = ('Courier New', 16, 'bold'), justify = CENTER)
            self.pTitle.place(relx = 0.5, y = 20, anchor = CENTER)

            self.functionName = f"{self.pTitleName[funcNum]}" #Store the name of the function the user is currently using.

            #Tell the user to input 'Input number without the precent sign.'.
            self.pWarning = ttk.Label(self.inputFrame, text = '(Input number without the precent sign)', font = ('Courier New', 9), justify = LEFT)
            self.pWarning.place(x = 390, y = 205)


            #Label that will tell the user where to input there precent.
            self.pEnterLabel1 = ttk.Label(self.inputFrame, text = 'Enter Precent: ',  style = 'IndecatorLabel.TLabel', justify = LEFT)
            self.pEnterLabel1.place(x = 20, y = 200)

            #The Enter widget that will take the users input.
            self.percentInput = ttk.Entry(self.inputFrame, font = ('Courier New', 13), justify = CENTER)
            self.percentInput.place(x = 225, y = 200, width = 100, height = 30)


            #The precent sign that will appear next to entry widget
            self.percentSign = ttk.Label(self.inputFrame, text = '%', font = ('Courier New', 24), justify = LEFT)
            self.percentSign.place(x = 335, y = 195)

            #Change the value to true to signal that it has been setup and set the other values to false meaning that they will have to be setup.
            self.setup["fraction"] = False
            self.setup["precent"] = True
            self.setup["decimal"] = False

        if self.pTitleName[funcNum] == self.pCurrentName:
            self.pTitle.destroy()

            #The title telling what function they are using.
            self.pTitle = ttk.Label(self.inputFrame, text = f'{self.pTitleName[funcNum]}', font = ('Courier New', 16, 'bold'), justify = CENTER)
            self.pTitle.place(relx = 0.5, y = 15, anchor = CENTER)

            self.functionName = f"{self.pTitleName[funcNum]}" #Store the name of the function the user is currently using.



    def decimalSetup(self, funcNum):#funcNum is used to get the funciton numeber
        #d will be but infront of the names so it will be defined as a different variable
        #The number that comes from funcNum will be the index number for this list.
        self.dTitleName = ['Decimal to Fraction', 'Decimal to Precent']
        self.dCurrentName = self.dTitleName[funcNum]
         
        if self.setup['decimal'] == False:#This will create the setup for decimal only if the setup hasn't been already setup.
            
            #Destroy the widgets in the widgets in the input frame.
            self.destroyWidgets()

            #The title telling what function they are using.
            self.dTitle = ttk.Label(self.inputFrame, text = f'{self.dTitleName[funcNum]}', font = ('Courier New', 16, 'bold'), justify = CENTER)
            self.dTitle.place(relx = 0.5, y = 20, anchor = CENTER)

            self.functionName = f"{self.dTitleName[funcNum]}" #Store the name of the function the user is currently using.
          

            #Tell the user to input 'If the number doesn't have a ones places than add a zero infront of it. Like this 0.56'.
            self.pWarning = ttk.Label(self.inputFrame, text = "(Enter a decimal number only)", font = ('Courier New', 9), justify = LEFT)

            self.pWarning.place(x = 332, y = 205)

            #Label that will tell the user where to input there precent.
            self.dEnterLabel1 = ttk.Label(self.inputFrame, text = 'Enter Decimal: ',  style = 'IndecatorLabel.TLabel', justify = LEFT)
            self.dEnterLabel1.place(x = 20, y = 200)


            #The Enter widget that will take the users input.
            self.decimalInput = ttk.Entry(self.inputFrame, font = ('Courier New', 13), justify = CENTER)
            self.decimalInput.place(x = 210, y = 200, width = 100, height = 30)

            #Change the value to true to signal that it has been setup and set the other values to false meaning that they will have to be setup.
            self.setup["fraction"] = False
            self.setup["precent"] = False
            self.setup["decimal"] = True
        


        if self.dTitleName[funcNum] == self.dCurrentName:
            self.dTitle.destroy()

            #The title telling what function they are using.
            self.dTitle = ttk.Label(self.inputFrame, text = f'{self.dTitleName[funcNum]}', font = ('Courier New', 16, 'bold'), justify = CENTER)
            self.dTitle.place(relx = 0.5, y = 15, anchor = CENTER)

            self.functionName = f"{self.dTitleName[funcNum]}" #Store the name of the function the user is currently using.
    


    def clearOutput(self):
            #Delete the contiants of the text widget
            self.output.config(state = 'normal')
            self.output.delete('1.0', 'end')
            self.output.config(state = 'disabled')

            #Delete user input depending on what setup they are using
            if self.setup['fraction'] == True:
                self.numeInput.delete(0, END)
                self.denoInput.delete(0, END)
            #
            elif self.setup['precent'] == True:
                self.percentInput.delete(0, END)
            #
            elif self.setup['decimal'] == True:
                self.decimalInput.delete(0, END)

    def export(self):
        
        #This will check if there is actual contents in the ouput text field.
        if self.output.get('1.0', 'end') == '\n':
            messagebox.showerror(title = 'Export', message = 'There must be contents in the output field.')
            
         #Take the given file path create a txt file which will have all of the ouptut contents. 
        else:
            self.filepath = filedialog.asksaveasfilename() #get the file path and name

            #This will get the file name the user has inputed without the .txt
            self.point = self.filepath.rfind('/') + 1
            self.filename = self.filepath[self.point:]

            #Check if the user didn't cancel the file save. 
            if self.filename != '':
                
                self.filepath = f'{self.filepath}.txt' #Add the .txt to the end of the filepath so the OS knows its a text file
                

                if not os.path.exists(self.filepath):

                    self.usersFile = open(self.filepath, 'wt') #Open the file in write mode becuase then it will create the file and save it to a variable.
                    self.outputContents = self.output.get('1.0', 'end')

                    #Put the contents from the ouput field to the txt file.
                    print(self.outputContents.rstrip(), file=self.usersFile)
                    print(end=' ', flush=True)
                    self.usersFile.close()

                    #tell the user that the contenst of the ouput field are in file.
                    messagebox.showinfo(title = 'File', message = f'The contents in the ouput field are now in the a text file called {self.filename}.')
                else:
                    
                    self.tmp = messagebox.askokcancel(title = 'File', message = f'Do you want to replace the file {self.filename}?')

                    if self.tmp:
                        
                        self.usersFile = open(self.filepath, 'wt') #Open the file in write mode becuase then it will create the file and save it to a variable.
                        self.outputContents = self.output.get('1.0', 'end')

                        #Put the contents from the ouput field to the txt file.
                        print(self.outputContents.rstrip(), file=self.usersFile)
                        print(end=' ', flush=True)
                        self.usersFile.close()

                        #tell the user that the contenst of the ouput field are in file.
                        messagebox.showinfo(title = 'File', message = f'The contents in the ouput field are now in the a text file called {self.filename}.')


    def calculate(self):
        #Go through each case to see what calcultion should be preformed depending on what the value is in functionName, which contains the name of the math function the user is on.

        if self.functionName == "Simplifying Fractions":
            
            #Try to convert the users input to int.
            try:
                #Pass in the the output text widget, the numerator entry widgets, and the denominator entry widget.
                self.Simplifing.__init__(self.output, self.numeInput.get(), self.denoInput.get()) 
            except:

                #Tell the user that there input is invalid
                self.output.config(state = 'normal')
                self.output.insert('end', 'Invalid Input. Enter whole numbers only.\n')
                self.output.insert('end', '_____________________________________________________________________________________\n\n')
                self.output.config(state = 'disabled')
             #
            else:
                self.Simplifing.calculate()

        
         #
        elif self.functionName == "Converting Fraction to Precent":
           
            #Try to convert the users input to int.
            try:
                #Pass in the the output text widget, the numerator entry widgets, the denominator entry widget and the function code. 'p' is for fraction to precent
                self.Fraction.__init__(self.numeInput.get(), self.denoInput.get(), self.output, 'p')
            except:

                #Tell the user that there input is invalid.
                self.output.config(state = 'normal')
                self.output.insert('end', 'Invalid Input. Enter whole numbers only.\n')
                self.output.insert('end', '_____________________________________________________________________________________\n\n')
                self.output.config(state = 'disabled')
             #
            else:
                self.Fraction.calculate()

         
         #
        elif self.functionName == "Converting Fraction to Decimal":
           
            #Try to convert the users input to int.
            try:
                #Pass in the the output text widget, the numerator entry widgets, the denominator entry widget and the function code. 'd' is for fraction to decimal 
                self.Fraction.__init__(self.numeInput.get(), self.denoInput.get(), self.output, 'd')
            except:

                #Tell the user that there input is invalid.
                self.output.config(state = 'normal')
                self.output.insert('end', 'Invalid Input. Enter whole numbers only.\n')
                self.output.insert('end', '_____________________________________________________________________________________\n\n')
                self.output.config(state = 'disabled')
             #  
            else:
                self.Fraction.calculate()
         #
        elif self.functionName == "Precent to Fraction":

            try: #Pass in the output text widget, the precent input entry widget, the function code and the simplifing class object. 'f' is for Precent to Fraction.
                
                try:
                    
                    #Try to convert the users input to int.
                    self.tmp = int(self.percentInput.get())
                    self.Precent.__init__(self.output, self.tmp, 'f')

                 #
                except:

                    #Try to convert users input to float. 
                    self.tmp = float(self.percentInput.get())
                    self.Precent.__init__(self.output, self.tmp, 'f')

                #   
            except:

               #Tell the user that there input is invalid.
                self.output.config(state = 'normal')
                self.output.insert('end', 'Invalid Input. Enter whole numbers only.\n')
                self.output.insert('end', '_____________________________________________________________________________________\n\n')
                self.output.config(state = 'disabled') 

             #
            else:
                self.Precent.calculate()

         #
        elif self.functionName == "Precent to Decimal":

            try: #Pass in the output text widget, the precent input entry widget, and function code. 'd' is for Precent to decimal.
                self.tmp = float(self.percentInput.get()) #This will get the number in float.
                
                self.Precent.__init__(self.output, self.tmp, 'd')

             #   
            except:

               #Tell the user that there input is invalid.
                self.output.config(state = 'normal')
                self.output.insert('end', 'Invalid Input. Enter whole numbers only.\n')
                self.output.insert('end', '_____________________________________________________________________________________\n\n')
                self.output.config(state = 'disabled') 

             #
            else:
                self.Precent.calculate()

         #
        elif (self.functionName == "Decimal to Fraction") or (self.functionName == "Decimal to Precent"):

                #This will tell the user there input is invalid if it blows up.
                try: 
                    self.tmp = f'{float(self.decimalInput.get())}'.rfind(".0") #Get the poinstion of .0 in the string. 
                except:
                     #Tell the user that there input is invalid.
                    self.output.config(state = 'normal')
                    self.output.insert('end', 'Invalid Input. Enter a number that has numbers after the decimal point.\n')
                    self.output.insert('end', '_____________________________________________________________________________________\n\n')
                    self.output.config(state = 'disabled')

                if f'{float(self.decimalInput.get())}'[self.tmp:] != '.0': #Check to see if it is just zeros after the decimal point.
                    
                    try:
                        #Pass in the output text widget, the decimal input entry widget, function code, and the input without the decimal point. 10.01 will become 1001. 'f' is for decimal to precent and 'p' is for decimal to precent.
                        
                        if self.functionName == "Decimal to Fraction":

                            self.Decimal.__init__(self.output, float(self.decimalInput.get()), f'{self.decimalInput.get()}'.replace('.', ''), 'f')
                            self.Decimal.calculate()

                         #
                        elif self.functionName == "Decimal to Precent":

                            self.Decimal.__init__(self.output, float(self.decimalInput.get()), f'{self.decimalInput.get()}'.replace('.', ''), 'p')
                            self.Decimal.calculate()

                    except:
                                
                        #Tell the user that there input is invalid.
                        self.output.config(state = 'normal')
                        self.output.insert('end', 'Invalid Input. Enter a decimal number only.\n')
                        self.output.insert('end', '_____________________________________________________________________________________\n\n')
                        self.output.config(state = 'disabled')
                else:
                    #Tell the user that there input is invalid.
                    self.output.config(state = 'normal')
                    self.output.insert('end', 'Invalid Input. Enter a number that has numbers after the decimal point.\n')
                    self.output.insert('end', '_____________________________________________________________________________________\n\n')
                    self.output.config(state = 'disabled')
      
class Simplifying():

    def __init__(self, output = None, nume = '0', deno = '0'):
        self.output = output #This will have the ouptut text widget that will be passed in.
        self.nume = int(nume) #Users numerator input
        self.deno = int(deno) #Users denominator input
        self.fraction = f'{self.nume}/{self.deno}' #This will have the fraction before it has been simplified
        self.steps = []


    def calculate(self):
        fail = 0 #This will keep track of the number of times it fialed to properly divied the nume and deno

        while fail != 9: #If it didn't fialed to divied 9 times
            fail = 0

            for i in range(10, 1, -1): #This will go through the 9 unique numbers which are 10,9,8,7,6,5,4,3,2. 
                
                if self.nume % i == 0: #is the numerator evenly disivable by i?

                    if self.deno % i == 0: #is the denominator evenly disivable by i?
                        
                        self.nume //= i
                        self.deno //= i

                        #Store the step
                        self.steps.append(f'{self.nume} / {self.deno} divided by {i}\n')
                         
                     #
                    else:
                        #If not then add one 
                        fail += 1
                else:
                    #If not then add one
                    fail += 1


        if self.nume == self.deno:
            
            #Display the answer
            self.output.config(state = 'normal')
            self.output.insert('end', f"The fraction {self.fraction} is: {self.nume}, which is its simplest form.\n\n")
            self.output.config(state = 'disabled')

         #
        elif self.deno % self.nume == 0: #is the denominator able to be divied by the numerator equaly.
            
            self.deno //= self.nume
            self.nume //= self.nume
            
            #Display the answer
            self.output.config(state = 'normal')
            self.output.insert('end', f"The fraction {self.fraction}, simplest form is {self.nume}/{self.deno}.\n\n")
            self.output.config(state = 'disabled')

         #
        elif self.nume > self.deno: #is the numerator greater than the denominator?
            self.leftOver = self.nume % self.deno #Reminder of numerator and denominator which will become the new numerator
            self.wholeNum = self.nume // self.deno #How many times the denominator can go into teh numerator

            if self.leftOver == 0: #is the new numerator equal to zero?
                
                #Display the answer
                self.output.config(state = 'normal')
                self.output.insert('end', f"The fraction {self.fraction}, simplest form is {self.wholeNum}.\n\n")
                self.output.config(state = 'disabled')
                
             #   
            else:

                #Display the answer
                self.output.config(state = 'normal')
                self.output.insert('end', f"The fraction {self.fraction}, simplest form is {self.wholeNum}  {self.leftOver}/{self.deno}.\n\n")
                self.output.config(state = 'disabled')
         #
        else:
            #Display the answer
            self.output.config(state = 'normal')
            self.output.insert('end', f"The fraction {self.fraction}, simplest form is {self.nume}/{self.deno}.\n\n")
            self.output.config(state = 'disabled')
        
        #Show the steps
        self.output.config(state = 'normal')
        self.output.insert('end', "Steps:\n")

        for i in range(len(self.steps)):
            self.output.insert('end', f"{self.steps[i]}")

        self.output.config(state = 'disabled')

        #Put a seperator for organization
        self.output.config(state = 'normal')
        self.output.insert('end', '_____________________________________________________________________________________\n\n')
        self.output.config(state = 'disabled')

class Fraction():
    
    def __init__(self, nume = '0', deno = '0', output = None, funcNum = None): 
        self.nume = int(nume) #Users numerator input 
        self.deno = int(deno) #Users denominator input 
        self.output = output #This will have the ouptut text widget that will be passed in.
        self.funcNum = funcNum #This will tell what calculation we should execute. 

    def calculate(self):
        
        if self.funcNum == 'p': #Fraction to precent
            
            if self.deno <= 100: #Is the denominator less than 100?

                multi = 100 / self.deno #This will get the number that takes the denominator to 100
                
                
                #Display the answer
                self.output.config(state = 'normal')
                self.output.insert('end', f'The fraction {self.nume} / {self.deno} is {(self.nume * multi)}%\n')
                self.output.config(state = 'disable')
             #
            else: #The denominator is greater than 100

                multi = self.deno / 100 #This will get the number that takes the denominator to 100
                

                #Display the answer
                self.output.config(state = 'normal')
                self.output.insert('end', f'The fraction {self.nume}/{self.deno} is {(self.nume / multi)}%\n')
                self.output.config(state = 'disabled')
         #
        elif self.funcNum == 'd': # fraction to decimal

                self.output.config(state = 'normal')
                self.output.insert('end', f'The fraction {self.nume}/{self.deno} is {(self.nume/self.deno)}\n')



        #Put a seperator for organization
        self.output.config(state = 'normal')
        self.output.insert('end', '_____________________________________________________________________________________\n\n')
        self.output.config(state = 'disabled')




class Precent():
    
    def __init__(self, output = None, precent = None, funcNum = None): 
        self.precent = precent #Users precent input
        self.output = output #This will have the ouptut text widget that will be passed in.
        self.simplify = Simplifying() #This will have the simplifing class object.
        self.funcNum = funcNum #This will tell what calculation we should execute. 
    

    def calculate(self):
        
        if self.funcNum == 'f': #Precent to Fraction
            
            self.precent = int(round(self.precent, ndigits = 0)) #Round the precent to the nearest ones digit becuase fractions are whole numbers. 

            #display the results 
            self.output.config(state = 'normal')
            self.output.insert('end', f'The fraction representation of {self.precent}% is {self.precent}/100.\n')
            self.output.config(state = 'disabled')
            
            self.simplify.__init__(self.output, self.precent, 100)
            self.simplify.calculate()
        
         #
        elif self.funcNum == 'd':
            
            #Precent to Decimal
            self.output.config(state = 'normal')
            self.output.insert('end', f'The decimal representation of {self.precent}% is {(self.precent / 100)}.\n')
            self.output.config(state = 'disabled')

            #Put a seperator for organization
            self.output.config(state = 'normal')
            self.output.insert('end', '_____________________________________________________________________________________\n\n')
            self.output.config(state = 'disabled')
        



class Decimal():
    
    def __init__(self, output = None, decimal = '0', endRusult = '0', funcNum = None): 
        
        self.output = output #This will have the ouptut text widget that will be passed in. 
        self.decimal = decimal #Users decimal input
        self.endRusult = float(endRusult) #This is the decimal but it doesn't have the decimal point
        self.simplify = Simplifying() #This will have the simplifing class object.
        self.funcNum = funcNum #This will tell me what calculation we should execute. 
    

    def calculate(self):
        
        if self.funcNum == 'f': #Decimal to Fraction
            
            self.deno = '1 ' #This will become the denominator for decimal.
            multiplier = 10 #This will be gets the decimal to a whole number.
            time = 0 #This will track the amount of times we will have to multiply 10 times the decimal.
            tmp = int(self.decimal) #This stores the int version of decimal

            while tmp != self.endRusult:

                time += 1
                self.decimal = self.decimal * multiplier
                tmp = int(self.decimal)

            
            for i in range(time):
                self.deno = self.deno.replace(' ', '0 ') #By adding a zero and a space we can keep adding zeros to the end of the string.

            self.deno = int(self.deno) #Onces we have added the nessesary number of zeros to the orignal 1 we can now turn it into an int.


            #Display the result
            self.output.config(state = 'normal')
            self.output.insert('end', f'The fraction representation of {self.decimal / self.deno} is {int(self.decimal)}/{self.deno}.\n')
            self.simplify.__init__(self.output, int(self.decimal), self.deno)
            self.simplify.calculate()
            self.output.config(state = 'disable')

                
        elif self.funcNum == 'p': #Decimal to precent

            #Display the results
            self.output.config(state = 'normal')
            self.output.insert('end', f'The precent representation of {self.decimal} is {self.decimal * 100}%.\n')
            self.output.config(state = 'disabled')

            #Put a seperator for organization
            self.output.config(state = 'normal')
            self.output.insert('end', '_____________________________________________________________________________________\n\n')
            self.output.config(state = 'disabled')

def main():
    #Setup the top level window
    root = Tk()
    root.title('Math Calculator')
    root.geometry('1400x700+100+100')
    root.resizable(False, False)
    root.option_add('*tearOff', False)
    root.configure(background = '#002953')

    app = mainControls(root)

    root.mainloop()

if __name__ == "__main__":
    main()