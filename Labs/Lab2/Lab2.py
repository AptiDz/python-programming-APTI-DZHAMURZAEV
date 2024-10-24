"""
Lab2 Maskininlärning av Apti Dzhamurzaev
"""


import math as mt
import matplotlib.pyplot as plt

"""
Grunduppgift
"""

# Nameing the variable for the datapoints text file
datapokemon = "datapoints.txt"
# Storing as lists regarding widths, heights of the pokemon also storing the labels of the two pokemon types (0 for Pichu and 1 for Pikachu)
widths = []
heights = [] 
labels = [] 
# Data file opening to read mode
with open(datapokemon, "r") as datapokemons:
# Looping through from start to end on each row of data in the file now called datapokemons
    for data in datapokemons:
        # Skips the row that starts with string (
        if data.startswith("("):
            continue
        # Spliting the data by commas so it separates lists in width, height and labels
        dataparts = data.split(",")
        # Converting the strings to float data types. Int for label it does not posses decimals. The indexes for lists goes by that specific order
        width = float(dataparts[0])
        height = float(dataparts[1])
        label = int(dataparts[2]) 
        # Appending the dataparts to store into the lists of the pokemon
        widths.append(width)
        heights.append(height)
        labels.append(label) 


# Creating the lists to store Pichu data        
pichu_widths = []
pichu_heights = []
# Creating the lists to store Pikachu data        
pikachu_widths = []
pikachu_heights = []          
# Looping through all data of the labels
for label in range(len(labels)):
    if labels[label] == 0:
        # If label is 0, Its the pokemon Pichu (It follows indexes from lists Labels and adds the widths and heights the same order)
        pichu_widths.append(widths[label])
        pichu_heights.append(heights[label])
    else:
        # if Label is anything else its Pikachu (datapokemons) didnt have any other label besides 0 or 1)
        pikachu_widths.append(widths[label])
        pikachu_heights.append(heights[label])  
  
   
# Creating a scatter plot for Pichus
plt.scatter(pichu_widths, pichu_heights, color="orange", label="Pichu")
# Creating a scatter plot for Pikachus
plt.scatter(pikachu_widths, pikachu_heights, color="yellow", label="Pikachu")
# Labeling the axes
plt.xlabel("Width (cm)")        
plt.ylabel("Height (cm)")   
# Axes values with increment of 1
x_values = list(range(16, 29))
y_values = list(range(28, 43))
# Axes ticks to show the values
plt.xticks(x_values)
plt.yticks(y_values)
# Adds Legends to show which dots aka scatter represents Pichus and Pikachus
plt.legend()
# Adds the grid to easier see where the dots are in the axes
plt.grid()
# Displaying the plot
plt.show()


# Creating function by recreating euclidean distance formula.
def euclidean_distance(x2, x1, y2, y1):
    # Applying the formula to the function
    return mt.sqrt((x2-x1)**2 + (y2-y1)**2)
  
  
# Nameing the variable for the testpoints text file
testpokemon = "testpoints.txt"
# Test file opening to read mode
with open(testpokemon, "r") as testpokemons:
    # Looping through each line in the test file
    for testdata in testpokemons:
        # Skips the row that starts with string T
        if testdata.startswith("T"):
            continue
        # Creating new variabel with cleaned the imported test file by removing commas and paranthesis
        cleaned_testdata = testdata.strip().replace("(", "").replace(")", "").replace(",", "")
        # Creating a new variabel for spliting the string into separate elements applies by whitespace inside a list
        more_cleaned_testdata = cleaned_testdata.split()
        # Variabel created in float format. The indexes inside the list goes by that order as index 0 is just a number by order of the test point without any other meaning. 
        test_width = float(more_cleaned_testdata[1])
        test_height = float(more_cleaned_testdata[2])
        # Making variables to find nearest distance for prediction for pokemon. nearest_distance as infinity float to make it bigger than any natural number as a beginning step and nearest_label as none for placeholder. 
        nearest_distance = float("inf")
        nearest_label = None 
        #Looping through to stored list of pokemon data
        for i in range(len(widths)):
            # Calculationg the euclidean distance between the test point and current data of stored list of pokemon
            distance = euclidean_distance(test_width, widths[i], test_height, heights[i])
            # Updating the nearest distance and label to the current data point.
            if distance < nearest_distance:
                nearest_distance = distance
                nearest_label = labels[i]
        # Printing the test points based on the label of its nearest label. 
        if nearest_label == 0:
            print(f"Sample with (width, height): ({test_width}, {test_height}) classified as Pokemon - Pichu")
        else:
            print(f"Sample with (width, height): ({test_width}, {test_height}) classified as Pokemon - Pikachu")


"""
Uppgifter 1 & 2
"""

