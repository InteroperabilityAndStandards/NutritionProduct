import json


def main(product: dict, status_option):
    ingredients = []
    manufacturer = []
    nutrients = []

    category = "Supplement"

    for ingredient in product["dietarySupplementsFacts"][0]["ingredients"]:
        ingredients.append(
            {
                "name": ingredient["name"],
                "quantity": ingredient["data"]["sfbQuantityQuantity"],
                "quantity_unit_symbol": ingredient["data"]["unitName"],
            }
        )
    for contanct in product["contacts"]:
        manufacturer.append({"active": True, "name": contanct["name"]})

    other_ingredients = (
        product["dietarySupplementsFacts"][0]["otheringredients"]
        if "dietarySupplementsFacts" in product
        else None
    )

    if other_ingredients is not None:
        for other_ingredient in other_ingredients["text"].split(", "):
            print(other_ingredient)

    nutrition_product = {
        "resourceType": "NutritionProduct",
        "status": status_option,
        "category": category,
        "manufacturer": manufacturer,
        "ingredient": ingredients,
    }

    return nutrition_product
