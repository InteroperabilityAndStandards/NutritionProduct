from ..functions import remove_nulls
from .components import (
    get_category,
    get_know_allergen,
    get_intstance,
    # get_manufacturer,
    get_nutrient,
    get_ingredient,
    get_ingredient_summary,
    get_code,
)


def main(product: dict, status_option, nlp, ruler):
    code = get_code.main(product)  # check
    category = get_category.main(product)  # check
    # manufacturer = get_manufacturer.main(product)
    ingredient = get_ingredient.main(product, nlp, ruler)
    nutrient = get_nutrient.main(product)
    known_allergens = get_know_allergen.main(product, status_option)
    instance = get_intstance.main(product)  # check

    ingredient_summary = get_ingredient_summary.main(product, status_option)

    nutrition_product = {
        "resourceType": "NutritionProduct",
        "code": code,
        "status": status_option,
        "category": category,
        # "manufacturer": manufacturer,
        "ingredientSummary": ingredient_summary,
        "ingredient": ingredient,
        "nutrient": nutrient,
        "knownAllergen": known_allergens,
        "instance": instance,
    }

    final_nutrition_product = remove_nulls.delete_none(nutrition_product)

    return final_nutrition_product
