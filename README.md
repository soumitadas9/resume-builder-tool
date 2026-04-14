# Resume Builder Tool

This project reviews a resume against a job description and generates missing skills plus a roadmap.

## What it does

- Reads a resume file in `pdf`, `doc`, `docx`, or `txt` format.
- Reads a job description from a `txt` file.
- Uses an LLM to identify missing job-description skills from the resume.
- Generates an actionable roadmap for acquiring or demonstrating the missing skills.
- Falls back to local skill extraction if the LLM response cannot be parsed.

## Files

- `main.py` - Main script to run the resume processing flow.
- `requirements.txt` - Python package dependencies.
- `README.md` - This file.

## Setup

1. Copy your resume and job description into the project folder.

- `resume.pdf` or `resume.docx` or `resume.txt`
- `job_description.txt`

2. Create and activate the virtual environment:

```bash
cd '/Users/<yourproject folder>/resume-builder-tool'
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

Run the script with the resume and job description:

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

## Output

The script writes:

- `missing_skills.txt` - list of missing skills discovered.
- `roadmap.txt` - actionable steps to build or demonstrate the missing skills.
- `llm_raw_output.txt` - raw LLM output when the response cannot be parsed as JSON (for debugging).

## Notes

- `job_description.txt` must be plain text.
- `main.py` uses Groq for the LLM call and falls back to local extraction if parsing fails.
- The script does not generate updated resume outputs anymore.
