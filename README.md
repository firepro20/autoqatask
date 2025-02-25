# MeD API Testing

## Overview

This repository contains a Postman collection for testing the API endpoints of the [Restful Booker](https://restful-booker.herokuapp.com/apidoc/index.html) service. The collection includes various requests for testing functionalities such as authentication, booking creation, retrieval, updating, and deletion.

## Prerequisites

Before using this Postman collection, ensure that you have the following installed:

- [Postman](https://www.postman.com/downloads/)
- [Newman](https://learning.postman.com/docs/collections/using-newman-cli/installing-running-newman/)

## Collection Details

### Folder Structure

There is one folder representing the collection for the Restful Booker service API. This was done for easier readability and automated test runs.

### Environment Variables

<b>Note:</b> The environment file should already contain all the necessary variables. Running the MeD collection will generate all the necessary variables required for test execution. If this is not the case, you can set the following in the environment config:

- `baseUrl`: Set to `https://restful-booker.herokuapp.com`
- `authToken`: Token for authenticated requests (generated using the authentication endpoint)

## Running the Tests

### Using Postman

1. Import the `RestfulBooker.postman_collection.json` file into Postman.
2. Import the `MeD Environment.postman_environment.json` file into Postman.
3. Execute individual requests or run the entire collection using the **Runner**.

### Using Newman (CLI) *Optional*

1. Install Newman globally using npm:
   ```sh
   npm install -g newman
   ```
2. Run the collection with Newman:
   ```sh
   newman run RestfulBooker.postman_collection.json -e MeD Environment.postman_environment.json
   ```
3. To generate an HTML report, run:
   ```sh
   newman run RestfulBooker.postman_collection.json -e MeD Environment.postman_environment.json -r html
   ```

## Test Cases Covered

The collection covers the following test scenarios:

- Successful and failed authentication attempts
- Creating, retrieving, updating, and deleting a booking
- Validating required fields and error handling
- API response time and status code verification

# E2E API Service Tests

## Setup

### Prerequisites 

Ensure the latest version of python is installed.


### Install pytest

1. Install virtual environment for python:
``` pip install virtualenv ```

2. Create a new virtual environment in the API test folder: 
``` virtualenv venv ```

3. Run virtual environment activation script depending on OS used (Windows):
```  .\venv\Scripts\activate.ps1 ```

4. Install pytest: ``` pip install -U pytest ```

5. Confirm installation was successful: ``` pytest --version ```

### Running test suite

You can run the suite by entering the following: ``` .\tests\test_suite.py ```

# Future Work

## Update e2e tests

## Front-end automated tests

Front-end automation tests using Cypress or Selenium in order to integrate with a service such as Saucelabs for periodical checks.


## Contributing

If you wish to contribute, feel free to fork this repository and submit pull requests with improvements or additional test cases.

## License

This project is licensed under the MIT License.

## Contact

For any queries or issues, reach out to [dzamm20@gmail.com].

