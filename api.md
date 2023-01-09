# Steps for zipping requirements for AWS lamda function

- pip install -t lib -r requirements_api.txt
- (cd lib; zip ../lambda_function.zip -r .)
- zip lambda_function.zip -u api.py


