""" 
NutritionIntake FHIR Resource
http://hl7.org/fhir/2021May/nutritionintake.html
https://github.com/nazrulworld/fhir.resources
"""

from fhir.resources.annotation import Annotation
from fhir.resources.attachment import Attachment
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.fhirtypes import (
    Base64Binary,
    Boolean,
    Code,
    DateTime,
    QuantityType,
    String,
    RatioType,
)
from fhir.resources.identifier import Identifier
from fhir.resources.organization import Organization
from fhir.resources.quantity import Quantity
from fhir.resources.ratio import Ratio
from fhir.resources.reference import Reference
from fhir.resources.substance import Substance


NutritionIntake = {
    "resourceType": "NutritionIntake",
    "status": Code,
    "category": [{CodeableConcept}],
    "code": {CodeableConcept},
    "manufacturer": [{Reference.register(Organization)}],
    "nutrient": [{"item": {Reference.register(Substance)}, "amount": [{Ratio}]}],
    "ingredient": [
        {"item": {Reference.register(NutritionIntake)}, "amount": [{Ratio}]}
    ],
    "knownAllergen": [{Reference.register(Substance)}],
    "productCharacteristic": [
        {
            "type": {CodeableConcept},
            "value": {
                "valueCodeableConcept": {CodeableConcept},
                "valueString": String,
                "valueQuantity": {Quantity.register(QuantityType)},
                "valueBase64Binary": Base64Binary,
                "valueAttachment": {Attachment},
                "valueBoolean": Boolean,
            },
        }
    ],
    "instance": {
        "quantity": {Quantity(SimpleQuantity)},
        "identifier": [{Identifier}],
        "name": String,
        "lotNumber": String,
        "expiry": DateTime,
        "useBy": DateTime,
        "biologicalSourceEvent": {Identifier},
    },
    "note": [{Annotation}],
}
