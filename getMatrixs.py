import numpy as np
from scipy.sparse.csgraph import connected_components
import sys
import conditions
def getMatrix():

    print('a) macierz 1')
    print('b) macierz 2')
    print('c) macierz 3')
    print('d) macierz 4')
    print('e) macierz 5')
    print('f) macierz 6')
    print('g) macierz 7')
    print('h) macierz 8')
    print('i) macierz 9')
    print('j) macierz 10')
    print('k) macierz 11')
    print('z) macierz 12')
    print('y) macierz 13')
    print('x) macierz 14')


    print('Wybierz zestaw ktory chcesz pobrac, zeby nasz program go rozwiązał')
    user=input('Podaj opcje : ')

    if user not in 'abcdefghijkzxy':
        conditions.incorrectInputMessage()

    with open(f"macierze/{user}.txt",mode='r') as file:
        n = sum(1 for linia in file)
    matrix = np.loadtxt(f"macierze/{user}.txt", usecols=range(n), dtype=float)


    suma_wartosci_przekatnej = np.sum(np.absolute(np.diagonal(matrix )))
    suma_wartosci_z_nad_przekatnej = np.sum(np.absolute(np.triu(matrix , 1)))
    suma_wartosci_z_pod_przekatnej = np.sum(np.absolute(np.tril(matrix , -1)))



    if suma_wartosci_z_pod_przekatnej + suma_wartosci_z_nad_przekatnej >= suma_wartosci_przekatnej:
        print('Nie został spełniony warunek zbieznosci dla metody Jacobiego')
        sys.exit(1)

    if np.linalg.det(matrix) == 0:
        print("Macierz jest sprzeczna lub ma nieskończenie wiele rozwiązań.")
    else:
        print("Macierz jest nie sprzeczna i ma jedno rozwiązanie.")
    # Sprawdzenie, czy macierz jest nieredukowalna

    eigenvalues, _ = np.linalg.eig(matrix)

    if np.any(np.iscomplex(eigenvalues)):
        #print("Macierz jest nieredukowalna.")
        print(' ')
    else:
        #print("Macierz jest redukowalna.")
        print(' ')




    matrixB = np.loadtxt(f"macierze/{user}.txt", usecols=range(n, n + 1), dtype=float)
    return [matrix, matrixB, n]
