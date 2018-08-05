class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

question_list = [
    'What color are apples?\n (a) Red/Green\n (b) Blue\n (c) Yellow\n',
    'What color are bananas?\n (a) Green\n (b) Yellow\n (c) Orange\n',
    'What color are strawberries?\n (a) Yellow\n (b) Green\n (c) Red\n'
]

questions = [
    Question(question_list[0], 'a'),
    Question(question_list[1], 'b'),
    Question(question_list[2], 'c')
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(f'You got {str(score)}/{str(len(questions))} correct!')

run_test(questions)