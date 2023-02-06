import re
import random

from ..functions import remove_nulls


def main(product: dict, status_option):
    ingredients = []
    manufacturer = []
    nutrients = []
    ingredient_summary = None

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
            "identifier": product["gtinUpc"] if "gtinUpc" in product else None,
            "name": product["description"],
            "lotNumber": "10000004",
            "expiry": "2023/1/31",
            "useBy": "2023/1/28",
            "biologicalSourceEvent": "",
        }

    manufacturer.append(
        {
            "active": True if "brandOwner" in product else False,
            "name": product["brandOwner"] if "brandOwner" in product else None,
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
        count = 0
        ingredient_summary = product["ingredients"]
        for ingredient in re.split(r",(?![^()]*\))", product["ingredients"]):
            count += 1
            random.seed(count)
            seed = random.random()
            ingredients.append(
                {
                    "system": "https://fdc.nal.usda.gov/",
                    "code": int(seed * 100000000),
                    "display": ingredient.replace(".", "").strip(),
                }
            )

    nutrition_product = {
        "resourceType": "NutritionProduct",
        "code": code,
        "status": status_option,
        "category": category if category is not None else None,
        "manufacturer": manufacturer,
        "ingredientSummary": ingredient_summary
        if ingredient_summary is not None
        else None,
        "ingredient": ingredients,
        "nutrients": nutrients,
        "knownAllergen": known_allergens,
        "instance": instance,
    }

    final_nutrition_product = remove_nulls.delete_none(nutrition_product)

    return final_nutrition_product
