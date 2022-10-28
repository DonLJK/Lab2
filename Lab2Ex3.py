# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
#    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.

# See PyCharm help at https://www.jetbrains.com/help/pycharm/




def display_main_menu():
    print("Enter Some numbers separated by spaces (e.g 5 67 32)")

def calc_average():
    print("calc_average")

def get_user_input():
    val = input("INPUT:")
    val1 = val.split()
    for i in range(len(val1)):
        val1[i] = float(val1[i])
    return val1


def find_min_max():
    print("find_min_max")

def sort_temperature():
    print("sort_temperature")

def calc_median_temperature():
    print("Cal_Median_temp")


print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to python")
display_main_menu()
get_user_input()
calc_average()

