from src.bingo import carton

def test_fila_exactamente_5_celdas():
    mi_carton = carton()
    contador = 0
    contador2 = 0
    contaux = 0
    for contador2 in range(3):
        for contador in range(9):
            if mi_carton[contador2][contador] != 0:
                contaux = contaux + 1
        assert contaux == 5
        contaux = 0
