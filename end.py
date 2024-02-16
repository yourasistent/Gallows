import colorama
import random
green = colorama.Fore.GREEN
red = colorama.Fore.RED
gold= colorama.Fore.YELLOW
ugbj = colorama.Style.RESET_ALL
print(f"Поздравляю, дорогой друг! Вы папали в уникальную игру - {red} ♣ ВИСЕЛИЦА ♣ {ugbj}")
input(" Нажимай Enter чтобы продолжить)")
print(f"Ну что ж, поехали.{green} У тебя будет 10 попыток...{ugbj} Удачи!")

slova=["рентгеноэлектрокардиография","яблоко", "породистая собака","любимка","литература","черепашка","уютное кафе"]
word =random.choice(slova)
p=[]
isWin = True
popitka=10
if " " in word:
    print("У вас два слова")
while popitka != 0:
    isWin = True
    bookva = input("Прелестный человечек, пожалуйста введите букву: ")
    p.append(bookva)
    for symb in word:
        if symb in p:
           print(symb, end=" ")
        elif symb==" ":
            print(" ", end=" ")
        else:
           print("_", end=" ")
           isWin = False
    print()
    if bookva not in word:
        popitka = popitka -1
        print(f"{red}У вас осталось {popitka} попыток{ugbj}")
    if popitka == 0:
        print("Ты проиграл :(")
    print()
    if isWin==True :
        print(f"{gold} А я так старалась чтоб ты не смог отгадать, но ты слишком гениален, МОЛОДЕЦ! 🏆{ugbj}")
        break
