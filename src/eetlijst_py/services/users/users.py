from dataclasses import dataclass

from eetlijst_py.generated.base_model import UNSET, UnsetType
from eetlijst_py.generated.input_types import eetschema_user_set_input

from eetlijst_py.services.base import BaseService

from .transformers import (
    transform_get_user,
    transform_remove_account_reasons,
    transform_update_user,
)


@dataclass
class Users(BaseService):

    async def get(self, user_id: str):
        result = await self._client.get_user(
            user_id=user_id,
            headers=self._get_headers(),
        )
        return transform_get_user(result)

    async def get_subscription(self, user_id: str):
        async for result in self._client.get_user_subscription(
            user_id=user_id,
            headers=self._get_ws_headers(),
        ):
            yield transform_get_user(result)

    async def update(self, user_id: str, data: eetschema_user_set_input):
        result = await self._client.update_user(
            user_id=user_id,
            set_=data,
            headers=self._get_headers(),
        )
        return transform_update_user(result)

    async def remove_reasons(
        self,
        user_id: str,
        reason_to_remove_account_text: str,
        reason_to_remove_account_selection: list[str] | UnsetType | None = UNSET,
        reason_to_remove_account_selection_all_options: (
            list[str] | UnsetType | None
        ) = UNSET,
    ):
        result = await self._client.remove_account(
            user_id,
            reason_to_remove_account_text,
            reason_to_remove_account_selection,
            reason_to_remove_account_selection_all_options,
            headers=self._get_headers(),
        )
        return transform_remove_account_reasons(result)
