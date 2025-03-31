from pydantic import BaseModel, Field
from typing import Literal

class MortgageRequest(BaseModel):
    sum_property: float = Field(..., gt=0, description="Стоимость недвижимости (руб)")
    first_payment: float = Field(..., ge=0, description="Первоначальный взнос (руб)")
    periods: int = Field(..., gt=0, le=30, description="Срок кредита (лет, макс 30)")
    rate: float = Field(..., gt=0, le=20, description="Процентная ставка (%)")
    type_payment: Literal["annuity", "differentiated"] = Field(..., description="Тип платежа")