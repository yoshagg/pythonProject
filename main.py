# n = input("motherfuckinggermansheppard: \n")
# print(n)

questions = ["My name ___ Vova", "I ___ a coder", "I live ___ Moscow"]
answers = ["is", "am", "in"]
counter = 0

dick = {"My name ___ Vova": "is",
        "I ___ a coder": "am",
        "I live ___ Moscow": "in"}

starter = input("""Привет! Предлагаю проверить свои знания английского! \n Набери "ready", чтобы начать!\n""")
if starter == "ready":
    for x in questions:
        answer = input(f"{x}\n")
        if answer in answers[counter]:
            print("Верно, красавчик епта")
        else:
            print("Ты че далбаеб")
        counter += 1
else:
    print("Похоже, вы не готовы учиться. Тогда идите нахуй")

