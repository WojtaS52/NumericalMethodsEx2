import conditions
import numpy as np
import getMatrixs as gm
import matrix


def menuStart():
    print('Rozwiązywania układu N równań liniowych z N niewiadomym metoda iteracyjna Jacobiego (iteracji prostej)')
    print('--------------Menu główne--------------')
    print('1)Metoda Jacobiego')
    print('2)Zakonczenie programu')
    user=int(input('Podaj opcje : '))

    if(user == 1):
        print('Wybierz metode zakonczenia: ')
        print('1) Epsilon')
        print('2) Iteracja')

        user2 = int(input('Podaj warunek zakonczenia metody jacobiego'))

        if user2 == 1:
            eps = float(input('Podaj wartosc epsilonu'))

            temp_list = gm.getMatrix()
            A, B, n = temp_list
            D = np.zeros((n, n))
            row, col = np.diag_indices_from(D)
            D[row, col] = np.diagonal(A)

            L = np.triu(A, 1)

            U = np.tril(A, -1)


            N = np.zeros((n, n))
            row, col = np.diag_indices_from(N)
            N[row, col] = (np.diagonal(D)) ** (-1)


            M =np.matmul(-N, (np.add(L, U)))

            x1 = np.zeros(n)

            value = matrix.my_jacobiMethod_epsilon(N, B, M, x1, eps)
            print(value)


        elif user2 == 2:
            iterations = int(input('Podaj liczbe iteracji'))
            temp_list = gm.getMatrix()
            A, B, n = temp_list
            D = np.zeros((n, n))
            row, col = np.diag_indices_from(D)
            D[row, col] = np.diagonal(A)


            L = np.triu(A, 1)


            U = np.tril(A, -1)

            N = np.zeros((n, n))
            row, col = np.diag_indices_from(N)
            N[row, col] = (np.diagonal(D)) ** (-1)

            M = matrix.my_matmul(-N, (matrix.my_add(L, U)))

            x1 = np.zeros(n)

            value = matrix.my_jacobiMethod_itteration(N, B, M, x1, iterations)
            print( value)
    elif user == 2:
        conditions.shutDownThisProgram()
