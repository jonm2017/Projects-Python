
# Jonathan Masino    6/17/2021    Assignment 4: Fuel Consumption    Dr. Marques

import csv
import pylab

def option_one():
    mpg_list = []
    mpg_min = input('Please enter the minimum MPG value you would like to use: ')
    mpg_max = input('Please enter the maximum MPG value you would like to use: ')
    with open('epadata2015.csv', 'r') as file2015:
        reader_2015 = csv.reader(file2015)
        for row in reader_2015:
            if row[10] >= mpg_min and row[10] <= mpg_max:
                temp = (row[2] + " " + row[3])
                mpg_list.append(temp)
        print("\nHere are all of the cars from 2015 that fall in the " + mpg_min + " to " + mpg_max + " MPG range:\n")
        for i in mpg_list:
            print(i)
    file2015.close()

def option_two():
    userChoice = input('Please choose a measurement: Highway MPG (H), City MPG (C) or Overall MPG (O): ')
    if userChoice == 'H':
        highway_mpg()
    elif userChoice == 'C':
        city_mpg()
    elif userChoice == 'O':
        overall_mpg()
    else:
        print('Invalid entry, try again.')
        option_two()

def highway_mpg():
    label = "Highway MPG"
    file2020 = open('epadata2020.csv', 'r')
    x, y = [], []
    reader_highway = csv.reader(file2020)
    next(reader_highway)
    for row in reader_highway:
        x.append(row[0])
        y.append(row[6])
    file2020.close()
    display = input('Would you like to display the plot to the screen (D) or to a file (F): ')
    if display != "D" and display != "F":
        print("Invalid input, try again.")
        overall_mpg()
    else:
        display_plot(x, y, label, display)

def city_mpg():
    label = "City MPG"
    file2020 = open('epadata2020.csv', 'r')
    x, y = [], []
    reader_city = csv.reader(file2020)
    next(reader_city)
    for row in reader_city:
        x.append(row[0])
        y.append(row[5])
    file2020.close()
    display = input('Would you like to display the plot to the screen (D) or to a file (F): ')
    if display != 'D' and display != 'F':
        print("Invalid input, try again.")
        city_mpg()
    else:
        display_plot(x, y, label, display)

def overall_mpg():
    label = "Overall MPG"
    file2020 = open('epadata2020.csv', 'r')
    x, y = [], []
    reader_overall = csv.reader(file2020)
    next(reader_overall)
    for row in reader_overall:
        x.append(row[0])
        y.append(row[4])
    file2020.close()
    display = input('Would you like to display the plot to the screen (D) or to a file (F): ')
    if display != 'D' and display != 'F':
        print("Invalid input, try again.")
        overall_mpg()
    else:
        display_plot(x, y, label, display)
        

def display_plot(xcoord, ycoord, label, screen_or_file):
    pylab.plot(xcoord, ycoord)
    pylab.xlabel(label)
    pylab.ylabel("Year")
    pylab.title("EPA Annual Average " + label + " Data")
    if screen_or_file == 'D':
        pylab.show()
    elif screen_or_file == 'F':
        pylab.savefig("epa_plot.png")

print("\nWelcome. In this assingment, we use CSV files to find and print cars that fall in an MPG range.")
print("We also create a plot with either the Highway MPG, City MPG, or Overall MPG. The user gets to choose.")
print("The plot can be displayed on the screen or saved to a file, the user also gets to choose which one.\n")
playagain = "y"
while playagain == 'y':
    option = input('Please choose enter 1 for Milage Info or 2 for Trend Plot: ')
    if option == "1":
        option_one()
    elif option == "2":
        option_two()
    else:
        print("Invalid input")
    playagain = input('Would you like to play again? (y/n): ')
print("Thank you, have a nice day.")