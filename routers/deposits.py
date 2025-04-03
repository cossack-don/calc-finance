from fastapi import APIRouter,Body, status, HTTPException
from fastapi.responses import JSONResponse
from models import deposits
import json
import datetime
from utils.get_current_name_month import get_current_name_month
from utils.get_count_days_from_current_month import get_count_days_from_current_month
from utils.get_current_name_month import month_names

router = APIRouter(
    prefix="/deposits",  # автоматически добавляет префикс ко всем путям
    tags=["Deposits"],   # группирует эндпоинты в документации Swagger
)

# Получаем текущую дату
today = datetime.datetime.now()
current_month = today.month

@router.get("/list_months")
async def get_list_months():
    try:
        return JSONResponse(content={"data": [month for month in month_names.values()] })
    except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))


@router.post("/calc_deposit_from_month")
async def get_calc_deposit_from_month(payload: deposits.Deposits):
    """
    Расчет по точным дням без капитализации для нескольких ставок.
    Возвращает список кортежей (проценты, итоговая сумма) для каждой ставки.
    """

    try:
        current_month_name = None
        days_in_current_month = None

        if payload.list_rates == []:
            print(payload.name_current_month)
            current_month_name = get_current_name_month(current_month)
            days_in_current_month = get_count_days_from_current_month(current_month_name)
        else:
             days_in_current_month = get_count_days_from_current_month(payload.name_current_month)

        days_in_current_month = get_count_days_from_current_month(payload.name_current_month)

        results = []
        for i, item_rate in enumerate(payload.list_rates):
            interest = payload.initial_sum * (item_rate / 100) * (days_in_current_month / 365)
            total = payload.initial_sum + interest
            results.append({
                "id": i,
                "initial_sum": payload.initial_sum,
                "rate": payload.list_rates[i],
                "profit": round(interest, 2),
                "result_sum": round(total, 2)
            })

        return JSONResponse(content={"data": results })

    except ValueError as e:
            raise HTTPException(status_code=400, detail=str(e))