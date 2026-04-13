import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def read_tasks(filepath):
    with open(filepath, "r") as f:
        return f.read()

def summarize_tasks(tasks):
    prompt = f"""You are a smart task planning agent. Given a list of tasks, categorize them into 3 priority buckets:
- High priority
- Medium Priority
- Low Priority

Tasks:
{tasks}

Return the response in this format:

High priority:
- task 1
- task 2

Medium Priority:
- task 1
- task 2

Low Priority:
- task 1
- task 2
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",  
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content

if __name__ == "__main__":
    task_text = read_tasks("tasks.txt")
    summary = summarize_tasks(task_text)

    print("\nTask Summary\n")
    print("-" * 30)
    print(summary)