# Defining function to be able to input with how many nearest point it will be compared to.
def user_input_pokemon_data(nearest_points):
    # Creating empty list to store distances and labels as tuples
    pokemon_list = [] 
    # Creating loop that gives user choice to input the data
    while True:
        print("Wanna find out which of the pokemon you got?")
        user_choice  = input("input -> y <- for yes ")
        #Creating try, except ValueError to handle the wrong input
        try: 
            if user_choice == "y":
                # Asks user to input width and height and gives error if its other input then positiv numbers
                user_width = float(input("What is your pokemons testpoints, start with width? "))
                if user_width <= 0:
                    raise ValueError("Width has to be positiv number")
                user_height = float(input("What is your pokemons testpoints, start with height? "))
                if user_height <= 0:
                    raise ValueError("Height has to be positiv number")
                #Looping through to stored list of pokemon data in goal to calculate distances which each width and height data and store the calculated distances with each label as tuple
                for step in range(len(widths)):
                    input_distance = euclidean_distance(user_width, widths[step],  user_height, heights[step])
                    pokemon_list.append((input_distance, labels[step]))

            # Loop Broken because of the other input than y
            else: 
                print("Your not a pokemon fan, Good Bye!")
            break 
            
        except ValueError as err:
                # Catch and show errors related to wrong input
                print(f"Input error: {err}. Please enter positiv numbers")    
    
    # Sorting the list of calculated distances and labels. 
    sorted_list = sorted(pokemon_list)
    # Slicing the list to get range of nearest points. Thanks to sort before. Its possible to pick them up.
    slice_list = sorted_list[:nearest_points]
    # Creating empy list to store labels and nearest distance for the pokemon.
    pichu_label_list = []
    pikachu_label_list = []
    pichu_distance_list = []
    pikachu_distance_list = []

    # Go through the nearest points and separate them and add them to their respective lists based on labels
    for slice in slice_list:
        print(f"{slice[0]}, {slice[1]}")
    
        if slice[1] == 0:
            pichu_label_list.append(slice[1])
            pichu_distance_list.append(slice[0])
        else:
            pikachu_label_list.append(slice[1])
            pikachu_distance_list.append(slice[0])
            
            
            
    # To not print pokemon if user declines to input. Pokemon is reveade by majority of specifik typ in their labels if they are not in equal number otherwise the closer distance is choosen.
    if user_choice == "y":   
        if len(pichu_label_list) > len(pikachu_label_list):
            print(f" The user input with (width, height, nearest point(s)): ({user_width}, {user_height}, {nearest_points}) classified as Pokemon - Pichu")   
        elif len(pichu_label_list) == len(pikachu_label_list):   
            if sum(pichu_distance_list) > sum(pikachu_distance_list):
                print(f" The user input with (width, height, nearest point(s)): ({user_width}, {user_height}, {nearest_points}) classified as Pokemon - Pichu")   
            else:
                print(f" The user input with (width, height, nearest point(s)): ({user_width}, {user_height}, {nearest_points}) classified as Pokemon - Pichu")   
        else:
            print(f" The user input with (width, height, nearest point(s)): ({user_width}, {user_height}, {nearest_points}) classified as Pokemon - Pikachu")   
        
# Loop to get number of nearest points from the user also you have ability to input integer 1, 10 or any other positiv integer.        
while True:
    try:
        nearest_point = int(input("User how many nearest point(s) do you wanna use? "))
        if nearest_point > 0:
            user_input_pokemon_data(nearest_point)
            break
        else:
            raise ValueError("You have to input positive integer")
    except ValueError as err:
            print(f"Input error: {err}. Please enter positiv integer")    


        

"""
References 
1. AI24-Programming (2024, september 20). Github. Retrieved from: https://github.com/pr0fez/AI24-Programmering
2. Python Infinity(inf) (2023, december 27). GeeksforGeeks. Retrieved from: https://www.geeksforgeeks.org/python-infinity/
3. Pyhon None Keyword (2023, april 26). GeeksforGeeks. Retrieved from: https://www.geeksforgeeks.org/python-none-keyword/?ref=header_outind
4. Python Continue Statement (2023, april 09). GeeksforGeeks. Retrieved from: https://www.geeksforgeeks.org/python-continue-statement/?ref=header_outind
5. Python String replace() Method (2024, juli 05). GeeksforGeeks. Retrieved from: https://www.geeksforgeeks.org/python-string-replace/?ref=header_outind
6. Python | String startswitch() (2023, juli 20). GeeksforGeeks. Retrieved from: https://www.geeksforgeeks.org/python-string-startswith/?ref=header_outind
7. Python - Created a List of Tuples (2023, december 27). GeeksforGeeks. Retrieved from: https://www.geeksforgeeks.org/python-create-a-list-of-tuples/
8. Python - List of Slicing (2024, june 20). GeeksforGeeks. Retrieved from: https://www.geeksforgeeks.org/python-list-slicing/
9. sum() function in Python (2024, june 28). GeeksforGeeks. Retrieved from: https://www.geeksforgeeks.org/sum-function-python/
"""