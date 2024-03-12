


class Quiz:
    def __init__(self):
        self.questions = [
            {
                "question": "What is the capital of Telangana?",
                "options": ["A. Amravathi", "B. Hyderabad", "C. Manipur", "D. Dehli"],
                "answer": "B"
            },
            {
                "question": "Which datatype is immutable in python?",
                "options": ["A. List", "B. Tuple", "C. Set", "D. Dictionary"],
                "answer": "B"
            },
            {
                "question": "In Which  year India got Independence ?",
                "options": ["A. 1945", "B. 1935", "C. 1955", "D. 1987"],
                "answer": "A"
            }
        ]
        self.score = 0

    def display_question(self, question):
        print(question["question"])
        for option in question["options"]:
            print(option)
    
    def check_answer(self, question, answer):
        if answer.upper() == question["answer"]:
            print("Correct!")
            self.score += 1
        else:
            print("Incorrect. The correct answer is:", question["answer"])

    def start_quiz(self):
        print("Welcome to the Quiz!")
        for i, question in enumerate(self.questions, 1):
            print("\nQuestion", i)
            self.display_question(question)
            user_answer = input("Your answer (Enter A, B, C, or D): ")
            self.check_answer(question, user_answer)
        
        print("\nQuiz completed!")
        print("Your final score is:", self.score)

if __name__ == "__main__":
    quiz = Quiz()
    quiz.start_quiz()
