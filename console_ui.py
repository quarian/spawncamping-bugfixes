#!/bin/python

from house import House
from account import Account
import sys
import time
import getpass

def get_hello():
    print "Welcome to the Intelligent House Manager!"
    print "Use numeric keys to navigate"
    print "You can return to main meny by pressing X"
    print "Jump up one hierachy level with U"
    print "Exit the application with Q"
    print "Commands are not case sensitive."

def get_help():
    global message
    message = "Numeric keys to navigate.\n"
    message += "X for main menu\n"
    message += "U to go up a hierarchy level.\n"
    message += "Exit the aaplication with Q.\n"
    message += "Commands are not case sensitive."

def print_options(options):
    for key, value in sorted(options.iteritems()):
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
    functions["Turn on lights"] = lights_on
    functions["Turn off lights"] = lights_off
    functions["Turn on stove"] = stove_on
    functions["Turn off stove"] = stove_off
    functions["Alarm state"] = alarm_state
    functions["Check Sauna temperature"] = sauna_temperature
    functions["Check outside temperature"] = outside_temperature
    functions["Check temperature of a chosen room"] = chosen_temperature
    functions["Call 911"] = call_911
    functions["Help"] = get_help
    functions["Schelude"] = get_schelude
    functions["Sign in"] = sign_in
    functions["Sign out"] = sign_out
    functions["Start heating"] = start_heating
    functions["Power down sauna"] = kill_sauna
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
    options["Lights"] = light_options()
    options["Stove"] = stove_options()
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
    options["H"] = "Help"
    return options

def applicance_options():
    options = {}
    options["name"] = "Manage Applicances"
    options["1"] = "Sauna"
    options["2"] = "Stove"
    options["3"] = "Lights"
    options["U"] = "Up"
    options["X"] = "Return to Main Menu"
    options["H"] = "Help"
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
    options["H"] = "Help"
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
    options["H"] = "Help"
    options["Q"] = "Quit"
    return options

def sauna_options():
    options = {}
    options["name"] = "Sauna"
    options["1"] = "Check Sauna temperature"
    options["2"] = "Start heating"
    options["3"] = "Power down sauna"
    options["U"] = "Up"
    options["X"] = "Return to Main Menu"
    options["H"] = "Help"
    options["Q"] = "Quit"
    return options

def kitchen_options():
    options = {}
    options["name"] = "Check Kitchen"
    options["1"] = "Check fridge"
    options["3"] = "Turn off stove"
    options["2"] = "Turn on stove"
    options["U"] = "Up"
    options["X"] = "Return to Main Menu"
    options["H"] = "Help"
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
    options["H"] = "Help"
    options["Q"] = "Quit"
    return options

def light_options():
    options = {}
    options["name"] = "Lights"
    options["1"] = "Turn on lights"
    options["2"] = "Turn off lights"
    options["U"] = "Up"
    options["X"] = "Return to Main Menu"
    options["H"] = "Help"
    options["Q"] = "Quit"
    return options

def stove_options():
    options = {}
    options["name"] = "Stove"
    options["1"] = "Turn on stove"
    options["2"] = "Turn off stove"
    options["U"] = "Up"
    options["X"] = "Return to Main Menu"
    options["H"] = "Help"
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
    options["H"] = "Help"
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
    global message
    people = house.getPeople()
    print ""
    message = "Currently there are following people in the house:\n\n"
    for person in people:
        message += person + "\n"

def get_next_bus():
    global message
    bus = house.getButler()
    print ""
    message = bus

def get_weather():
    global message
    weather = house.getWeather()
    print ""
    message = weather

def tell_joke():
    print ""
    global message
    message = house.getJoke()

def check_fridge():
    print ""
    global message
    thing = str(raw_input("What would you like to check in your fridge?\n"))
    if (house.flipCoin()):
        message = "There is " + thing + " still left."
    else:
        message = "You are all out of " + thing + "."

def shut_down_stove():
    print ""
    global message
    if (house.getSwitch(2)):
        house.onOff(2)
        message = "Shut down stove"
    else:
        message = "Stove already shut down"

def lock_doors():
    global message
    if (house.doorsLocked):
        message = "House is already locked"
    else:
        message = house.switchDoorState()

