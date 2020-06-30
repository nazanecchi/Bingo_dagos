from src import bingo

mi_carton = bingo.carton
def test_fila_exactamente_5_celdas():
    assert bingo.fila_exactamente_5_celdas(mi_carton)
