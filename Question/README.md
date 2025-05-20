# Python & AWS Candidate Test

## Basic knowledge questions

- What is \_\_main\_\_.py used for?

- How to prevent python module code from executing when the module is imported?

- What's the name of method that represents a class constructor in Python?

- What options do you have when you need to insert value of a variable into string? Name at least three.

- How can you truly restrict access to a private method of a class in Python?

- What Python feature would you use to add some functionalities to an existing function without interfering into its code?

- How is @staticmethod different from @classmethod?

- What is the advantage of using **with** keyword when reading/writing a file in Python?

## Problem solving

**problem-solving.py** script takes advantage of Person class in order to create every person defined in the "people" array and then, for each of them, run introducing method. It also prints total number of created people. Threading is used to create each person in a different thread. Unfortunately, script has some bugs preventing it from working properly. 
- Please debug, fix and explain what issues the script had.  
- Currently, number of created people is printed at the beginning. Please implement some improvements, so that number of people created is printed always at the very end (without using time.sleep).
- You are not allowed to interfere into **introduce** method code.

## Create something whilst learning something new
For this task you will need your personal account in AWS. Please create one if you don't have it yet (do not worry about costs, everything you do here will covered by AWS Free Tier).

- Create a REST API in AWS API Gateway.
- Create 2 HTTP methods in the API: GET & POST.
- Create a DynamoDB Table (keep provisioned WCU & RCU low to stay within Free Tier, 2 will be OK) and name it "users". It should consist only of a parition key (hash key) which is "user_id".
- Create a lambda function and integrate it with the API POST method. In the JSON body of HTTP POST request, user should be able to specify his first name and age. Lambda should take provided body and insert it into your DynamoDB table as a new item. Value for user_id column should be generated as a random GUID and returned to the caller in the response.
- Create second lambda function and integrate it with the API GET method. GET method should take a user_id as path parameter. Lambda should lookup the DynamoDB table (using **query** method!) and either return user or 404 status code if it doesn't exist.

Please create a new GitLab/GitHub repository, upload your lambda code in there and share link to the repo with us.
Repository should also contain a README.md with URLs to your API GET & POST methods and explanation about how to use them (exact paths, example body for POST method).