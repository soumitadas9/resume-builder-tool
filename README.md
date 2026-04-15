# Resume Analyzer Tool

A Python-powered resume analysis web app that compares a resume against a job description, identifies missing skills, and generates an actionable roadmap.

## Project Summary

`Resume Analyzer Tool` combines document parsing, keyword extraction, and an LLM-driven scoring workflow to help job seekers understand the skill gaps in their resume based on a target job description.

## Features

- Upload resume files in `PDF`, `DOC`, `DOCX`, or `TXT` format
- Paste the job description into the Streamlit UI
- Detect missing skills using a Groq LLM prompt
- Generate a clear, actionable roadmap for improving the resume
- Fallback local extraction when LLM output cannot be parsed
- Supports both CLI and Streamlit UI modes

## Architecture

### Backend (`main.py`)

- Parses resumes and job descriptions into plain text
- Builds a structured prompt for the Groq LLM
- Receives LLM output and extracts `missing_skills` and `roadmap`
- Uses local keyword matching fallback when necessary
- Supports multiple resume formats with dedicated parser functions

### Frontend (`app.py`)

- Streamlit web interface for file upload and text input
- Handles temporary file creation for uploaded resumes
- Calls backend logic and displays the result
- Shows errors and fallback results in the browser

## Technology Stack

- Python
- Streamlit
- Groq LLM API
- PyPDF2 for PDF text extraction
- python-docx and docx2txt for Word document parsing
- Git/GitHub for version control
- Streamlit Community Cloud for deployment

## Repository Structure

- `app.py` — Streamlit front-end app
- `main.py` — application logic, parsing, LLM request, fallback
- `requirements.txt` — dependency list
- `README.md` — project documentation

## Supported Resume Formats

- PDF (`.pdf`)
- DOC (`.doc`)
- DOCX (`.docx`)
- TXT (`.txt`)

## Setup

### Prerequisites

- Python 3.12+ installed
- `git` installed
- Groq API key

### Install dependencies

```bash
cd '/Users/<yourproject folder>/resume-builder-tool'
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Configure environment

```bash
export GROQ_API_KEY="your_api_key_here"
```

If you are using Windows PowerShell:

```powershell
$env:GROQ_API_KEY = "your_api_key_here"
```

## Usage

### CLI mode

```bash
python main.py -i resume.pdf -j job_description.txt
```

Optional format override:

```bash
python main.py -i resume.docx -f docx -j job_description.txt
```

### Streamlit UI

```bash
streamlit run app.py
```

Open the local URL shown by Streamlit and:

1. Upload a resume file
2. Paste the job description text
3. Click **Analyze**

## How it Works

### Backend control flow

1. `main.py` detects the input file type.
2. It parses the resume text using one of:
   - `parse_pdf_file()`
   - `parse_doc_file()`
   - `parse_docx_file()`
   - `parse_txt_file()`
3. It passes resume text and job description text to `llm_generate_missing_skills_and_roadmap()`.
4. The function sends a prompt to the Groq LLM and receives completion output.
5. The response is parsed by `parse_llm_json_response()`.
6. If parsing fails, the app uses `local_extract_skills()` and `gen_local_roadmap()`.
7. The results are returned to CLI or the Streamlit app.

### Frontend control flow

1. User uploads a resume and enters a job description.
2. `app.py` writes the file to a temporary location.
3. The correct parser is invoked based on file extension.
4. The backend LLM and fallback logic execute.
5. The Streamlit UI displays missing skills and roadmap.

## Output

The CLI mode saves:

- `missing_skills.txt` — sorted missing skills list
- `roadmap.txt` — recommended improvement roadmap

The Streamlit app displays results in-browser and does not write output files by default.

## Deployment

1. Push the repository to GitHub
2. Use Streamlit Community Cloud to deploy the app
3. Set `GROQ_API_KEY` in the Streamlit app secrets or environment
4. Restart the app after pushing updates

## Troubleshooting

- If Streamlit Cloud fails during dependency install, verify `requirements.txt` and the pinned package versions
- Confirm `GROQ_API_KEY` is available in the environment
- If the LLM response fails to parse, check `llm_raw_output.txt` for raw model output

## Notes

- The app currently performs live LLM requests on each analyze action
- There is no caching in the current Streamlit implementation
- The fallback logic ensures the app still returns a roadmap even when the LLM output is invalid
