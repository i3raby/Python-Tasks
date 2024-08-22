import os

# © 2024 iAraby. All rights reserved.

def XCalculator():
    try:
        while True:
            A = float(input("💡 What's the first number you'd like to work with?\n → "))
            os.system("cls");
            # © 2024 iAraby. All rights reserved.
            B = float(input("🔢 Great! Now, what's the second number?\n → "))
            os.system("cls");
            # © 2024 iAraby. All rights reserved.
            C = int(input("🚀 Ready to crunch some numbers? Pick your operation:\n\n[1] Add ➕\n[2] Subtract ➖\n[3] Multiply ✖️\n[4] Divide ➗\n → "))
            os.system("cls");
            # © 2024 iAraby. All rights reserved.
            if C == 1:
                result = A + B
            elif C == 2:
                result = A - B
            elif C == 3:
                result = A * B
            elif C == 4:
                result = A / B
            else:
                print('Invalid operation selected!')
                continue
            # © 2024 iAraby. All rights reserved.
            print(f"🧮 Your result is: {result}\n")
            # © 2024 iAraby. All rights reserved.
            D = int(input("🔄 Would you like to continue?\n\n[1] Yes, let's go again! 💪\n[2] No, I'm done for now. 🛑\n → "))
            # © 2024 iAraby. All rights reserved.
            if D != 1:
            # © 2024 iAraby. All rights reserved.            
                break
            elif D == 1 :
                os.system("cls");
            # © 2024 iAraby. All rights reserved.
    except ValueError:
        print('Invalid input! Please enter numbers and select a valid operation.')

# © 2024 iAraby. All rights reserved.

XCalculator()