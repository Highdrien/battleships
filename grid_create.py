import math as m
import numpy as np
import random as rng


def place_ships(n, L):
    """
    Placement of the ships on an n*n matrix. The ships are represented under a list of length L.
    :param n: size of the grid (int)
    :param L: list of length of the ships (list)
    :return: List of ships. The ships are represented by a list of their coordinates
    """
    n = n + 2
    M = [[0 for i in range(n)] for j in range(n)]
    ships = []
    for k in L:
        c = 0
        ship_placed = False
        while c < 1000 and not ship_placed:
            c += 1
            dx = rng.randint(0, 1)
            dy = 1 - dx
            i = rng.randint(1, n - 2 - dx * k)
            j = rng.randint(1, n - 2 - dy * k)
            bat = [(i + l * dx, j + l * dy) for l in range(k)]
            ship_placed = possible_ship(bat, M, dx, dy)
        if c <= 1000 and ship_placed:
            ships.append(bat)
            for i in range(len(bat)):
                a, b = bat[i]
                M[a][b] = 1
    M, ships = resize_grid(M, ships)
    # print(np.array(M))
    return ships


def resize_grid(M, ships):
    """
    removes the sides of the grid, and changes the ship list accordingly
    :param M: grid
    :param ships: list of ship
    :return: resized grid and list of ships (with the new coordinates)
    """
    resize_M = [M[i][1:-1] for i in range(1, len(M) - 1)]
    resize_ships = [[(b[0] - 1, b[1] - 1) for b in ship] for ship in ships]
    return resize_M, resize_ships


def possible_ship(ship, M, dx, dy):
    """
    Check if the ship can enter the grid M with the directions dx, dy
    :param ship: list of ship's coordinates
    :param M: grid
    :param dx: x-direction: -1 0 or 1
    :param dy: y-direction: -1 0 or 1
    :return: bool
    """
    i, j = ship[0]
    for k in range(-1, 1 + len(ship)):
        for l in range(-1, 2):
            i1, j1 = i + k * dx + l * dy, j + k * dy + l * dx
            if M[i1][j1] != 0:
                return False
    return True


def create_ships(l_min=3, l_max=10, nb_bat=8, average=3, sigma=1.5):
    """
    creates a list of ship lengths
    :param l_min: minimum length of the ships
    :param l_max: maximum length of the ships
    :param nb_bat: number of ships
    :param average: average length of the ships
    :param sigma: variance of the length of the ships
    :return: list of ship lengths
    """
    X = [normal_distribution(i, average, sigma) for i in range(l_max)]
    S_tot = sum(X[l_min:])
    Y = [0 for i in range(len(X))]
    S = 0
    for i in range(l_min, len(X)):
        S += X[i]
        Y[i] = S / S_tot
    L = []
    for k in range(nb_bat):
        r = rng.random()
        append_ship = False
        for i in range(len(Y)):
            if r < Y[i] and not append_ship:
                L.append(-i)
                append_ship = True
    L.sort()
    L = [-i for i in L]
    # print(L)
    return L


def normal_distribution(x, average, s):
    A = 1 / (s * m.sqrt(m.pi))
    B = ((x - average) / s) ** 2
    return A * m.exp(-B / 2)


if __name__ == "__main__":
    n = 10
    L = create_ships(l_min=2, l_max=10, nb_bat=12, average=4, sigma=1.5)
    place_ships(n, L)
