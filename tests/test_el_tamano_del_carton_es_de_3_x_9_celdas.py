from src import bingo

mi_carton = bingo.carton
def test_tamano_del_carton_3_x_9():
    assert bingo.tamano_del_carton_3_x_9(mi_carton)
