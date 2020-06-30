from src import bingo

mi_carton = bingo.carton
def test_no_existen_filas_vacias():
    assert bingo.no_existen_filas_vacias(mi_carton)
