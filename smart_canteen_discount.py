# 1 condition - if statement
# 1 condition, 2 outputs - if-else statement
# 2 conditions, 3 outputs - if-elif-else statement

# Topic 1: Conditional Statements 
# Program 1: Smart Canteen Discount System
# Topic: if, elif, else, comparison operators, and logical thinking.
# Real-World Scenario
# Imagine a college canteen where students receive discounts based 
# on their total bill.

# The canteen follows these rules:
# - If the bill is Rs. 3,000 or more, the student receives a 
# 20% discount.
# - If the bill is Rs. 2,000 or more but less than Rs. 3,000, 
# the student receives a 10% discount.
# - If the bill is Rs. 1,000 or more but less than Rs. 2,000, 
# the student receives a 5% discount.
# - If the bill is less than Rs. 1,000, no discount is provided.
# - The program must display the original bill, discount amount,
# and final payable amount.


print("================================")
print("       SMART CANTEEN")
print("================================")

bill_amount = float(input("Enter your total bill amount (Rs.): "))

if bill_amount <= 0:
    print("Invalid Bill! Please enter a positive amount.")

else:

    # Standard Discount
    if bill_amount >= 3000:
        discount_rate = 20

    elif bill_amount >= 2000:
        discount_rate = 10

    elif bill_amount >= 1000:
        discount_rate = 5

    else:
        discount_rate = 0

    # Calculate Standard Discount
    standard_discount = bill_amount * discount_rate / 100

    # Calculate Remaining Amount
    remaining_amount = bill_amount - standard_discount

    # Membership Check
    membership = input("Do you have a membership card? (yes/no): ").lower()

    if membership == "yes":
        membership_discount = remaining_amount * 5 / 100

    elif membership == "no":
        membership_discount = 0
        print("No Additional Discount Granted")

    else:
        membership_discount = 0
        print("Invalid Membership Answer. No Additional Discount Granted.")

    # Calculate Total Savings
    total_saving = standard_discount + membership_discount

    # Calculate Final Amount
    final_amount = bill_amount - total_saving

    # Congratulations Message
    if total_saving > 0:
        print(f"\nCongratulations! You saved Rs. {total_saving:.2f}")

    # Bill Summary
    print("\n================================")
    print("          BILL SUMMARY")
    print("================================")

    print(f"Original Bill: Rs. {bill_amount:.2f}")
    print(f"Standard Discount ({discount_rate}%): Rs. {standard_discount:.2f}")
    print(f"Membership Discount: Rs. {membership_discount:.2f}")
    print(f"Total Savings: Rs. {total_saving:.2f}")
    print(f"Final Payable Amount: Rs. {final_amount:.2f}")

    print("================================")



# Practice Question:
# Student Challenge
# Ask students to extend the program with these features:
# 1. If the bill is less than or equal to zero, display an invalid 
# bill message.
# 2. If the student has a membership card, provide an additional 5% 
# discount.
# 3. Display a message saying "Congratulations! You saved Rs. X" 
# when a discount is applied.
# Teaching question: Why do we use elif instead of writing several 
# independent if statements?


