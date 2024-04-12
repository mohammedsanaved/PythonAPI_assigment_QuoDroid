from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from robot.api import TestSuiteBuilder
from robot.run import run
from robot.api import TestSuiteBuilder
from robot.run import RobotFramework



def execute_test(request):
    try:
        test_file = '/home/user/Sanaved_Assignment/task/task/test.robot'
        suite = TestSuiteBuilder().build(test_file)
        
        # Run the test suite
        result = run(test_file, output=None)
        
        # Check the execution status
        if result.return_code == 0:
            return JsonResponse({"message": "Test execution successful"})
        else:
            return JsonResponse({"error": "Test execution failed"})
    except Exception as e:
        return JsonResponse({"error": str(e)})