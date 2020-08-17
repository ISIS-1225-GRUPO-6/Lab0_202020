"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad de Los Andes
 * 
 * Contribución de:
 *
 * Cristian Camilo Castellanos
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

"""
  Este módulo es una aplicación básica con un menú de opciones para cargar datos, contar elementos, y hacer búsquedas sobre una lista.
"""

import config as cf
import sys
import csv
from time import process_time 
import pytest

def loadCSVFile (file, lst, sep=";"):
    """
    Carga un archivo csv a una lista
    Args:
        file 
            Archivo de texto del cual se cargaran los datos requeridos.
        lst :: []
            Lista a la cual quedaran cargados los elementos despues de la lectura del archivo.
        sep :: str
            Separador escodigo para diferenciar a los distintos elementos dentro del archivo.
    Try:
        Intenta cargar el archivo CSV a la lista que se le pasa por parametro, si encuentra algun error
        Borra la lista e informa al usuario
    Returns: None   
    """
    del lst[:]
    print("Cargando archivo ....")
    t1_start = process_time() #tiempo inicial
    dialect = csv.excel()
    dialect.delimiter=sep
    try:
        with open(file, encoding="utf-8") as csvfile:
            spamreader = csv.DictReader(csvfile, dialect=dialect)
            for row in spamreader: 
                lst.append(row)
    except:
        del lst[:]
        print("Se presento un error en la carga del archivo")
    
    t1_stop = process_time() #tiempo final
    print("Tiempo de ejecución ",t1_stop-t1_start," segundos")

def printMenu():
    """
    Imprime el menu de opciones
    """
    print("\nBienvenido")
    print("1- Cargar Datos")
    print("2- Contar los elementos de la Lista")
    print("3- Contar elementos filtrados por palabra clave")
    print("4- Consultar elementos a partir de dos listas")
    print("0- Salir")

def countElementsFilteredByColumn(criteria, column, lst):
    """
    Retorna cuantos elementos coinciden con un criterio para una columna dada  
    Args:
        criteria:: str
            Critero sobre el cual se va a contar la cantidad de apariciones
        column
            Columna del arreglo sobre la cual se debe realizar el conteo
        list
            Lista en la cual se realizará el conteo, debe estar inicializada
    Return:
        counter :: int
            la cantidad de veces ue aparece un elemento con el criterio definido
    """
    if len(lst)==0:
        print("La lista esta vacía")  
        return 0
    else:
        t1_start = process_time() #tiempo inicial
        counter=0 #Cantidad de repeticiones
        for i in range(len(lst)):
            if lst[i][column]==criteria: #filtrar por palabra clave 
                counter+=1
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
    return counter

def countElementsByCriteria(criteria, column, lst,lst1):
    if len(lst)==0 or len(lst1)==0:
        print("lista vacia")
        return 0
    else:
        t1_start=process_time()
        contador=0
        suma=0
        for i in range(len(lst1)):
            if lst1[i][column]==criteria:
                id=int(lst1[i]['id'])
                for j in range(len(lst)):
                    if int(lst[j]['\ufeffid'])==id and float(lst[j]['vote_average']) >= 6.0:
                        cont+=1
                        suma+= float(lst1[j]['vote_average'])
        t1_stop = process_time() #tiempo final
        print("Tiempo de ejecución ",t1_stop-t1_start," segundos")
        prom=(suma/cont)
    return("El director tiene"+str(cont)+" peliculas buenas y su calificación media es "+str(prom))
    
    
def selcol(resp):
    resp1=''
    if resp ==1:
        resp1 = '\ufeffid'
    elif resp ==2:
        resp1 = 'genres'
    elif resp ==3:
        resp1 = 'imdb_id'
    elif resp ==4:
        resp1 = 'original_title'
    elif resp ==5:
        resp1 = 'vote_average'
    else:
        print("no seleccionaste ninguna opcion valida")
    
    return resp1

def menu1():
    print("\nBienvenido")
    print("1- id")
    print("2- genero")
    print("3- id imdb")
    print("4- titulo original")
    print("5- popularidad")

def main():
    """
    Método principal del programa, se encarga de manejar todos los metodos adicionales creados
    Instancia una lista vacia en la cual se guardarán los datos cargados desde el archivo
    Args: None
    Return: None 
    """
    lista = [] #instanciar una lista vacia
    lista1 = []
    while True:
        printMenu() #imprimir el menu de opciones en consola
        inputs =input('Seleccione una opción para continuar\n') #leer opción ingresada
        if len(inputs)>0:
            if int(inputs[0])==1: #opcion 1
                loadCSVFile("Data/themoviesdb/AllMoviesDetailsCleaned.csv", lista) #llamar funcion cargar datos
                loadCSVFile("Data/themoviesdb/AllMoviesCastingRaw.csv", lista1)
                print("Datos cargados, "+str(len(lista))+" elementos cargados")
                print("Datos cargados, "+str(len(lista1))+" elementos cargados")
            elif int(inputs[0])==2: #opcion 2
                if len(lista)==0: #obtener la longitud de la lista
                    print("La lista esta vacía")    
                else: print("La lista tiene "+str(len(lista))+" elementos")
            elif int(inputs[0])==3: #opcion 3
                menu1()
                resp = input("seleccione que columna buscar \n")
                columna = selcol(int(resp))
                criteria =str(input('Ingrese el criterio de búsqueda\n'))
                counter=countElementsFilteredByColumn(criteria, columna, lista) #filtrar una columna por criterio  
                print("Coinciden ",counter," elementos con el crtierio: ", criteria  )
            elif int(inputs[0])==4: #opcion 4
                print("en esta opcion te mostraremos la cantidad de peliculas \n  bien calificadas de un autor")
                criteria =input('Ingrese el criterio de búsqueda , el nombre del autor\n')
                counter=countElementsByCriteria(criteria,'director_name',lista,lista1)
                print(counter," elementos con el crtierio: '", criteria ,"' (\n y que tienen una calificacion mayor a 6.0)")
            elif int(inputs[0])==0: #opcion 0, salir
                sys.exit(0)

if __name__ == "__main__":
    main()
