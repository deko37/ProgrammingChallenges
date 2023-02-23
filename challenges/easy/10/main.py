#!/usr/bin/python
# Programming challenge number 10 : To-do list app (cli)
from todo import *
import sys
import os
import pickle

def clear():
    if os.name == "posix":
        os.system("clear")
    elif os.name == "nt":
        os.system("cls")

def get_input() -> str:
    clear()
    print("TO-DO list tool from command line interface, at your disposal.\n"
          "Multiple choices are disponible to you : \n"
          "(a)ppend a to-do to your list\n"
          "(s)how your last to-does\n"
          "(c)heck a to-do\n"
          "(q)uit")
    user_choice = ''
    while not (user_choice := input("Choose between these options : ")) in "ascq" or len(user_choice) != 1:
        print("Please, choose a single and correct character.")
    return user_choice

def manage_inputs(to_do_list: list, user_choice: str):
    if user_choice == 'a':
        have_to_do = input("What do you have to do ? ")
        new_to_do(to_do_list, have_to_do)
    elif user_choice == 's':
        if to_do_list:
            print_informations(to_do_list)
        else:
            input("There is nothing to see. Press Enter...")
    elif user_choice == 'c':
        if to_do_list:
            print_informations(to_do_list, False)
            user_i = ''
            while True:
                user_i = input("Which to-do you want to check (write the number of the fixed to-do) ? ")
                try:
                    user_i = int(user_i) - 1
                    to_do_list[user_i]
                    break
                except:
                    print("Please, enter a valid number who is include in the range of your to-do list.")
            modify_todo(to_do_list, user_i)
        else:
            input("There is nothing to check. Press Enter...")
    else:
        print("Quitting...")
        write_on_file(to_do_list)
        clear()
        sys.exit()

def new_to_do(to_do_list: list, have_to_do: str):
    to_do_list.append(ToDo(have_to_do))

def write_on_file(to_do_list: list):
    with open("todolist.pkl", 'wb') as file:
        pickle.dump(to_do_list, file)

def print_informations(to_do_list: list, wait=True):
    for i, to_do in enumerate(to_do_list):
        if not to_do.checked:
            print(f"{i + 1} - {to_do}")
    if wait: input("Press any button...")

def modify_todo(to_do_list: list, i: int):
    to_do_list[i].check()

if __name__ == "__main__":
    to_do_list = []
    try:
        with open("todolist.pkl", 'rb') as file:
            to_do_list = pickle.load(file)
    except:
        with open("todolist.pkl", 'wb') as file:
            pickle.dump([], file)
    if sys.argv == 1:
        print_informations(to_do_list)
    else:
        while True:
            manage_inputs(to_do_list, get_input())

