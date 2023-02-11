from pydantic import BaseModel
from fastapi import FastAPI, Request
from fastapi import FastAPI
from datetime import date
from utils import pred_crop, pred_rainfall, pred_temp_hum

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


app = FastAPI()


class Inputs(BaseModel):
    nitrogen: float
    phosphorous: float
    potassium: float
    ph: float
    state: str
    district: str
    month: str


@app.post("/predict/")
async def predict(inputs: Inputs):
    print(inputs)
    nitrogen = inputs.nitrogen
    phosphorous = inputs.phosphorous
    potassium = inputs.potassium
    state = inputs.state
    district = inputs.district
    month = inputs.month
    ph = inputs.ph

    rainfall = pred_rainfall.get_rainfall(state, district, month)

    temperature, humidity = pred_temp_hum.get_temp_hum(district)

    prediction = pred_crop.predict_crop(
        nitrogen, phosphorous, potassium, temperature, humidity, ph, rainfall)

    return {"result": prediction[0]}
