import tkinter as tk
import time as time

import grid_create as gc
import ID as id


def create_board(n):
    """
    place ships and create the board
    :param n: board's size
    :return: list of ships
    """
    ships = gc.place_ships(n, gc.create_ships(l_min=n // 5, l_max=n, nb_bat=n // 2, average=n**(1/2), sigma=1.5))
    for i in range(n):
        for j in range(n):
            can.create_rectangle(j * h, i * w, (j + 1) * h,  (i + 1) * w, fill="blue")
    return ships


def get_cursor_click(event):
    """
    get the coordinates of a click
    """
    x, y = event.x, event.y
    i, j = min(x // h, n), min(y // w, n)
    play(j, i)


def play(i, j):
    """
    plays the cell i,j
    """
    global sunken_ships, M
    if M[i][j] != "O":
        lab.config(text='already played...')
    else:
        cell = is_a_ship(i, j, ships)
        if cell == -1:
            lab.config(text='miss')
            M[i][j] = ' '
            can.create_rectangle(j * h, i * w, (j + 1) * h,  (i + 1) * w, fill="white")
        else:
            lab.config(text='you have touched the boat number:' + str(cell + 1))
            M[i][j] = 'X'
            can.create_rectangle(j * h, i * w, (j + 1) * h,  (i + 1) * w, fill="orange")
            sunken_ships[cell][0] += -1
            if sunken_ships[cell][0] == 0:
                lab.config(text='you have sunk boat number :' + str(cell + 1))
                lab_nb_bat.config(text=str(nb_alive_ship(sunken_ships)) + ' boats left')
                for b in ships[cell]:
                    i, j = b
                    M[i][j] = 'M'
                    can.create_rectangle(j * h, i * w, (j + 1) * h,  (i + 1) * w, fill="red")
                if nb_alive_ship(sunken_ships) == 0:
                    t = time.time()
                    lab.config(text='Congratulations, you have won  !')
                    win = nb_coups(M)
                    lab_nb_bat.config(text='in ' + str(win) + ' moves and ' + str(t - t0) + ' seconds')
                    if id.User != 'User':
                        leaderboard(id.User, win, t - t0)


def is_a_ship(i, j, ships):
    """
    say if cell i,j is a ship or not
    :param i: cell line
    :param j: cell column
    :param ships: list of ships
    :return: the number of the boat in cell i,j if it is a boat, -1 otherwise
    """
    for b in range(len(ships)):
        if (i, j) in ships[b]:
            return b
    return -1


def nb_alive_ship(sunken_ships):
    """
    returns the number of boats still alive
    """
    i = 0
    for ship in sunken_ships:
        if ship[0] == 0:
            i += 1
    return len(sunken_ships) - i


def nb_coups(M):
    """
    returns the number of moves that have been played
    """
    c = 0
    for i in range(len(M)):
        for j in range(len(M[0])):
            if M[i][j] != 'O':
                c += 1
    return c


def leaderboard(User, win, play_time):
    """
    writes the result of the game to the leaderboard_n.txt file
    :param User: the name of the User
    :param win: number of moves that have been played
    :param play_time: playing time
    """
    name = 'leaderboard_' + str(n) + '.txt'
    with open(name, 'a') as f:
        f.write(str(User) + '/' + str(win) + '/' + str(play_time))
        f.write('\n')


n = 10
fen = tk.Tk()
h, w = 650 // n, 650 // n

can = tk.Canvas(fen, bg='blue', height=n * h, width=n * w)
can.pack(side=tk.TOP)

ships = create_board(n)
sunken_ships = [[len(ship), len(ship)] for ship in ships]
M = [['O' for i in range(n)] for j in range(n)]

lab = tk.Label(fen, text='Battleship', fg="red")
lab.pack()

lab_nb_bat = tk.Label(fen, text= str(len(ships)) + ' boats left', fg="green")
lab_nb_bat.pack()

can.bind("<Button-1>", get_cursor_click)
t0 = time.time()

fen.mainloop()
