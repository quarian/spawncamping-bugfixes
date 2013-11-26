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

def main_menu_options():
    options = {}
    options["name"] = "Main Menu"
    options["1"] = "Manage applicances"
    options["2"] = "Manage security"
    options["3"] = "People interface"
    options["4"] = "Call 911"
    options["Q"] = "to quit"
    return options

def print_breadcrumb(option_stack):
    print "Current location in application"
    for option in option_stack:
        sys.stdout.write(option["name"])
        sys.stdout.write(" >> ")

def read_input(options):
    while True:
        print ""
        selection = str(raw_input("Select your action\n"))
        if (selection in options):
            print "Selected: " + options[selection]
            break
        else:
            print "No option " + selection + " available. Choose something else"


def main():
    options = {}
    option_stack = []
    print_separator()
    get_hello()
    print_separator()
    options = main_menu_options()
    option_stack.append(options)
    print_breadcrumb(option_stack)
    print_separator()
    print_options(options)
    read_input(options)

main()
