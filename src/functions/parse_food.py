def main(product: dict, status_option):
    ingredients = []
    manufacturer = []
    nutrients = []

    # for ingredient in product["dietarySupplementsFacts"][0]["ingredients"]:
    #     ingredients.append({"name": ingredient["name"]})
    # for contanct in product["contacts"]:

    category = (
        product["foodCategory"]["description"] if "foodCategory" in product else "n/a"
    )

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
                "quantity": quantity,
                "quantity_unit_symbol": unit,
            }
        )

    for ingredient in product["ingredients"] if "ingredients" in product else []:
        print(ingredient)

    nutrition_product = {
        "resourceType": "NutritionProduct",
        "status": status_option,
        "category": category,
        "manufacturer": manufacturer,
        "ingredient": ingredients,
        "nutrients": nutrients,
    }

    return nutrition_product
