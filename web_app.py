from flask import Flask, request, jsonify, send_file
import os
import base64
import shutil
import zipfile
from zlm import AutoApplyModel
from zlm.utils.utils import read_file
from zlm.variables import LLM_MAPPING
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

# Ensure necessary directories exist
if os.path.exists("output"):
    shutil.rmtree("output")

os.makedirs("uploads", exist_ok=True)
os.makedirs("output", exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload_resume():
    try:
        # Extract files and form data
        if 'resume' not in request.files or 'job_description' not in request.form:
            return jsonify({"error": "Missing resume or job description"}), 400

        resume = request.files['resume']
        job_description = request.form['job_description']
        api_key = request.form['api_key']
        provider = request.form['provider']
        model = request.form['model']

        # Save the uploaded resume file
        resume_path = os.path.join("uploads", resume.filename)
        resume.save(resume_path)

        # Process the resume using AutoApplyModel
        resume_llm = AutoApplyModel(api_key=api_key, provider=provider, model=model, downloads_dir="output")
        user_data = resume_llm.user_data_extraction(resume_path)
        job_details, _ = resume_llm.job_details_extraction(job_site_content=job_description)

        if not user_data or not job_details:
            return jsonify({"error": "Failed to process resume or job description."}), 500

        # Build the resume based on the user data and job description
        resume_path, _ = resume_llm.resume_builder(job_details, user_data)

        # Return the generated resume as a PDF file
        return send_file(resume_path, as_attachment=True, mimetype='application/pdf')

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/models', methods=['GET'])
def get_models():
    # Fetch the list of models for the given provider
    provider = request.args.get('provider', default=None, type=str)
    if not provider or provider not in LLM_MAPPING:
        return jsonify({"error": "Invalid or missing provider"}), 400
    models = LLM_MAPPING[provider]['model']
    return jsonify({"models": models}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8504)