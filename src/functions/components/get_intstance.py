from typing import TypedDict

from fhir_types import (
    FHIR_string,
    FHIR_Quantity,
    FHIR_Identifier,
    FHIR_dateTime,
)

FHIR_NutritionProductInstance = TypedDict(
    "FHIR_NutritionProductInstance",
    {
        "quanity": FHIR_Quantity,
        "identifier": FHIR_Identifier,
        "name": FHIR_string,
        "lotNumber": FHIR_string,
        "expiry": FHIR_dateTime,
        "useBy": FHIR_dateTime,
        "biologicalSourceEvent": FHIR_Identifier,
    },
    total=False,
)


def main(product: dict):

    instance: FHIR_NutritionProductInstance = {}

    if "butter" in product["description"].lower():
        instance = {
            "lotNumber": "10000004",
            "expiry": "2023-01-31",
            "useBy": "2023-01-28",
        }
    return instance
