from datetime import datetime
from typing import Optional

from pydantic import BaseModel

from eetlijst_py.generated.fragments import UserFields, UserFieldsPrivate
from eetlijst_py.generated.get_user import GetUser
from eetlijst_py.generated.remove_account import (
    RemoveAccount,
    RemoveAccountUpdateEetschemaUserByPk,
)
from eetlijst_py.generated.update_user import UpdateUser

from eetlijst_py.exceptions import EetlijstException


class CookPointsImportResult(BaseModel):
    cook_points: float
    allowed_to_edit: bool


class UserResult(BaseModel):
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
    cook_points_imports: list[CookPointsImportResult]


class UserPrivateResult(UserFieldsPrivate):
    profile_image_url: Optional[str] = None


def transform_user_private(user: Optional[UserFieldsPrivate]) -> UserPrivateResult:
    if not user:
        raise EetlijstException("User not found")

    profile_image_url = (
        f"https://node.eetlijst.nl/api/v1/drive/get_file/{user.profile_image}"
        if user.profile_image
        else None
    )

    return UserPrivateResult(
        **user.model_dump(),
        profile_image_url=profile_image_url,
    )


def transform_user(user: Optional[UserFields]) -> UserResult:
    if not user:
        raise EetlijstException("User not found")

    profile_image_url = (
        f"https://node.eetlijst.nl/api/v1/drive/get_file/{user.profile_image}"
        if user.profile_image
        else None
    )

    cook_points_imports = [
        CookPointsImportResult(
            cook_points=entry.cook_points,
            allowed_to_edit=entry.allowed_to_edit,
        )
        for entry in (user.cook_points_imports or [])
        if entry is not None
    ]

    user_data = user.model_dump(exclude={"cook_points_imports"})

    return UserResult(
        **user_data,
        profile_image_url=profile_image_url,
        cook_points_imports=cook_points_imports,
    )


def transform_get_user(result: GetUser) -> UserPrivateResult:
    if not result.eetschema_user_private or len(result.eetschema_user_private) == 0:
        raise EetlijstException("User not found")

    return transform_user_private(result.eetschema_user_private[0])


def transform_update_user(result: UpdateUser) -> UserResult:
    if not result.update_eetschema_user_by_pk:
        raise EetlijstException("Failed to update user")

    return transform_user(result.update_eetschema_user_by_pk)


def transform_remove_account_reasons(
    result: RemoveAccount,
) -> RemoveAccountUpdateEetschemaUserByPk:
    if not result.update_eetschema_user_by_pk:
        raise EetlijstException("Failed to remove user")

    return result.update_eetschema_user_by_pk
