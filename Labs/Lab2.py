import math as mt
import matplotlib.pyplot as plt


widths = [] # storing the widths of the pokemon
heights = [] # storing the heights of the pokemon
labels = [] # storing the labels of the two pokemon (0. Pichu or 1. Pikachu)

# Nameing the variable for the datapoints text file
datapokemon = "datapoints.txt"

# Data file opening to read mode
with open(datapokemon, "r") as datapokemons:
    # Looping through each row of data in the file now called datapokemons
    for data in datapokemons:
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
        # if Label is anything else its Pikachu (Datapointers didnt have any other label besides 0 or 1)
        pikachu_widths.append(widths[label])
        pikachu_heights.append(heights[label])  
        
# Creating a scatter plot for Pichus
plt.scatter(pichu_widths, pichu_heights, color="orange", label="Pichu")
# Creating a scatter plot for Pikachus
plt.scatter(pikachu_widths, pikachu_heights, color="yellow", label="Pikachu")
# Labeling the axes
plt.xlabel("Width (cm)")        
plt.ylabel("Height (cm)")   
# Adds Legends to show which dots represents Pichus and Pikachus
plt.legend()
# Adds the grid to easier see where the dots are in the axes
plt.grid()
# Displaying the plot
plt.show()
     

        
 


testpath = "testpoints.txt"

with open(testpath, "r") as testpointers:
    testpointers = testpointers.read()
    
print(testpointers)



