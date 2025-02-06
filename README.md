# HNG DevOps Interns - The Cool Kids : Stage One

## Number Classification & Fun Fact API

This FastAPI-based application classifies a given number based on mathematical properties and provides fun facts using the [Numbers API](http://numbersapi.com/).

---

## Features
- Check if a number is **prime** or **perfect**.
- Identify properties such as **even/odd** and **Armstrong numbers**.
- Compute the **digit sum** of a given number.
- Fetch fun mathematical facts from [Numbers API](http://numbersapi.com/).
- Returns JSON responses with structured data.
- Includes error handling for invalid inputs.

---

## API Endpoint
### **Classify a Number**
#### **Endpoint:**
```http
GET /api/classify-number?number=<your_number>
```
#### **Query Parameter:**
| Parameter | Type   | Required | Description |
|-----------|--------|-----------|-------------|
| number    | string | Yes       | The number to classify. Must be an integer. |

#### **Response (Success)**
**Status Code:** `200 OK`
```json
{
  "number": 28,
  "is_prime": false,
  "is_perfect": true,
  "properties": ["even"],
  "digit_sum": 10,
  "fun_fact": "28 is a perfect number, equal to the sum of its proper divisors."
}
```

#### **Response (Error: Invalid Input)**
**Status Code:** `400 Bad Request`
```json
{
  "number": "abc",
  "error": true
}
```

---

## Installation & Setup
### **Prerequisites**
Ensure you have Python 3.7+ installed.

### **Step 1: Clone the Repository**
```sh
git clone <your-repo-url>
cd <your-repo-folder>
```

### **Step 2: Create a Virtual Environment (Optional but Recommended)**
```sh
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate     # On Windows
```

### **Step 3: Install Dependencies**
```sh
pip install fastapi uvicorn requests
```

---

## Running the API
Start the FastAPI application using Uvicorn:
```sh
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

The API will be available at: [http://127.0.0.1:8000](http://127.0.0.1:8000)

For interactive API documentation, visit:
- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **Redoc UI:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## Deployment
This API can be deployed on AWS EC2 using GitHub Actions for CI/CD automation.

### **Docker Deployment**
```sh
docker build -t number-fact-api .
docker run -p 8000:8000 number-fact-api
```

### **AWS Deployment (EC2)**
- Provision an EC2 instance (Amazon Linux / Ubuntu)
- Install Python and dependencies
- Clone the repo and start the API with Uvicorn
- Expose port 8000 via security groups

---

## References
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Pydantic Documentation](https://docs.pydantic.dev/)
- [Numbers API](http://numbersapi.com/)
- [Uvicorn ASGI Server](https://www.uvicorn.org/)

---

## Contributors
- **[Your Name]** - HNG DevOps Intern
- **Community Contributions Welcome!**

---

## License
This project is licensed under the MIT License.


