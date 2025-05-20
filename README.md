
# 🧠 AI-Powered Resume Screener

This is an intelligent resume screening tool that uses **TF-IDF (Term Frequency-Inverse Document Frequency)** and **Cosine Similarity** to automatically match and rank candidate resumes against a given job description. The solution includes a user-friendly **Streamlit web interface**, making it easy for recruiters and HR professionals to assess resume-job fit without manual scanning.

---

## 🚀 Features

- ✅ Upload resumes in **PDF** or **DOCX** format
- 📝 Paste a job description directly into the interface
- 📊 View similarity-based **match scores** for each candidate
- 📥 Download the screening results as a **CSV**
- 💡 Built using **Python**, **scikit-learn**, **Streamlit**, and **NLP techniques**

---

## 🔧 How It Works

### 1. **Resume Text Extraction**
Resumes are parsed using:
- `PyPDF2` for PDFs
- `docx2txt` for DOCX files

### 2. **Job Description Input**
The job description is pasted into a sidebar text box.

### 3. **TF-IDF Vectorization**
All resume texts and the job description are converted into TF-IDF vectors using `TfidfVectorizer` from `scikit-learn`.

### 4. **Cosine Similarity Calculation**
The similarity score between each resume and the job description is computed using cosine similarity.

### 5. **Ranking and Display**
Candidates are ranked by score and displayed in descending order. Scores are downloadable as a CSV.

---

## 🖥️ Web UI (Streamlit)

- The app is designed using [Streamlit](https://streamlit.io/).
- To run the app locally:

```bash
pip install -r requirements.txt
streamlit run app.py
```

---

## 📁 Folder Structure

```
.
├── app.py                 # Main application script (the code above)
├── README.md              # This file
├── requirements.txt       # Dependencies
```

---

## 📦 Dependencies

Install dependencies with:

```bash
pip install streamlit pandas numpy scikit-learn PyPDF2 docx2txt
```

---

## 📌 Example Use Case

Imagine you're hiring a **Data Analyst**. You paste the job description, upload 10 resumes, and instantly see which candidates best match your job post — saving hours of manual review.

---

## 📜 Acknowledgements

Developed by **Kajola Gbenga**, a Certified Data Scientist and AI/ML Engineer.

---

## 📬 Contact

For collaborations or inquiries, connect on [LinkedIn](https://www.linkedin.com/in/kajolagbenga/) or via k.gbenga234@gmail.com.

