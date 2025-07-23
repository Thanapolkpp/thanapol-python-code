''' 
Personal Finance Calcullator 
Student:Thanapol Khampimpit
Date: 23/07/2025
Purpose: Calculate monthly budget and savings
'''

income = float(input("User's monthly income in THB: "))
rent = float(input("Monthly rent / housing cost: "))
food = int(input("Monthly food budget in THB: "))
transportation = float(input("Monthly transportation expenses: "))
entertainment = int(input("Monthly entertainment budget: "))
emergency_percent = float(input("Percentage to save for emergency: "))
investment_percent = float(input("Percentage to invest: "))

total_fixed = rent + transportation
total_variable = food + entertainment
total_expenses = total_fixed + total_variable
remaining_income = income - total_expenses
emergency_fund = income * (emergency_percent / 100)
investment = income * (investment_percent / 100)

available_savings = remaining_income - emergency_fund - investment

expense_ratio = (total_expenses / income) * 100  # เปลี่ยนจาก *10 เป็นเปอร์เซ็นต์

print("\n=== MONTHLY BUDGET REPORT ===")
print(f"Income: {income:.2f} THB")
print(f"Fixed Expenses: {total_fixed:.2f} THB")
print(f"Variable Expenses: {total_variable:.2f} THB")
print(f"Total Expenses: {total_expenses:.2f} THB")
print(f"Remaining Income after expenses: {remaining_income:.2f} THB")

print("\n=== SAVINGS BREAKDOWN ===")
print(f"Emergency Fund ({emergency_percent}%): {emergency_fund:.2f} THB")
print(f"Investment ({investment_percent}%): {investment:.2f} THB")
print(f"Available for other savings: {available_savings:.2f} THB")

print("\n=== ANALYSIS ===")
print(f"Expense Ratio: {expense_ratio:.2f}%")

    
    