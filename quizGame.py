class Quiz:
    def __init__(self, questions):
        self.questions = questions
        self.score = 0

    def display_question(self, question):
        print(question['text'])
        for i, option in enumerate(question['options'], start=1):
            print(f"{i}. {option}")
        user_input = input("Enter the number of your answer: ")
        return int(user_input)

    def run_quiz(self):
        for question in self.questions:
            user_answer = self.display_question(question)
            if user_answer == question['answer']:
                print("Correct!\n")
                self.score += 1
            else:
                print(f"Wrong! The correct answer was {question['options'][question['answer'] - 1]}\n")
        print(f"Quiz completed! Your score is {self.score}/{len(self.questions)}")


# Sample questions for the quiz
questions = [
    {
        'text': 'What is the capital of France?',
        'options': ['Berlin', 'Paris', 'Madrid', 'Rome'],
        'answer': 2,
    },
    {
        'text': 'Which planet is known as the Red Planet?',
        'options': ['Mars', 'Venus', 'Jupiter', 'Saturn'],
        'answer': 1,
    },
    {
        'text': 'What is the largest mammal?',
        'options': ['Elephant', 'Blue whale', 'Giraffe', 'Hippopotamus'],
        'answer': 2,
    },
]

# Create a Quiz instance and run the quiz
quiz = Quiz(questions)
quiz.run_quiz()
