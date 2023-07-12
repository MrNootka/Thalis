import json
import sys
import os
import json
from f3_memory_management import status_memory
os.chdir(os.path.dirname(os.path.abspath(__file__)))
def pilot_terminal():
    # Execute terminal actions on the computer
    # read the scripts from memory.json and execute them
    return status_memory()