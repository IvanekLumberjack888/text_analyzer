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

# Oddělovač
separator = "-" * 40

# Přihlášení uživatele
print("Welcome to the app, please log in.")
user = input("username: ").strip()  # odstraní mezery na začátku a konci
password = input("password: ").strip()  # odstraní mezery na začátku a konci
print(separator)

# Vyřešit, jestli je uživatel zaregistrován
if users.get(user) != password:
    print("Unregistered user or wrong password, terminating program..")
    quit()
else:
    print(f"Welcome to the app, {user}")
    print(f"We have {len(TEXTS)} texts to analyze.")
    print(separator)

# Vyřešit, jestli zadal uživatel číslo textu v rozmezí počtu textů
user_choice = input(f"Enter a number btw. 1 and {len(TEXTS)} to select: ").strip()  # odstraní mezery na začátku a konci
if not user_choice.isdigit() or int(user_choice) not in range(1, len(TEXTS) + 1):
    print("This is not right number, terminating program..")
    quit()
else:
    print(separator)

# Vybrané číslo textu od uživatele
selected_text = TEXTS[int(user_choice) - 1]

# ...
# A jedem statistiky:
#   --- 1. Počet slov
#   --- 2. Počet slov začínajících velkým písmenem,
#   --- 3. Počet slov psaných velkými písmeny
#   --- 4. Počet slov psaných malými písmeny
#   --- 5. Počet čísel (ne cifer)
#   --- 6. Sumu všech čísel (ne cifer) v textu
# ...
# Proměnné
word_count = 0
titlecase_count = 0
uppercase_count = 0
lowercase_count = 0
numeric_count = 0
sum_numbers = 0
# bez importu, Python 3.9+
lengths: dict[int, int] = {}

# Projít text
words = []
for raw in selected_text.split():
    clean = raw.strip(",.-")  # odstraní čárky, tečky a pomlčky
    clean = clean.strip('"')  # odstraní uvozovky
    clean = clean.strip("'")  # odstraní apostrofy
    if not clean:
        continue

    # Pro každé slovo spočítá - kolikát se vyskytlo, jestli je titlecase, uppercase, lowercase, numeric
    # a spočítá délku slova.
    word_count += 1
    if clean.istitle():
        titlecase_count += 1
    if clean.isupper():
        uppercase_count += 1
    if clean.islower():
        lowercase_count += 1
    if clean.isdigit():
        numeric_count += 1
        sum_numbers += int(clean)
    length = len(clean)
    lengths[length] = lengths.get(length, 0) + 1
    words.append(clean)

# Teď ty printy
print(f"There are {word_count} words in the selected text.")
print(f"There are {titlecase_count} titlecase words.")
print(f"There are {uppercase_count} uppercase words")
print(f"There are {lowercase_count} lowercase words")
print(f"There are {numeric_count} numbers.")
print(f"The sum of all the numbers {sum_numbers}")
print(separator)

# A teď ta tabulka
# Udělám proměnnou delka slova/níku
dict_length: dict[int, int] = {}

print(" LEN|    OCCURENCES       |NR.")
print(separator)
# Pro každé slovo (délku) spočítá - kolikát se vyskytl jako kdyby znak.
for length in sorted(lengths):
    stars = '*' * lengths[length]  # Vytvoří hvězdičky podle počtu výskytů
    print(f" {length:>3}| {stars:<20}| {lengths[length]}")
print()

# Čas refaktoringu 2:45 h
