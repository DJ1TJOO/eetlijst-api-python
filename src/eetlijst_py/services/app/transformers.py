from eetlijst_py.generated.get_app_status import GetAppStatus
from eetlijst_py.generated.get_app_status_subscription import GetAppStatusSubscription

from eetlijst_py.exceptions import EetlijstException

from eetlijst_py.services.app.types import AppStatus


def transform_app_status(
    status: GetAppStatus | GetAppStatusSubscription,
) -> AppStatus:
    if not status.eetschema_app_status:
        raise EetlijstException("App status not found")

    return status.eetschema_app_status[0]
