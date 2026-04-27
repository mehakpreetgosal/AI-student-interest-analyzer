from openai import OpenAI

# Create client
client = OpenAI(api_key="api-key")

def generate_response(name, branch, interests, goal):
    prompt = f"""
You are a career advisor.

Student Name: {name}
Branch: {branch}
Interests: {interests}
Career Goal: {goal}

Write a short personalized message (3-4 lines) suggesting a suitable career path and encouraging the student.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

def generate_response(name, branch, interests, goal):
    return f"Hi {name}, based on your interest in {interests}, you can pursue a career in {goal}. Keep learning and growing!"

# Example
result = generate_response(
    "Mehak",
    "CSE",
    "Coding, AI",
    "Software Engineer"
)

print(result)