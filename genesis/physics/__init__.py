"""Physical simulation layer: terrain, fluids, thermodynamics, rigid bodies."""

from .terrain import Terrain, generate_terrain
from .fields import HydrostaticWater, Plants, ShallowWater, ThermalField
from .rigid import BallisticSystem, Sphere
from .world import PhysicsWorld

__all__ = [
    "BallisticSystem",
    "HydrostaticWater",
    "PhysicsWorld",
    "Plants",
    "ShallowWater",
    "Sphere",
    "Terrain",
    "ThermalField",
    "generate_terrain",
]
