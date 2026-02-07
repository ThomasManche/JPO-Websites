import csv
from fastapi import FastAPI, UploadFile, File, Form, HTTPException, Request, Response
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
import secrets

connexion_sql = None
sessions = {}

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

origins = [
    "https://localhost",
    "https://localhost:5173",
]

API_app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class user(BaseModel):
    username: str
    mdp: str

@API_app.post("/user_safe")
def is_user_safe_connected(payload: user, response: Response):
    sha_signature = sha256(payload.mdp.encode('utf-8')).hexdigest()
    try:
        with connexion_sql.cursor() as cursol_sql:
            cursol_sql.execute(
                'SELECT user_id FROM "insa_safe_user" WHERE "username"=%s AND "hash_mdp"=%s;',
                (payload.username, sha_signature)
            )
            result = cursol_sql.fetchone()
            if result is None:
                raise HTTPException(status_code=401)

            session_id = secrets.token_hex(32)
            sessions[session_id] = payload.username

            response.set_cookie(
                key="session_id",
                value=session_id,
                httponly=True,
                secure=True,
                samesite="strict"
            )
            return True
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(status_code=500)

@API_app.get("/me")
def get_current_user(request: Request):
    session_id = request.cookies.get("session_id")
    if session_id is None or session_id not in sessions:
        raise HTTPException(status_code=401)
    return {"username": sessions[session_id]}
