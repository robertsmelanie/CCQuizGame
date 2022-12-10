# Step 0:First things first, create the virtual environment
# 1. Navigate to the QuizGame project folder
# 2. In Terminal type the command: python3 -m venv venv
# 3. Activate the environment: source venv/bin/activate

#  Step 2 Import dat list and question model
from question_model import Question
from data import question_data
# Step 3: Create question bank using the question_data hat has been imported (hint: loops >_>)
from quiz_brain import QuizBrain

#3a. Place to store our questions in the question bank, i.e. an empty list


question_bank = []

# 3b. Loop through the question_data
for question in question_data:
    #3.c Get a hold of question text and question answers from the question_data list
    question_text = question["question"]
    question_answer = question["correct_answer"]
    # 3.d Create a new question using imported Class
    new_question = Question(question_text, question_answer)
    # 3.e. Add question to the question_bank list
    question_bank.append(new_question)

# print(question_bank[1].answer)
# 3f. Test to see if the loop working
# print(question_bank)
# Should print out a list of Question objects

# Step 6: Create new QuizBrain object using the QuizBrain Class and pass in the question_bank
quiz = QuizBrain(question_bank)
# 6a. Run the next_question() method on the object just created
# quiz.next_question()

# 7a. Create a game loop (whilel loop) to run the game
while quiz.still_has_questions():
    # 7b. Move the quiz.next_question() from step 6a into the while loop
    quiz.next_question()

# Step 9. Notify the user when the quiz is
print("You have completed the quiz", f"Your final score was: {quiz.score}/{quiz.question_number}")