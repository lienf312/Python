import random

player1 = "inimene"
player2 = "Robot"

choices = ["kivi", "Käärid", "Paber"]

player1_score = 0
player2_score = 0

rounds = 5

for round_num in range(1, rounds + 1):
    print(f"rounds {round_num}")
    
    # человек
    player1_choice = input("Teie valik (Кivi, Käärid, Paber): ").capitalize()
    while player1_choice not in choices:
        print("Viga! Proovi uuesti.")
        player1_choice = input("Teie valik (Кivi, Käärid, Paber): ").capitalize()
    
    # робот 
    player2_choice = random.choice(choices)
    print(f"Robot võtis: {player2_choice}")
    
    # победитель
    if player1_choice == player2_choice:
        result = "viik"
    elif (player1_choice == "Kivi" and player2_choice == "Käärid") or \
         (player1_choice == "Käärid" and player2_choice == "Paber") or \
         (player1_choice == "Paber" and player2_choice == "Kivi"):
        result = "Mängija 1 võit"
        player1_score += 1
    else:
        result = "Mängija 2 võit"
        player2_score += 1

    print(f"Tulemus: {result}")

# результаты
print(f"\nLõpptulemus: {player1} - {player1_score} очков, {player2} - {player2_score} punktid")

if player1_score > player2_score:
    print(f"{player1} võitis!")
elif player2_score > player1_score:
    print(f"{player2} võitis!")
else:
    print("Viik!")
