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

### Using Newman (CLI)

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

## Contributing

If you wish to contribute, feel free to fork this repository and submit pull requests with improvements or additional test cases.

## License

This project is licensed under the MIT License.

## Contact

For any queries or issues, reach out to [dzamm20@gmail.com].

