from dataclasses import dataclass

from eetlijst_py.exceptions import EetlijstException

from eetlijst_py.services.app.transformers import transform_app_status
from eetlijst_py.services.base import BaseService


@dataclass
class App(BaseService):

    async def status(self):
        result = await self._client.app_status(headers=self._get_headers())

        if not result or not result.eetschema_app_status:
            raise EetlijstException("App status not found")

        return transform_app_status(result)