def unlock_doors():
    global message
    if (house.doorsLocked):
        message = house.switchDoorState()
    else:
        message = "Doors already unlocked"

def turn_stove_on():
    print ""
    global message
    if (house.getSwitch(2)):
        message = "Stove already on."
    else:
        house.onOff(2)
        message = "Stove turned on"

def call_911():
    print ""
    global message
    message = "Notified the authorities."

def set_alarm():
    global message
    if (house.alarm):
        message = "Alarm already on."
    else:
        pwd = str(raw_input("Enter your password\n"))
        message = house.switchAlarmState(pwd)

def disable_alarm():
    global message
    if (house.alarm):
        pwd = str(raw_input("Enter yout password\n"))
        message = house.switchAlarmState(pwd)
    else:
        message = "Alarm already off."

def alarm_state():
    global message
    if (house.alarm):
        message = "Alarm is on."
    else:
        message = "Alarm is off."

def sauna_temperature():
    global message
    temperature = house.getTemperature(0)
    message = "Your sauna's temperature is " + str(temperature) + " degrees celsius."

def outside_temperature():
    global message
    temperature = house.getTemperature(2)
    message = "Outside temperature is " + str(temperature) + " degrees celsius."

def chosen_temperature():
    global message
    temperature = house.getTemperature(0)
    room = str(raw_input("Which room's temperature would you like to know?\n"))
    message = room.title() + "'s temperature is " + str(temperature) + " degrees celsius."

def lights_on():
    global message
    if (house.getSwitch(3)):
        message = "Lights are already on."
    else:
        message = "Lights turned on."
        house.onOff(3)

def lights_off():
    global message
    if (not house.getSwitch(3)):
        message = "Lights are already off."
    else:
        message = "Lights turned off."
        house.onOff(3)

def stove_on():
    global message
    if (house.getSwitch(2)):
        message = "Stove is already on."
    else:
        message = "Stove turned on."
        house.onOff(2)

def stove_off():
    global message
    if (not house.getSwitch(2)):
        message = "Stove is already off."
    else:
        message = "Stove turned off."
        house.onOff(2)

def get_schelude():
    global message
    message = 22 * "_" + "\n"
    message += "People:\tMatti\tTeppo\n" 
    message += "At:\tYoga\tMarket\n"
    message += 22 * "-"

def sign_in():
    global message
    message = house.account.name + " signed into the house."

def sign_out():
    global message
    message = house.account.name + " signed out of the house."

def start_heating():
    global message
    target_time = str(raw_input("When would you like to have your sauna ready?\n"))
    message = "Your sauna will be ready at " + target_time + "."
    if (not house.getSwitch(1)):
        house.onOff(1)

def kill_sauna():
    global message
    if (house.getSwitch(1)):
        message = "Turned off sauna."
        house.onOff(1)
    else:
        message = "Sauna already off."

def print_breadcrumb(option_stack):
    print ""
    print "Current location in application:"
    for option in option_stack:
        sys.stdout.write(option["name"])
        sys.stdout.write(" >> ")
    print ""
    print ""

def login():
    global house
    print "Log in to the smart house."
    print "Note that password input is masked."
    username = str(raw_input("Username:\n"))
    password = str(getpass.getpass("Password:\n"))
    house = House(Account(username, password))

def read_input(name):
    global message
    while True:
        print ""
        if (message != ""):
            print message
        print ""
        message = ""
        selection = str(raw_input("Select your action\n")).upper()
        if (selection in options[name]):
            selection = options[name][selection]
            print "Selected: " + selection
            if (selection in functions):
                functions[selection]()
            return selection
        else:
            print "No option " + selection + " available. Choose on of the listed commands."

options = generate_option_dictionary()
functions = generate_function_dictionary()
option_stack = []
#house = House(Account("Foo", "bar"))
message = ""


def main():
    login()
    current_option = "Main Menu"
    functions = generate_function_dictionary()
    print_separator()
    get_hello()
    print_separator()
    option_stack.append(options[current_option])
    print_breadcrumb(option_stack)
    print_options(options[current_option])
    while (True):
        current_option = read_input(option_stack[-1]["name"])
        if (current_option in options):
            option_stack.append(options[current_option])
        print_breadcrumb(option_stack)
        print_options(option_stack[-1])

main()

# Add status method
