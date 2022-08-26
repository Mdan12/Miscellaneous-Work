board = {'A1': ' ' , 'B1': ' ' , 'C1': ' ' ,
        'A2': ' ' , 'B2': ' ' , 'C2': ' ' ,
        'A3': ' ' , 'B3': ' ' , 'C3': ' ' }
space = (' ')



player1points = 0
player2points = 0


playerchoice = 0

class tictactoe():

    def player1wins():
        row1 = board['A1'] + board['B1'] + board['C1']
        row2 = board['A2'] + board['B2'] + board['C2']
        row3 = board['A3'] + board['B3'] + board['C3']
        col1 = board['A1'] + board['A2'] + board['A3']
        col2 = board['B1'] + board['B2'] + board['B3']
        col3 = board['C1'] + board['C2'] + board['C3']
        mix1 = board['A1'] + board['B2'] + board['C3']
        mix2 = board['C1'] + board['B2'] + board['A3']
        if row1 == 'XXX' or row2 == 'XXX' or row3 == 'XXX':
            print('Player 1 wins')
            tictactoe.winner1()
        elif col1 == 'XXX' or col2 == 'XXX' or col3 == 'XXX':
            print('Player 1 wins')
            tictactoe.winner1()
        elif mix1 == 'XXX' or mix2 == 'XXX':
            print('Player 1 wins')
            tictactoe.winner1()
        elif row1 == 'OOO' or row2 == 'OOO' or row3 == 'OOO':
            print('Player 1 wins')
            tictactoe.winner2()
        elif col1 == 'OOO' or col2 == 'OOO' or col3 == 'OOO':
            print('Player 1 wins')
            tictactoe.winner2()
        elif mix1 == 'OOO' or mix2 == 'OOO':
            print('Player 1 wins')
            tictactoe.winner2()
        elif ' ' not in list(board.values()):
            tictactoe.Tryagain()
        else:
            tictactoe.checkinput()


    def checkinput():
        global playerchoice
        invalidinput = True
        while invalidinput:
            letnumb = input("Please enter a letter (A, B or C) followed by a number (1, 2, 3)").upper()
            letnumb = list(letnumb)
            col = letnumb[0]
            row = letnumb[1]
            if col in ['A', 'B', 'C'] and row in ['1', '2', '3']:
                if board[col + row] == 'X' or board[col + row] == 'O':
                    print("Filled")
                else:
                    if playerchoice % 2 == 0:
                        playerchoice += 1
                        board[col + row] = 'X'
                        invalidinput = False
                        tictactoe.printBoard()
                    else:
                        playerchoice += 1
                        board[col + row] = 'O'
                        invalidinput = False
                        tictactoe.printBoard()


    def printBoard():
        print('1:' + space + board['A1'] + space + '|' + space + board['B1'] + space + '|' + space + board['C1'])
        print('  -----------')
        print('2:' + space + board['A2'] + space + '|' + space + board['B2'] + space + '|' + space + board['C2'])
        print('  -----------')
        print('3:' + space + board['A3'] + space + '|' + space + board['B3'] + space + '|' + space + board['C3'])
        print('   A   B   C')
        row1 = board['A1'] + board['B1'] + board['C1']
        row2 = board['A2'] + board['B2'] + board['C2']
        row3 = board['A3'] + board['B3'] + board['C3']
        col1 = board['A1'] + board['A2'] + board['A3']
        col2 = board['B1'] + board['B2'] + board['B3']
        col3 = board['C1'] + board['C2'] + board['C3']
        mix1 = board['A1'] + board['B2'] + board['C3']
        mix2 = board['C1'] + board['B2'] + board['A3']
        tictactoe.player1wins()


    def winner1():
        board = {'A1': ' ' , 'B1': ' ' , 'C1': ' ' ,
                    'A2': ' ' , 'B2': ' ' , 'C2': ' ' ,
                    'A3': ' ' , 'B3': ' ' , 'C3': ' ' }
        space = (' ')
        global player1points
        player1points += 1
        if player1points == 1:
            print ('Player one has 1 point')
            print('Do you want to play again?')
            inputwrong = True
            while inputwrong:
                answer = input("Yes / No\n").capitalize()
                if answer == 'Yes':
                    inputwrong = False
                if answer == 'No':
                    inputwrong = False
                    print("Fine by me. Bye.")
                    exit()
        else:
            print('Player has', player1points, 'points')
            print('Do you want to play again?')
            inputwrong = True
            while inputwrong:
                answer = input("Yes / No\n").capitalize()
                if answer == 'Yes':
                    inputwrong = False
                if answer == 'No':
                    inputwrong = False
                    print("Fine by me. Bye.")
                    exit()


    def winner2():
        board = {'A1': ' ' , 'B1': ' ' , 'C1': ' ' ,
                    'A2': ' ' , 'B2': ' ' , 'C2': ' ' ,
                    'A3': ' ' , 'B3': ' ' , 'C3': ' ' }
        space = (' ')
        global player2points
        player2points += 1
        if player2points == 1:
            print ('Player one has 1 point')
            print('Do you want to play again?')
            inputwrong = True
            while inputwrong:
                answer = input("Yes / No\n").capitalize()
                if answer == 'Yes':
                    inputworng = False
                if answer == 'No':
                    inputwrong = False
                    print("Fine by me. Bye.")
                    exit()
        else:
            print('Player has', player2points, 'points')
            print('Do you want to play again?')
            inputwrong = True
            while inputwrong:
                answer = input("Yes / No\n").capitalize()
                if answer == 'Yes':
                    inputworng = False
                if answer == 'No':
                    inputwrong = False
                    print("Fine by me. Bye.")
                    exit()

    def Tryagain():
        print("Noody wins. Want to try again?")
        inputwrong = True
        while inputwrong:
            answer = input("Yes / No\n").capitalize()
            if answer == 'Yes':
                inputworng = False
            if answer == 'No':
                inputwrong = False
                print("Fine by me. Bye.")
                exit()

while True:
    board = {'A1': ' ' , 'B1': ' ' , 'C1': ' ' ,
            'A2': ' ' , 'B2': ' ' , 'C2': ' ' ,
            'A3': ' ' , 'B3': ' ' , 'C3': ' ' }
    space = (' ')
    playerchoice = 0
    tictactoe.checkinput()
