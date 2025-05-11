## Text analyzer
'''
projekt_1.py: první projekt Engeto Online Python Akademie

autor: Ivo Doležal
email: ivousd@seznam.cz
'''

## Aplikace, kde má registovaný uživatel možnost analyzovat texty.

# Vstupní tabulka s údaji.-> Registovaní uživatelé a hesla.

users = {
    "bob": "123", 
    "ann": "pass123", 
    "mike": "password123", 
    "liz": "pass123"
    }

# Texty k anylýze

TEXTS = ['''"Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley."''',
    '''"At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick."''',
    '''"The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present."'''
]

# oddělovač

oddelovac = "-" * 40

number_text = len(TEXTS)

# Zadání jména a hesla.

user = input("username: ")
password = input("password: ")
print(oddelovac)
# Vyřešit, jestli je správně zadáno jméno a heslo
if users.get(user) != password:
    print(f"username:  {user}\npassword: {password}")
    print("unregistered user, terminating the program..")
    quit()
print(f"Welcome to the app, {user}")
print(f"We have {number_text} texts to be analyzed.")
print(oddelovac)
# Vyřešit, jestli zadal uživatel číslo textu v rozmezí počtu textů
your_nmbr_choice = input(f"Enter a number btw. 1 and {number_text} to select: ")
if not your_nmbr_choice.isdigit() or int(your_nmbr_choice) not in range(1, number_text + 1):
    print("This is not right number, terminating program..")
    quit()
else:
    print(oddelovac)
# Vybrané číslo textu od uživatele
selected_text = TEXTS[int(your_nmbr_choice) - 1]
# ...
# A jedem statistiky:
#   --- 1. Počet slov
#   --- 2. Počet slov začínajících velkým písmenem,
#   --- 3. Počet slov psaných velkými písmeny
#   --- 4. Počet slov psaných malými písmeny
#   --- 5. Počet čísel (ne cifer)
#   --- 6. Sumu všech čísel (ne cifer) v textu
# ...
# proměnné
word_count = 0
word_start_title = 0
word_upper = 0
word_lower = 0
word_isdigit = 0
sum_digit_number = 0

#Projít text
words = []
for word in selected_text.split():
    word_alone = word.strip(",.-")
    words.append(word_alone)
# Text rozdělíme na řetězce. Vyjmeme čárky, tečky a možná i pomlčky.
for word in words:
    if word == " ":
        continue
# Pokud tam je mezera. Jedeme dál s počítáme bez mezer.
    word_count += 1
# 1. hotová, jedeme další body.
    if word.istitle():
        word_start_title += 1
    if word.isupper():
        word_upper += 1
    if word.islower():
        word_lower += 1
    if word.isdigit():
        word_isdigit +=1 #čísla a cifry, př.: 198 je čílo a cifry jsou 1,9,8
        sum_digit_number += int(word)
# Teď ty printy
print(f"There are {word_count} words in the selected text.")
print(f"There are {word_start_title} titlecase words.")
print(f"There are {word_upper} uppercase words")
print(f"There are {word_lower} lowercase words")
print(f"There are {word_isdigit} numeric strings")
print(f"The sum of all the numbers {sum_digit_number}")
print(oddelovac)
# A teď ta tabulka
# Udělám proměnnou delka slovníku
dict_length: dict[int, int] = {}
# Musím udělat přičítání délky
for word in words:
    length = len(word)
    dict_length[length] = dict_length.get(length, 0) + 1
print("LEN| OCCURENCES  |NR.")
print()