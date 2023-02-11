from fhir_types import FHIR_CodeableConcept


def main(product: dict, status_option):
    manufacturer = []
    manufacturer.append(
        {
            "active": True if "brandOwner" in product else False,
            "display": product["brandOwner"] if "brandOwner" in product else None,
        }
    )
    return manufacturer
