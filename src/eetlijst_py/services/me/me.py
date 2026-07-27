import base64
import binascii
import json
from datetime import datetime, timezone
from typing import Any, Optional

from eetlijst_py.services.users import Users


class Me:
    def __init__(self, api_key: str, users: Users):
        self._users = users
        payload = self._decode_payload(api_key)

        self.user_id: Optional[str] = payload.get("sub")
        self.name: Optional[str] = payload.get("name")

        iat_timestamp = payload.get("iat")
        self.issued_at: Optional[datetime] = (
            datetime.fromtimestamp(iat_timestamp, tz=timezone.utc)
            if iat_timestamp is not None
            else None
        )

        exp_timestamp = payload.get("exp")
        self.expires: Optional[datetime] = (
            datetime.fromtimestamp(exp_timestamp, tz=timezone.utc)
            if exp_timestamp is not None
            else None
        )

    async def get(self):
        if not self.user_id:
            raise ValueError(
                "Cannot fetch user profile: missing 'sub' (user_id) in JWT."
            )
        return await self._users.get(self.user_id)

    @staticmethod
    def _decode_payload(token: str) -> dict[str, Any]:
        try:
            if token.lower().startswith("bearer "):
                token = token[7:]

            parts = token.split(".")
            if len(parts) != 3:
                return {}

            payload_b64 = parts[1]
            padding = "=" * (-len(payload_b64) % 4)
            decoded_bytes = base64.urlsafe_b64decode(payload_b64 + padding)
            return json.loads(decoded_bytes.decode("utf-8"))
        except binascii.Error, UnicodeDecodeError, json.JSONDecodeError:
            return {}
