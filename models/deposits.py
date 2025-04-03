from pydantic import BaseModel, validator
from typing import List
import datetime
from utils.get_count_days_from_current_month import get_count_days_from_current_month
from utils.get_current_name_month import get_current_name_month

# Получаем текущую дату
today = datetime.datetime.now()
current_month = today.month

class Deposits(BaseModel):
    initial_sum: float = 100000 # сумма вклада
    list_rates: List[float] = [20,15,10] # процент годовой
    name_current_month: str = get_current_name_month(current_month) # за какой месяц считать "may" // сделать ручку на месяцы


class BondResponse(BaseModel):
    price: float # текущая цена на рынке за облигацию
    face_value: float # номинальная цена обычно 1 000 руб
    coupon: float # купон
    days_to_maturity: int # Срок до погашения или дата следующего купона Например: 30 дней до выплаты купона