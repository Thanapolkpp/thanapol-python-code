"""
Write a program that analyzes daily temperatures for a week:

Create a function get_temperatures() that:

- Uses a local list to store 7 temperature values (use input or predefined values)
- Returns the list

Create a function analyze_temps(temp_list) that:

- Calculates and returns the average temperature (local variable)
- Finds and returns the highest temperature
- Finds and returns the lowest temperature
- Returns all three values as a tuple

Create a function display_analysis(avg, high, low) that prints the results nicely formatted

Example Output:
Temperature Analysis for the Week:
Average: 23.5 C
Highest: 28 C
Lowest: 19 C

"""
def get_temperatures():
    temp7day = []
    for i in range(0,7):
        tempday= int(input(f"What is temp/day {i+1}: "))
        temp7day.append(tempday)
    return temp7day

def analyze_temps(temp_list):
    sum =0
    for i in temp_list :
        sum+= i
    avg = sum/7

    highest_temp = max(temp_list)
    lowest_temp = min(temp_list)

    return (avg,highest_temp,lowest_temp)

def display(avg,high,low):
    print(f"Temperature Analysis for the Week:\nAverage: {avg:} C \nHighest: {high} C \nLowest: {low} C")

list = get_temperatures()
result = analyze_temps(list)
display(*result)