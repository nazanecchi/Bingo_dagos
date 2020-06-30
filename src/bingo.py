import random
import math
def carton():
    contador = 0
    carton = (
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0]
    )
    numerosCarton = 0

    while (numerosCarton < 15):
      contador = contador + 1
      if (contador == 50):
        return carton
      numero = random.randint(1,90)

      columna = math.floor(numero / 10)
      if (columna == 9):
          columna = 8
      huecos = 0
      for i in range(3):
        if (carton[i][columna] == 0):
          huecos = huecos + 1
        if (carton[i][columna] == numero):
          huecos = 0
          break
      if (huecos < 2):
        continue
      fila = 0
      for j in range(3):
        huecos = 0
        for i in range(9):
          if (carton[fila][i] == 0):
              huecos = huecos + 1
        if (huecos < 5 or carton[fila][columna] != 0):
          fila = fila + 1
        else:
          break
      if (fila == 3):
        continue
      carton[fila][columna] = numero
      numerosCarton = numerosCarton + 1
      contador = 0
    for x in range(9):
      huecos = 0
      for y in range(3):
        if (carton[y][x] == 0):
            huecos = huecos + 1
      if (huecos == 3):
        return carton
    return carton

def imprimirCarton(carton):
    for columna in range(3):
        for fila in range(9):
            if carton[columna][fila] > 9:
                print(carton[columna][fila], end='   ')
            if carton[columna][fila] <= 9:
                print(carton[columna][fila], end='    ')
        print('\n')
        
def tres_y_solo_tres_columnas_con_1_celda_llena(mi_carton):
    contador = 0
    contador2 = 0
    contaux = 0
    contaux2 = 0
    x = 0
    for contador in range(9):
        for contador2 in range(3):
            if mi_carton[contador2][contador] == 0:
                contaux = contaux + 1
        if contaux == 2:
            contaux2 = contaux2 + 1
        contaux = 0
    if contaux2 == 3:
        x = 1
    return (x==1)

def fila_exactamente_5_celdas(mi_carton):
    contador = 0
    contador2 = 0
    contaux = 0
    x = 0
    for contador2 in range(3):
        for contador in range(9):
            if mi_carton[contador2][contador] != 0:
                contaux = contaux + 1
        if contaux == 5:
            x = 1
        contaux = 0
    return (x==1)

def separadas_por_decenas(mi_carton):
    contador = 0
    contador2 = 0
    decenas = 1
    decenas2 = 9
    x = 1
    for contador in range(9):
        for contador2 in range(3):
            if mi_carton[contador2][contador] != 0:
                if decenas > mi_carton[contador2][contador] > decenas2:
                    x = 0
        if decenas == 1:
            decenas = decenas + 9
        else:
            decenas = decenas + 10
        if decenas2 == 79:
            decenas2 = decenas2 + 11
        else:
            decenas2 = decenas2 + 10
    return (x==1)

def tamano_del_carton_3_x_9(mi_carton):
    x = 0
    if len(mi_carton) == 3 and len(mi_carton[0]) == 9 and len(mi_carton[1]) == 9 and len(mi_carton[2]) == 9:
        x = 1
    return (x==1)

def no_existen_mas_de_2_celdas_vacias_consecutivas(mi_carton):
    contador = 0
    contador2 = 0
    contaux = 0
    x = 1
    for contador2 in range(3):
        for contador in range(7):
            if mi_carton[contador2][contador] == 0 and mi_carton[contador2][contador+1] == 0 and mi_carton[contador2][contador+2] == 0:
                contaux = contaux + 1
                if contaux != 0:
                    x = 0
                contaux = 0
    return (x==1)

def no_existen_2_celdas_ocupadas_consecutivas(mi_carton):
    contador = 0
    contador2 = 0
    contaux = 0
    x = 1
    for contador2 in range(3):
        for contador in range(7):
            if mi_carton[contador2][contador] != 0 and mi_carton[contador2][contador+1] != 0 and mi_carton[contador2][contador+2] != 0:
                contaux = contaux + 1
                if contaux != 0:
                    x = 0
                contaux = 0
    return (x==1)

