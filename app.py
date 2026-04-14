import os
import tempfile
import streamlit as st
from main import (
    llm_generate_missing_skills_and_roadmap,
    local_extract_skills,
    gen_local_roadmap,
    parse_pdf_file,
    parse_doc_file,
    parse_docx_file,
    parse_txt_file,
)

st.set_page_config(page_title='Resume Skill Analyzer', layout='wide')

st.title('Resume Skill Analyzer')
st.markdown(
    'Upload your resume and paste the job description below. Click **Analyze** to identify missing skills and get a roadmap.'
)

uploaded_file = st.file_uploader('Upload resume (PDF, DOC, DOCX, or TXT)', type=['pdf', 'doc', 'docx', 'txt'])
job_description = st.text_area('Paste job description here', height=250)

analyze_clicked = st.button('Analyze')

if analyze_clicked:
    if not uploaded_file:
        st.warning('Please upload your resume file before analyzing.')
    elif not job_description.strip():
        st.warning('Please paste the job description text before analyzing.')
    else:
        with st.spinner('Analyzing resume and job description...'):
            try:
                input_text = ''
                suffix = os.path.splitext(uploaded_file.name)[1].lower()
                with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp_file:
                    temp_file.write(uploaded_file.read())
                    temp_path = temp_file.name

                if suffix == '.pdf':
                    input_text = parse_pdf_file(temp_path)
                elif suffix == '.doc':
                    input_text = parse_doc_file(temp_path)
                elif suffix == '.docx':
                    input_text = parse_docx_file(temp_path)
                elif suffix == '.txt':
                    input_text = parse_txt_file(temp_path)
                else:
                    st.error('Unsupported resume file format.')
                    input_text = None

                if input_text is None:
                    raise ValueError('Unable to parse uploaded resume file.')

                llm_missing_skills, llm_roadmap_text = llm_generate_missing_skills_and_roadmap(
                    input_text, job_description
                )

                if llm_missing_skills is None or not isinstance(llm_missing_skills, list):
                    missing_skills = sorted(
                        set(local_extract_skills(job_description.lower()))
                        - set(local_extract_skills(input_text.lower()))
                    )
                    roadmap_text = gen_local_roadmap(missing_skills)
                    st.error('LLM output could not be parsed. Showing local fallback results.')
                else:
                    missing_skills = [skill.strip() for skill in llm_missing_skills if skill.strip()]
                    roadmap_text = llm_roadmap_text.strip() if isinstance(llm_roadmap_text, str) else ''

                if missing_skills:
                    st.subheader('Missing skills')
                    st.write('- ' + '\n- '.join(missing_skills))
                else:
                    st.success('No missing skills detected.')

                st.subheader('Roadmap')
                st.write(roadmap_text or 'No roadmap generated.')

            except Exception as exc:
                st.error(f'Error during analysis: {exc}')
            finally:
                try:
                    os.remove(temp_path)
                except Exception:
                    pass
