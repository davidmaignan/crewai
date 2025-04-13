#!/usr/bin/env python
import sys
import warnings

from datetime import datetime

from code_execution_tool.crew import CodeExecutionTool

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")

# This main file is intended to be a way for you to run your
# crew locally, so refrain from adding unnecessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information

def run():
    """
    Run the crew.
    """
    question = input("Enter your code question: ")
    language = input("Enter the language of the code: ")
    inputs = {
        'question': f"Write a code to {question} in {language}",
        'filename': f'{question.replace(" ", "_")}.py'
    }
    
    try:
        return CodeExecutionTool().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


    """
    Test the crew execution and returns the results.
    """
    inputs = {
        "topic": "AI LLMs",
        "current_year": str(datetime.now().year)
    }
    try:
        CodeExecutionTool().crew().test(n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs)

    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")

if __name__ == "__main__":
    result = run()
    print(result)