from fhir_types import FHIR_CodeableConcept


def main(product: dict):
    category: FHIR_CodeableConcept = {}
    if "foodCategory" in product:
        category = {
            "text": product["foodCategory"]["description"],
            "coding": [
                {
                    "system": "https://fdc.nal.usda.gov/",
                    "code": product["foodCategory"]["code"],
                    "display": product["foodCategory"]["description"],
                }
            ],
        }

    if "brandedFoodCategory" in product:
        category = product["brandedFoodCategory"]

    return category
