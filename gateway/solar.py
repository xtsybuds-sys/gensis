"""Solar position from real orbital geometry.

No scripted clock: the sun's declination and hour angle come from the standard
low-precision solar formulae (Meeus / NOAA), so day length, sun height and the
seasonal drift all follow from the planet's tilt, spin and orbit. The planet's
latitude and longitude are viewer initial conditions (stated in the contract), not
measurements.
"""

from __future__ import annotations

import math

J2000 = 2451545.0
_UNIX_EPOCH_JD = 2440587.5


def solar_position(unix_time, latitude_deg=35.0, longitude_deg=0.0):
    """Return the sun's elevation, azimuth and unit direction for a UTC instant.

    Direction is in a right-handed frame with +y up, +x east and +z south, which is
    what the viewer consumes.
    """
    jd = unix_time / 86400.0 + _UNIX_EPOCH_JD
    n = jd - J2000

    mean_long = math.radians((280.460 + 0.9856474 * n) % 360.0)
    mean_anom = math.radians((357.528 + 0.9856003 * n) % 360.0)
    ecliptic = mean_long + math.radians(
        1.915 * math.sin(mean_anom) + 0.020 * math.sin(2.0 * mean_anom)
    )
    obliq = math.radians(23.439 - 0.0000004 * n)

    right_asc = math.atan2(math.cos(obliq) * math.sin(ecliptic), math.cos(ecliptic))
    decl = math.asin(math.sin(obliq) * math.sin(ecliptic))

    gmst_hours = (18.697374558 + 24.06570982441908 * n) % 24.0
    lst_deg = gmst_hours * 15.0 + longitude_deg
    hour_angle = math.radians(lst_deg - math.degrees(right_asc))

    lat = math.radians(latitude_deg)
    sin_elev = math.sin(lat) * math.sin(decl) + math.cos(lat) * math.cos(decl) * math.cos(
        hour_angle
    )
    elevation = math.asin(max(-1.0, min(1.0, sin_elev)))

    # Azimuth measured clockwise from north.
    azimuth = math.atan2(
        -math.cos(decl) * math.sin(hour_angle),
        math.sin(decl) * math.cos(lat) - math.cos(decl) * math.sin(lat) * math.cos(hour_angle),
    )
    azimuth_deg = (math.degrees(azimuth) + 180.0) % 360.0
    elevation_deg = math.degrees(elevation)

    az = math.radians(azimuth_deg)
    el = math.radians(elevation_deg)
    direction = [
        math.cos(el) * math.sin(az),
        math.sin(el),
        -math.cos(el) * math.cos(az),
    ]
    return {
        "elevation_deg": round(elevation_deg, 3),
        "azimuth_deg": round(azimuth_deg, 3),
        "direction": [round(value, 6) for value in direction],
        "is_day": elevation_deg > 0.0,
        "hour_angle_deg": round(math.degrees(hour_angle), 3),
        "solar_time_hours": round((12.0 + math.degrees(hour_angle) / 15.0) % 24.0, 3),
        "latitude_deg": latitude_deg,
        "longitude_deg": longitude_deg,
    }
