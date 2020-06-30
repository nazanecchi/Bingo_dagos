from src import bingo

mi_carton = bingo.carton
def test_izq_der():
    assert bingo.izq_der(mi_carton)
