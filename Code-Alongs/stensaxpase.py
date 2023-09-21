from random import choice

TECKEN = ["sten", "sax", "påse"]

def main():
    print(f"\nVälkommen till {', '.join(TECKEN)}!\n")
    print_rules()
    game_loop(select_number_of_rounds())
    print_score()


def print_rules():
    print("Regler:")
    print(f"- Du väljer ett av följande tecken: {', '.join(TECKEN)}")
    print("- Detta program väljer sedan slumpmässigt ett av dessa tecken")
    for winners, losers in zip(TECKEN, TECKEN[1:] + TECKEN[:1]):
        print(f"- {winners.title()} vinner över {losers}.")

def select_number_of_rounds():
    while True:
        try:
            number_of_rounds = int(input("\nHur många omgångar vill du spela? "))
            if number_of_rounds > 0:
                return number_of_rounds
            else:
                print("Du måste välja ett positivt heltal.")
        except ValueError:
            print("Du måste välja ett positivt heltal.")

def game_loop(number_of_rounds):
    player_score = 0
    computer_score = 0
    for current_run in range(1, number_of_rounds + 1):
        print(f"\nOmgång {current_run} av {number_of_rounds}")
        player_sign = get_sign_from_user()
        computer_sign = choice(TECKEN)
        print(f"Du valde {player_sign}, datorn valde {computer_sign}")
        
        if is_draw(player_sign, computer_sign):
            print("Det blev lika!")
            
        elif wins_over(player_sign, computer_sign):
            print("Du vann!")
            player_score += 1
            
        else:
            print("Datorn vann!")
            computer_score += 1
            
    return player_score, computer_score

def is_draw(player_sign, computer_sign):
    return player_sign  == computer_sign

def wins_over(player_sign, computer_sign):
    for winners, losers in zip(TECKEN, TECKEN[1:] + TECKEN[:1]):
        return player_sign == winners and computer_sign == losers

def print_score():
    print("\nSlutställning:")
    #print(f"Du: {player_score} poäng")
    #print(f"Datorn: {computer_score} poäng")

def get_sign_from_user():
    while True:
        sign = input("\nVälj ett tecken: ").lower()
        if sign in TECKEN:
            return sign
        else:
            print(f"Du måste välja ett av följande tecken: {', '.join(TECKEN)}")

main()