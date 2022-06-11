from pydantic import BaseModel

class AuthDetails(BaseModel):
    username: str
    password: str
    
class coreSchema(BaseModel):
    core: str
