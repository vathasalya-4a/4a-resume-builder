CERTIFICATIONS = """You are going to write a JSON resume section of "Certifications" for an applicant applying for job posts.

Step to follow:
1. Analyze my certification details to match job requirements.
2. Create a JSON resume section that highlights strongest matches
3. Optimize JSON section for clarity and relevance to the job description.

Instructions:
1. Focus: Include relevant certifications aligned with the job description.
2. Proofreading: Ensure impeccable spelling and grammar.

<CERTIFICATIONS>
{section_data}
</CERTIFICATIONS>

<job_description>
{job_description}
</job_description>

<example>
  "certifications": [
    {{
      "name": "Deep Learning Specialization"
    }},
    {{
      "name": "Server-side Backend Development"
    }}
    ...
  ],
</example>

{format_instructions}
"""

EDUCATIONS = """You are going to write a JSON resume section of "Education" for an applicant applying for job posts.

Step to follow:
1. Analyze my education details to match job requirements.
2. Create a JSON resume section that highlights strongest matches
3. Optimize JSON section for clarity and relevance to the job description.

Instructions:
- Maintain truthfulness and objectivity in listing experience.
- Prioritize specificity - with respect to job - over generality.
- Proofread and Correct spelling and grammar errors.
- Aim for clear expression over impressiveness.
- Prefer active voice over passive voice.

<Education>
{section_data}
</Education>

<job_description>
{job_description}
</job_description>

<example>
"education": [
  {{
    "university": "Masters of Science in Computer Science (Thesis), Arizona State University, Tempe, USA",
    "to_date": "May 2025"
  }}
  [and So on ...]
],
</example>

{format_instructions}
"""

SKILLS="""You are going to write a JSON resume section of "Skills" for an applicant applying for job posts.

Step to follow:
1. Analyze my Skills details to match job requirements.
2. Create a JSON resume section that highlights strongest matches.
3. Optimize JSON section for clarity and relevance to the job description.

Instructions:
- Specificity: Prioritize relevance to the specific job over general achievements.
- Proofreading: Ensure impeccable spelling and grammar.

<SKILL_SECTION>
{section_data}
</SKILL_SECTION>

<job_description>
{job_description}
</job_description>

<example>
"skill_section": [
    {{
      "skill": "Programming Languages",
      "subskill": ["Python", "JavaScript", "C#", and so on ...]
    }},
    {{
      "Skill": "Cloud and DevOps",
      "Sub Skills": [ "Azure", "AWS", and so on ... ]
    }},
    and so on ...
  ]
</example>
  
  {format_instructions}
  """


EXPERIENCE="""You are going to write a JSON resume section of "Work Experience" for an applicant applying for job posts.

Step to follow:
1. Analyze my Work details to match job requirements.
2. Create a JSON resume section that highlights strongest matches
3. Optimize JSON section for clarity and relevance to the job description.

Instructions:
1. Focus: Craft three highly relevant work experiences aligned with the job description.
2. Content:
  2.1. Bullet points: 3 per experience, closely mirroring job requirements.
  2.2. Impact: Quantify each bullet point for measurable results.
  2.3. Storytelling: Utilize STAR methodology (Situation, Task, Action, Result) implicitly within each bullet point.
  2.4. Action Verbs: Showcase soft skills with strong, active verbs.
  2.5. Honesty: Prioritize truthfulness and objective language.
  2.6. Structure: Each bullet point follows "Did X by doing Y, achieved Z" format.
  2.7. Specificity: Prioritize relevance to the specific job over general achievements.
3. Style:
  3.1. Clarity: Clear expression trumps impressiveness.
  3.2. Voice: Use active voice whenever possible.
  3.3. Proofreading: Ensure impeccable spelling and grammar.

<work_experience>
{section_data}
</work_experience>

<job_description>
{job_description}
</job_description>

<example>
"work_experience": [
    {{
      "Job": "Winjit Technologies, Virginia",
      "Job Title": "Software Engineer",
      "Duration": "Jan 2020 - Jun 2022",
      "Responsibilities": [
        "Engineered 10+ RESTful APIs Architecture and Distributed services; Designed 30+ low-latency responsive UI/UX application features with high-quality web architecture; Managed and optimized large-scale Databases. (Systems Design)",  
        "Initiated and Designed a standardized solution for dynamic forms generation, with customizable CSS capabilities feature, which reduces development time by 8x; Led and collaborated with a 12 member cross-functional team. (Idea Generation)"  
        and so on ...
      ]
      "Technologies":[ 
      "React, Angular, HTML5, CSS3, SASS, TypeScript, C#, Visual Basic, .NET, MSSQL, Figma, 
      Google Cloud, FastAPI, Edge.js, Fabric.js, Bootstrap, ASP.NET, Visual Studio, Azure, JSON"]
    }},
    {{
      "Job": "IMATMI, Robbinsville (Remote)",
      "Job Title": "Research Intern",
      "Duration": "Jan 2020 - Jun 2022",
      "Responsibilities": [
        "Conducted research and developed a range of ML and statistical models to design analytical tools and streamline HR processes, optimizing talent management systems for increased efficiency.",
        "Created 'goals and action plan generation' tool for employees, considering their weaknesses to facilitate professional growth.",
        and so on ...
      ]
      "Technologies":[
       "Angular, React, Vue, Express.js, Node.js, HTML5, CSS3, SASS, TypeScript, C#, .NET, MSSQL, 
       Figma, Bootstrap, ASP.NET, PrimeNG, WebGL, Angular Material, Visual Studio, Azure, JSON"
      ]
    }}
  ],
</example>

{format_instructions}
"""