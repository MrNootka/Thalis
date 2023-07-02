import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Core.gpt import GPT
from goal_decomposition import GoalDecomposer
import os
import subprocess
from Core.gpt import GPT
from goal_decomposition import GoalDecomposer

class TaskExecutor:
    def __init__(self):
        self.gpt = GPT()
        self.decomposer = GoalDecomposer()

    def think_and_execute(self, task):
        sub_tasks = self.decomposer.decompose_goal(task)
        
        try:
            for sub_task in sub_tasks:
                self.execute_sub_task(sub_task)
                print(f"The task '{sub_task}' was successfully executed.")
        except Exception as e:
            print(f"Error executing task '{sub_task}': {e}")

    def execute_sub_task(self, sub_task):
        prompt = f"Write a PowerShell command or script to accomplish the following task: {sub_task}"
        response = self.gpt.generate_text(prompt)
        code = response.strip()
        
        print(f"Thalis generated the following code for the task '{sub_task}':\n{code}\n")

        temp_script_file = "terminal_custom_script.ps1"

        with open(temp_script_file, "w") as script_file:
            script_file.write(code)

        os.chmod(temp_script_file, 0o755)

        # Execute the script and capture any errors
        process = subprocess.Popen(f'powershell.exe -ExecutionPolicy Bypass -NoProfile -NonInteractive -File {temp_script_file}', shell=True, stderr=subprocess.PIPE, stdout=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if process.returncode != 0:
            raise Exception(f"Execution failed. Error message: {stderr.decode().strip()}")
        else:
            print(f"Successfully executed the task. Output: {stdout.decode().strip()}")

os.system("")

if __name__ == "__main__":
    task_executor = TaskExecutor()
    user_task = input("Enter a task: ")
    task_executor.think_and_execute(user_task)