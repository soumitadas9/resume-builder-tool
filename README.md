# Resume Builder Tool

This project is a simple resume review and rewriting tool.

## What it does

- Reads a resume file in `pdf`, `doc`, `docx`, or `txt` format.
- Reads a job description from a `txt` file.
- Extracts keywords and skills from both documents.
- Identifies missing job-description skills in the resume.
- Generates an updated resume summary locally without requiring Hugging Face model downloads.

## Files

- `main.py` - Main script to run the resume processing flow.
- `requirements.txt` - Python package dependencies.
- `README.md` - This file.

## Setup

1. Copy your resume and job description into the project folder:

- `resume.pdf`
- `job_description.txt`

> Note: These files are included in `.gitignore` so they do not get added to the repository.

2. Create and activate the virtual environment:

```bash
cd '/Users/moue/Documents/GenAI projects/resume-builder-tool'
python3 -m venv .venv
source .venv/bin/activate
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Configure your Groq API key:

```bash
export GROQ_API_KEY="your_api_key_here"
```

## Usage

If your resume file is named with its proper extension, the script can infer the format automatically.

```bash
python main.py -i resume.pdf -j job_description.txt
```

```bash
python main.py -i resume.docx -j job_description.txt
```

If you need to override the detected format, use `-f`:

```bash
python main.py -i resume.docx -f docx -j job_description.txt
```

Supported formats for `-f/--input_format`:

- `pdf`
- `doc`
- `docx`
- `txt`

Output files:

- `missing_skills.txt` - list of missing skills.
- `updated_cv.txt` - generated resume text.
- `updated_cv.pdf` - generated resume PDF when input is `resume.pdf`.
- `updated_cv.docx` - generated resume DOCX when input is `resume.docx`.

## Notes

- The script requires `job_description.txt` to be a plain text file.
- `main.py` uses Groq for LLM-based missing skill detection and resume rewriting.
- If the LLM response cannot be parsed, `main.py` falls back to a local skill-matching extraction and resume update.
