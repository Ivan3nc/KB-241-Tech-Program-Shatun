import random

def play_game():
    options = ["stone", "scissor", "paper"]
    
    print("--- Гра: Камінь, Ножиці, Папір ---")
    
    while True:
        user_choice = input("\nВаш вибір (stone, scissor, paper) або 'exit': ").lower()
        
        if user_choice == 'exit':
            print("Гру завершено.")
            break
            
        if user_choice not in options:
            print("Некоректний вибір. Спробуйте ще раз.")
            continue

        comp_choice = random.choice(options)
        print(f"Комп'ютер обрав: {comp_choice}")

        if user_choice == comp_choice:
            print("Нічия!")
        elif (user_choice == "stone" and comp_choice == "scissor") or \
             (user_choice == "scissor" and comp_choice == "paper") or \
             (user_choice == "paper" and comp_choice == "stone"):
            print("Ви перемогли!")
        else:
            print("Переміг комп'ютер!")

if __name__ == "__main__":
    play_game()