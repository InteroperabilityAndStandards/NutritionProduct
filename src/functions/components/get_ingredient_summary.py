from fhir_types import FHIR_CodeableConcept


def main(product: dict, status_option):
    ingredient_summary = None
    if "ingredients" in product:
        ingredient_summary = product["ingredients"]

    return ingredient_summary
