from dataclasses import dataclass
from typing import Optional

from eetlijst_py.generated import GraphQlClient


@dataclass
class BaseService:
    _client: GraphQlClient
    _api_key: str

    def _get_headers(
        self, additional_headers: Optional[dict[str, str]] = None
    ) -> dict[str, str]:
        headers = {"Authorization": f"Bearer {self._api_key}"}

        if additional_headers:
            headers.update(additional_headers)

        return headers

    def _get_ws_headers(
        self, additional_ws_headers: Optional[dict[str, str]] = None
    ) -> dict[str, str]:
        ws_headers = {"Authorization": f"Bearer {self._api_key}"}

        if additional_ws_headers:
            ws_headers.update(additional_ws_headers)

        return ws_headers
