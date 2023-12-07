words_easy = {
    "family":"семья",
    "hand": "рука",
    "people":"люди",
    "evening": "вечер",
    "minute":"минута",
}

words_medium = {
    "believe":"верить",
    "feel": "чувствовать",
    "make":"делать",
    "open": "открывать",
    "think":"думать",
}

words_hard = {
    "rural":"деревенский",
    "fortune": "удача",
    "exercise":"упражнение",
    "suggest": "предлагать",
    "except":"кроме",
}
levels = {
   0: "Нулевой",
   1: "Так себе",
   2: "Можно лучше",
   3: "Норм",
   4: "Хорошо",
   5: "Отлично",
}
answers = {}
right_answer = []
wrong_answer = []
words = {'легкий': words_easy, 'средний': words_medium, 'сложный': words_hard }

difficulty_level = input("Выберите уровень сложности: \n легкий, средний, сложный.\n").lower()

if difficulty_level in words.keys():
    print (f"Выбран {difficulty_level} уровень сложности, мы предложим 5 слов, подберите перевод.")
    word = words[difficulty_level]
    for k in word:
        start = input("Нажмите Enter")
        users_translation = input(f'{k}, {len(word[k])} букв, начинается на {word[k][0]}\n').lower()
        if word[k] == users_translation:
            print(f'Верно, {k.title()} - это {word[k]}')
            answers[word[k]] = True
        else:
            print(f'Неверно, {k.title()} - это {word[k]}')
            answers[word[k]] = False

    for key, value in answers.items():
        if value == True:
            right_answer.append(key)
        else:
            wrong_answer.append(key)

    print(f'Правильно отвечены слова: \n{", ".join(right_answer).title()}\n')
    print(f'Неправильно отвечены слова: \n{", ".join(wrong_answer).title()}\n')
    print(f'Ваш ранг: {levels[len(right_answer)]}')

else:
    print(f"Уровня сложности {difficulty_level} нет")
