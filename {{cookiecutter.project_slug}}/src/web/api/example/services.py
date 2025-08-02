import operator

from web.api.example.constants import ArithmeticOpsEnum
from web.api.example.schemas import CalculationParamsSchema


class CalculationService:
    def calculate(self, data: CalculationParamsSchema) -> int | float:
        op = {
            ArithmeticOpsEnum.ADD: operator.add,
            ArithmeticOpsEnum.SUB: operator.sub,
            ArithmeticOpsEnum.MUL: operator.mul,
            ArithmeticOpsEnum.DIV: operator.truediv,
        }[data.op]
        return op(data.num1, data.num2)
