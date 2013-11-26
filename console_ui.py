#!/bin/python

import sys

def get_hello():
    print "Welcome to the Intelligent House Manager!"
    print "Use numeric keys to navigate"
    print "You can return to main meny by pressing X"
    print "Jump up one hierachy level with Y"
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
    return functions

def generate_option_dictionary():
    options = {}
    options["Main Menu"] = main_menu_options()
    options["Manage Applicances"] = applicance_options()
    options["People Interface"] = people_interface()
    options["Manage Security"] = security_options()
    options["Sauna"] = sauna_options()
    return options

def main_menu_options():
    options = {}
    options["name"] = "Main Menu"
    options["1"] = "Manage Applicances"
    options["2"] = "Manage Security"
    options["3"] = "People Interface"
    options["4"] = "Call 911"
    options["Q"] = "Quit"
    return options

def applicance_options():
    options = {}
    options["name"] = "Manage Applicances"
    options["1"] = "Sauna"
    options["2"] = "Stove"
    options["3"] = "Lights"
    options["X"] = "Up"
    options["Q"] = "Quit"
    return options

def people_interface():
    options = {}
    options["name"] = "People Interface"
    options["1"] = "Status"
    options["2"] = "Sign in"
    options["3"] = "Sign out"
    options["4"] = "Schelude"
    options["X"] = "Up"
    options["Q"] = "Quit"
    return options

def security_options():
    options = {}
    options["name"] = "Manage Security"
    options["1"] = "Lock doors"
    options["2"] = "Unlock doors"
    options["X"] = "Up"
    options["Q"] = "Quit"
    return options

def sauna_options():
    options = {}
    options["name"] = "Sauna"
    options["1"] = "Get temperature"
    options["2"] = "Start heating"
    options["X"] = "Up"
    options["Q"] = "Quit"
    return options

def quit():
    print "Exiting. Bye bye!"
    exit(0)

def up():
    option_stack.pop()

def print_breadcrumb(option_stack):
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
