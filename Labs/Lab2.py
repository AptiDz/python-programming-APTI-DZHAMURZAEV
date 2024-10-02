"""
Lab2 Maskinlära av Apti Dzhamurzaev
"""


import math as mt
import matplotlib.pyplot as plt


# storing as lists regarding widths, heights of the pokemon also storing the labels of the two pokemon types (0 for Pichu and 1 for Pikachu)
widths = []
heights = [] 
labels = [] 


# Nameing the variable for the datapoints text file
datapokemon = "datapoints.txt"


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
def euclidean_distance(x1, x2, y1, y2):
    dx = x2 - x1
    dy = y2 - y1
    # Applying the formula to the function
    euc_distance = mt.sqrt((dx)**2 + (dy)**2)
    return euc_distance

  
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
        
        
        #Looping through to stored list of pokemon data with goal in finding nearest distance.
        for i in range(len(widths)):
            # Calculationg the euclidean distance between the test point and current data of stored list of pokemon
            distance = euclidean_distance(widths[i], test_width, heights[i], test_height)
            # Updating the nearest distance and label to the current data point.
            if distance < nearest_distance:
                nearest_distance = distance
                nearest_label = labels[i]
                        
        
        # Printing the test points based on the label of its closets distance. 
        if nearest_label == 0:
            print(f"Sample with (width, height): ({test_width}, {test_height}) classified as Pichu")
        else:
            print(f"Sample with (width, height): ({test_width}, {test_height}) classified as Pikachu")

# Making variables to find nearest distance regarding inputs
nearest_distance_input = float("inf")
nearest_label_input = None

# Creating loop that gives user choice to input the data
while True:
    print("Wanna find out which of the pokemon you got?")
    user_choice  = input("input -> y <- for yes ")
    #Creating ValueError to handle wrong input
    try: 
        if user_choice == "y":
            
            # Asks user to input width and height and gives error if its other input then positiv numbers
            user_width = float(input("What is your pokemons testpoints, start with width? "))
            if user_width <= 0:
                raise ValueError("Width has to be positiv number")
            
            user_height = float(input("What is your pokemons testpoints, start with height? "))
            if user_height <= 0:
                raise ValueError("Height has to be positiv number")
            
            
            #Looping through to stored list of pokemon data with goal in finding nearest distance comparison to input value.
            for i in range(len(widths)):
                input_distance = euclidean_distance(widths[i], user_width, heights[i], user_height)
            # Updating the nearest distance input and label to the current data point.           
            if input_distance < nearest_distance_input:
                nearest_distance_input = input_distance
                nearest_label_input = labels[i]
                
                
            # Printing the test points based on the label of its closets distance. 
            if nearest_label_input == 0:
                print(f"Sample with (width, height): ({user_width}, {user_height}) classified as Pichu")
            else:
                print(f"Sample with (width, height): ({user_width}, {user_height}) classified as Pikachu")
       
        # Loop Broken because of the other input than y
        else: 
            print("Good Bye")
        break 
        
    except ValueError as err:
            # Catch and display errors related to invalid input
            print(f"Input error: {err}. Please enter positiv numbers")    
            
       


"""
References 
1. AI24-Programming (2024, september 20). Hämtad från: https://github.com/pr0fez/AI24-Programmering
2. Python Infinity(inf) (2023, december 27). GeeksforGeeks. Hämtad från: https://www.geeksforgeeks.org/python-infinity/
3. Pyhon None Keyword (2023, april 26). GeeksforGeeks. Hämtad från: https://www.geeksforgeeks.org/python-none-keyword/?ref=header_outind
4. Python Continue Statement (2023, april 09). Hämtad från: https://www.geeksforgeeks.org/python-continue-statement/?ref=header_outind
5. Python String replace() Method (2024, jul 05). Hämtad från: https://www.geeksforgeeks.org/python-string-replace/?ref=header_outind
6. Python | String startswitch() (2023, jul 20). Hämtad från: https://www.geeksforgeeks.org/python-string-startswith/?ref=header_outind
"""