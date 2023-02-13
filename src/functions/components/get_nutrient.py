from fhir_types import FHIR_Ratio
from fhir_types import FHIR_CodeableConcept, FHIR_Ratio, FHIR_string, FHIR_Substance
from typing import TypedDict

# from custom_types.FHIR_CodeableReference import FHIR_CodeableReference

""" 
https://build.fhir.org/references.html#Reference
https://build.fhir.org/references.html#CodeableReference

type should be: FHIR_CodeableReference(FHIR_Substance)

FHIR_CodeableReference is not a valid type in the FHIR spec.

"""

FHIR_CodeableReference = TypedDict(
    "FHIR_CodeableReference",
    {
        "id": FHIR_string,
        "reference": FHIR_Substance,
        "concept": FHIR_CodeableConcept,
    },
    total=False,
)


def main(product: dict):
    nutrients = []

    for nutrient in product["foodNutrients"]:

        quantity = nutrient["amount"] if "amount" in nutrient else None
        unit = (
            nutrient["nutrient"]["unitName"]
            if "unitName" in nutrient["nutrient"]
            else None
        )

        if quantity is not None and unit is not None:
            amount: FHIR_Ratio = {
                "numerator": {"value": quantity, "unit": unit, "comparator": "ad"}
            }

            item: FHIR_CodeableReference = {
                "concept": {
                    "text": nutrient["nutrient"]["name"],
                    "coding": [
                        {
                            "system": "https://fdc.nal.usda.gov/",
                            "code": nutrient["nutrient"]["id"],
                            "display": nutrient["nutrient"]["name"],
                        }
                    ],
                }
            }

            nutrients.append({"item": item, "amount": amount})
    return nutrients
