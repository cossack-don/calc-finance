from fastapi import APIRouter
from models import mortgage

router = APIRouter(
    prefix="/mortgage",  # автоматически добавляет префикс ко всем путям
    tags=["Mortgage"],   # группирует эндпоинты в документации Swagger
)

@router.post("/calc")
async def get_mortgage_calc(payload: mortgage.MortgageRequest):
          loan_amount = payload.sum_property - payload.first_payment
          months = payload.periods * 12
          monthly_rate = payload.rate / 100 / 12

          if payload.type_payment == "annuity":
              # Аннуитетный платеж
              monthly_payment = loan_amount * (monthly_rate * (1 + monthly_rate)**months) / ((1 + monthly_rate)**months - 1)
              payments = [round(monthly_payment, 2)] * months
          else:
              # Дифференцированный платеж
              base_payment = loan_amount / months
              payments = []
              remaining_amount = loan_amount
              for month in range(1, months + 1):
                  interest_payment = remaining_amount * monthly_rate
                  payment = base_payment + interest_payment
                  payments.append(round(payment, 2))
                  remaining_amount -= base_payment

              total_payment = round(sum(payments), 2)
              overpayment = round(total_payment - loan_amount, 2)

          return {
              "loan_amount": round(loan_amount, 2),
              "monthly_payments": payments,
              "average_monthly_payment": round(sum(payments) / len(payments), 2),
              "first_payment": payments[0],
              "last_payment": payments[-1],
              "total_payment": total_payment,
              "overpayment": overpayment,
              "overpayment_percent": round(overpayment / loan_amount * 100, 2),
              "payment_schedule": [
                  {
                      "month": i + 1,
                      "payment": payments[i],
                      "remaining_balance": round(loan_amount - sum(payments[:i]) if i > 0 else loan_amount, 2)
                  }
                  for i in range(min(12, months))  # Выводим график для первых 12 месяцев
              ]
          }


@router.get("/{user_id}")
async def get_mortgage_history(user_id: int):
    return {"message": f"Get user {user_id}"}