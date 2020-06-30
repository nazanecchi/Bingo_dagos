from src import bingo

mi_carton = bingo.carton
def test_no_existen_2_celdas_ocupadas_consecutivas():
    assert bingo.no_existen_2_celdas_ocupadas_consecutivas(mi_carton)
