#!/bin/python

from house import House
from account import Account
import sys
import time

def get_hello():
    print "Welcome to the Intelligent House Manager!"
    print "Use numeric keys to navigate"
    print "You can return to main meny by pressing X"
    print "Jump up one hierachy level with U"
    print "Exit the application with Q"

def print_options(options):
    for key, value in options.iteritems():
        if (key != "name"):
            print "(" + str(key) + ") " + str(value)

def print_separator():
    print ""
    print 50 * "="
    print ""

def generate_function_dictionary():
    functions = {}
    functions["Quit"] = quit
    functions["Up"] = up
    functions["Return to Main Menu"] = return_to_main_menu
    functions["People in the house"] = get_people
    functions["Get next bus"] = get_next_bus
    functions["Check weather"] = get_weather
    functions["Tell a joke!"] = tell_joke
    functions["Check fridge"] = check_fridge
    functions["Shut down stove"] = shut_down_stove
    functions["Turn Stove on"] = turn_stove_on
    functions["Lock doors"] = lock_doors
    functions["Unlock doors"] = unlock_doors
    functions["Set alarm"] = set_alarm
    functions["Disable alarm"] = disable_alarm
    functions["Alarm state"] = alarm_state
    functions["Call 911"] = call_911
    return functions

def generate_option_dictionary():
    options = {}
    options["Main Menu"] = main_menu_options()
    options["Manage Applicances"] = applicance_options()
    options["People Interface"] = people_interface()
    options["Manage Security"] = security_options()
    options["Sauna"] = sauna_options()
    options["Check Kitchen"] = kitchen_options()
    options["Check Temperature"] = temperature_options()
    options["Butler"] = butler_options()
    return options

def main_menu_options():
    options = {}
    options["name"] = "Main Menu"
    options["1"] = "Manage Applicances"
    options["2"] = "Manage Security"
    options["3"] = "People Interface"
    options["4"] = "Call 911"
    options["5"] = "Check Kitchen"
    options["6"] = "Butler"
    options["7"] = "Check Temperature"
    options["Q"] = "Quit"
    return options

def applicance_options():
    options = {}
    options["name"] = "Manage Applicances"
    options["1"] = "Sauna"
    options["2"] = "Stove"
    options["3"] = "Lights"
    options["U"] = "Up"
    options["X"] = "Return to Main Menu"
    options["Q"] = "Quit"
    return options

def people_interface():
    options = {}
    options["name"] = "People Interface"
    options["1"] = "People in the house"
    options["2"] = "Sign in"
    options["3"] = "Sign out"
    options["4"] = "Schelude"
    options["U"] = "Up"
    options["X"] = "Return to Main Menu"
    options["Q"] = "Quit"
    return options

def security_options():
    options = {}
    options["name"] = "Manage Security"
    options["1"] = "Lock doors"
    options["2"] = "Unlock doors"
    options["3"] = "Set alarm"
    options["4"] = "Disable alarm"
    options["5"] = "Alarm state"
    options["U"] = "Up"
    options["X"] = "Return to Main Menu"
    options["Q"] = "Quit"
    return options

def sauna_options():
    options = {}
    options["name"] = "Sauna"
    options["1"] = "Get temperature"
    options["2"] = "Start heating"
    options["U"] = "Up"
    options["X"] = "Return to Main Menu"
    options["Q"] = "Quit"
    return options

def kitchen_options():
    options = {}
    options["name"] = "Check Kitchen"
    options["1"] = "Check fridge"
    options["2"] = "Shut down stove"
    options["3"] = "Turn Stove on"
    options["U"] = "Up"
    options["X"] = "Return to Main Menu"
    options["Q"] = "Quit"
    return options

def temperature_options():
    options = {}
    options["name"] = "Check Temperature"
    options["1"] = "Check Sauna temperature"
    options["2"] = "Check outside temperature"
    options["3"] = "Check temperature of a chosen room"
    options["U"] = "Up"
    options["X"] = "Return to Main Menu"
    options["Q"] = "Quit"
    return options

def butler_options():
    options = {}
    options["name"] = "Butler"
    options["1"] = "Get next bus"
    options["2"] = "Check weather"
    options["3"] = "Tell a joke!"
    options["U"] = "Up"
    options["X"] = "Return to Main Menu"
    options["Q"] = "Quit"
    return options

def quit():
    print "Exiting. Bye bye!"
    exit(0)

def up():
    option_stack.pop()

def return_to_main_menu():
    while len(option_stack) > 1:
        up()

def get_people():
    people = house.getPeople()
    print ""
    print "Currently there are following people in the house:"
    for person in people:
        print person

def get_next_bus():
    bus = house.getButler()
    print ""
    print bus

def get_weather():
    weather = house.getWeather()
    print ""
    print weather

def tell_joke():
    print ""
    print house.getJoke()

def check_fridge():
    print ""
    thing = str(raw_input("What would you like to check in your fridge?\n"))
    if (house.flipCoin()):
        print "There is " + thing + " still left."
    else:
        print "You are all out of " + thing + "."

def shut_down_stove():
    print ""
    if (house.getSwitch(2)):
        house.onOff(2)
        print "Shut down stove"
    else:
        print "Stove already shut down"

def lock_doors():
    if (house.doorsLocked):
        print "House is already locked"
    else:
        print house.switchDoorState()

def unlock_doors():
    if (house.doorsLocked):
        print house.switchDoorState()
    else:
        print "Doors already unlocked"

def turn_stove_on():
    print ""
    if (house.getSwitch(2)):
        print "Stove already on."
    else:
        house.onOff(2)
        print "Stove turned on"

def call_911():
    print ""
    print "Notified the authorities."

def set_alarm():
    if (house.alarm):
        print "Alarm already on."
    else:
        pwd = str(raw_input("Enter yout password\n"))
        print house.switchAlarmState(pwd)

def disable_alarm():
    if (house.alarm):
        pwd = str(raw_input("Enter yout password\n"))
        print house.switchAlarmState(pwd)
    else:
        print "Alarm already off."

def alarm_state():
    if (house.alarm):
        print "Alarm is on."
    else:
        print "Alarm is off."

def print_breadcrumb(option_stack):
    print ""
    print "Current location in application"
    for option in option_stack:
        sys.stdout.write(option["name"])
        sys.stdout.write(" >> ")
    print ""

def read_input(name):
    while True:
        print ""
        selection = str(raw_input("Select your action\n")).upper()
        if (selection in options[name]):
            selection = options[name][selection]
            print "Selected: " + selection
            if (selection in functions):
                functions[selection]()
            return selection
        else:
            print "No option " + selection + " available. Choose something else"

options = generate_option_dictionary()
functions = generate_function_dictionary()
option_stack = []
house = House(Account("Foo", "bar"))


def main():
    current_option = "Main Menu"
    functions = generate_function_dictionary()
    print_separator()
    get_hello()
    print_separator()
    option_stack.append(options[current_option])
    print_breadcrumb(option_stack)
    print_separator()
    print_options(options[current_option])
    while (True):
        current_option = read_input(option_stack[-1]["name"])
        if (current_option in options):
            option_stack.append(options[current_option])
        print_breadcrumb(option_stack)
        print_options(option_stack[-1])

main()

# Add status method
