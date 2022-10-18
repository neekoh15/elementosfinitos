# -*- coding: utf-8 -*-
"""tp1elementosfinitos.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1128z0JoQqv9TqBAvcvqbl_XCYgznDPIK

Objetivos del trabajo:
> Utilizar las herramientas numpy, matplotlib y scipy para graficar una curva representativa de un ensayo de esfuerzo vs deformacion de un material dado, calcular el valor del esfuerzo maximo, y la tenacidad de dicho material.

**LIBRERIAS A UTILIZAR**

> Se importan las librerias necesarias y algunas auxiliares para realizar todas las operaciones
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy import integrate

"""**SELECCION DEL MATERIAL ENSAYADO**

*`update 1: Si la seleccion no es un caracter valido o no es un ensayo existente, permite seleccionar otro`*





"""

lista_ensayos = ["ensayo_material1","ensayo_material2","ensayo_material3","ensayo_material4"]

global material_seleccionado

def seleccionar_ensayo():
  global eleccion
  try:
    print("Ensayos disponibles: \n", lista_ensayos)
    eleccion = int(input("Seleccione el material ensayado: "))
    if 1 <= eleccion <= len(lista_ensayos):
      print("Has seleccionado {}\n".format(lista_ensayos[eleccion-1]))
      return(eleccion)
    else:
      print("No es un ensayo válido, selecciona alguno de los disponibles \n")
      seleccionar_ensayo()

  except:
    print(" ")
    print("No es un caracter valido, intenta de nuevo \n")
    seleccionar_ensayo() 
    
seleccionar_ensayo()
material_seleccionado = int(eleccion)

"""**IMPORTACION DE DATOS**

> Utilizando la libreria "pandas" se procede a importar los datos del ensayo del material deseado, cargados previamente en un repositorio de Github (el repositorio es de mi autoria).

*`update 1: Si no encuentra el enlace seleccionado permite volver a intentarlo con otro a eleccion`*


"""

def primer_acceso(x):
    seleccion = x
    global df
    try:
      csv_url = "https://github.com/neekoh15/elementosfinitos/blob/main/{}.csv".format(lista_ensayos[seleccion-1])
      proper_url = csv_url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
      df = pd.read_csv(proper_url) 
      print("Accediendo a los datos del ensayo del material {}".format(seleccion))
      return(df)
    except:
        print("No hay datos sobre el ensayo al que se intenta acceder - Error accediendo a {} \n".format(lista_ensayos[seleccion-1]))
        print("Intenta seleccionando otro material")
        acceso_auxiliar()

def acceso_auxiliar():
    seleccionar_ensayo()
    nueva_seleccion = eleccion
    print("Nueva seleccion = {}".format(lista_ensayos[nueva_seleccion-1]))
    primer_acceso(nueva_seleccion)

primer_acceso(material_seleccionado)

data_frame = df
print("\n",data_frame)

"""****"""

choice = int(input("Decides: "))
    if choice == :

"""**CONVERSION DE DATOS**

> Se convierten los datos tipo "pandas.core.frame.DataFrame
" hacia el tipo "numpy.ndarray"



"""

data_array = data_frame.to_numpy()
print(data_array)

"""**CORRECCION DE FORMATO**

> Se redimensionan los datos para poder ser graficados correctamente


"""

esfuerzo = data_array[:,[0]]
deformacion = data_array[:,[1]]
re_arange1 = np.transpose(esfuerzo)
re_arange2 = np.transpose(deformacion)
x = np.array([])
y = np.array([])
a = np.concatenate((x, re_arange2), axis=None)
b = np.concatenate((y, re_arange1), axis=None)

"""**GRAFICO "ESFUERZO VS DEFORMACION"**

> Utilizando la libreria "matplotlib" se procede a graficar la curva "esfuerzo vs deformacion"


"""

fig, (ax1) = plt.subplots(1)
ymax = max(esfuerzo)
xmax = deformacion[np.argmax(esfuerzo, axis = 0)]
plt.title("Esfuerzo vs Deformacion - Material {}".format(material_seleccionado)) 
plt.xlabel("deformacion [mm/mm]") 
plt.ylabel("esfuerzo [Mpa]") 
ax1.plot(a, b)
plt.plot(xmax, ymax, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="green")
ax1.annotate('Punto de esfuerzo maximo', xy=(xmax, ymax), xytext=(xmax-0.02, ymax-500),
            arrowprops=dict(facecolor='black', shrink=0.02),
            )
plt.show() 
print("Valor de maximo esfuerzo = {} Mpa , correspondiente a una deformacion de {} mm".format(ymax,xmax))

"""**CALCULO DE LA TENACIDAD**

