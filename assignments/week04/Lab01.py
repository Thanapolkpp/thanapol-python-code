"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""

# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("pun",20, "bangkok", "Thailand")  # name, age, city, country
    hobbies = []

    while(True):
        print("\n===========Program List_and_Tuples =========")
        choice = input("Choose choice\n1:Display\n2:Add hobby\n3:Remove hobby\n4:Edit age\n5:Exit\nEnter: ")

        if choice=='1':
        # Your code here
            print(f"Name:{person[0]}\nAge:{person[1]}\nCity:{person[2]}\nContry:{person[3]}\nHobby:{hobbies}")
        
        elif choice=='2':
            hobby = input('What is your favorits hobby:')
            hobbies.append(hobby)

        elif choice=='3':
            hobbies.pop()

        elif choice=='4':
            personlist = list(person)
            age = int(input("How old are you :"))
            personlist[1] = age
            person = tuple(personlist)

        elif choice=='5':
            break

        else: 
            print("You choose NEW!!!!")
        

        

if __name__ == "__main__":
    personal_info_manager()



    