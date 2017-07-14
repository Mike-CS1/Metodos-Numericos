# -*- coding: utf-8 -*-
"""
Created on Thu Jul 13 23:34:48 2017

@author: Miguel
"""

import math

def f(x, b=False):
    '''
    FUNCIÓN A RESOLVER
    f(x) = (x-3)^3 + 5*x    
    x: valor para evaluar f
    d: False para indicar f
    d: True para indicar f'
    
    Al ser una ecuación de tercer grado, dos de sus soluciones son complejas y una sola es real, donde dicha raiz es aproximadamente x = 1.188634444
    '''
    return (x-3)**3 + 5*x

def Df(x, h):
    '''
    Derivada de la funcion en cuestion, por medio de diferencias definidas centradas
    x: valor a evaluar
    h: incrementos en las variaciones
    
    Nota: Éste método asume que existe una función definida previamente de nombre f(x).
    '''
    return (-f(x + 2.0*h) + 8*f(x + h) - 8*f(x - h) + f(x - 2.0*h))/(12.0*h)
    
def Biseccion(a, b, eps):
    '''
    METODO DE LA BISECCIÓN
    Intervalo de busqueda [a,b]
    eps: tolerancia de error
    
    Return: Retorna el valor x que es la raiz encontrada en caso satisfactorio, o retorna el valor obtenido sin éxito.
    
    Nota: Éste método asume que existe una función definida previamente de nombre f(x).
    '''
    print "n\tpn"
    i = 1
    while (b-a)/2.0 >= eps:
        c = (a+b)/2.0
        print str(i) + "\t" + str(c)
        if f(c)==0:
            print "Proceso terminado satisfactoriamente."
            return c
        elif f(a)*f(c)<0:
            b = c
        else:
            a = c
        i += 1
    print "Proceso terminado en " + str(i-1) + " iteraciones, \nCon un error de", (b-a)/2.0
    return c
    
def Newton(p0, tol, ni):
    '''
    METODO DE NEWTON-RAPHSON
    p0: punto de partida para iniciar la busqueda
    tol: tolerancia permitida de error
    ni: numero de iteraciones de calculos
    
    Return: Retorna el valor x que es la raiz encontrada en caso satisfactorio, o retorna el valor obtenido sin éxito.
    
    Nota: Éste método asume que existe una función definida previamente de nombre f(x). Tambien utiliza un modelo de derivada por diferencias divididas centrada de nombre Df(x, h), con h como incrementos.
    '''
    print "n\tpn"
    i = 1
    while i<=ni:
        p = p0 - f(p0)/Df(p0, 0.25)
        print str(i) + "\t" + str(p) 
        if math.fabs(p-p0) < tol:
            print "Proceso terminado satisfactoriamente en "+str(i)+" iteraciones.\nCon un error de",math.fabs(p-p0)
            return p
        p0 = p
        i+=1
    print "El método fracasó despues de " + str(ni) + " iteraciones."
    print "Procedimiento terminado sin éxito"
    return p
    
def Secante(x0, x1, eps, ni):
    '''
    METODO DE LA SECANTE
    x0: Primer valor inicial
    x1: Segundo valor inicial
    eps: Tolerancia permitida
    ni: Numero de Iteraciones
    
    Return: Retorna el valor x que es la raiz encontrada en caso satisfactorio, o retorna el valor obtenido sin éxito.
    
    Nota: Éste método asume que existe una función definida previamente de nombre f(x).
    '''
    print "n\tpn"
    i = 1
    while i<=ni:
        p = x1 - (f(x1)*(x0 - x1))/(f(x0)-f(x1))
        print str(i) + "\t" + str(p) 
        if math.fabs(p-x1) < eps:
            print "Proceso terminado satisfactoriamente en "+str(i)+" iteraciones.\nCon un error de",math.fabs(p-x1)
            return math.fabs(p)
        x0 = x1
        x1 = p
        i+=1
    print "El método fracasó despues de " + str(ni) + " iteraciones."
    print "Procedimiento terminado sin éxito"
    return p
    
def FalsaP(p0, p1, tol, ni):
    '''
    METODO DE LA FALSA POSICIÓN
    p0: punto extremo 1
    p1: punto extremo 2
    tol: tolerancia permitida
    ni: numero de iteraciones
    
    Return: Retorna el valor x que es la raiz encontrada en caso satisfactorio, o retorna el valor obtenido sin éxito.
    
    Nota: Éste método asume que existe una función definida previamente de nombre f(x).
    '''
    i = 1
    q0 = f(p0)
    q1 = f(p1)
    while i <= ni:
        p = p1 - q1*(p1 - p0)/(q1 - q0)
        print str(i) + "\t" + str(p)
        if math.fabs(p-p1) < tol:
            print "Proceso terminado satisfactoriamente en "+str(i)+" iteraciones.\nCon un error de",math.fabs(p-p1)
            return p
        i += 1
        q = f(p)
        if q*q1 < 0:
            p0 = p1
            q0 = q1
        p1 = p
        q1 = q
    print "El método fracasó despues de " + str(ni) + " iteraciones."
    print "Procedimiento terminado sin éxito"
    return p
    
def run():
    print "Método de Newton-Raphson"
    r1 = Newton(-10.0, 0.0000001, 10000)
    print "Método de la Secante"
    r2 = Secante(-10.0, 0.0, 0.0000001, 10000)
    print "Método de Bisección"
    r3 = Biseccion(-10.0, 10.0, 0.0000001)
    print "Método de Falsa Posición"
    r4 = FalsaP(-10.0, 10.0, 0.0000001, 10000)
    print "Raíces: \nNM: " + str(r1) + "\nSec: " + str(r2) + "\nBis: " + str(r3) + "\nFP: " + str(r4)
    print "La raiz real es aproximadamente x = 1.188634444"