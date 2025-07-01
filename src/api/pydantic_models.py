# src/api/pydantic_models.py
from pydantic import BaseModel


class InputData(BaseModel):
    TotalAmount: float
    AvgAmount: float
    TxnCount: float
    StdAmount: float
    TotalValue: float
    AvgValue: float
    StdValue: float
    ChannelId_ChannelId_1: int
    ChannelId_ChannelId_2: int
    ChannelId_ChannelId_3: int
    ChannelId_ChannelId_5: int
    ProductCategory_airtime: int
    ProductCategory_data_bundles: int
    ProductCategory_financial_services: int
    ProductCategory_movies: int
    ProductCategory_other: int
    ProductCategory_ticket: int
    ProductCategory_transport: int
    ProductCategory_tv: int
    ProductCategory_utility_bill: int


class PredictionResponse(BaseModel):
    is_high_risk: int
    probability: float
