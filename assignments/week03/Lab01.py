# Complete this program to classify people by age
#age = int(input("Enter age: "))

# Add your if-elif-else statements here
# 0-12: Child
# 13-19: Teenager  
# 20-59: Adult
# 60+: Senior

# Your code here:


age = int(input("Enter age:"))

if 0 <= age <= 12 :
    print("You are Child") 
        
elif 13 <= age <= 19 :
    print("You are Teenager")
    
elif 20 <= age <= 59 :
    print("You are Adult")
       
elif 60 <= age :
    print("You are Senior")
        
else :
    print("You enter wrong")
