import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv

load_dotenv()
app= FastAPI()
# this defines the data structure 
class DataInput(BaseModel):
  numbers: list[float]
@app.post("/calculate/")
def calculate_stats(data: DataInput):
    nums = data.numbers

    # 1. Validate input
    if len(nums) == 0:
        raise HTTPException(status_code=400, detail="The list of numbers cannot be empty.")

    # 2. Calculate the mean
    mean = sum(nums) / len(nums)

    # 3. Calculate the variance
    squared_diffs = [(x - mean) ** 2 for x in nums]
    variance = sum(squared_diffs) / len(nums)

    # 4. Calculate the standard deviation (sqrt of variance)
    std_dev = variance ** 0.5

    return {
        "mean": mean,
        "variance": variance,
        "standard_deviation": std_dev,
    }
@app.get("/")
def root():
   return{"app":os.getenv("APP_NAME", "Statistics API")}

   