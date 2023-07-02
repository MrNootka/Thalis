import json
import sys
import os
import json
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from f3_memory_management import status_memory, update_memory

def objective():
    from core.f5_gpt_interpreter import gpt4_api
    from core.f2_handbook_management import read_handbook
    
    # craft the prompt to send to gpt api
    handbook_prompt = read_handbook("prompt")
    prefix="Please find the objective of this task:\n" # template
    suffix="\nStart your reply with 'The objective of this query is'" # check how formatting influences output
    api_prompt = (prefix + " " + handbook_prompt + suffix)
    print("\nFull prompt to send to api:\n ",api_prompt)
    gpt4_answer = gpt4_api(api_prompt)

    # fill memory.json objective value with gpt4 answer
    target = ["objective",gpt4_answer]
    with open("memory.json", "r") as file:
        memory_data = json.load(file)
    memory_data[target[0]] = target[1]
    with open("memory.json", "w") as file:
        json.dump(memory_data, file)    
    print("\nMemory updated: ", target)

    # update memory.json status to dossier
    target = ["status","dossier"]
    update_memory(target) # update status
    
    return status_memory() 

def dossier():
    from f3_memory_management import status_memory
    from f5_gpt_interpreter import gpt4_api
    # craft the prompt to send to gpt api
    memory_dossier = json.load(open("memory.json"))["objective"]
    memory_dossier_str = json.dumps(memory_dossier) 
    #??? content? dossier_str = memory_data["dossier"]["content"]
    prefix="""Please make a plan dossier for the objective. 
The purpose of this dossier is to use the power of gpt4 and the computer terminal if one of these two are needed.
The dossier must contain to lists, one for openAI gpt calls and one for computer terminal commands. 
Objective:
"""
    suffix="""Please answer in this format:

GPT messages to send
1.
2.
...

Terminal commands for windows 11
1.
2.
...'""" # check how formatting influences output
    api_prompt = (prefix + memory_dossier_str + "\n" + suffix )
    print("\nFull prompt to send to api:\n ",api_prompt)
    gpt4_answer = gpt4_api(api_prompt)

    # fill memory.json dossier value with gpt4 answer
    target = ["dossier",gpt4_answer]
    with open("memory.json", "r") as file:
        memory_data = json.load(file)
    memory_data[target[0]] = target[1]
    with open("memory.json", "w") as file:
        json.dump(memory_data, file)    
    print("\nMemory updated: ", target)

    # update memory.json status to 
    target = ["status","-"]
    update_memory(target) # update status
    return exit()


#########################################################

def execute_work():
    from f3_memory_management import status_memory
    memory = json.load(open("memory.json"))["apply_theory"]
    # Output and actions to apply_theory#
    # actions in theory do them
    return status_memory()

def modify_work():
    from f1_pilot import initialize_system
    from f3_memory_management import status_memory
    print("Execution halted, open 'memory.json' and apply changes. Write 'continue' to proceed or 'reboot' to start over.")
    user_input = input("Action: ")
    if user_input == "continue":
        print("Continuing...")
        memory = {"status": "display_work"}
        json.dump(memory, open("memory.json", "w"))
        return status_memory()
    
    elif user_input == "reboot":
        print("Rebooting...")
        memory = {"status": "inactive"}
        json.dump(memory, open("memory.json", "w"))        
        return initialize_system()
    
    else:
        print("Invalid choice. Exiting...")
        return