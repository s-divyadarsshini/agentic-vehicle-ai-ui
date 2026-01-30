from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from datetime import datetime

app = FastAPI()

# ---------------------------
# DATA MODELS
# ---------------------------
class Component(BaseModel):
    name: str
    health: int
    failure_score: float

class VehicleInput(BaseModel):
    vehicle: str
    components: List[Component]

# ---------------------------
# API ENDPOINT
# ---------------------------
@app.post("/predict")
def run_agent(data: VehicleInput):

    rca = []
    for c in data.components:
        if c.failure_score > 0.3:
            rca.append(f"{c.name} has high failure probability")

    service_booking = {
        "date_time": datetime.now().strftime("%d %b %Y, %I:%M %p"),
        "center": "Nearest Available Center",
        "booking_id": "BK161543"
    }

    return {
        "rca": rca,
        "security_logs": "No anomalies detected",
        "service_booking": service_booking
    }