> Se obtiene la tenacidad, a traves del calculo del area bajo la curva "esfuerzo vs deformacion" mediante el metodo de Simpson y se muestra el grafico correspondiente a la misma.


"""

tenacidad1 = integrate.simps(b,a)

fig, (ax2) = plt.subplots(1)
ax2.plot(a, b)
ax2.fill_between(a, 0, b , color = "orange")
plt.text(a[-1]/3, b[-1]/2, r'TENACIDAD = {:.2f}'.format(tenacidad1), color = 'black')
plt.xlim(a[0], a[-1]*1.05)
plt.ylim(b[0], b[-1]*1.35)
plt.show()

"""
Codigo funcional completo:


"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy import integrate 

lista_ensayos = ["ensayo_material1","ensayo_material2","ensayo_material3","ensayo_material4"]

def seleccionar_ensayo():
  global eleccion
  try:
    print("Ensayos disponibles: \n", lista_ensayos)
    eleccion = int(input("Seleccione el material ensayado: "))
    if 1 <= eleccion <= len(lista_ensayos):
      print("Has seleccionado {}\n".format(lista_ensayos[eleccion-1]))
      return(eleccion)
    else:
      print("No es un ensayo válido, selecciona alguno de los disponibles \n")
      seleccionar_ensayo()

  except:
    print(" ")
    print("No es un caracter valido, intenta de nuevo \n")
    seleccionar_ensayo() 
    
seleccionar_ensayo()
material_seleccionado = int(eleccion)


def primer_acceso(x):
    seleccion = x
    global df
    try:
      csv_url = "https://github.com/neekoh15/elementosfinitos/blob/main/{}.csv".format(lista_ensayos[seleccion-1])
      proper_url = csv_url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")
      df = pd.read_csv(proper_url) 
      print("Accediendo a los datos del ensayo del material {}".format(seleccion))
      return(df)
    except:
        print("No hay datos sobre el ensayo al que se intenta acceder - Error accediendo a {} \n".format(lista_ensayos[seleccion-1]))
        print("Intenta seleccionando otro material")
        acceso_auxiliar()

def acceso_auxiliar():
    seleccionar_ensayo()
    nueva_seleccion = eleccion
    print("Nueva seleccion = {}".format(lista_ensayos[nueva_seleccion-1]))
    primer_acceso(nueva_seleccion)

primer_acceso(material_seleccionado)

data_frame = df
print("\n",data_frame, "\n")

data_array = data_frame.to_numpy()

print("Graficos de esfuerzo vs deformacion \n")

esfuerzo = data_array[:,[0]]
deformacion = data_array[:,[1]]
re_arange1 = np.transpose(esfuerzo)
re_arange2 = np.transpose(deformacion)
x = np.array([])
y = np.array([])
a = np.concatenate((x, re_arange2), axis=None)
b = np.concatenate((y, re_arange1), axis=None)

fig, (ax1) = plt.subplots(1)
ymax = max(esfuerzo)
xmax = deformacion[np.argmax(esfuerzo, axis = 0)]
plt.title("Esfuerzo vs Deformacion - Material {}".format(material_seleccionado)) 
plt.xlabel("deformacion [mm/mm]") 
plt.ylabel("esfuerzo [Mpa]") 
ax1.plot(a, b)
plt.plot(xmax, ymax, marker="o", markersize=5, markeredgecolor="red", markerfacecolor="green")
ax1.annotate('Punto de esfuerzo maximo', xy=(xmax, ymax), xytext=(xmax-0.02, ymax-500),
            arrowprops=dict(facecolor='black', shrink=0.02),
            )
plt.show() 
print("\n Valor de maximo esfuerzo = {} Mpa , correspondiente a una deformacion de {} mm \n".format(ymax,xmax))

print("Area bajo la curva - Calculo de la tenacidad del material \n")
tenacidad1 = integrate.simps(b,a)

fig, (ax2) = plt.subplots(1)
ax2.plot(a, b)
ax2.fill_between(a, 0, b , color = "orange")
plt.text(a[-1]/3, b[-1]/2, r'TENACIDAD = {:.2f}'.format(tenacidad1), color = 'black')
plt.xlim(a[0], a[-1]*1.05)
plt.ylim(b[0], b[-1]*1.35)
plt.show()