from src.bingo import carton

#Ejercicio de la practica 2
def test_prac2_eje1():
    mi_carton = carton()
    contador = 0
    casillas_llenas_fila_1 = 0
    casillas_llenas_fila_2 = 0
    casillas_llenas_fila_3 = 0
    for contador in range(9):
        casillas_llenas_fila_1 = casillas_llenas_fila_1 + mi_carton[0][contador]

    contador = 0

    for contador in range(9):
        casillas_llenas_fila_2 = casillas_llenas_fila_2 + mi_carton[1][contador]

    contador = 0

    for contador in range(9):
        casillas_llenas_fila_3 = casillas_llenas_fila_3 + mi_carton[2][contador]

    assert casillas_llenas_fila_1 >= 1
    assert casillas_llenas_fila_2 >= 1
    assert casillas_llenas_fila_3 >= 1
