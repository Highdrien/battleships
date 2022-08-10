import os

N = [int(file[12:-4]) for file in os.listdir(os.getcwd()) if 'leaderboard_' in file]
top = 5


for n in N:
    print('\n')
    print('*'*10)
    print('\n')
    print('LEADERBOARD:')
    print('grid:', n, '*', n)
    L_time = []
    L_coup = []
    name = 'leaderboard_' + str(n) + '.txt'
    with open(name, 'r') as f:
        lines = f.readlines()
        for line in lines:
            User, coup, time = line[:-1].split('/')
            User += ' ' * (10 - len(User))
            L_time.append((float(time), int(coup), User))
            L_coup.append((int(coup), float(time), User))
    f.close()

    L_time.sort()
    L_coup.sort()

    if len(L_coup) >= top:
        print('top ' + str(top) + ' in the number of moves played:')
        for i in range(top):
            (coup, time, User) = L_coup[i]
            print(User, 'moves played : ', coup, '   time : ', time)
    print('\n')
    if len(L_time) >= top:
        print('top ' + str(top) + ' in the time: ')
        for i in range(top):
            (time, coup, User) = L_time[i]
            print(User, 'time : ', time, '   moves played : ', coup)

