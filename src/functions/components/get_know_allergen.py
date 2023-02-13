from fhir_types import FHIR_CodeableConcept, FHIR_Substance
from fhir_types import FHIR_CodeableConcept, FHIR_Ratio, FHIR_string, FHIR_Substance
from typing import TypedDict


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
    known_allergens: FHIR_CodeableReference = {}
    if "butter" in product["description"].lower():
        known_allergens: FHIR_CodeableReference = {
            "concept": {
                "text": "Peanut (substance)",
                "coding": [
                    {
                        "system": "http://snomed.info/sct",
                        "code": "226355009",
                        "display": "Peanut (substance)",
                    }
                ],
            },
        }

    return known_allergens
