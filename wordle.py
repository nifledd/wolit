import random
import sys
import time
from time import sleep
from termcolor import colored
import threading
import itertools
import webbrowser

tablica_wykluczen = []
cntgames = 6
tablica_kolorow = []
done = False


def animate():
    global done
    space = " "
    table = []
    for i in range(35):
        table.append(space*i+":)")
    for c in itertools.cycle(table):
        if done:
            break
        sys.stdout.write('\r'+c)
        sys.stdout.flush()
        time.sleep(0.1)
def sl():
    sleep(2)
def out_game():
    global done
    print(colored("  Dziękuję za zagranie w moją grę!", "green"))
    print(colored("------------------------------------", "green"))
    sl()
    print(colored("  Gra została stworzona przez D.C\n         Github: nifledd", "green"))
    print(colored("------------------------------------", "green"))
    threading.Thread(target=animate).start()
    time.sleep(11.5)
    done = True

def rules():
    print("Zasady gry:")
    sl()
    print("1. Wpisz słowo 5-cio literowe, a...")
    sl()
    print(colored("2. Jeżeli litera podświetliła się na niebiesko to oznacza,\nże litera występuje w słowie, ale na złym miejscu","blue"))
    sl()
    print(colored("3. Jeżeli litera podświetla się na zielono to oznacza,\nże litera występuje w haśle i jest na dobrym miejscu","green"))
    sl()
    print("4. Jeżeli litery się nie podświetlają to oznacza to,\nże nie występuje żadna z nich w słowie")
    sl()
    print(colored("5. Na czerwono wyświetlane są litery które były użyte i nie znajdują się w haśle","red"))
    sl()
    print("6. Możesz zmienic liczbę prób poprzez wpisanie przy następnej grze(przy komunikacie czy chcesz poznać zadady gry?)\nnp. słowo  newsetting10")
    sl()
    print("\n___Miłej zabawy!___")
def print_menu():
    global cntgames
    print("Gra w słowa: ")
    while True:
        zadady = input("Czy chcesz poznać zasady gry?(tak/nie): ")
        if zadady == "tak":
            rules()
            break
        elif zadady == "nie":
            print("W takim razie miłej gry  :)")
            sleep(1)
            break
        elif zadady[0:10] == "newsetting":
            try:
                cntgames = int(zadady[10::])
                if cntgames not in range(1,101):
                    print("za mała albo za duża licza prób(od:1 do:100)")
                    continue
                else:
                    print("Wybrana licza prób: ",cntgames)
            except ValueError:
                continue
        else:
            input("Coś wpisał*ś źle(kliknij dowolny przycisk)")
            continue
def read_random_word():
    with open("kutas.txt","r") as file:
        words = file.read().split()
        return random.choice(words)
def check_input():
    global tablica_wykluczen
    while True:

        print("\n",colored(tablica_wykluczen, "red"))
        guess = input("\nPodaj słowo: ").lower()
        '''with open("kutas.txt","r") as file1:
            file = file1.read().split()
            for i in file:
                if guess == i:
                    print("yes")
        file1.close()'''
        if len(guess) == 5:
            return guess
        if len(guess) != 5:
            input("You must enter only 5 letters:\nto continue click any button")
            continue
print_menu()
while True:
    word = read_random_word()
    for proba in range(1, cntgames+1):
        guess = check_input()
        for i in range(min(len(guess),5)):
            if guess[i] == word[i]:
                print(colored(guess[i], 'green'), end="")
                tablica_kolorow.append(guess[i])
            elif guess[i] in word:
                if guess[i] in tablica_kolorow:
                    print(guess[i], end="")
                else:
                    print(colored(guess[i],'blue'), end="")
            else:
                print(guess[i],end="")
                if guess[i] not in tablica_wykluczen:
                    tablica_wykluczen.append(guess[i])
        if guess == word:
            print(f"\nWygrłeś za {proba} razem")
            break
    print("\nSłowem było: ",word)
    while True:
        IsExists = input("Czy znasz to słowo?(tak/nie): ")
        if IsExists == "nie":
            while True:
                DEFINITON = input("Czy chesz poznać definicję slowa(T/N): ").lower()
                if DEFINITON == "t":
                    try:
                        webbrowser.open(f"https://sjp.pwn.pl/szukaj/{word}.html")
                    except:
                        continue
                    break
                elif DEFINITON == 'n':
                    break
                else:
                    print("Źle wpisałeś!")
                    continue
            while True:
                RUS = input("Usunąć z bazy to słowo?(tak/nie)").lower()
                if RUS == "tak":
                    with open("kutas.txt", "r", encoding="utf-8") as filetodel:
                        DEL = filetodel.read().split()
                        for words in DEL:
                            if words == word:
                                DEL.remove(word)

                    with open("kutas.txt", "w", encoding="utf-8") as filetodelout:
                        for OutputText in DEL:
                            filetodelout.write(OutputText+"\n")
                    filetodelout.close()
                    filetodel.close()
                    break
                break
            break
        elif IsExists != "tak" and IsExists != "nie":
            input("Źle wprowadził*ś\nkliknij dowolny przycisk")
        elif IsExists == "tak":
            break
    while True:
        PlayAgain = input("Czy chcesz zagrać jeszcze raz?(tak/nie) ").lower()
        if PlayAgain == "nie":
            out_game()
            exit()
        elif PlayAgain == "tak":
            tablica_wykluczen = []
            tablica_kolorow = []
            break
        elif PlayAgain != "tak" and PlayAgain != "nie":
            continue