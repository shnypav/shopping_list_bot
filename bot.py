from notion_client import Client

from pprint import pprint
from props import TOKEN, DB_ID

notion = Client(auth=TOKEN)


# https://www.notion.so/

def get_all():
    my_page = notion.databases.query(
        **{
            "database_id": DB_ID,
            "filter":

                {"property": "DoWeEat_2",
                 "formula": {
                     "checkbox": {
                         "equals": True
                     }
                 }
            },
        }
    )

    results = my_page["results"]
    prods = []
    pprint(results)
    for result in range(0, len(results)):
        try:
            prods_dict = map_results(results[result])
            prods.append(prods_dict)
        except IndexError as ie:
            pprint(ie)
    pprint(prods)


def map_results(result):
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
                            "equals": "A lot"
                        }
                    },
                    {
                        "or": [
                            {"property": "Едим ли",
                             "rollup": {
                                 "any":
                                     {
                                         "relation": {
                                             "is_not_empty": True
                                         }
                                     }
                             }
                             },
                            {
                                "property": "Едим",
                                "relation": {
                                    "is_not_empty": True
                                }
                            }
                        ]
                    }
                ]
            }
        }
    )

    results = my_page["results"]
    prods = []
    for result in range(0, len(results)):
        prods_dict = map_results(results[result])
        prods.append(prods_dict)
    pprint(prods)


def filter_results(results):
    filtered = []
    for i in results:
        pass


if __name__ == "__main__":
    get_all()
