from src import bingo

mi_carton = bingo.carton
def test_arriba_abajo():
    assert bingo.arriba_abajo(mi_carton)