def no_columnas_con_las_3_celdas_llenas(mi_carton):
    contador = 0
    contador2 = 0
    contaux = 0
    x = 1
    for contador in range(9):
        for contador2 in range(3):
            if mi_carton[contador2][contador] != 0:
                contaux = contaux + 1
        if contaux == 3:
            x = 0
        contaux = 0
    return (x==1)

def hay_15_celdas_ocupadas(mi_carton):
    contador = 27
    x = 0
    for fila in mi_carton:
        for celda in fila:
            if celda==0:
                contador=contador-1

    if contador == 15:
        x = 1
    return (x==1)

def no_existen_columnas_vacias(mi_carton):
    contador = 0
    x = 1
    for contador in range(9):
        if (mi_carton[0][contador] + mi_carton[1][contador] + mi_carton[2][contador]) == 0:
            x = 0
    return (x==1)

def no_existen_filas_vacias(mi_carton):
    contador = 0
    casillas_llenas_fila_1 = 0
    casillas_llenas_fila_2 = 0
    casillas_llenas_fila_3 = 0
    x = 0
    for contador in range(9):
        casillas_llenas_fila_1 = casillas_llenas_fila_1 + mi_carton[0][contador]

    contador = 0

    for contador in range(9):
        casillas_llenas_fila_2 = casillas_llenas_fila_2 + mi_carton[1][contador]

    contador = 0

    for contador in range(9):
        casillas_llenas_fila_3 = casillas_llenas_fila_3 + mi_carton[2][contador]

    if casillas_llenas_fila_1 >= 1 and casillas_llenas_fila_2 >= 1 and casillas_llenas_fila_3 >= 1:
        x = 1
    return (x==1)

def no_existen_2_celdas_vacias_consecutivas(mi_carton):
    contador = 0
    contador2 = 0
    contaux = 0
    x = 1
    for contador2 in range(3):
        for contador in range(7):
            if mi_carton[contador2][contador] == 0 and mi_carton[contador2][contador+1] == 0 and mi_carton[contador2][contador+2] == 0:
                contaux = contaux + 1
                if contaux != 0:
                    x = 0
                contaux = 0
    return (x==1)

def numeros_1_a_90(mi_carton):
    contador = 0
    x = 0
    for fila in mi_carton:
        for celda in fila:
            if celda != 0:
                if celda >= 1 and celda <= 90:
                    contador=contador+1

    if contador == 15:
        x = 1
    return (x==1)

def arriba_abajo(mi_carton):
    contador = 0
    contador2 = 0
    x = 1
    for contador in range(9):
        for contador2 in range(1):
            if mi_carton[contador2][contador] != 0 and mi_carton[contador2+1][contador] != 0:
                if (mi_carton[contador2][contador] > mi_carton[contador2+1][contador]):
                    x = 0
            if mi_carton[contador2][contador] != 0 and mi_carton[contador2+1][contador] == 0:
                if (mi_carton[contador2][contador] > mi_carton[contador2+2][contador]):
                    x = 0
    return(x==1)


def izq_der(mi_carton):
    contador = 0
    contador2 = 0
    x = 1
    for contador2 in range(3):
        for contador in range(8):
            if mi_carton[contador2][contador] != 0 and mi_carton[contador2][contador+1] != 0:
                if (mi_carton[contador2][contador] > mi_carton[contador2][contador+1]):
                    x = 0
    return(x==1)

def generar_carton_valido():
    r=0
    while(r==0):
        mi_carton=carton()
        if tamano_del_carton_3_x_9(mi_carton) == True and izq_der(mi_carton) == True and arriba_abajo(mi_carton) == True and numeros_1_a_90(mi_carton) == True and no_existen_2_celdas_vacias_consecutivas(mi_carton) == True and no_existen_filas_vacias(mi_carton) == True and no_existen_columnas_vacias(mi_carton) == True and hay_15_celdas_ocupadas(mi_carton) == True and no_columnas_con_las_3_celdas_llenas(mi_carton) == True and no_existen_2_celdas_ocupadas_consecutivas(mi_carton) == True and no_existen_mas_de_2_celdas_vacias_consecutivas(mi_carton) == True and separadas_por_decenas(mi_carton) == True and fila_exactamente_5_celdas(mi_carton) == True and tres_y_solo_tres_columnas_con_1_celda_llena(mi_carton) == True:
            r = 1
    return mi_carton

carton = generar_carton_valido()
imprimirCarton(carton)
