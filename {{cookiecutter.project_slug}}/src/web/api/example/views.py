from fastapi import APIRouter, Depends

from web.api.example.schemas import CalculationParamsSchema, CalculationResultSchema
from web.api.example.services import CalculationService

router = APIRouter(tags=["Пример"])


@router.post("/calculate", response_model=CalculationResultSchema)
async def calculate(data: CalculationParamsSchema, service: CalculationService = Depends()):
    result = service.calculate(data)
    return {"result": result}
