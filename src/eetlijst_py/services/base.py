from dataclasses import dataclass
from typing import Optional

from eetlijst_py.generated import GraphQlClient


@dataclass
class BaseService:
    _client: GraphQlClient
    _api_key: str

    def _get_headers(
        self, custom_headers: Optional[dict[str, str]] = None
    ) -> dict[str, str]:
        headers = {"Authorization": f"Bearer {self._api_key}"}

        if custom_headers:
            headers.update(custom_headers)

        return headers
