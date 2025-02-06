from fastapi import FastAPI, Query, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import math

app = FastAPI()

# CORS Handling
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Utility Functions
def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def is_perfect(n: int) -> bool:
    return n > 1 and sum(i for i in range(1, n) if n % i == 0) == n

def is_armstrong(n: int) -> bool:
    digits = list(map(int, str(n)))
    power = len(digits)
    return sum(d ** power for d in digits) == n

def classify_number(n: int):
    properties = []
    if n % 2 == 0:
        properties.append("even")
    else:
        properties.append("odd")

    if is_prime(n):
        properties.append("prime")
    
    if is_perfect(n):
        properties.append("perfect")

    if is_armstrong(n):
        properties.append("armstrong")

    digit_sum = sum(map(int, str(n)))
    
    fun_fact = None
    if "armstrong" in properties:
        fun_fact = f"{n} is an Armstrong number because {' + '.join(f'{d}^{len(str(n))}' for d in map(int, str(n)))} = {n}"
    elif is_prime(n):
        fun_fact = f"{n} is a prime number because it has exactly two divisors: 1 and {n}."
    elif is_perfect(n):
        fun_fact = f"{n} is a perfect number because its divisors sum up to {n}."

    return {
        "number": n,
        "is_prime": is_prime(n),
        "is_perfect": is_perfect(n),
        "properties": properties,
        "digit_sum": digit_sum,
        "fun_fact": fun_fact or f"{n} is an interesting number!"
    }

# API Route with Improved Error Handling
@app.get("/api/classify-number")
async def classify_number_api(number: str = Query(..., description="Enter an integer")):
    # Check if the input is a valid integer
    if not number.lstrip("-").isdigit():
        return {"number": number, "error": True}
    
    # Check if the input is a negative number or a decimal
    if number.startswith('-') or '.' in number:
        return {"number": number, "error": True}
    
    # Convert to integer and classify the number
    number = int(number)
    return classify_number(number)

