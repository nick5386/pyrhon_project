"""A collection of function for doing my project."""

import string

def greeting():
     
    print("Hey! I'm Nishant.\nWelcome to Insura. Let me guide you through our easy to go process for Home Insurance Policy Quote!")
    
def base_premium_price(square_foot):
    """This function calculates the base price according to how big the house is.
    
    Parameters
    ----------
    square_foot = string
        square foot or area of house in integer
        
    Returns
    -------
    premium_price: int
        Result is the base price for insurance poilcy.
    """  
        
    # Assigning the premium price based on the square footage of the house
    if int(square_foot) < 2500:
        premium_price = 1000
    elif int(square_foot) >=2500 and int(square_foot) <=4000:
        premium_price = 1500
    elif int(square_foot) > 4000:
        premium_price = 2000
    
    print("Base price: ", premium_price)
    return premium_price

def get_area():  
    
    """This function is used to check whether user enetered the valid area (in square foot) and returns that square foot.
    
    Parameters
    ----------
        None
        
    Returns
    -------
    square_foot = string
        Returns the square foot as a string
    """
    
    is_valid_area = False 
    
    # while user enters valid area
    while not is_valid_area:
        square_foot = input("\nWhat is the square foot area (in whole number) of the house?: ")
        # Checking if the square foot area entered is a positive integer
        if square_foot.isdigit():
            # Setting the flag to true if the user enter positive integer
            is_valid_area = True
        else:
            print("Invalid response! please try again\n")
    
    return square_foot 

def calc_discount(customer_age, student, base_price):
    """This function calculates the discount for customer's home insurance policy.
    
    Parameters
    ----------
    customer_age = string
        Customer's age
    student = string
        Customer is a student or not.
    base_price = int
        Starting base price for insurance policy.
        
    Returns
    -------
    output = int or float
        Result is the total discount a customer cen get.
    """
    
    # Calculating discount based on either age or student status of the owner
    if int(customer_age) >= 65:
        discount = base_price * (9/100)   
    elif int(customer_age) < 65 and student.upper() == 'YES':
        discount = base_price * (5/100)
    else:
        discount = 0
    
    print("Total discount: ", discount)
    return discount

def get_age_student():
        
    """This function is used to check whether user entered valid age and student status(yes/no) and returns customer age and student                status
    
    Parameters
    ----------
        None
        
    Returns
    -------
    customer_age = string
        Age of the customer
        
    is_student = string
        Student status
    """
    
    valid_customer_age = False
    valid_student_status = False
    
    # while customer age is invalid
    while not valid_customer_age:
        
        customer_age = input("\nWhat is your age?: ")
        # Checking if the customer age entered is a positive integer
        if customer_age.isdigit():
            valid_customer_age = True
        else:
            print("Invalid Response! Please Try again\n")
    
    # while student status is invalid
    while not valid_student_status:
        
        is_student = input("Are you a student?: ")
        # Checking if the user entered either yes or no and converting the input to uppercase and 
        # removing the leading and trailing spaces
        if is_student.upper().strip() == 'YES' or is_student.upper().strip() == 'NO':
            valid_student_status = True
        else:
            print("Invalid Response! Please Try again\n")
            
    return customer_age, is_student

def calc_additional_premium(property_age, existing_claim, base_price):
    """This function calculates the Additional costs that needs to be added in the quote.
    
    Parameters
    ----------
    property_age = string
        How old the property is.
    existing_claim = string
        Has customer filed any property claim in last 5 years.
    base_price = int
        Starting base price for insurance policy
        
    Returns
    -------
    additional_premium = int or float
        Result is the additional cost that needs to be added in the quote.
    """
    
    # Calculating additional premium by checking age of the property and existing claim (if any)  
    if int(property_age) >= 5 and existing_claim.upper() == 'YES':
        additional_premium = base_price * 3/100
    elif int(property_age) < 5 and existing_claim.upper() == 'YES':
        additional_premium = base_price * 2/100
    elif int(property_age) >=5 and existing_claim.upper() == 'NO':
        additional_premium = base_price * 1/100
    elif int(property_age) < 5 and existing_claim.upper() == 'NO':
        additional_premium = 0
        
    print("Additional Premium cost: ", additional_premium)
    return additional_premium

