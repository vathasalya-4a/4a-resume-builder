from fastapi import FastAPI, File, Form, UploadFile, HTTPException
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
import os
import shutil
from zlm import AutoApplyModel
from zlm.prompts.resume_prompt import RESUME_WRITER_PERSONA  # Import RESUME_WRITER_PERSONA

# Using FastAPI for server 

app = FastAPI()

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust this based on your security preferences
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ensure necessary directories exist
if os.path.exists("output"):
    shutil.rmtree("output")
os.makedirs("uploads", exist_ok=True)
os.makedirs("output", exist_ok=True)

@app.post("/upload")
async def upload_resume(
    resume: UploadFile = File(...),
    job_description: str = Form(...),
    api_key: str = Form(...),
    provider: str = Form(...),
    model: str = Form(...),
    prompt: str = Form(None)  # Optional prompt
):
    try:
        # Save the uploaded resume file
        resume_path = os.path.join("uploads", resume.filename)
        with open(resume_path, "wb") as f:
            f.write(await resume.read())

        # Append the prompt to the RESUME_WRITER_PERSONA if provided
        system_prompt = RESUME_WRITER_PERSONA
        if prompt:
            system_prompt += f"\n\n{prompt}"

        # Process the resume using AutoApplyModel with the appended prompt
        resume_llm = AutoApplyModel(api_key=api_key, provider=provider, model=model, downloads_dir="output", system_prompt=system_prompt)
        user_data = resume_llm.user_data_extraction(resume_path)
        job_details, _ = resume_llm.job_details_extraction(job_site_content=job_description)

        if not user_data or not job_details:
            raise HTTPException(status_code=500, detail="Failed to process resume or job description.")

        # Build the resume based on the user data and job description
        final_resume_path, _ = resume_llm.resume_builder(job_details, user_data)

        # Return the generated resume as a PDF file
        return FileResponse(final_resume_path, media_type="application/pdf", filename="resume.pdf")

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.get("/models")
async def get_models(provider: str):
    if not provider or provider not in LLM_MAPPING:
        raise HTTPException(status_code=400, detail="Invalid or missing provider")
    
    models = LLM_MAPPING[provider]['model']
    return {"models": models}

# Running the app:
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8504)
