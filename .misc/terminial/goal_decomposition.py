import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from Core.gpt import GPT

class GoalDecomposer:
    def __init__(self):
        # Instantiate a GPT object to interact with OpenAI's GPT model
        self.gpt = GPT()

    def decompose_goal(self, goal):
        # Set up the prompt for the GPT model to get sub-tasks for the given goal
        prompt = f"Given a goal '{goal}', please break it down into sub-tasks:"

        # Execute the GPT model using the prompt and obtain its output
        response_text = self.gpt.generate_text(prompt)

        # Split the obtained output into individual sub-tasks
        sub_tasks_string = response_text.strip().split("\n")
        
        # Remove empty strings after splitting
        sub_tasks = [task.strip() for task in sub_tasks_string if task.strip()]

        return sub_tasks

if __name__ == "__main__":
    decomposer = GoalDecomposer()
    test_goal = "Install a new software"
    print(f"Sub-tasks for the goal '{test_goal}':")
    sub_tasks = decomposer.decompose_goal(test_goal)
    for sub_task in sub_tasks:
        print(f" - {sub_task}")