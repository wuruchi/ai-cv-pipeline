import os

USERS_ARE_BASED_IN = os.getenv("USERS_ARE_BASED_IN", "Spain")

JSON_FORMAT_INSTRUCTION = """
json
{
  "full_name": "string",
  "email": "string",
  "phone": "string",
  "location": "string",
  "title": "string",
  "summary": "string",
  "skills": {
    "programming_languages": ["string"],
    "frameworks": ["string"],
    "databases": ["string"],
    "cloud": ["string"],
    "other": ["string"]
  },
  "work_experience": [
    {
      "company": "string",
      "role": "string",
      "location": "string",
      "start_date": "YYYY-MM",
      "end_date": "YYYY-MM or 'Present'",
      "description": ["string"],
      "technologies": ["string"]
    }
  ],
  "education": [
    {
      "institution": "string",
      "degree": "string",
      "location": "string",
      "start_date": "YYYY",
      "end_date": "YYYY"
    }
  ],
  "languages": [
    {"name": "string", "level": "string"}
  ],
  "certifications": [
    {
      "name": "string",
      "issuer": "string",
      "year": 2000
    }
  ],
  "avatar_seed": "string"
}
"""

CV_GENERATION_PROMPT = f"""
You are generating realistic but fully synthetic CVs for software and data roles. Always respond with a single JSON object that strictly follows the schema I will provide. Do not include any additional text, comments, or Markdown. All people, companies, and emails must be fictional.

User:
Generate a CV for a candidate. The candidate should work in the tech industry (backend, data, MLOps, full‑stack, or similar). Vary seniority (junior, mid, senior) and tech stacks between CVs. The CV should reflect someone based in {USERS_ARE_BASED_IN}. Use common names and companies from that location to make the CV more realistic. Ensure the email domain matches the fictional company they work for or a common email provider.
Use diverse names and locations for each CV.
Use this exact JSON schema:
{JSON_FORMAT_INSTRUCTION}

The avatar_seed must be a deterministic identifier like the candidate email or full name, to be used with an avatar API.
"""