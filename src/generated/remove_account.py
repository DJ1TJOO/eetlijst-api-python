from typing import Optional

from .base_model import BaseModel


class RemoveAccount(BaseModel):
    update_eetschema_user_by_pk: Optional["RemoveAccountUpdateEetschemaUserByPk"]


class RemoveAccountUpdateEetschemaUserByPk(BaseModel):
    reason_to_remove_account_text: Optional[str]
    reason_to_remove_account_selection: Optional[list[str]]
    reason_to_remove_account_selection_all_options: Optional[list[str]]


RemoveAccount.model_rebuild()
