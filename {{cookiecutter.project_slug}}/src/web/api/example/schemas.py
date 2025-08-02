from pydantic import BaseModel

from web.api.example.constants import ArithmeticOpsEnum


class CalculationParamsSchema(BaseModel):
    num1: int
    num2: int
    op: ArithmeticOpsEnum


class CalculationResultSchema(BaseModel):
    result: int | float
