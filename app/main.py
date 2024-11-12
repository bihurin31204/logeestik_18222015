from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, List
from enum import Enum
from datetime import datetime
from pydantic import BaseModel

app = FastAPI(
    title="logeestik",
    description="delivery package",
    version="1.0",
    contact={
        "name": "bihurin",
        "email": "bihurin@gmail.com"
    }
)

@app.get("/")
def read_root():
    return {
        "project": "Logee API",
        "version": "1.0",
        "developer": "bihurin",
        "description": "delivery package",
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
