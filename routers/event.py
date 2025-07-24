from fastapi import APIRouter

from models.event import Event
from controllers.event import Controller

router: APIRouter = APIRouter()

controller: Controller = Controller()


@router.post("/event")
async def add(event: Event) -> int:
    return await controller.handle(event)
