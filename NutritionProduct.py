""" 
NutritionProduct FHIR Resource
http://hl7.org/fhir/2021May/nutritionproduct.html
https://github.com/nazrulworld/fhir.resources
"valueQuantity": {Quantity(SimpleQuantity)}
"quantity": {Quantity(SimpleQuantity)}
"item": {Reference.register(NutritionProduct)}, "amount": [{Ratio}]
"""


from fhir.resources.annotation import Annotation
from fhir.resources.attachment import Attachment
from fhir.resources.codeableconcept import CodeableConcept
from fhir.resources.fhirprimitiveextension import FHIRPrimitiveExtension
from fhir.resources.fhirtypes import (
    Base64Binary,
    Boolean,
    Code,
    DateTime,
    Decimal,
    Integer,
    QuantityType,
    String,
)
from fhir.resources.identifier import Identifier
from fhir.resources.organization import Organization
from fhir.resources.quantity import Quantity
from fhir.resources.ratio import Ratio
from fhir.resources.reference import Reference
from fhir.resources.substance import Substance


NutritionProduct = {
    "resourceType": "NutritionProduct",
    "status": Code,
    "category": [{CodeableConcept}],
    "code": {CodeableConcept},
    "manufacturer": [{Reference.register(Organization)}],
    "nutrient": [{"item": {Reference.register(Substance)}, "amount": [{Ratio}]}],
    "ingredient": [{"item": {Reference}, "amount": [{Ratio}]}],
    "knownAllergen": [{Reference.register(Substance)}],
    "productCharacteristic": [
        {
            "type": {CodeableConcept},
            "value": {
                "valueCodeableConcept": {CodeableConcept},
                "valueString": String,
                "valueQuantity": {Decimal},
                "valueBase64Binary": Base64Binary,
                "valueAttachment": {Attachment},
                "valueBoolean": Boolean,
            },
        }
    ],
    "instance": {
        "quantity": {Decimal},
        "identifier": [{Identifier}],
        "name": String,
        "lotNumber": String,
        "expiry": DateTime,
        "useBy": DateTime,
        "biologicalSourceEvent": {Identifier},
    },
    "note": [{Annotation}],
}
