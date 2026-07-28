from .base_model import BaseModel
from .fragments import UserFieldsPrivate


class GetUserSubscription(BaseModel):
    eetschema_user_private: list["GetUserSubscriptionEetschemaUserPrivate"]


class GetUserSubscriptionEetschemaUserPrivate(UserFieldsPrivate):
    pass


GetUserSubscription.model_rebuild()
