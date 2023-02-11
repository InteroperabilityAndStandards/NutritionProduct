import re
import random
from fhir_types import FHIR_CodeableConcept, FHIR_Ratio


def main(product: dict, status_option):
    ingredients = []

    if "ingredients" in product:
        count = 0
        for ingredient in re.split(r",(?![^()]*\))", product["ingredients"]):
            count += 1
            random.seed(count)
            seed = random.random()

            item: FHIR_CodeableConcept  # not correct
            amount: FHIR_Ratio

            ingredients.append(
                {
                    "system": "https://fdc.nal.usda.gov/",
                    "code": int(seed * 100000000),
                    "display": ingredient.replace(".", "").strip(),
                }
            )
    return ingredients
