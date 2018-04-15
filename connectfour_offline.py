# Bradley Morton ID BMORTON    Ariana Rowlands  ID AEROWLAN
import connectfour
import connectfour_opp


def game():
    '''plays the game'''
    gameboard=connectfour.new_game()
    connectfour_opp.display_board(gameboard)
    while True:
        try:
            gameboard=connectfour_opp.move_user_red(gameboard)[0]
            connectfour_opp.display_board(gameboard)
            print()
            gameboard=connectfour_opp.move_user_yellow(gameboard)
            connectfour_opp.display_board(gameboard)
            print()
        except:
            break
        

if __name__ == '__main__':
    game()

