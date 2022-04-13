pole = list(range(1,11))
win_combinions = ([1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7])


def polee():
    for i in range(3):
        print('|', pole[0 + i * 3], '|', pole[1 + i * 3], '|', pole[2 + i * 3], '|')


def check_win():
    for each in win_combinions:
        if (pole[each[0]-1]) == (pole[each[1]-1]) == (pole[each[2]-1]):
            return pole[each[1]-1]
        else:
            return False
def take_input(player_token):
    while True:
        value = input('Выберите число поля, куда поставить ' + player_token + ':')
        if not (value in '123456789'):
            print('Такого поля нет.')
            continue
        value = int(value)
        if str(pole[value - 1]) in 'XO':
            print('Поле занято.')
            continue
        pole[value - 1] = player_token
        break

def main():
    counter = 0
    while True:
        polee()
        if counter % 2 == 0:
            take_input('X')
        else:
            take_input('О')
        if counter > 3:
            winner = check_win()
            if winner:
                polee()
                print(winner, 'выиграл!')
                break
        counter +=1
        if counter > 8:
            polee()
            print('Ничья!')
            break

main()