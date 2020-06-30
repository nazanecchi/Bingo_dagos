from src import bingo

mi_carton = bingo.carton
def test_tres_y_solo_tres_columnas_con_1_celda_llena():
    assert bingo.tres_y_solo_tres_columnas_con_1_celda_llena(mi_carton)
