import csv
from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from hashlib import sha256

from typing import Any, List, Optional
import psycopg2
import os
from datetime import datetime
import json
from pathlib import Path
import shutil
import time 
import paho.mqtt.client as mqtt 

connexion_sql = None

name_database = os.getenv("DATABASE")

def connect_sql():
    global connexion_sql
    try:
        connexion_sql = psycopg2.connect(
            database=name_database,
            user="program",
            host="postgresql",
            password="program"
        )
        print("Connexion à la base de données établie avec succès.")
    except Exception as e:
        print(f"Exception lors du lancement de la base de données : {e}")

connect_sql()

API_app = FastAPI(title="Hub Management API", version="1.1")

API_app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class user(BaseModel):
    username: str
    mdp: str

@API_app.post("/user")
def is_user_connected(payload: user):
    try:
        with connexion_sql.cursor() as cursol_sql:
            cursol_sql.execute(
                "SELECT user_id FROM insa_user WHERE username='"+payload.username+"' AND mdp='"+payload.mdp+"';"
            )
            rows = cursol_sql.fetchall()
            return len(rows) == 1
    except Exception:
        return False
