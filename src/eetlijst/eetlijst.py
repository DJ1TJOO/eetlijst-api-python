from typing import Optional

from eetlijst.generated import GraphQlClient
from eetlijst.services import (
    App,
    EventAttendance,
    Events,
    Expenses,
    GroupList,
    Groups,
    GroupUsers,
    Settlements,
    Users,
)


class Eetlijst:
    def __init__(self, api_key: str, url: Optional[str] = None):
        self._client = GraphQlClient(
            url or "https://api.eetlijst.nl/v1/graphql",
            {"Authorization": f"Bearer {api_key}"},
        )

        self.app = App(self._client)

        event_attendance = EventAttendance(self._client)
        self.events = Events(self._client, event_attendance)

        group_users = GroupUsers(self._client)
        group_list = GroupList(self._client)
        self.groups = Groups(self._client, group_users, group_list)

        settlements = Settlements(self._client)
        self.expenses = Expenses(self._client, settlements)

        self.users = Users(self._client)
