from dataclasses import dataclass

from eetlijst_py.services.app.transformers import transform_app_status
from eetlijst_py.services.base import BaseService


@dataclass
class App(BaseService):

    async def status(self):
        result = await self._client.get_app_status(headers=self._get_headers())

        return transform_app_status(result)

    async def status_subscription(self):
        async for result in self._client.get_app_status_subscription(
            additional_headers=self._get_ws_headers(),
        ):
            if result and result.eetschema_app_status:
                yield transform_app_status(result)
