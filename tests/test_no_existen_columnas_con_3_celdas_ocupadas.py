from src import bingo

mi_carton = bingo.carton
def test_no_columnas_con_las_3_celdas_llenas():
    assert bingo.no_columnas_con_las_3_celdas_llenas(mi_carton)
