"""Users service type exports."""

from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from eetlijst_py.generated.fragments import (
    UserFields,
    UserFieldsCookPointsImports,
    UserFieldsPrivate,
)
from eetlijst_py.generated.get_user import GetUserEetschemaUserPrivate
from eetlijst_py.generated.input_types import (
    eetschema_user_set_input as _eetschema_user_set_input,
)
from eetlijst_py.generated.remove_account import RemoveAccountUpdateEetschemaUserByPk
from eetlijst_py.generated.update_user import UpdateUserUpdateEetschemaUserByPk


class CookPointsImport(BaseModel):
    cook_points: float
    allowed_to_edit: bool


class User(BaseModel):
    id: str
    name: str
    origin: Optional[str]
    email: Optional[str]
    allergies: list[str]
    birthday: Optional[datetime]
    profile_image: Optional[str]
    profile_image_url: Optional[str]
    order_of_buttom_bar: Optional[list[str]]
    wants_to_recieve_notifications: bool
    funnel_lead: Optional[list[str]]
    cook_points_imports: list[CookPointsImport]


class UserPrivate(UserFieldsPrivate):
    profile_image_url: Optional[str] = None


UpdateUser = _eetschema_user_set_input

__all__ = [
    "UserFields",
    "UserFieldsCookPointsImports",
    "UserFieldsPrivate",
    "GetUserEetschemaUserPrivate",
    "UpdateUserUpdateEetschemaUserByPk",
    "RemoveAccountUpdateEetschemaUserByPk",
    "UpdateUser",
]
