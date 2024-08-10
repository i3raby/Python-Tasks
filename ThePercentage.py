try:
    ThePercentage = float(input('Please enter the percentage of the result → '))
    if 1 <= ThePercentage <= 100:
        if 50 <= ThePercentage <= 64 :
            print(f"Passable: The percentage is {ThePercentage}%, which is in the range of 50% to 64%.")
        elif 65 <= ThePercentage <= 74 :
            print(f"Good: The percentage is {ThePercentage}%, which is in the range of 65% to 74%.")
        elif  75 <= ThePercentage <= 84 :
            print(f"Very Good: The percentage is {ThePercentage}%, which is in the range of 75% to 84%.")
        elif  85 <= ThePercentage <= 100 :
            print(f"Excellent: The percentage is {ThePercentage}%, which is in the range of 85% to 100%.")
        else:
            print(f"Declined: The percentage {ThePercentage}% is outside the specified ranges.")
    else:
        print('The percentage must be between 1 and 100. Please try again.')
except ValueError:
    print('Invalid input! Please enter a valid number for the percentage.')



