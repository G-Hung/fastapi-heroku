from pydantic import BaseModel, Field


class CensusData(BaseModel):
    age: int = Field(..., gt=0, example=39)
    workclass: str = Field(..., example="State-gov")
    fnlgt: int = Field(..., example=77516)
    education: str = Field(..., example="Bachelors")
    education_num: int = Field(..., gt=0, example=13, alias="education-num")
    marital_status: str = Field(..., example="Never-married", alias="marital-status")
    occupation: str = Field(..., example="Adm-clerical")
    relationship: str = Field(..., example="Not-in-family")
    race: str = Field(..., example="White")
    sex: str = Field(..., example="Male")
    capital_gain: int = Field(..., example=2174, alias="capital-gain")
    capital_loss: int = Field(..., example=0, alias="capital-loss")
    hours_per_week: int = Field(..., ge=0, example=40, alias="hours-per-week")
    native_country: str = Field(..., example="United-States", alias="native-country")


class Income(BaseModel):
    Income: str = Field(..., example=">50K")
