from ..functions import remove_nulls
from .components import (
    get_category,
    get_know_allergen,
    get_intstance,
    get_manufacturer,
    get_nutrient,
    get_ingredient,
    get_ingredient_summary,
    get_code,
)


def main(product: dict, status_option):
    code = get_code.main(product, status_option)
    category = get_category.main(product, status_option)
    manufacturer = get_manufacturer.main(product, status_option)
    ingredient = get_ingredient.main(product, status_option)
    nutrient = get_nutrient.main(product, status_option)
    known_allergens = get_know_allergen.main(product, status_option)
    instance = get_intstance.main(product, status_option)

    ingredient_summary = get_ingredient_summary.main(product, status_option)

    nutrition_product = {
        "resourceType": "NutritionProduct",
        "code": code,
        "status": status_option,
        "category": category,
        "manufacturer": manufacturer,
        "ingredientSummary": ingredient_summary,
        "ingredient": ingredient,
        "nutrient": nutrient,
        "knownAllergen": known_allergens,
        "instance": instance,
    }

    final_nutrition_product = remove_nulls.delete_none(nutrition_product)

    return final_nutrition_product
