from notion_client import Client

from pprint import pprint
from props import TOKEN, DB_ID

notion = Client(auth=TOKEN)


# https://www.notion.so/

def get_all():
    my_page = notion.databases.query(
        **{
            "database_id": DB_ID

        }
    )

    results = my_page["results"]
    prods = []
    for result in results:
        prods_dict = map_results(result)
        prods.append(prods_dict)
    # pprint(prods)


def map_results(result):
    # pprint(result)
    i = 0
    prod_id = result["id"]
    props = result["properties"]["Name"]["title"][i]
    # name = props
    pprint(props)
    return prod_id
    # name = props["Name"]["title"]["text"]["content"]
    # return {
    #     "prod_id": prod_id,
    #     "name": name
    #     }


if __name__ == "__main__":
    get_all()
