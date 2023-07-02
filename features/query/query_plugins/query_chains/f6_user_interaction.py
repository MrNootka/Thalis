import json
import sys
import os
import json
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from f3_memory_management import status_memory
def display_work():
    print("Do you want to see everything or theory_delegation? (all/td)")
    user_input = input("Choice: ")
    if user_input == "all":
        memory = json.load(open("memory.json"))
        print(memory)
    elif user_input == "td":
        memory = json.load(open("memory.json"))
        print(memory["theory_scripts_terminal"] + memory["theory_scripts_gpt"])
    return user_feedback()

def user_feedback():
    
    print("Apply theory or modify something? (apply/modify)")
    user_input = input("Choice: ")
    if user_input == "apply":
        memory = {"status": "apply_theory"}
        json.dump(memory, open("memory.json", "w"))
        return status_memory()

    elif user_input == "modify":
        memory = {"status": "modify_theory"}
        json.dump(memory, open("memory.json", "w"))
        return status_memory()