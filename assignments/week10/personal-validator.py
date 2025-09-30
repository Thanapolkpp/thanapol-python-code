"""
Create a Personal Information Validator program that:
    Asks user for their name, age, and phone number
    Validates that name contains only alphabetic characters and spaces
    Converts age from string to integer and validates it's between 18-65
    Validates phone number contains exactly 10 digits
    
    Uses appropriate string methods for validation
    Displays formatted output with proper string formatting
    
    USE: isalpha(), isdigit(), upper(), string formatting with % or .format()
    
Example Result

=== PERSONAL INFORMATION VALIDATOR ===
Enter your name: John Doe
Enter your age: 25
Enter your phone number: 9876543210

Validation Results:
Name: Name: Valid (contains only letters and spaces)
Age: Valid (25 years old)
Phone: Valid (10-digit number)

Formatted Information:
Name: JOHN DOE
Age Group: Young Adult (18-30)
Phone: +91-9876543210

"""


print("=== PERSONAL INFORMATION VALIDATOR ===")
name = input("Enter your name:")
age = int(input("Enter your age:"))
phonenumber = input("Enter your phone number:")

nameFlag = True
for i in name :
    if i.isalpha()== False and i ==" ":
        nameFlag = True
        break
    elif i.isalpha():
        nameFlag = False


ageFlag = True

if age < 18 or age > 65:
    ageFlag = False

phoneFlag = True

if len(phonenumber) != 10:
    phoneFlag = False

for i in phonenumber :
    if i.isdigit()==False:
        phoneFlag =False
    

print("\nValidation Results:")
if nameFlag :
    print("Name: Valid (contains only letters and spaces)")
else :
    print("Name: Invalid (not contains only letters and spaces)")

if ageFlag :
    print(f"Age:Valid({age} years old)")
else:
    print(f"Age:Invalid(less 18 morethon 65)")

if phoneFlag:
    print("Phone:Valid (10-digit number)")
else:
    print("Phone:Invalid (Not 10-digit number)")


print("\nFormatted Information:")
print(f"Name:{name.upper()}")
if age >= 18 and age<=30 :
    print("Age Group: Young Adult (18-30)")
else:
    print("Age Group: Old Adult (31-65)")

print(f"Phone:+66-{phonenumber}")
