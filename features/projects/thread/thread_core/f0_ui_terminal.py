import json
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from core.f1_pilot import start_query
from features.introspection.guided_introspection import guided_introspection
from features.converse.conversational_gpt import engage_gpt


def ui_terminal():
    while True:
        print("\nWelcome to Thalis!")
        print("Choose an option:")
        print("1. Query")
        print("2. Guided introspection")
        print("3. Converse with GPT")
        print("4. - Exit")

        while True:  # Add loop
            try:
                user_choice = int(input("\nYour choice (Number): "))
                if user_choice not in [1, 2, 3, 4]:  # Check if input is among the valid choices                   
                    raise ValueError("Invalid option. Please choose from the available options.")
                break  # If input is valid, break the loop to proceed.
            except ValueError as e:
                print(e)  # Print the error message
        if user_choice == 1:
            start_query()
        elif user_choice == 2:
            guided_introspection()
        elif user_choice == 3:
            engage_gpt()
        elif user_choice == 4:
            # Instead of breaking, print a goodbye message and quit the application completely.
            print("Thank you for using Thalis. Goodbye!")
            sys.exit()


if __name__ == "__main__":
    ui_terminal()
