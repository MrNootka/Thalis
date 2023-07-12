import os
import json
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from f3_memory_management import read_memory

print(read_memory("dossier"))