from src.bingo import carton

def test_no_existen_2_celdas_vacias_consecutivas():
    mi_carton = carton()
    contador = 0
    contador2 = 0
    contaux = 0
    for contador2 in range(3):
        for contador in range(8):
            if mi_carton[contador2][contador] == 0 and mi_carton[contador2][contador+1] == 0 and mi_carton[contador2][contador+2] == 0:
                contaux = contaux + 1
                assert contaux == 0
                contaux = 0
