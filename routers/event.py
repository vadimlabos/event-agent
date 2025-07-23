from fastapi import routing

from models.event import Event
from controllers.event import Controller

event = routing.APIRouter()


@event.post("/event")
def add(event: Event) -> None:
    controller: Controller = Controller()
    return controller.handle(event)
