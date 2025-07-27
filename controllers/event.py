from models.event import Event
from httpx import AsyncClient
import asyncio


class Controller:
    def __init__(self):
        self.__client: AsyncClient = AsyncClient()

    async def handle(self, event: Event) -> int:
        tasks = []
        counter: int = 0
        for session in event.session:
            for _, value in session.items():
                tasks.append(self.__client.post(
                    headers={
                        "X-Laas-Username": "labos",
                        "X-Laas-Password": "labos",
                        "X-Laas-Application": "7012"
                    },
                    url=f"http://localhost:8084/session/{value}/action/clean_term"))

        responses = await asyncio.gather(*tasks, return_exceptions=True)
        counter = 0
        for resp in responses:
            if isinstance(resp, Exception):
                continue  # or log it
            if resp.status_code < 300:
                counter += 1

        return counter
