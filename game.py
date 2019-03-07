from random import randint

game_running = True
game_results = []

def calculate_monster_attack(attack_min, attack_max):
    return randint(attack_min, attack_max)

def game_ends(winner_name):
    print(f'{winner_name} won the game')

while game_running == True:
    counter = 0
    new_round = True
    player = {'name': 'Manuel', 'attack': 13, 'heal': 16, 'health': 100}
    monster = {'name': 'Max', 'attack_min': 10, 'attack_max': 20, 'health': 100}

    print('---' * 7)
    print('Enter Player name')
    player['name'] = input()

    print('---' * 7)
    print(player['name'] + ' has ' + str(player['health']) + ' health')
    print(monster['name'] + ' has ' + str(monster['health']) + ' health')

    while new_round == True:

        counter = counter + 1
        player_won = False
        monster_won = False

        print('---' * 7)
        print('Please select action')
        print('1) Attack')
        print('2) Heal')
        print('3) Exit Game')
        print('4) Show Results')

        player_choice = input()

        if player_choice == '1':
            monster['health'] = monster['health'] - player['attack']
            if monster['health'] <= 0:
                player_won = True
            
            else:
                player['health'] = player['health'] - calculate_monster_attack(monster['attack_min'], monster['attack_max'])
                
                if player['health'] <= 0:
                    monster_won = True

        elif player_choice == '2':
            player['health'] = player['health'] + player['heal']

            player['health'] = player['health'] - calculate_monster_attack(monster['attack_min'], monster['attack_max'])
            if player['health'] <= 0:
                monster_won = True


        elif player_choice == '3':
            new_round = False
            game_running = False

        elif player_choice == '4':
            for player_stat in game_results:
                print(player_stat)

        else:
            print('Invalid Input')

        if player_won == False and monster_won == False:
            print(player['name'] + ' has ' + str(player['health']) + ' left')
            print(monster['name'] + ' has ' + str(monster['health']) + ' left')

        elif player_won:
            game_ends(player['name'])
            round_result = {'name': player['name'], 'health': player['health'], 'rounds': counter}
            game_results.append(round_result)
            new_round = False

        elif monster_won:
            game_ends(monster['name'])
            round_result = {'name': player['name'], 'health': player['health'], 'rounds': counter}
            game_results.append(round_result)
            new_round = False

