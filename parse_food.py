def main(product: dict, status_option):
    ingredients = []
    manufacturer = []
    nutrients = []

    # for ingredient in product["dietarySupplementsFacts"][0]["ingredients"]:
    #     ingredients.append({"name": ingredient["name"]})
    # for contanct in product["contacts"]:

    category = None
    if "foodCategory" in product:
        category = product["foodCategory"]["description"]

    if "brandedFoodCategory" in product:
        category = product["brandedFoodCategory"]

    code = {
        "coding": {
            "system": "https://fdc.nal.usda.gov/",
            "code": product["fdcId"],
            "display": product["description"],
        }
    }

    known_allergens = None
    instance = None
    if "butter" in product["description"].lower():
        known_allergens = [
            {
                "coding": {
                    "system": "http://snomed.info/sct",
                    "code": "226355009",
                    "display": "Peanut (substance)",
                }
            }
        ]

        instance = {
            "quantity": "6",
            "identifier": product["gtinUpc"],
            "name": product["description"],
            "lotNumber": "10000004",
            "expiry": "2023/1/31",
            "useBy": "2023/1/28",
            "biologicalSourceEvent": "",
        }

    manufacturer.append(
        {
            "active": True if "brandOwner" in product else False,
            "name": product["brandOwner"] if "brandOwner" in product else "n/a",
        }
    )
    for nutrient in product["foodNutrients"]:

        quantity = nutrient["amount"] if "amount" in nutrient else None
        unit = (
            nutrient["nutrient"]["unitName"]
            if "unitName" in nutrient["nutrient"]
            else None
        )

        nutrients.append(
            {
                "name": nutrient["nutrient"]["name"],
                "amount": {
                    "value": quantity,
                    "unit": unit,
                    "comparator": "ad",
                },
            }
        )

    if "ingredients" in product:
        ingredients = product["ingredients"]
    # for ingredient in product["ingredients"] if "ingredients" in product else []:
    # print(product["ingredients"])

    nutrition_product = {
        "resourceType": "NutritionProduct",
        "code": code,
        "status": status_option,
        "category": category if category is not None else "n/a",
        "manufacturer": manufacturer,
        "ingredient": ingredients,
        "nutrients": nutrients,
        "knownAllergen": known_allergens,
        "instance": instance,
    }

    return nutrition_product
