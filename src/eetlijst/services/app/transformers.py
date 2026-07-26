from eetlijst.generated.app_status import AppStatus, AppStatusEetschemaAppStatus

from eetlijst.exceptions import EetlijstException


def transform_app_status(status: AppStatus) -> AppStatusEetschemaAppStatus:
    if not status.eetschema_app_status:
        raise EetlijstException("App status not found")

    return status.eetschema_app_status[0]
