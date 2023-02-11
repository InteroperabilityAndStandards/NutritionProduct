from fhir_types import (
    FHIR_CodeableConcept,
    FHIR_Quantity,
    FHIR_Identifier,
    FHIR_string,
    FHIR_dateTime,
)


def main(product: dict, status_option):

    quanity: FHIR_Quantity
    identifier: FHIR_Identifier
    name: FHIR_string
    lotNumber: FHIR_string
    expiry: FHIR_dateTime
    useBy: FHIR_dateTime
    biologicalSourceEvent: FHIR_Identifier
    instance = None

    if "butter" in product["description"].lower():
        instance = {
            "quantity": "6",
            "identifier": product["gtinUpc"] if "gtinUpc" in product else None,
            "name": product["description"],
            "lotNumber": "10000004",
            "expiry": "2023/1/31",
            "useBy": "2023/1/28",
            "biologicalSourceEvent": "",
        }
    return instance
