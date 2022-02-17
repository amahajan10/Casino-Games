import cards
import time
import universal_commands

class bjPlayer(cards.Player):
    def __init__(self, name):
        super().__init__(name)

    def get_total(self):
        """return total of player's hand"""
        sum = 0
        for i in self.hand:
            value = i.val
            if i.val > 10:
                value = 10
            elif i.val == 1 and (sum + 11) < 21:
                value = 11
            sum = sum + value
        return sum


def player_phase(deck):
    """Players phase/turn"""
    name = input("Enter player name: ")
    player = bjPlayer(name)
    player.draw(deck, 2)
    player.show_hand()
    keepGoing = True

    while(keepGoing):
        move = input("Enter next move (Hit, Stand): ")
        if move.lower() == "hit":
            player.draw(deck)
            player.show_hand()
        elif move.lower() == "stand":
            keepGoing = False
            break
        else:
            print("Invalid move")

    return player

def print_both(cpu, player):
    """Print display for console/terminal"""
    universal_commands.clear()
    cpu.show_hand()
    if player != None:
        player.show_hand()
   

def computer_phase(deck, cpu, player):
    """CPU/dealer turn"""
    while cpu.get_total() < 17:
        cpu.draw(deck, 1)
        time.sleep(2)
        print_both(cpu, player)

def eval(cpu, play):
    """"Blackjack evaluation of card totals and determines result"""
    cpu_total = cpu.get_total()
    player_total = play.get_total()
    # Tie Case
    if player_total == cpu_total and player_total <= 21: 
        print("Tie")
    # player win case
    elif player_total > cpu_total and player_total <= 21:
        print(f'{play.name} wins!')
    # player win with cpu bust
    elif player_total < cpu_total and player_total <= 21 and cpu_total > 21: 
       print(f'{play.name} wins!') 
    # cpu win case
    elif player_total < cpu_total and cpu_total <= 21:
        print(f'{cpu.name} wins!')
    # cpu win with player bust
    elif player_total > cpu_total and cpu_total <= 21 and player_total > 21:
       print(f'{cpu.name} wins!') 
    # both player and cpu bust 
    elif player_total > 21 and cpu_total > 21:
        print("Both players bust.")
    else:
        print("Unimplemented result")


    

if __name__ == "__main__":  
        deck = cards.Deck()
        deck.shuffle_deck()
        cpu = bjPlayer("CPU")
        cpu.draw(deck, 1)
        cpu.show_hand()
        play = player_phase(deck)
        cp = computer_phase(deck, cpu, play)
        eval(cpu, play)

