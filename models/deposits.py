from pydantic import BaseModel

class Model_Deposits(BaseModel):
    full_sum: float # Сумма общая
    first_installment: float  # первый взнос
    period: int  # срок кредита - лет
    percent: int  # процентная ставка
    type_monthly_payments: str  # Тип ежемесячных платежей

