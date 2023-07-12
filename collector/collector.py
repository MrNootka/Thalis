import os

def safe_join(*args):
    return os.path.normpath(os.path.join(*args))

current_script_path = os.path.dirname(os.path.abspath(__file__))
rootDir = safe_join(current_script_path, '..')

fout_path = safe_join(current_script_path, 'context.txt')
rootDir = os.path.normpath(rootDir)
maxDepth = 100
ignoreDirs = ['.git', "collector",'.misc', '__pycache__']
files_list = []

def print_tree(directory, file_output, prefix = ''):
    file_output.write(prefix + '+--' + os.path.basename(directory) + '/' + '\n')
   
    if len(os.listdir(directory)) > 0:  
        new_prefix = prefix + '|   '
    else:
        new_prefix = prefix + '    '

    for item in os.listdir(directory):
        if item in ignoreDirs or item == "__init__.py":
            continue 
        item_path = safe_join(directory, item)
        
        if os.path.isdir(item_path): 
            print_tree(item_path, file_output, new_prefix)
        else:
            # Store relative path from root directory instead of just file name.
            rel_path = os.path.relpath(item_path, start = rootDir)
            file_output.write(new_prefix + '+--' + rel_path + '\n') 
            files_list.append(rel_path)

with open(fout_path, 'w') as fout:
    fout.write("Folder structure of the source code:\n") 
    print_tree(rootDir, fout)

print("Select a file to append to context.txt:")

for i, f in enumerate(files_list):
    print(f"{i}. {f}")  

selected_file_indices = input("Enter the numbers corresponding to the files: ")
selected_file_indices = [int(k.strip()) for k in selected_file_indices.split(',') if k.strip().isdigit()]

for selected_file_index in selected_file_indices:
    if 0<= selected_file_index < len(files_list):
        selected_file = safe_join(rootDir, files_list[selected_file_index])  
    
        ## Check if the selected file exist
        if not os.path.isfile(selected_file):
            print(f"File '{selected_file}' does not exist. Please select another file.")
            continue
        
        with open(fout_path, 'a') as fout:
            fout.write('\n\n' + '='*10+'\n' + "File: " + selected_file+'\n'+'='*10+'\n')
            if selected_file.endswith('.bat'):
                with open(selected_file, 'rb') as fin:
                    fout.write(fin.read().decode(errors='ignore'))
            else:
                with open(selected_file, 'r') as fin:
                    fout.write(fin.read())
    else:
         print(f"Invalid index '{selected_file_index}'. Please provide indices between 0 and {len(files_list)-1}.")
