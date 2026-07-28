from typing import Any, Optional

from httpx import AsyncClient

from eetlijst_py.generated import GraphQlClient

from eetlijst_py.services import (
    App,
    EventAttendance,
    Events,
    Expenses,
    GroupList,
    Groups,
    GroupUsers,
    Me,
    Settlements,
    Users,
)


class Eetlijst:

    def __init__(
        self,
        api_key: str,
        url: Optional[str] = None,
        headers: Optional[dict[str, str]] = None,
        http_client: Optional[AsyncClient] = None,
        ws_url: str = "",
        ws_headers: Optional[dict[str, Any]] = None,
        ws_origin: Optional[str] = None,
        ws_connection_init_payload: Optional[dict[str, Any]] = None,
    ):
        self._api_key = api_key
        self._client = GraphQlClient(
            url=url or "https://api.eetlijst.nl/v1/graphql",
            headers=headers,
            http_client=http_client,
            ws_url=ws_url or "wss://api.eetlijst.nl/v1/graphql",
            ws_headers=ws_headers,
            ws_origin=ws_origin,
            ws_connection_init_payload=ws_connection_init_payload,
        )

        self.app = App(self._client, self._api_key)

        event_attendance = EventAttendance(self._client, self._api_key)
        self.events = Events(self._client, self._api_key, event_attendance)

        group_users = GroupUsers(self._client, self._api_key)
        group_list = GroupList(self._client, self._api_key)
        self.groups = Groups(self._client, self._api_key, group_users, group_list)

        settlements = Settlements(self._client, self._api_key)
        self.expenses = Expenses(self._client, self._api_key, settlements)

        self.users = Users(self._client, self._api_key)
        self.me = Me(api_key, self.users)
