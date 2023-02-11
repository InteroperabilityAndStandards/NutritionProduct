from fhir_types import FHIR_Ratio, FHIR_Reference, FHIR_Substance


def main(product: dict, status_option):
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

            item: FHIR_Substance = {}

            nutrients.append(
                {"concept": {"text": nutrient["nutrient"]["name"]}, "amount": amount}
            )
    return nutrients
