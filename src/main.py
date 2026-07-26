import asyncio
import os

from dotenv import load_dotenv

from src.eetlijst import Eetlijst

load_dotenv()

api_key = os.environ["API_KEY"]


eetlijst = Eetlijst(api_key)
marsu_group_id = "28439571-4675-4c2b-ad76-54b985b4bd37"


async def main():
    app_status = await eetlijst.app.status()
    print(app_status)
    event = await eetlijst.events.get(
        "300acfe6-aee7-431f-bc86-d593a42b170b", True, True
    )
    print(event.attendees[0])


if __name__ == "__main__":
    asyncio.run(main())
