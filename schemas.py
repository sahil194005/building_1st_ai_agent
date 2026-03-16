from pydantic import BaseModel, Field


class ROIInput(BaseModel):
    investment: float = Field(..., gt=0)
    return_amount: float = Field(..., gt=0)


class AddNumbersInput(BaseModel):
    a: float = Field(..., description="First addend")
    b: float = Field(..., description="Second addend")


class MultiplyNumbersInput(BaseModel):
    a: float = Field(..., description="First factor")
    b: float = Field(..., description="Second factor")


class StockPriceInput(BaseModel):
    symbol: str = Field(..., min_length=1)


class CurrencyConvertInput(BaseModel):
    amount: float = Field(..., gt=0, description="Amount to convert")
    from_currency: str = Field(..., min_length=1, description="Source currency code")
    to_currency: str = Field(..., min_length=1, description="Target currency code")
