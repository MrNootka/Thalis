import json
import sys
import os
import json
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from f3_memory_management import status_memory, read_memory
from f2_handbook_management import process_handbook

def initialize_system():
    # \\\ log_process() \\\ #
    
    return status_memory()

def log_process():
    # Log the process in logger.json
    pass

def start_query():
    # ------------ user_input = input("\nPlease enter your query: ")
    print("\nStart query")
    user_input = "write a poem about flowers and save it in a file called flowers.txt please"

    #~~~~process_handbook(user_input) 
    
    #initialize_system()    

    # print("do you want to start a new query or load old memory?")
    # user_input = input(" type n or m: ")


    # if user_input == "n"
    #   memory(status)="inactive"
    #   initialize_system()
    

    # if user_input == "m"
    #   print("Search for the memory or write the ID of the memory: ")
    #   print("type search or ID")?

    #   if user_input="search":  
    #       print("Here is a list of the memories:")  
    #       print memories with details
    #       print("submit the ID of the memory you want to load:") 
    #       load selected memory to memory.json 
    #       memory(status)="display work"
    #       initialize_system()

    #   if user_input="ID":
    #   load selected memory to memory.json     
    #   memory(status)="display work"
    #   initialize_system()


    # elif:
    #   print("wrong input, type n or m:")
    #   user_input = input(" ")