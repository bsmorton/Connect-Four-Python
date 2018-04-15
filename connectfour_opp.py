# Bradley Morton ID BMORTON    Ariana Rowlands  ID AEROWLAN
import connectfour
import string



def display_board(gameboard_temp: connectfour.GameState):
    '''prints out the current game board'''
    temp_list=[[],[],[],[],[],[],[]]
    for pos in range(len(gameboard_temp.board)):
        temp_list[pos]=''
        for val in gameboard_temp.board[pos]:
            if val==0:
                temp_list[pos]='.'+temp_list[pos]
            elif val==1:
                temp_list[pos]='R'+temp_list[pos]
            elif val==2:
                temp_list[pos]='Y'+temp_list[pos]
    result=[]
    for num in range(len(temp_list)-1):
        s=''
        for str_list in temp_list :
            s+=str_list[num]+' '
        result.insert(0,s)
    print(('{} {} {} {} {} {} {}').format(1,2,3,4,5,6,7))
    for item in result:
        print(item)


def _prompt_user_red():
    '''prompts the Red player for a drop or pop and a column'''
    while True:
        try:
            red_choice=input("Would you like to drop (d) or pop (p)?",)
            col_choice=int(input("Please select a column (1-7).",))-1
        except (ValueError):
            print("Error! Invalid Input!\n")
            print()
            pass
        else:
            return red_choice,col_choice
    
    

def _prompt_user_yellow():
    '''prompts the Yellow player for a drop or pop and a column'''
    try:
            yellow_choice=input("Would you like to drop (d) or pop (p)?",)
            col_choice=int(input("Please select a column (1-7).",))-1
    except (ValueError):
            print("Error! Invalid Input!\n")
            print()
            pass
    else:
            return yellow_choice,col_choice
        
def _handle_prompt_user_yellow(gameboard: connectfour.GameState,prompt: tuple)->connectfour.GameState:
    '''handels the yellow players choices'''
    while True:
        
        try:
            yellow_choice,col_choice=prompt
            if yellow_choice=='d'and 0<=col_choice<=6:
                    new_gameboard=connectfour.drop(gameboard,col_choice)
                    return new_gameboard
            elif yellow_choice=='p'and 0<=col_choice<=6:
                    new_gameboard=connectfour.pop(gameboard,col_choice)
                    return new_gameboard
            else:
                    raise (connectfour.InvalidMoveError)
        except(connectfour.InvalidMoveError):
            print("Error! Invalid Input!\n")
            prompt=_prompt_user_yellow()
            pass
        



def _handle_prompt_user_red(gameboard: connectfour.GameState,prompt: tuple)->tuple:
    '''handels the red players choices'''
    while True:
        
        try:
            red_choice,col_choice=prompt

            if red_choice=='d'and 0<=col_choice<=6:
                    new_gameboard=connectfour.drop(gameboard,col_choice)
                    return new_gameboard, 'DROP '+ str(col_choice+1)
            elif red_choice=='p'and 0<=col_choice<=6:
                    new_gameboard=connectfour.pop(gameboard,col_choice)
                    return new_gameboard, 'POP '+ str(col_choice+1)
            else:
                    raise (connectfour.InvalidMoveError)
        except(connectfour.InvalidMoveError):
            print("Error! Invalid Input!\n")
            prompt=_prompt_user_red()
            pass
        



def _chk_gameover(gameboard: connectfour.GameState)->bool:
    '''checks if the game is over and if so returns a winner'''
    return not connectfour.winner(gameboard)==0



def _winning_player(gameboard: connectfour.GameState)->None:
    '''Displays the text for winning player color'''
    if connectfour.winner(gameboard)==1:
        print("RED PLAYER WINS")
    elif connectfour.winner(gameboard)==2:
        print("YELLOW PLAYER WINS")

        
            

def move_user_red(gameboard:connectfour.GameState)-> connectfour.GameState:
    '''makes the move for player Red'''
    try:
        if (_chk_gameover(gameboard)):
            raise (connectfour.GameOverError)
        print("RED PLAYER TURN")
        return _handle_prompt_user_red(gameboard,_prompt_user_red())
    except (connectfour.GameOverError):
        return _winning_player(gameboard)



def move_user_yellow(gameboard: connectfour.GameState)-> connectfour.GameState:
    '''makes the move for player yellow'''
    try:
        if (_chk_gameover(gameboard)):
            raise (connectfour.GameOverError)
        print("YELLOW PLAYER TURN")
        return _handle_prompt_user_yellow(gameboard,_prompt_user_yellow())
    except (connectfour.GameOverError):
        return _winning_player(gameboard)
