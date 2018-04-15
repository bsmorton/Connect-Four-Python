# Bradley Morton ID BMORTON    Ariana Rowlands  ID AEROWLAN
import socket

def _read_host()-> str:
    '''takes user input and returns a host'''
    while True:
        host = input('Host: ').strip()

        if host == '':
            print('Please specify a host (either a name or an IP address)')
        else:
            return host

def _read_port() -> int:
    '''takes user input and returns a port'''
    while True:
        try:
            port = int(input('Port: ').strip())

            if port < 0 or port > 65535:
                print('Ports must be an integer between 0 and 65535')
            else:
                return port

        except ValueError:
            print('Ports must be an integer between 0 and 65535')

def _read_user_name()-> str:
    '''takes user input and returns a user name'''
    while True:
        user = input('Username: ').strip()

        if user == '' or ' ' in user:
            print('Please specify a valid Username')
        else:
            return user


def send_message(connection: 'connection', message: str) -> None:
    '''sends message to client'''
    echo_socket, echo_socket_input, echo_socket_output = connection

    
    echo_socket_output.write(message + '\r\n')
    echo_socket_output.flush()



def receive_response(connection: 'connection') -> None:
    '''recieves message from client'''
    echo_socket, echo_socket_input, echo_socket_output = connection
    word_1=echo_socket_input.readline()[:-1]
    if word_1=='OKAY':
        word_2=echo_socket_input.readline()[:-1]
        word_3=echo_socket_input.readline()[:-1]
        result=[word_1,word_2,word_3]
    elif word_1 =='INVALID':
        word_2=echo_socket_input.readline()[:-1]
        result=[word_1,word_2]
    else:
        result=[word_1]
    return result



def connect() -> 'connection':
    '''connects host and port with appropriate client'''
    host=_read_host()
    port=_read_port()
    
    echo_socket = socket.socket()
    echo_socket.connect((host, port))


    echo_socket_input = echo_socket.makefile('r')
    echo_socket_output = echo_socket.makefile('w')

    return echo_socket, echo_socket_input, echo_socket_output


def initialize_online(connection:'connection'):
    '''initializes the online functionality of the module'''
    user_name=_read_user_name()
    send_message(connection,'I32CFSP_HELLO '+user_name)
    message_rec=receive_response(connection)
    send_message(connection,'AI_GAME')
    message_rec=receive_response(connection)


















    
