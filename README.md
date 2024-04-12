
---

# Challenge Document: Innovative Solution Development with Python, Django, and Robot Framework

## Objective:
The core objective of this system is to create an application that can accept a detailed API call, execute the testing steps provided within as a Robot Framework test, and subsequently return the test output.

## System Overview:
The system consists of a Python-based backend developed using Django framework. It exposes an API endpoint that accepts a POST request containing test instructions in a specific JSON format. These instructions are then processed and executed as Robot Framework tests. The test results are returned as the response to the API call.

## API Endpoint Details:
- **Endpoint:** http://127.0.0.1:8000/testai/tests/v1/execute
- **Method:** POST
- **Headers:** 
  - Content-Type: application/json
- **Body Format:**
```json
{
  "tests": [
    {
      "title": "Open google.com",
      "steps": [
        "Open Browser browser='chrome'",
        "Go To url='https://google.com'"
      ]
    }
  ]
}
```
- **Description:** 
  - The JSON payload contains an array under the key `TESTS`, with each item representing a single test case.
  - Each test case has a `TITLE` and an array of `STEPS`.
  - Each step is a command to be executed by the Robot Framework, such as opening a browser or navigating to a URL.

## System Components:
1. **Django Application:** 
   - Responsible for handling API requests and orchestrating the execution of Robot Framework tests.
   - Provides the necessary endpoints to accept API calls.
   - Parses the JSON payload, generates Robot Framework test files dynamically, and executes them.
   - Captures and formats the test results for the response.
   
2. **Robot Framework:**
   - Used for writing and executing automated test cases.
   - Processes the test instructions received from the Django application and executes them.
   - Generates detailed test reports containing the results of each test step.
   
## Execution Flow:
1. The client sends a POST request to the provided API endpoint with the test instructions in the JSON format.
2. The Django application receives the request and extracts the test instructions from the payload.
3. For each test case, the Django application dynamically generates a Robot Framework test file with the provided test steps.
4. The Django application executes the generated test files using Robot Framework.
5. Robot Framework executes the test cases and generates detailed test reports.
6. The Django application captures the test results, formats them, and sends them back as the response to the client.

## Conclusion:
The API Test Automation System provides a robust and scalable solution for executing automated tests based on Robot Framework. By following the specified API call format, users can easily define and execute test cases, while receiving detailed test reports for analysis.

---