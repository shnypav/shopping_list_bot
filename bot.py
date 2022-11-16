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
    for result in range(2, len(results)):
        prods_dict = map_results(results[result])
        prods.append(prods_dict)
    pprint(prods)


def map_results(result):
    # pprint(result)
    i = []
    prod_id = result["id"]
    name = result["properties"]["Name"]["title"][0]["text"]["content"]
    return {
        "prod_id": prod_id,
        "name": name
        }


def get_all_to_buy():
    my_page = notion.databases.query(
        **{
            "database_id": DB_ID,
            "filter": { "property": "Available",
                        "status": { "equals": "No",
                        }
            }
        }
    )

    results = my_page["results"]
    prods = []
    for result in range(2, len(results)):
        prods_dict = map_results(results[result])
        prods.append(prods_dict)
    pprint(prods)


if __name__ == "__main__":
    get_all_to_buy()
