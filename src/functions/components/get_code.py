from fhir_types import FHIR_CodeableConcept


def main(product: dict, status_option):

    code: FHIR_CodeableConcept = {
        "text": product["description"],
        "coding": [
            {
                "system": "https://fdc.nal.usda.gov/",
                "code": product["fdcId"],
                "display": product["description"],
            },
        ],
    }

    return code
