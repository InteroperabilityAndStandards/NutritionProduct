# Steps for zipping requirements for AWS lamda function

- pip install -t python -r requirements_api.txt
- zip lambda_python_layer.zip -r python
- zip lambda_function.zip -ru src/functions src/types api.py
- zip lambda_function.zip -ru src/types
- zip lambda_function.zip -u api.py

https://aws.amazon.com/premiumsupport/knowledge-center/lambda-import-module-error-python/
