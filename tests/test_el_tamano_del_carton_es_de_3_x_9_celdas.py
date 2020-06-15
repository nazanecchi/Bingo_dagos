from src.bingo import carton

def test_no_columnas_con_las_3_celdas_llenas():
    mi_carton = carton()
    assert len(mi_carton) == 3
    assert len(mi_carton[0]) == 9
    assert len(mi_carton[1]) == 9
    assert len(mi_carton[2]) == 9
