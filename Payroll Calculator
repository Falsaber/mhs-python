##Declare Variables - especially since we are using global here.##
#Use of globals is for simplicity. Sorry!

grossPay = 0.00
overtimeHours = 0
overtimePay = 0
regularPay = 0
empName = ""
hoursWorked = 0
payRate = 0
#This sets the base for the variables used later on.

#Helper Functions
#def creates what's known as a function, that when called, performs an action or set of actions that it was defined to do.
def loopCheck():
    #Repeat?
    print("Would you like to calculate pay for another employee?")
    answer = str(input("'yes' or 'no' to quit:"))
    print("-"*60)
    if answer == 'yes':
        calculatePay()
    else:
        return
        
#If params (the input of the user) is blank, this function will bring it back to the base function after a warning input.
#From here on out, if an input is left blank, the process will loop back to make sure it's complete.
def notNull(params):
    if params:
        return params
    else:
        input("Error: Input must not be blank. Press any key to continue...")
        calculatePay()


#Main Loop
def calculatePay():
    global grossPay, overtimeHours,overtimePay,regularPay, empName, hoursWorked, payRate
        
    #For Presentation
    print("Payroll System")
    print("=-"*30)


    ##Input Section##
    #This section involves string and float inputs, where float inputs are numbers, including decimals.
    empName = notNull(str(input("Enter the Employee's Full Name:")))
    hoursWorked = notNull(float(input("Enter Hours Worked:")))
    payRate = notNull(float(input("Enter " + empName + "'s hourly rate of pay:$")))
    print("-"*60)

    ##Logic Functions##
    #This section involves a lot of math lines, refer to the math tut on this page if you need help with this.
    if hoursWorked > 40:
        overtimeHours = hoursWorked - 40
        regularPay = 40 * payRate
        overtimePay = (payRate*1.5) * overtimeHours
        grossPay = regularPay + overtimePay
    else:
        regularPay = hoursWorked * payRate
        grossPay = regularPay
    outputReport()

#This is where the magic happens, and the script comes to a head.
def outputReport():
    global grossPay, overtimeHours,overtimePay,regularPay, empName, hoursWorked, payRate
    #Output
    print("=-"*30)
    print("Payroll Report for " + empName)
    print("=-"*30)
    print("--Hours Worked--")
    print("Total Hours Worked:" + str(hoursWorked))
    print("Overtime Hours:" + str(overtimeHours))
    print("--Pay Information--")
    print("Regular Pay:$" + str(format(regularPay, "9,.2f")))
    print("Overtime Pay:$" + str(format(overtimePay, "9,.2f")))
    print("Total Gross Pay:$" + str(format(grossPay, "9,.2f")))
    print("=-"*30)
    print("End Payroll Report")
    #Spacer
    print("-"*60)
    #Go again?
    loopCheck()


calculatePay()
