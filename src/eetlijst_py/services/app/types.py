"""App service type exports."""

from eetlijst_py.generated.fragments import AppStatusFields
from eetlijst_py.generated.get_app_status import GetAppStatusEetschemaAppStatus

AppStatus = AppStatusFields

__all__ = [
    "AppStatus",
    "AppStatusFields",
    "GetAppStatusEetschemaAppStatus",
]
