from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

class User_Input(BaseModel):
    TypeOfProperty: str
    TypeOfSale: str
    SubtypeOfProperty: str
    Region: str
    Province: str
    District: str
    BedroomCount: int
    BathroomCount: int
    ToiletCount: int
    ShowerCount: int
    LivingArea: float
    Garden: bool
    GardenArea: float | None
    SurfaceOfPlot: float | None
    SwimmingPool: bool 
    Fireplace: bool
    Furnished: bool
    Terrace: bool
    ConstructionYear: int
    NumberOfFacades: int
    Kitchen: str
    StateOfBuilding: str
    PEB: str

preprocessor = joblib.load('preprocessor_compressed.pkl')
model = joblib.load('model.pkl')

app = FastAPI()

def data_conversion(data:dict):
    if data['TypeOfProperty'] == 'House':
        data['TypeOfProperty'] = 1
    else:
        data['TypeOfProperty'] = 2

    if data['TypeOfSale'] == 'Sale':
        data['TypeOfSale'] = 'residential_sale'
    else:
        data['TypeOfSale'] = 'residential_monthly_rent'
    
    data['SubtypeOfProperty'] = data['SubtypeOfProperty'].lower().replace(' ', '_')

    if data['Region'] == 'Wallonia':
        data['Region'] = 'Wallonie'

    bools = ['Garden', 'SwimmingPool', 'Fireplace', 'Furnished', 'Terrace']
    for key in bools:
        if data[key]:
            data[key] = 1
        else:
            data[key] = 0
    
    data['Kitchen'] = data['Kitchen'].upper().replace(' ', '_').replace('-', '_')

    data['StateOfBuilding'] = data['StateOfBuilding'].upper().replace(' ', '_')

    return data
    


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post('/predict')
def test(input: User_Input):
    data = pd.DataFrame([data_conversion(input.model_dump())])
    processed = preprocessor.transform(data)
    prediction = model.predict(processed)
    return prediction[0]