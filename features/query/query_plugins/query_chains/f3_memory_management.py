import json
import sys
import os
import json
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def status_memory():
    status = json.load(open("memory.json"))["status"]

    if status == "inactive": # unused?
        from f2_handbook_management import process_handbook
        return process_handbook()

    elif status == "objective":
        from f4_trajectory_and_actions import objective
        return objective()

    elif status == "dossier":
        from core.f4_trajectory_and_actions import dossier
        return dossier()
        
    
    elif status == "gpt_instructions":
        from core.f6_user_interaction import gpt_instructions
        return print("Halt") #gpt_instructions()  # function / template

    elif status == "terminal_instructions":
        from core.f6_user_interaction import terminal_instructions
        return terminal_instructions()  # function / template

    elif status == "display_work":
        from core.f6_user_interaction import display_work
        return display_work()
    
    elif status == "user_feedback":
        from core.f6_user_interaction import user_feedback
        return user_feedback()    

    elif status == "execute_work":
        from core.f4_trajectory_and_actions import execute_work
        return execute_work()

    elif status == "modify_work":
        from core.f4_trajectory_and_actions import modify_work
        return modify_work()
    
    elif status == "archive_memory":
        return archive_memory()

    elif status == "execute_memory":
        return execute_memory()


def update_memory(target):
    with open("memory.json", "r") as file:
        memory_data = json.load(file)
    memory_data[target[0]] = target[1]
    with open("memory.json", "w") as file:
        json.dump(memory_data, file)    

    print("\nMemory updated: ", target)
    return status_memory()

def read_memory(variable):
    with open("memory.json", "r") as file:
        memory_data = json.load(file)
    memory = memory_data[variable]
    return memory


def archive_memory():
    print("Do you want to save or discard memory.json? (s/d)")
    user_input = input("Choice: ")
    if user_input == "s":
        history = json.load(open("history.json"))
        current_memory = json.load(open("memory.json"))
        history.append(current_memory)
        json.dump(history, open("history.json", "w"))
        print("Current memory.json saved in history.json.")        

    elif user_input == "d":
        print("Current memory.json discarded.")
        
    memory = {
        "status":"inactive",
        "objective":"",
        "theory":"",
        "theory_dossier":"",
        "theory_assessment":"",
        "theory_delegation":"",
        "theory_scripts_gpt":"",
        "theory_scripts_terminal":"",
        "display_work":"",
        "apply_theory":"",
        "modify":"",
        "modify_theory":"",
        "archive_memory":"",
        "execute_old_memory":"" 
        }
    json.dump(memory, open("memory.json", "w"))        
    return print ("memory archived")

def execute_memory():
    print("Executing an old memory...")
    # pass memory to memory.json
    # set status to memory.json
    return status_memory()