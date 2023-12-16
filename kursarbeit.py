words = ["tranquility", "redemption", "evaluation", "perpetrator",
         "proliferation"]
answers = []
counter_of_words = 1


def morse_encode(word):
    """
    Функция кодирует слово, используя азбуку морзе
    """
    morse_alphabet = {
        "0": "-----",
        "1": ".----",
        "2": "..---",
        "3": "...--",
        "4": "....-",
        "5": ".....",
        "6": "-....",
        "7": "--...",
        "8": "---..",
        "9": "----.",
        "a": ".-",
        "b": "-...",
        "c": "-.-.",
        "d": "-..",
        "e": ".",
        "f": "..-.",
        "g": "--.",
        "h": "....",
        "i": "..",
        "j": ".---",
        "k": "-.-",
        "l": ".-..",
        "m": "--",
        "n": "-.",
        "o": "---",
        "p": ".--.",
        "q": "--.-",
        "r": ".-.",
        "s": "...",
        "t": "-",
        "u": "..-",
        "v": "...-",
        "w": ".--",
        "x": "-..-",
        "y": "-.--",
        "z": "--..",
        ".": ".-.-.-",
        ",": "--..--",
        "?": "..--..",
        "!": "-.-.--",
        "-": "-....-",
        "/": "-..-.",
        "@": ".--.-.",
        "(": "-.--.",
        ")": "-.--.-"
    }
    encoded_word = ""
    for letter in word:
        encoded_word += morse_alphabet[letter]
    return encoded_word


def get_word(words):
    """
    Функция вытаскивает случайное слово из списка
    """
    from random import choice
    word = choice(words)
    return word


def print_statistics(answers):
    """
    Функция выдает статистику ответов
    """
    right_answers = 0
    wrong_answers = 0
    for answer in answers:
        if answer == True:
            right_answers += 1
        else:
            wrong_answers += 1
    print(f"Всего задачек: {len(answers)}"
          f"\nОтвечено верно: {right_answers}"
          f"\nОтвечено неверно: {wrong_answers}")


print("Сегодня мы потренируемся расшифровывать азбуку Морзе"
      "\n Нажмите Enter и начнем")
input()

while len(words) != 0:
    word = get_word(words)
    words.remove(word)
    encoded_word = morse_encode(word)

    user_answer = input(f"Слово {counter_of_words}: {encoded_word}"
                        "\nВведите расшифровку:")
    if user_answer == word:
        answers.append(True)
        print(f'Верно, {word}!')
    else:
        answers.append(False)
        print(f'Неверно, {word}!')
    counter_of_words += 1

print(print_statistics(answers))
