# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

import statistics


def display_main_menu():
    print("Enter Some numbers separated by spaces (e.g 5 67 32)")

def calc_average(val2):
    avg = sum(val2)/len(val2)
    average = float(avg)
    print("The average is ", average)

def get_user_input():
    val = input("INPUT:")
    print("values are: ", val)
    val1 = val.split()
    for i in range(len(val1)):
        val1[i] = float(val1[i])
    return val1


def find_min_max(val2):
    print("minimum :", min(val2))
    print("maximum :", max(val2))

def sort_temperature(val2):
    sortval = sorted(val2)
    print("sorted in ascending: ", sortval)

def calc_median_temperature(val2):
    print("The median Number is: ", statistics.median(val2))

print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to python")
display_main_menu()
val2 = get_user_input()
calc_average(val2)
find_min_max(val2)

sort_temperature(val2)
calc_median_temperature(val2)




