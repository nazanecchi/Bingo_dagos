from src.bingo import carton

def test_1_a_90():
    mi_carton = carton()
    contador = 0
    for fila in mi_carton:
        for celda in fila:
            if celda != 0:
                if celda >= 1 and celda <= 90:
                    contador=contador+1

    assert contador == 15
