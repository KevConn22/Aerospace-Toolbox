from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class AtmosphereRequest(BaseModel):
    altitude: float

class AtmosphereResponse(BaseModel):
    temperature: float
    pressure: float
    density: float
    speed_of_sound: float

@router.post("/atmosphere", response_model=AtmosphereResponse)
def get_atmosphere(data: AtmosphereRequest):
    h = data.altitude
    T0 = 288.15
    P0 = 101325
    L = 0.0065
    R = 287.05
    g = 9.80665

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
