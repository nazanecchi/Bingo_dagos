from src.bingo import carton

def test_3_y_solo_3_columnas_con_1_celda_llena():
    mi_carton = carton()
    contador = 0
    contador2 = 0
    contaux = 0
    contaux2 = 0
    for contador in range(9):
        for contador2 in range(3):
            if mi_carton[contador2][contador] == 0:
                contaux = contaux + 1
        if contaux == 2:
            contaux2 = contaux2 + 1
        contaux = 0
    assert contaux2 == 3
