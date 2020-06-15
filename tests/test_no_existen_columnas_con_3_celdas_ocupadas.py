from src.bingo import carton

def test_no_columnas_con_las_3_celdas_llenas():
    mi_carton = carton()
    contador = 0
    contador2 = 0
    contaux = 0
    for contador in range(9):
        for contador2 in range(3):
            if mi_carton[contador2][contador] == 0:
                contaux = contaux + 1
        assert contaux != 0
        contaux = 0
