from fhir_types import FHIR_CodeableConcept, FHIR_Organization, FHIR_Reference


def main(product: dict):
    manufacturer = []

    manufacturer.append(
        {
            "active": True if "brandOwner" in product else False,
            "display": product["brandOwner"] if "brandOwner" in product else None,
        }
    )
    return manufacturer
