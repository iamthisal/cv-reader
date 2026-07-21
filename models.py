from pydantic import BaseModel

from typing import List,Optional


class Experience(BaseModel):
    role:str
    company:str
    years:str


class CVData(BaseModel):
    name:str
    email:str
    skills:List[str]
    experience:List[Experience]
    education:List[str]
    