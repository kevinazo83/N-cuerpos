# -*- coding: utf-8 -*-
"""
Created on Thu Jun  2 09:34:04 2022

@author: Keven
"""
import math

class Vector:
    def __init__(self, x=0.0, y=0.0, z=0.0): #iniciar la clase vector
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other): #suma de vcetores
        return Vector(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z,
        )
    def __sub__(self, other): #resta de vectores
        return Vector(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z,
        )
    def __mul__(self, other):
        if isinstance(other, Vector):  # producto punto de vectores
            return (
                self.x * other.x
                + self.y * other.y
                + self.z * other.z
            )
        elif isinstance(other, (int, float)):  # multiplicacion por un escalar
            return Vector(
                self.x * other,
                self.y * other,
                self.z * other,
            )
        else:
            raise TypeError("operand must be Vector, int, or float")
            
    def __truediv__(self, other): #división por un escalar
        if isinstance(other, (int, float)):
            return Vector(
                self.x / other,
                self.y / other,
                self.z / other,
            )
        else:
            raise TypeError("operand must be int or float")
            
    def get_magnitude(self): #magnitud del vector
        return math.sqrt(self.x ** 2 + self.y ** 2 + self.z ** 2)
    
    def normalize(self): #normalizar el vector
        magnitude = self.get_magnitude()
        return Vector(
            self.x / magnitude,
            self.y / magnitude,
            self.z / magnitude,
        )
