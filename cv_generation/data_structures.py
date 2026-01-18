from pydantic import BaseModel
from typing import List, Optional

class Skills(BaseModel):
    programming_languages: List[str]
    frameworks: List[str]
    databases: List[str]
    cloud: List[str]
    other: List[str]

class WorkExperience(BaseModel):
    company: str
    role: str
    location: str
    start_date: str
    end_date: Optional[str]
    description: List[str]
    technologies: List[str]

class Education(BaseModel):
    institution: str
    degree: str
    location: str
    start_date: str
    end_date: str

class Language(BaseModel):
    name: str
    level: str

class Certification(BaseModel):
    name: str
    issuer: str
    year: int

class CV(BaseModel):
    full_name: str
    email: str
    phone: str
    location: str
    title: str
    summary: str
    skills: Skills
    work_experience: List[WorkExperience]
    education: List[Education]
    languages: List[Language]
    certifications: List[Certification]
    avatar_seed: str
    