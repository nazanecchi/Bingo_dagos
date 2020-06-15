from src.bingo import carton

def test_separadas_por_decenas():
    mi_carton = carton()
    contador = 0
    contador2 = 0
    decenas = 1
    decenas2 = 9
    for contador in range(9):
        for contador2 in range(3):
            if mi_carton[contador2][contador] != 0:
                assert decenas <= mi_carton[contador2][contador] <= decenas2
        if decenas == 1:
            decenas = decenas + 9
        else:
            decenas = decenas + 10
        if decenas2 == 79:
            decenas2 = decenas2 + 11
        else:
            decenas2 = decenas2 + 10
