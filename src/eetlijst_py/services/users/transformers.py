from typing import Optional

from eetlijst_py.generated.fragments import UserFields, UserFieldsPrivate
from eetlijst_py.generated.get_user import GetUser
from eetlijst_py.generated.get_user_subscription import GetUserSubscription
from eetlijst_py.generated.remove_account import (
    RemoveAccount,
    RemoveAccountUpdateEetschemaUserByPk,
)
from eetlijst_py.generated.update_user import UpdateUser

from eetlijst_py.exceptions import EetlijstException

from eetlijst_py.services.users.types import CookPointsImport, User, UserPrivate


def transform_user_private(user: Optional[UserFieldsPrivate]) -> UserPrivate:
    if not user:
        raise EetlijstException("User not found")

    profile_image_url = (
        f"https://node.eetlijst.nl/api/v1/drive/get_file/{user.profile_image}"
        if user.profile_image
        else None
    )

    return UserPrivate(
        **user.model_dump(),
        profile_image_url=profile_image_url,
    )


def transform_user(user: Optional[UserFields]) -> User:
    if not user:
        raise EetlijstException("User not found")

    profile_image_url = (
        f"https://node.eetlijst.nl/api/v1/drive/get_file/{user.profile_image}"
        if user.profile_image
        else None
    )

    cook_points_imports = [
        CookPointsImport(
            cook_points=entry.cook_points,
            allowed_to_edit=entry.allowed_to_edit,
        )
        for entry in (user.cook_points_imports or [])
        if entry is not None
    ]

    user_data = user.model_dump(exclude={"cook_points_imports"})

    return User(
        **user_data,
        profile_image_url=profile_image_url,
        cook_points_imports=cook_points_imports,
    )


def transform_get_user(result: GetUser | GetUserSubscription) -> UserPrivate:
    if not result.eetschema_user_private or len(result.eetschema_user_private) == 0:
        raise EetlijstException("User not found")

    return transform_user_private(result.eetschema_user_private[0])


def transform_update_user(result: UpdateUser) -> User:
    if not result.update_eetschema_user_by_pk:
        raise EetlijstException("Failed to update user")

    return transform_user(result.update_eetschema_user_by_pk)


def transform_remove_account_reasons(
    result: RemoveAccount,
) -> RemoveAccountUpdateEetschemaUserByPk:
    if not result.update_eetschema_user_by_pk:
        raise EetlijstException("Failed to remove user")

    return result.update_eetschema_user_by_pk
