from src.bingo import carton

def test_izq_der():
    mi_carton = carton()
    contador = 0
    contador2 = 0
    for contador2 in range(3):
        for contador in range(8):
            if mi_carton[contador2][contador] != 0 and mi_carton[contador2][contador+1] != 0:
                assert (mi_carton[contador2][contador] < mi_carton[contador2][contador+1])
