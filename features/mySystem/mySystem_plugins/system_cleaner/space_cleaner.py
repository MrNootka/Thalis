import os
import shutil

# Get the current script directory
current_dir = os.path.dirname(os.path.realpath(__file__))

# Walk up the directory structure until we reach the "Thalis 30" directory
main_dir = current_dir
while os.path.basename(main_dir) != "Thalis":
    main_dir = os.path.dirname(main_dir)

# Delete any "__pycache__" directories
for root_dir, dirs, _ in os.walk(main_dir):
    if "__pycache__" in dirs:
        pycache_path = os.path.join(root_dir, "__pycache__")
        shutil.rmtree(pycache_path)
        print(f"Deleted __pycache__ directory in {root_dir}")