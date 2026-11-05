"""Rigid-body ballistics used for thrown/dropped objects and physics tests."""

from __future__ import annotations

import math

GRAVITY = 9.81


class Sphere:
    __slots__ = (
        "pos", "vel", "radius", "mass", "restitution", "drag", "friction", "id",
    )

    def __init__(self, pos, vel=(0.0, 0.0, 0.0), radius=0.25, mass=1.0,
                 restitution=0.55, drag=0.02, friction=0.3, body_id="sphere"):
        self.pos = [float(v) for v in pos]
        self.vel = [float(v) for v in vel]
        self.radius = float(radius)
        self.mass = float(mass)
        self.restitution = float(restitution)
        self.drag = float(drag)
        self.friction = float(friction)
        self.id = body_id

    def kinetic_energy(self):
        vx, vy, vz = self.vel
        return 0.5 * self.mass * (vx * vx + vy * vy + vz * vz)

    def potential_energy(self, datum=0.0):
        return self.mass * GRAVITY * (self.pos[2] - datum)

    def energy(self, datum=0.0):
        return self.kinetic_energy() + self.potential_energy(datum)


class BallisticSystem:
    """Velocity-Verlet integrator with quadratic drag and ground contact.

    Velocity Verlet is chosen because it is symplectic and exact for constant
    acceleration, so a free-falling body shows no secular energy drift. Every
    inelastic loss (drag, impact, tangential friction) is accumulated in
    ``dissipated`` so the energy ledger still closes.
    """

    def __init__(self, terrain, gravity=-GRAVITY):
        self.terrain = terrain
        self.gravity = float(gravity)
        self.bodies = []
        self.dissipated = 0.0
        self.contacts = 0

    def add(self, body):
        self.bodies.append(body)
        return body

    def mechanical_energy(self, datum=0.0):
        return sum(b.energy(datum) for b in self.bodies)

    def _accel(self, body, vel):
        ax = 0.0
        ay = 0.0
        az = self.gravity
        if body.drag:
            speed = math.sqrt(vel[0] ** 2 + vel[1] ** 2 + vel[2] ** 2)
            factor = body.drag * speed / body.mass
            ax -= factor * vel[0]
            ay -= factor * vel[1]
            az -= factor * vel[2]
        return (ax, ay, az)

    def step(self, dt, substeps=4):
        h = dt / substeps
        for body in self.bodies:
            for _ in range(substeps):
                self._advance(body, h)

    def _advance(self, body, h):
        pos = body.pos
        vel = body.vel
        a0 = self._accel(body, vel)
        pos[0] += vel[0] * h + 0.5 * a0[0] * h * h
        pos[1] += vel[1] * h + 0.5 * a0[1] * h * h
        pos[2] += vel[2] * h + 0.5 * a0[2] * h * h

        v1 = (vel[0] + a0[0] * h, vel[1] + a0[1] * h, vel[2] + a0[2] * h)
        a1 = self._accel(body, v1)
        vel[0] += 0.5 * (a0[0] + a1[0]) * h
        vel[1] += 0.5 * (a0[1] + a1[1]) * h
        vel[2] += 0.5 * (a0[2] + a1[2]) * h

        ground = self.terrain.sample(pos[0], pos[1])
        if pos[2] - body.radius < ground:
            pos[2] = ground + body.radius
            before = body.energy()
            if vel[2] < 0.0:
                vel[2] = -vel[2] * body.restitution
                vel[0] *= 1.0 - body.friction
                vel[1] *= 1.0 - body.friction
                self.contacts += 1
            after = body.energy()
            if before > after:
                self.dissipated += before - after
