right_answer = "Ответ верный! \nВы получаете 10 баллов! \n"
wrong_answer = "Неправильно. \nВерный ответ:"
counter = 0
counter_of_answers = 0
counter_of_questions = 0
questions = ["My name ___  Vova", "I ___ a coder", "I live ___ Moscow", "I work ___ home"]
answers = ["is", "am", "in", "at"]

code_word = input("Привет! \n Предлагаю проверить свои знания английского! \n Наберите 'ready', чтобы начать! \n")
if code_word == "ready":
    for question in questions:
        counter_of_questions += 1
        print(question)
        answer = input()
        if answer == answers[counter]:
            print(right_answer)
            counter_of_answers +=1
        else:
            print(wrong_answer, answers[counter])
        counter += 1
    points = counter_of_answers * 10
    percentage_of_points = int(points * 10/counter_of_questions)
    print (f'Вот и всё! \nВы ответили на {counter_of_answers} вопросов из {counter_of_questions}\n'
           f''f'Вы заработали {points} баллов. '
           f'\nЭто {percentage_of_points} %.')
else:
     print('Кажется, вы не хотите играть. Очень жаль.')
