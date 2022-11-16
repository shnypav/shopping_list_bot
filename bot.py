from notion_client import Client

from pprint import pprint
from props import TOKEN, DB_ID

notion = Client(auth=TOKEN)


# https://www.notion.so/

def get_all():
    my_page = notion.databases.query(
        **{
            "database_id": DB_ID,
            "filter": {
                "property": "Едим",
                "has_more": {
                    "equals": "True"
                }
            }

        }
    )

    results = my_page["results"]
    pprint(results)
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
            "filter": {
                "and": [
                    {
                        "property": "Available",
                        "status": {
                            "equals": "No"
                        }
                    },
                    {
                        "or": [
                            # {
                            #     "property": "Едим ли",
                            #     "any": {
                            #         "is_not_empty": "True"
                            #     }
                            # },
                            {
                                "property": "Едим",
                                "is_not_empty": "true"
                            }
                        ]
                    }
                ]
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
    get_all()
