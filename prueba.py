# -*- coding: utf-8 -*-
"""
Created on Sun Jun  5 20:04:23 2022

@author: Laptop
"""
# simple_solar_system.py
from sistema_solar_3d import SolarSystem, Sun, Planet
solar_system = SolarSystem(400)
sun = Sun(solar_system)
planets = (
    Planet(
        solar_system,
        position=(150, 50, 0),
        velocity=(0, 5, 5),
    ),
    Planet(
        solar_system,
        mass=20,
        position=(100, -50, 150),
        velocity=(5, 0, 0)
    )
)
while True:
    solar_system.calculate_all_body_interactions()
    solar_system.update_all()
    solar_system.draw_all()