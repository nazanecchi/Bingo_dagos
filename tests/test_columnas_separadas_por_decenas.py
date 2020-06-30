from src import bingo

mi_carton = bingo.carton
def test_separadas_por_decenas():
    assert bingo.separadas_por_decenas(mi_carton)
