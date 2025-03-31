from fastapi import APIRouter,Body, status
from models import deposits

router = APIRouter(
    prefix="/deposits",  # автоматически добавляет префикс ко всем путям
    tags=["Deposits"],   # группирует эндпоинты в документации Swagger
)



@router.post("/")
async def get_deposits_calc(item: deposits.Model_Deposits):
    print(item)
    return {"message": "Get all users"}

# Сумма общая
# первый взнос
# срок кредита - лет
# процентная ставка
# Тип ежемесячных платежей


@router.get("/")
def get_deposits_history(user_id: int):
    return {"message": f"Get user {user_id}"}

#  fields
# Сумма вклада
# месяцов кол-во
# начало срока - дата
# процентная ставка - префикс
#