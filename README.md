

## Project Structure

The project is divided into two main folders:

### 1. Answer / Problem-solving

This folder contains answers to questions and solutions to problem-solving tasks.

Contents:
- `image.png` - Screenshot related to the task
- `problem-solving-new.py` - New version of the task solution
- `problem-solving.py` - Original version of the task solution
- `README.md` - Instructions for this part of the project

### 2. AWS-API

This folder contains all elements needed to create and run the API on AWS.

Contents:
- `json` - Configuration files in JSON format
- `lambda` - Lambda function code
- `image-1.png` to `image-5.png` and `image-9.png` - Screenshots documenting the configuration process
- `image.png` - Additional screenshot
- `README.md` - Instructions for AWS API
- `.gitignore` - File specifying which files should be ignored by Git

## Testing the API

The API is available at: https://d60eh9l118.execute-api.us-east-1.amazonaws.com/prod/

### Example requests:

#### Adding a new user (POST):
```bash
curl -X POST \
  -H "Content-Type: application/json" \
  -d '{"first_name": "Michal", "age": 24}' \
  https://d60eh9l118.execute-api.us-east-1.amazonaws.com/prod/users
```

#### Retrieving user information (GET):
```bash
curl -X GET "https://d60eh9l118.execute-api.us-east-1.amazonaws.com/prod/users/userID"
```

Replace `userID` with the actual user identifier that was returned after creating a user using the POST method.
