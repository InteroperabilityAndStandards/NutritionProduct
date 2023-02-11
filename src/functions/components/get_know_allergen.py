from fhir_types import FHIR_CodeableConcept, FHIR_Substance


def main(product: dict, status_option):
    known_allergens: FHIR_Substance = {}
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
    return known_allergens
