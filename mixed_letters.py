from random import sample

score = 0


def get_words():
    with open('words.txt', 'rt') as file:
        words = []
        for line in file:
            words += line.rstrip('\n').split('\n')
        return words


def mix_letters(words):
    mixed_words = {}
    for word in words:
        letters = list(word)
        letters = sample(letters, len(letters))
        mixed_word = ''.join(letters)
        mixed_words[word] = mixed_word
    return mixed_words


def write_statistics(user_name, score):
    with open('history.txt', 'a') as file:
        file.write(f"{user_name}:{score}\n")


def read_statistics():
    with open('history.txt', 'rt') as file:
        games = 0
        score_total = []

        for user_data in file:
            name, score = user_data.rstrip('\n').split(':')
            if name == user_name:
                games += 1
                score_total.append(score)

        print(f"Всего игр сыграно:{games}\n"
              f"Максимальный рекорд: {max(score_total)}")


user_name = str(input("Введите ваше имя: "))

words = get_words()
mixed_words = mix_letters(words)

for k, v in mixed_words.items():

    user_answer = input(f"Угадайте слово: {v}"
                        "\nВведите расшифровку:")
    if user_answer == k:
        print(f'Верно, вы получаете 10 очков!')
        score += 10
    else:
        print(f'Неверно, верный ответ - {k}!')

write_statistics(user_name, score)
print(read_statistics())
