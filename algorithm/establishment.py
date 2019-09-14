import numpy as np


class Establishment:

    def __init__(self):
        self.coords = np.array([43.5, -79.5])

    def distance_km(self, other_coords):
        self_lat, self_long = np.deg2rad(self.coords)
        other_lat, other_long = np.deg2rad(other_coords)
        a = 0.5 - np.cos(other_lat - self_lat) / 2 + np.cos(self_lat) * np.cos(other_lat) * (1 - np.cos(other_long - self_long)) / 2
        earth_diameter = 12742
        return earth_diameter * np.arcsin(np.sqrt(a))
