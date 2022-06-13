# Imports as required;
#
# import mysql.connector
from fastapi import FastAPI, Depends, HTTPException
from auth import AuthHandler
from schemas import AuthDetails, coreSchema

# Initialize the API Project
app = FastAPI()

# Handle auth and cliented user data
auth_handler = AuthHandler()
users = []

# Creating connection object
# Default login credentials provided
#
# URLgripper = mysql.connector.connect(
#   host="127.0.0.11",
#   user="root",
#   password="",
#   database="testdatabase"
# )

@app.get("/")
def home():
    return { 'home': 'homepage api' }

@app.post('/core')
def crex(data: coreSchema):
    return data

@app.get('/goob')
def goob():
    return { 'gooby': 'gooba-gii goob' }

# /api/register endpoint; requires username and password
@app.post('/api/register', status_code=201)
def register(auth_details: AuthDetails):
    if any(x['username'] == auth_details.username for x in users):
        raise HTTPException(status_code=400, detail='Username is taken')
    hashed_password = auth_handler.get_password_hash(auth_details.password)
    token = auth_handler.encode_token(auth_details.username)
    users.append({
        'username': auth_details.username,
        'password': hashed_password
    })

    # Insert the registration into the database;
    #
    # mycursor = URLgripper.cursor()
    # sql = "INSERT INTO users (username, password) VALUES (%s, %s)"
    # val = (auth_details.username, hashed_password)
    # mycursor.execute(sql, val)
    # URLgripper.commit()

    return { 'token': token }

# /api/login endpoint; requires username and password
@app.post('/api/login')
def login(auth_details: AuthDetails):
    user = None
    for x in users:
        if x['username'] == auth_details.username:
            user = x
            break
    if (user is None) or (not auth_handler.verify_password(auth_details.password, user['password'])):
        raise HTTPException(status_code=401, detail='Invalid login credentials')
    else:
        token = auth_handler.encode_token(user['username'])
        return { 'token': token }

# Unprotected Test Endpoint; exposable
@app.get('/unprotected')
def unprotected():
    return { 'hello': 'world!' }

# Protected Test Endpoint; non-exposable; Bearer Token required
@app.get('/protected')
def protected(username=Depends(auth_handler.auth_wrapper)):
    return { 'name': username }
    
# Protected Test Endpoint; non-exposable; Bearer Token required
@app.post('/post')
def protected(username=Depends(auth_handler.auth_wrapper)):
    a = [1, 2, 3], [4, 5], [6, 7, 8]
    for i in range(len(a)):
        for j in range(len(a[i])):
            print(a[i][j], end=' ')
        return(a)