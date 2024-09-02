import random

questions = [
    {
        "question": "Which is the largest state in India by area?",
        "options": ["1. Rajasthan", "2. Madhya Pradesh", "3. Maharashtra", "4. Uttar Pradesh"],
        "answer": "1"
    },
    {
        "question": "Which is the largest ocean in the world?",
        "options": ["1. Atlantic Ocean", "2. Indian Ocean", "3. Arctic Ocean", "4. Pacific Ocean"],
        "answer": "4"
    },
    {
        "question": "What is the capital of Australia?",
        "options": ["1. Sydney", "2. Melbourne", "3. Brisbane", "4. Canberra"],
        "answer": "4"
    },
    {
        "question": "Who was the first Prime Minister of independent India?",
        "options": ["1. Mahatma Gandhi", "2. Jawaharlal Nehru", "3. Sardar Vallabhbhai Patel", "4. Dr. Rajendra Prasad"],
        "answer": "2"
    },
    {
        "question": "How many states are there in India currently?",
        "options": ["1. 28", "2. 29", "3. 28 states and 8 union territories", "4. 29 states and 7 union territories"],
        "answer": "3"
    },
    {
        "question": "What is the minimum age to contest for the Lok Sabha elections in India?",
        "options": ["1. 18 years", "2. 21 years", "3. 25 years", "4. 30 years"],
        "answer": "3"
    },
    {
        "question": "What is the unit of Indian currency?",
        "options": ["1. Dollar", "2. Euro", "3. Pound", "4. Rupee"],
        "answer": "4"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "options": ["1. Au", "2. Ag", "3. Cu", "4. Fe"],
        "answer": "1"
    },
    {
        "question": "What is the speed of light in vacuum?",
        "options": ["1. 2 × 10^8 m/s", "2. 3 × 10^8 m/s", "3. 4 × 10^8 m/s", "4. 5 × 10^8 m/s"],
        "answer": "2"
    },
    {
        "question": "Who is known as the 'Father of the Nation' in India?",
        "options": ["1. Jawaharlal Nehru", "2. Mahatma Gandhi", "3. Sardar Vallabhbhai Patel", "4. B.R. Ambedkar"],
        "answer": "2"
    }
]

random.shuffle(questions)

score = 0

for q in questions:
    print("\n" + q["question"])
    for option in q["options"]:
        print(option)
    
    answer = input("Enter your choice (1-4): ")
    if answer == q["answer"]:
        print("Correct Answer!")
        score += 1
    else:
        print("Wrong Answer")

print(f"\nYour final score is: {score}/{len(questions)}")