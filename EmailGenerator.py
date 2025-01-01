import openai

# Step 1: Define prompts
system_prompt = "You are an assistant that summarizes emails."
user_prompt = """
    1. Welcome Email

    Subject: Welcome to Our Service!
    Body:
    Hello [Name],
    Thank you for joining [Service Name]! We’re thrilled to have you on board. Explore our features, and feel free to reach out if you have any questions.

    Best regards,
    [Service Team]
    
    2. Meeting Reminder

    Subject: Reminder: Project Kickoff Meeting Tomorrow
    Body:
    Hi Team,
    This is a reminder about our project kickoff meeting scheduled for tomorrow at 10:00 AM in the conference room. Please review the agenda beforehand.

    Best,
    [Your Name]
    
    3. Personal Invitation

    Subject: Dinner at My Place!
    Body:
    Hey [Name],
    I’d love for you to join us for dinner this Friday at 7 PM. It’s been too long since we caught up! Let me know if you can make it.

    Cheers,
    [Your Name]
"""
messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": user_prompt}
]

response = openai.chat.completions.create(
        model = "gpt-4o-mini",
        messages = messages
    )


# Step 4: Print the result
response_content = response.choices[0].message.content
print("Email Summary:", response_content)
