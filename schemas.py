from pydantic import BaseModel

class AuthDetails(BaseModel):
    username: str
    password: str
    
class goatSchema(BaseModel):
    goatData: str
