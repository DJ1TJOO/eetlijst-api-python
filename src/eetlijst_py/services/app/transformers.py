from eetlijst_py.generated.app_status import AppStatus
from eetlijst_py.generated.app_status_subscription import AppStatusSubscription
from eetlijst_py.generated.fragments import AppStatusFields

from eetlijst_py.exceptions import EetlijstException


def transform_app_status(
    status: AppStatus | AppStatusSubscription,
) -> AppStatusFields:
    if not status.eetschema_app_status:
        raise EetlijstException("App status not found")

    return status.eetschema_app_status[0]
