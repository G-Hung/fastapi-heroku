import pickle

import pandas as pd
from fastapi import FastAPI

from api import __version__
from api.api_model import *
from mltraining.train_model import cat_features
from mltraining.utils.data_util import process_data
from mltraining.utils.model_util import inference

app = FastAPI(
    title="Census data salary predictor", description="test", version=__version__,
)


@app.on_event("startup")
def startup_event():
    """
    Load the basic things
    """
    with open("model/label_binarizer.pkl", "rb") as f:
        lb = pickle.load(f)
    with open("model/encoder.pkl", "rb") as f:
        encoder = pickle.load(f)
    with open("model/model.pkl", "rb") as f:
        model = pickle.load(f)
    global prediction_objects
    prediction_objects = [model, encoder, lb]


@app.get("/")
async def welcome() -> str:
    return {"message": f"Welcome to Census Data salary predictor v{__version__}!"}


@app.post("/predict", response_model=Income)
async def predict(payload: CensusData):
    model, encoder, lb = prediction_objects
    df = pd.DataFrame.from_dict([payload.dict(by_alias=True)])
    X, _, _, _ = process_data(
        df, categorical_features=cat_features, training=False, encoder=encoder, lb=lb
    )
    pred = inference(model, X)

    if pred == 1:
        pred = ">50K"
    elif pred == 0:
        pred = "<=50K"
    return {"Income": pred}
