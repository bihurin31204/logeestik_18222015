from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from typing import Optional, List
from enum import Enum
from datetime import datetime
from pydantic import BaseModel

app = FastAPI(
    title="Logeestik API",
    description="Layanan antar barang logistik",
    version="1.0",
    contact={
        "name": "Bihurin",
        "email": "bihurin18222015@example.com"
    }
)

@app.get("/")
def read_root():
    return {
        "project": "Logeestik API",
        "version": "1.0",
        "developer": "Bihurin",
        "description": "Layanan antar barang logistik",
        "last_updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }