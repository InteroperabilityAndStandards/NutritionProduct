import re
import random
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


def main(product: dict, nlp):
    ingredients = []

    if "ingredients" in product:
        count = 0
        for ingredient in re.split(r",(?![^()]*\))", product["ingredients"]):
            count += 1
            random.seed(count)
            seed = random.random()

            doc = nlp(str(ingredient.lower()))
            entry_count = 0
            for entry in doc.ents:
                entry_count += 1
                if entry_count != 1:
                    term_type = "CHILD"

                if entry._.kb_ents:
                    umls_cui = entry._.kb_ents[0][0]
                    umls_term = entry.text

                    item: FHIR_CodeableReference = {
                        "concept": {
                            "text": umls_term,
                            "coding": [
                                {
                                    "system": "https://uts.nlm.nih.gov/uts/",
                                    "code": umls_cui,
                                    "display": umls_term,
                                }
                            ],
                        }
                    }

                    ingredients.append(
                        {
                            "item": item,
                        }
                    )
            # data = {
            #     "term_type": ingredient.replace(".", "").strip(),
            #     "umls_cui": umls_cui,
            #     "umls_term": umls_term.upper(),
            # }

            # ingredients.append(
            #     {
            #         "system": "https://uts.nlm.nih.gov/uts/",
            #         "code": "umls_cui",
            #         "display": "umls_term",
            #         "term_type": ingredient.replace(".", "").strip(),
            #     }
            # )
    return ingredients
