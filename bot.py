from notion_client import Client
from notion_client.helpers import is_full_page

from pprint import pprint

notion = Client(auth="")

list_users_response = notion.users.list()
# pprint(list_users_response)
# https://www.notion.so/
# my_page = notion.databases.query(
#     **{
#         "database_id": ""
#
#     }
# )
#
# for _ in my_page:
#     pprint(_)

async def name_fun():
    full_or_partial_pages = await notion.databases.query(
        database_id=
    )

    for page in full_or_partial_pages["results"]:
        if not is_full_page(page):
            continue
        print(f"Created at: {page['created_time']}")