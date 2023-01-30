# This is a guess the number game.
import random
secretNumber = random.randint(1, 10)
print('Estou pensando num número de 1 a 10')

# Ask the player to guess 6 times.
for guessesTaken in range(1, 7):
    print('Escolha um número.')
    guess = int(input())

    if guess < secretNumber:
        print('Seu chute está baixo.')
    elif guess > secretNumber:
        print('Seu chute está alto.')
    else:
        break    # This condition is the correct guess!
if guess == secretNumber:
    print('Parabéns, você acertou em ' + str(guessesTaken) + 'tentativas!')
else:
    print('Não, o número que estava pensando era ' + str(secretNumber))
