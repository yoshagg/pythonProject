right_answer = "Ответ верный!"
wrong_answer = "Увы, но нет. Верный ответ:"
counter = 0
counter_of_answers = 0
counter_of_points = 0
counter_of_questions = 0
questions = ["My name ___  Vova", "I ___ a coder", "I live ___ Moscow", "I work ___ home"]
answers = ["is", "am", "in", "at"]

code_word = input("Привет! \n Предлагаю проверить свои знания английского! \n Наберите 'ready', чтобы начать! \n")
if code_word == "ready":
    for question in questions:
        answer = input(f'{question} \n')
        attempts =3
        counter_of_attempts = 1
        while True:
            if answer != answers[counter] and counter_of_attempts < 3:
                attempts -= 1
                answer = input(f'Осталось попыток:{attempts}, попробуйте еще раз! \n')
                counter_of_attempts +=1
            elif counter_of_attempts == 3 and answer != answers[counter]:
                print(f'{wrong_answer} {answers[counter]}')
                attempts = 0
                break
            else:
                print (right_answer)
                counter_of_answers += 1
                break
        counter_of_points += attempts
        counter_of_questions += 1
        counter += 1
    print(f'Вот и всё! \nВы ответили на {counter_of_answers} вопросов из {counter_of_questions}\n'
           f''f'Вы заработали {counter_of_points} баллов. ')
else:
     print('Кажется, вы не хотите играть. Очень жаль.')
