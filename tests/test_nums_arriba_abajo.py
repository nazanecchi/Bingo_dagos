from src.bingo import carton

def test_arriba_abajo():
    mi_carton = carton()
    contador = 0
    contador2 = 0
    for contador in range(9):
        for contador2 in range(2):
            if mi_carton[contador2][contador] != 0 and mi_carton[contador2+1][contador] != 0:
                assert (mi_carton[contador2][contador] < mi_carton[contador2+1][contador])
