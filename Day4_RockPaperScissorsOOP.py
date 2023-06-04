import random

choices = {'rock' : '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',

'paper' : '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',

'scissors' : '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''}

class Player():
    def __init__(self,name=None,choice=None,score = 0):
        self.name = name
        self.choice = choice
        self.score = score
    def __str__(self):
        return f'{self.name.capitalize()}\'s score is: {self.score}'
    def roShamBo(self):
        while True:
            try:
                roShamBo = int(input(f'{self.name.capitalize()}, what do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: '))
                print()
            except:
                print('\nTry again!, You must choose 0, 1 or 2.\n')
                continue
            if roShamBo == 0:
                self.choice = 'rock'
                break
            elif roShamBo == 1:
                self.choice = 'paper'
                break
            elif roShamBo == 2:
                self.choice = 'scissors'
                break
            else:
                print('\nTry again!, You must choose 0, 1 or 2.\n')
        print(f'{self.name.capitalize()} chooses {self.choice.capitalize()}')
        print(choices[self.choice])
        
       
class Computer():
    def __init__(self, name = 'Computer', choice = None, score =0):
        self.name = name
        self.choice = choice
        self.score = score
    def __str__(self):
        return f'{self.name}\'s score is: {self.score}'
    def roShamBo(self):
        ComputerChoices = ('rock','paper','scissors')
        ComputerPlay = random.randint(0,2)
        self.choice = ComputerChoices[ComputerPlay]
        print(f'{self.name} chooses {self.choice.capitalize()}')
        print(choices[self.choice])

def gameLogic(player1,player2):
    if player1.choice == player2.choice:
        print('GAME TIED!')
    elif player1.choice == 'rock':
        if player2.choice == 'scissors':
            print(f'{player1.name.upper()} WINS!')
            player1.score += 1  
        else:
            print(f'{player2.name.upper()} WINS!')
            player2.score += 1      
    elif player1.choice == 'paper':
        if player2.choice == 'rock':
            print(f'{player1.name.upper()} WINS!')
            player1.score += 1        
        else:
            print(f'{player2.name.upper()} WINS!')
            player2.score +=1
    elif player1.choice == 'scissors':
        if player2.choice == 'paper':
            print(f'{player1.name.upper()} WINS!')
            player1.score += 1
        else:
            print(f'{player2.name.upper()} WINS!')
            player2.score += 1
            
def scoreCard(player1,player2):
    print(f'{player1.name.capitalize()} Score: {player1.score}\n{player2.name} Score: {player2.score}')

def playAgain():
    goAgain = input('\nDo you want to play again?\nEnter "Y" for Yes or "N" for No: ').upper()
    if goAgain == 'N':
        return False

print('Welcome to Rock, Paper, Scissors!')
player_name = input('Enter your name: ')
Player1 = Player(player_name)
Player2 = Computer()

playing = True
while playing:
    Player1.roShamBo()
    Player2.roShamBo()
    gameLogic(Player1,Player2)
    scoreCard(Player1,Player2)
    playing = playAgain()

print('Thanks For Playing!')