def get_additional_premium_details():
    
    """This function is used to check whether user entered valid property age and existing claim(yes/no) and returns user property age and          any existing claim
    
    Parameters
    ----------
    None
        
    Returns
    -------
    property_age = string
        Property age of the user
        
    existing_claim = string
        Any existing claim filed in the last five years
    """
    
    valid_property_age = False
    valid_existing_claim = False
    
    # While propert age is invalid
    while not valid_property_age:
      
        property_age = input("\nHow old is your property?(Please enter in years e.g. 5): ")
        # Checking if the property age entered is a positive integer
        if property_age.isdigit():
            valid_property_age = True
        else:
            print("Invalid Response! Please Try again\n")
            
    # While existing claim is invalid
    while not valid_existing_claim:
        
        existing_claim = input("Did you file a property claim in the past 5 years?: ")
        # Checking if the user entered either yes or no and converting the input to uppercase and
        # removing the leading and trailing spaces
        if existing_claim.upper().strip() == 'YES' or existing_claim.upper().strip() == 'NO':
            valid_existing_claim = True
        else:
            print("Invalid Response! Please Try again\n")
    
    return property_age, existing_claim

def calc_options_cost(options, base_price):
    """This function calculates how much each option cost based on customer requirements.
    
    Parameters
    ----------
    options = string
        Comma separated string of all options that are available.
    base_price = int
        Starting base price for insurance policy.
        
    Returns
    -------
    option_cost = int or float
        Result is the added cost of all options that customer select.
    """
    
    # Parsing comma separated options string into list
    lst = options.split(",")
    option_cost = 0
    # Iterating over the different options chosen by the customer in order to calculate cost of options
    for option in lst:
        # Converting the option string to upper case and removing the leading and trailing characters
        if option.upper().strip() == 'HURRICANE':
            option_cost = option_cost + (base_price * 3/100)
        elif option.upper().strip() == 'FLOOD':
            option_cost = option_cost + (base_price * 2/100)
        elif option.upper().strip() == 'EARTHQUAKE':
            option_cost = option_cost + (base_price * 4/100)
    
    print("Total options cost: ", option_cost)
    return option_cost

def get_options_cost():
    
    """This function is used to check whether user entered valid available options to add to their policy.
       
    Parameters
    ----------
       None
       
    Returns
    -------
        options = string
            Result is the string of available options chosen by user
    """
    
    valid_options = False
    lst = ['HURRICANE', 'FLOOD', 'EARTHQUAKE']
        
    # While options are invalid
    while not valid_options:
        
        options = input("\nWhich options do you want to add in your policy (e.g. Hurricane, Flood, Earthquake): ")
        # Removing spaces from the user entered string
        options = options.replace(' ','')
        # Creating a sub list of options enetered by a user
        sub_lst = list(options.upper().split(","))
        # Checking if the user entered options are part of available options
        if (set(sub_lst).issubset(set(lst))):
            valid_options = True
        else:
            print("Invalid Response! Please Try again\n")
            
    return options

def total_quote():
    """This functions calls every function i made above and asks questions to customer for thier policy quote.
    This is my chatbot.
    
    Parameters
    ----------
        None
        
    Returns
    -------
        None
    """
    
    # This function is used to greet the user
    greeting()
    
    # This function is used to take the area input from the user
    square_foot = get_area()
    # This function is used to calculate base price
    base_price = base_premium_price(square_foot) 
    
    # This function is used to get the customer age and student status from the user
    customer_age, student = get_age_student()
    # This function is used to calculate the total discount for the home insurance policy
    total_discount = calc_discount(customer_age, student, base_price)
    
    # This function is used to get property age and any existing claim (if any) from the user.
    property_age, existing_claim = get_additional_premium_details()
    # This function is used to calculate the addition premium price
    additional_premium_cost = calc_additional_premium(property_age, existing_claim, base_price)
    
    #This function is used to get input from user of all available options he/she wants to select for their policy 
    options = get_options_cost()
    # This function calculates cost of different options chosen by the user from the available options(i.e. hurricane, flood, earthquake)
    options_cost = calc_options_cost(options, base_price)
    
    # Calculate the Total cost
    total_cost = base_price - total_discount + additional_premium_cost + options_cost
    print("\nYour home insurance policy quote is: ", total_cost)