import random

def game():
	player = input('Enter your preferred username: ')
	print('\n\n')

	# This nullifies any wrong choices from the player and prompts him to make 
	## another choice   

	while True:
		game_dict = {'R':'Rock', 'P':'Paper', 'S':'Scissors'}
		# This is the player's choice
		choice = input('Pick an option; R for rock, P for Paper or S for scissors: ').title()

		# This generates random moves for the computer
		options = ['R','P', 'S']
		cpu = random.choice(options)

		#Prevents errors when the option is not a part of the game
		if choice not in options:
			print('Error!! This is not an option, {}'.format(player))
			print('Please pick R for Rock, P for Paper or S for Scissors. \n')
			continue
		
		else:
			#This loops the code afresh if the user and cpu picks the same thing.
			if choice == cpu:
				print('{} - {} : CPU - {}\n'.format(player, game_dict[choice], game_dict[cpu]))
				print('It\'s a tie. \nTry again.')
				continue 

			#Below, prints and determines the winner of the game 
			elif choice == 'R' and cpu == 'P':
				print('{} - {} : CPU - {}'.format(player, game_dict[choice], game_dict[cpu]))
				print('CPU wins')
				break
			
			elif choice == 'P' and cpu == 'R':
				print('{} - {} : CPU - {}'.format(player, game_dict[choice], game_dict[cpu]))
				print('{} wins'.format(player))
				break

			elif choice == 'R' and cpu == 'S':
				print('{} - {} : CPU - {}'.format(player, game_dict[choice], game_dict[cpu]))
				print('{} wins'.format(player))
				break

			elif choice == 'S' and cpu == 'R':
				print('{} - {} : CPU - {}'.format(player, game_dict[choice], game_dict[cpu]))
				print('CPU wins')
				break 

			elif choice == 'S' and cpu == 'P':
				print('{} - {} : CPU - {}'.format(player, game_dict[choice], game_dict[cpu]))  
				print('{} wins'.format(player))
				break

			elif choice == 'P' and cpu == 'S':
				print('{} - {} : CPU - {}'.format(player, game_dict[choice], game_dict[cpu])) 
				print('CPU wins')
				break
	return

game()