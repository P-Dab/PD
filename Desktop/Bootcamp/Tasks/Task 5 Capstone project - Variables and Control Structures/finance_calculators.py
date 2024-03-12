import math

# Investment calculator
def investment_calculator():
    deposit_amount = float(input("Enter the amount of money you are depositing: "))
    interest_rate = float(input("Enter the interest rate (do not enter the percentage sign): "))
    years = int(input("Enter the number of years you plan to invest: "))
    interest_type = input("Enter 'simple' or 'compound' interest: ").lower()

    if interest_type == 'simple':
        interest = deposit_amount * (1 + (interest_rate / 100) * years)
    elif interest_type == 'compound':
        interest = deposit_amount * math.pow((1 + interest_rate / 100), years)
    else:
        print("Invalid interest type. Please enter 'simple' or 'compound'.")
        return

    print(f"The total investment value after {years} years will be: {round(interest, 2)}")

# Home loan calculator 
def home_loan_calculator():
    loan_amount = float(input("Enter the current value of the property you want to buy: "))
    annual_interest_rate = float(input("Enter the annual interest rate (do not enter the percentage sign): "))
    repayment_period = int(input("Enter the number of months for repayment: "))

    monthly_interest_rate = (annual_interest_rate / 100) / 12
    monthly_repayment = (loan_amount * monthly_interest_rate) / (1 - math.pow(1 + monthly_interest_rate, -repayment_period))

    print(f"Your monthly home loan repayment will be: {round(monthly_repayment, 2)}")

# Main program 
print("Options:")
print("investment - to calculate the amount of interest you'll earn on your investment")
print("bond - to calculate the amount you will have to pay on a home loan")

user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed:")
selection = user_choice.lower().strip()

if selection == 'investment':
    investment_calculator()
elif selection == 'bond':
    home_loan_calculator()
else:
    print("Invalid input. Please enter either 'investment' or 'bond'.")