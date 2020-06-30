from src import bingo

mi_carton = bingo.carton
def test_no_existen_columnas_vacias():
    assert bingo.no_existen_columnas_vacias(mi_carton)

def test_hay_15_celdas_ocupadas():
    assert bingo.hay_15_celdas_ocupadas(mi_carton)
