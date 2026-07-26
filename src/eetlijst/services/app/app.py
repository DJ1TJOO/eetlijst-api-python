from dataclasses import dataclass

from eetlijst.exceptions import EetlijstException
from eetlijst.generated import GraphQlClient
from eetlijst.services.app.transformers import transform_app_status


@dataclass
class App:
    _client: GraphQlClient

    async def status(self):
        result = await self._client.app_status()

        if not result or not result.eetschema_app_status:
            raise EetlijstException("App status not found")

        return transform_app_status(result)
