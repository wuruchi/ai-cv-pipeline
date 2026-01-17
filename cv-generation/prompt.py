CV_GENERATION_PROMPT = """
You are generating realistic but fully synthetic CVs for software and data roles. Always respond with a single JSON object that strictly follows the schema I will provide. Do not include any additional text, comments, or Markdown. All people, companies, and emails must be fictional.

User:
Generate a CV for a candidate. The candidate should work in the tech industry (backend, data, MLOps, full‑stack, or similar). Vary seniority (junior, mid, senior) and tech stacks between CVs.
Use this exact JSON schema:

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
The avatar_seed must be a deterministic identifier like the candidate email or full name, to be used with an avatar API.
"""