from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class AtmosphereRequest(BaseModel):
    altitude: float  # in meters

class AtmosphereResponse(BaseModel):
    temperature: float      # Kelvin
    pressure: float         # Pascals
    density: float          # kg/m^3
    speed_of_sound: float   # m/s

@router.post("/atmosphere", response_model=AtmosphereResponse)
def get_atmosphere(data: AtmosphereRequest):
    h = data.altitude

    T0 = 288.15      # Sea level temp in K
    P0 = 101325      # Sea level pressure in Pa
    L = 0.0065       # Temperature lapse rate (K/m)
    R = 287.05       # Specific gas constant for air
    g = 9.80665      # Gravity (m/s^2)

    if h < 0 or h > 11000:
        raise ValueError("This model is valid only between 0 and 11,000 meters.")

    T = T0 - L * h
    P = P0 * (T / T0) ** (g / (R * L))
    rho = P / (R * T)
    a = (1.4 * R * T) ** 0.5

    return AtmosphereResponse(
        temperature=T,
        pressure=P,
        density=rho,
        speed_of_sound=a
    )
