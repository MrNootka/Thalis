import json
import sys
import os
import json
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


def process_handbook(user):
    from f3_memory_management import status_memory, update_memory
    with open("context.txt", "r") as context_file:
        context = context_file.read()

    with open("handbook.json", "r") as handbook_file:
        handbook_data = json.load(handbook_file)

    handbook_data["context"] = context
    handbook_data["user"] = user

    handbook_data["prompt"] = context + ". ¬ " + user


    with open("handbook.json", "w") as handbook_file:
        json.dump(handbook_data, handbook_file)

    
    print("\nHandbook processed")
    target = ["status","objective"]
    update_memory(target) # update status
    
    return status_memory

def read_handbook(variable):
    with open("handbook.json", "r") as file:
        variable_data = json.load(file)
    
    variable = variable_data[variable]
    return variable



