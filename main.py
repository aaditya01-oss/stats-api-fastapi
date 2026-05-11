import os
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging
import time
from fastapi import Request
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("stats-api")
from dotenv import load_dotenv

load_dotenv()
app= FastAPI()
#middleware for logging
@app.middleware("http")
async def log_requests(request:Request, call_next):
    start=time.time()
    response=await call_next(request)
    duration=(time.time()-start)*1000
    logger.info(f"{request.method} {request.url.path} -{response.status_code}  -{duration:.2f}ms")
    return response


#routes
@app.get("/")
def root():
   return{"app":os.getenv("APP_NAME", "Statistics API")}
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


   