from ..functions import remove_nulls
from .components import (
    get_category,
    get_know_allergen,
    get_intstance,
    # get_manufacturer,
    get_nutrient,
    get_ingredient,
    # get_ingredient_summary,
    get_code,
)


def add(self, key, value):
    self[key] = value


def main(product: dict, status_option, nlp):
    code = get_code.main(product)  # check
    category = get_category.main(product)  # check
    # manufacturer = get_manufacturer.main(product)
    ingredient = get_ingredient.main(product, nlp)
    nutrient = get_nutrient.main(product)
    known_allergens = get_know_allergen.main(product)
    instance = get_intstance.main(product)  # check

    # ingredient_summary = get_ingredient_summary.main(product, status_option)

    nutrition_product = {
        "resourceType": "NutritionProduct",
        "code": code,
        "status": status_option,
        "category": category,
        # "manufacturer": manufacturer,
        # "ingredientSummary": ingredient_summary,
        "nutrient": nutrient,
    }

    if known_allergens:
        nutrition_product["knownAllergen"] = known_allergens
    if instance:
        nutrition_product["instance"] = instance
    if ingredient:
        nutrition_product["ingredient"] = ingredient

    final_nutrition_product = remove_nulls.delete_none(nutrition_product)

    return final_nutrition_product
