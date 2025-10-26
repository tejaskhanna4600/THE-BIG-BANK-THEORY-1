"""
Configuration - Passwords and Settings
"""

# Passwords for each user type
PASSWORDS = {
    "ADMIN": "admin123",
    "T1": "team1",
    "T2": "team2", 
    "T3": "team3",
    "T4": "team4",
    "T5": "team5",
}

# User types
USER_TYPES = {
    "ADMIN": "Admin Panel",
    "T1": "Team 1",
    "T2": "Team 2",
    "T3": "Team 3",
    "T4": "Team 4",
    "T5": "Team 5",
}

# Chance questions
CHANCE_QUESTIONS = [
    {
        "question": "What is the capital of France?",
        "options": ["London", "Berlin", "Paris", "Madrid"],
        "correct": 2
    },
    {
        "question": "What is the largest planet in our solar system?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "correct": 2
    },
    {
        "question": "What does 'www' stand for?",
        "options": ["World Wide Web", "Web World Wide", "Wide Web World", "World Web Wide"],
        "correct": 0
    },
    {
        "question": "Which programming language is used for web development?",
        "options": ["Python", "JavaScript", "Java", "C++"],
        "correct": 1
    },
]

# Mystery wheel options
MYSTERY_OPTIONS = [
    {"text": "Advance 3 spaces", "action": "move", "value": 3},
    {"text": "Go back 2 spaces", "action": "move", "value": -2},
    {"text": "Go to Free Parking", "action": "goto", "value": 12},
    {"text": "Go to Society Penalty", "action": "goto", "value": 6},
    {"text": "No rent next turn", "action": "protection", "value": True},
]

