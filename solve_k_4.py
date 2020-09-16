# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 11:35:40 2020

@author: 1
"""

import numpy as np
import math as m
import pandas as pd

input_data = {'AB':2316.134, 'BC':1504.314, 'alphaA-B':[69, 24, 11.0],
              'Xa':2316.933, 'Ya':1614.121, 'theta':[22,16,24.1],
              'R':800, 'L':40, 'Crl':32000, 'h':0.105, 'ro':206265}
for k in input_data:
    print(k, input_data[k], sep=' = ')

def grad_r_sek(g, m=0, s=0):
    """ Переводит значение угла из градусов в секунды.
        На вход принимает значение угла в формате (g, m, s).
        Обязательный аргумент: g - градусы.
        Два не обязательных аргумента: m - минуты; s - секунды (по умолчанию
        равны 0)
        Возвращает значение угла в секундах.
    """
    s = g * 3600 + m * 60 + s
    return s


def sek_r_grad(s):
    """ Обратная функция для grad_r_sek.
        На вход принимает значение угла в секундах.
        Возвращает список в формате [g, m , s]
        g - градусы; m - минуты; s - секунды.
        Значения секунд округляються по правилам математики до 4 разряда
    """
    A = []
    A.append(int(s // 3600))
    A.append(int(m.fmod(s, 3600) // 60))
    A.append(float('{:.4f}'.format(m.fmod(m.fmod(s, 3600), 60))))
    return A


def gradVrad(angele_in_seconds):
    """ Принимает на вход значение угла в угловых секундах возвращает
        значение угла в радианах
    """
    angle_in_radians = angele_in_seconds * np.pi / (180 * 3600)
    return float('{:.9f}'.format(angle_in_radians))


def radVgrad(angle_in_radians):
    """ Принимает на вход значение угла в радианах возвращает
        значение угла в угловых секундах
    """
    angele_in_seconds = (angle_in_radians * 180 * 3600) / np.pi
    return float('{:.4f}'.format(angele_in_seconds))

def pickets(a):
    """ Принимает на вход число.
        Возвращает список:
            - первое значение в котором целое от деления числа на 100;
            - второе символ "+"
            - третье остаток от деления числа на 100
    """
    A = []
    A.append(int(a // 100))
    A.append('+')
    A.append(float('{:.3f}'.format(a % 100)))
    return A


basic_elements_of_a_circular_curve = {
    'T':input_data['R'] * np.tan(gradVrad(
            grad_r_sek(input_data['theta'][0],
                       input_data['theta'][1],
                       input_data['theta'][2]) / 2)),
    'K':(input_data['R'] * grad_r_sek(input_data['theta'][0],
                                      input_data['theta'][1],
                                      input_data['theta'][2])) / input_data['ro'],
    'D':2 * input_data['R'] * np.tan(gradVrad(
            grad_r_sek(input_data['theta'][0],
                       input_data['theta'][1],
                       input_data['theta'][2]) / 2)) - (input_data['R'] *
         grad_r_sek(input_data['theta'][0],
                    input_data['theta'][1],
                    input_data['theta'][2])) / input_data['ro'],
         }
beoacc = basic_elements_of_a_circular_curve
pick = {
        'PKnkk':pickets(input_data['AB'] - beoacc['T']),
        'PKkkk':pickets(input_data['AB'] - beoacc['T'] + beoacc['K']),
        'PKt_c':pickets(input_data['AB'] + input_data['BC'] - 2 * beoacc['T'] + beoacc['K']),
        'cPKkkk':pickets(input_data['AB'] + beoacc['T'] - beoacc['D']),
        'cPKt_c':pickets(input_data['AB'] + input_data['BC'] - beoacc['D']),
        }

for i in pick:
    print(i, pick[i])
   
calculating_the_coordinates_of_transition_curves = {
        't1':(input_data['L'] / 2 + 
              input_data['L'] ** 5 / (60 * 
                        input_data['Crl'] ** 2)),
        't2':(input_data['L'] / 2 - 
              input_data['L'] ** 5 / (24 * 
                        input_data['Crl'] ** 2)),
        'ph':(sek_r_grad(input_data['L'] / 
                         (2 * input_data['R']) * 
                         input_data['ro'])),
        'P':input_data['L'] ** 2 / (24 * input_data['R']),
        'q':input_data['h'] * 1.850 / 1.524
        }

Rn = input_data['R'] - calculating_the_coordinates_of_transition_curves['P']
Rm = (input_data['R'] - 
      calculating_the_coordinates_of_transition_curves['P'] - 
      calculating_the_coordinates_of_transition_curves['q'])

Xs = input_data['L'] - input_data['L'] ** 5 / (40 * input_data['Crl'] **2)
Ys = input_data['L'] ** 3 / (6 * input_data['Crl'])


x = 9.2
L = 893
n = 8
(x * input_data['ro']) / (L * 10 ** 3 * np.sqrt((n + 1.5) / 3))
1 / np.sqrt(15)
sek_r_grad(grad_r_sek(180, 0, 0)- grad_r_sek(1, 25, 56.6))
grad_r_sek(22, 16, 24.1)
input_data['AB'] - beoacc['T']
sek_r_grad(50 / (2 * 600) * 206265)
gradVrad(429718.75)
sek_r_grad(grad_r_sek(180, 0, 0) + grad_r_sek(91, 40, 35.1))






