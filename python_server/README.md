# Trivia API cURL Requests

### 1️⃣ Create User
- **Request**:
  ```bash
  curl -X POST "http://localhost:8000/user/?name=John"

### 1️⃣ Get All Questions
- **Request**:
  ```bash
  curl -X GET "http://localhost:8000/questions/"

### 1️⃣ Get Random Questions
- **Request**:
  ```bash
  curl -X GET "http://localhost:8000/questions/random/?n=3"

### 1️⃣ Submit Answers
- **Request**:
  ```bash
  curl -X POST "http://localhost:8000/answers/" \
     -H "Content-Type: application/json" \
     -d '[{"question_id": 1, "answer_index": 0}, {"question_id": 3, "answer_index": 1}]'



