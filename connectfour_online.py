# Bradley Morton ID BMORTON    Ariana Rowlands  ID AEROWLAN
import connectfour_client
import connectfour_opp
import connectfour


def human_player_move(connection:'connection', gameboard:connectfour.GameState)->connectfour.GameState:
    '''makes the move by the user'''
    player_move=connectfour_opp.move_user_red(gameboard)
    return player_move[0],player_move[1]


def nonhuman_player_move(connection:'connection', gameboard:connectfour.GameState,
                         player_choice: str)->connectfour.GameState:
    '''makes the move by the CPU'''
    connectfour_client.send_message(connection,player_choice)
    message_rec=connectfour_client.receive_response(connection)
    if message_rec[0]=='OKAY':
            if message_rec[1][0:4]=='DROP':
                gameboard=connectfour.drop(gameboard, int(message_rec[1][5])-1)
            elif message_rec[1][0:3]=='POP':
                gameboard=connectfour.pop(gameboard, int(message_rec[1][4])-1)
    return gameboard
    
def game():
    '''plays the game'''    

    connection=connectfour_client.connect()
    connectfour_client.initialize_online(connection)
    
    gameboard=connectfour.new_game()
    connectfour_opp.display_board(gameboard)

    while True:
        try:
            gameboard,player_choice=human_player_move(connection,gameboard)
            connectfour_opp.display_board(gameboard)
            gameboard=nonhuman_player_move(connection,gameboard,player_choice)
            connectfour_opp.display_board(gameboard)
        except:
            break
                
if __name__ == '__main__':         
    game()
    
