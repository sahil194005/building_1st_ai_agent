from pydantic import BaseModel, Field


class ROIInput(BaseModel):
    investment: float = Field(..., gt=0)
    return_amount: float = Field(..., gt=0)


class AddNumbersInput(BaseModel):
    a: float
    b: float


class MultiplyNumbersInput(BaseModel):
    a: float
    b: float


class StockPriceInput(BaseModel):
    symbol: str = Field(..., min_length=1)


class CurrencyConvertInput(BaseModel):
    amount: float = Field(..., gt=0)
    from_currency: str
    to_currency: str
