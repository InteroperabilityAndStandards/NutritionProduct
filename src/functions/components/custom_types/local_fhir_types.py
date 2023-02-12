from typing import TypedDict

from fhir_types import (
    FHIR_Substance,
    FHIR_string,
    FHIR_CodeableConcept,
    FHIR_Quantity,
    FHIR_Identifier,
    FHIR_dateTime,
)

FHIR_CodeableReference = TypedDict(
    "FHIR_CodeableReference",
    {
        "id": FHIR_string,
        "reference": FHIR_Substance,
        "concept": FHIR_CodeableConcept,
    },
    total=False,
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
