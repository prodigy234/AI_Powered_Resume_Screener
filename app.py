# Resume Screening with AI (TF-IDF + Cosine Similarity + Streamlit UI)

import streamlit as st
import pandas as pd
import numpy as np
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from PyPDF2 import PdfReader
import docx2txt

# ------------------- Helper Functions ------------------- #

def extract_text_from_pdf(pdf_file):
    try:
        reader = PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
        return text.strip()
    except Exception as e:
        return ""

def extract_text_from_docx(docx_file):
    try:
        text = docx2txt.process(docx_file)
        return text.strip()
    except Exception as e:
        return ""

def read_resume(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        return extract_text_from_pdf(uploaded_file)
    elif uploaded_file.name.endswith(".docx"):
        return extract_text_from_docx(uploaded_file)
    else:
        return ""

def compute_similarity(resume_texts, job_description):
    corpus = resume_texts + [job_description]
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(corpus)
    job_vec = tfidf_matrix[-1]  # last one is JD
    resume_vecs = tfidf_matrix[:-1]
    scores = cosine_similarity(resume_vecs, job_vec)
    return scores.flatten()

# ------------------- Streamlit UI ------------------- #

st.set_page_config(page_title="AI Resume Screener", layout="wide")
st.title("📄 AI-Powered Resume Screening Tool")
st.write("Automatically score resumes based on a job description using TF-IDF and cosine similarity.")

# Upload Job Description
st.sidebar.header("Upload Job Description")
jd_file = st.sidebar.text_area("Paste Job Description Here")

# Upload Resumes
st.sidebar.header("Upload Candidate Resumes")
resume_files = st.sidebar.file_uploader("Upload Multiple Resumes (PDF/DOCX)", type=['pdf', 'docx'], accept_multiple_files=True)

# Screening Button
if st.sidebar.button("⚙️ Run Screening"):
    if not jd_file or not resume_files:
        st.warning("Please provide both a job description and at least one resume.")
    else:
        st.info("🔍 Screening resumes... Please wait.")
        resume_texts = []
        candidate_names = []

        for file in resume_files:
            text = read_resume(file)
            if text:
                resume_texts.append(text)
                candidate_names.append(file.name)
            else:
                resume_texts.append("")
                candidate_names.append(file.name + " (Error Reading File)")

        scores = compute_similarity(resume_texts, jd_file)

        results_df = pd.DataFrame({
            'Candidate Name': candidate_names,
            'Match Score (%)': np.round(scores * 100, 2)
        }).sort_values(by='Match Score (%)', ascending=False).reset_index(drop=True)

        st.success("✅ Screening complete! Results below:")
        st.dataframe(results_df)

        st.download_button("📥 Download Results as CSV", data=results_df.to_csv(index=False), file_name="resume_scores.csv", mime="text/csv")

# Footer
st.markdown("---")
st.markdown("Made by Kajola Gbenga, a certified Data Scientist, and an AI/ML Engineer")