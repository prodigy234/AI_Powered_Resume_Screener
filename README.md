
# 🧠 AI-Powered Resume Screener

This is a highly intelligent resume screening tool that uses **TF-IDF (Term Frequency-Inverse Document Frequency)** and **Cosine Similarity** to automatically match and rank candidate resumes against a given job description. The solution includes a user-friendly **Streamlit web interface**, making it easy for recruiters and HR professionals to assess resume-job fit without manual scanning.

---

This intelligently developed AI-powered resume screening model which I built for seamless recruitment of talents and exceptionally seasoned individuals can be accessed live on streamlit [Here](https://screenresume.streamlit.app/)

---

## 📬 Author

**Gbenga Kajola**

[LinkedIn](https://www.linkedin.com/in/kajolagbenga)

[Certified_Data_Scientist](https://www.datacamp.com/certificate/DSA0012312825030)

[Certified_Data_Analyst](https://www.datacamp.com/certificate/DAA0018583322187)

[Certified_SQL_Database_Programmer](https://www.datacamp.com/certificate/SQA0019722049554)


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

## 📌 Example Use Case

Imagine you're hiring a **Data Analyst**. You paste the job description, upload 10 resumes, and instantly see which candidates best match your job post — saving hours of manual review.

---


## 🖥️ Web UI (Streamlit)

- The app is designed using [Streamlit](https://streamlit.io/).
- To run the app locally:


---

## 📁 Folder Structure

```
📦 Resume Screening AI/
├── app.py                 # Main application script
├── my_image.jpg                       # My image
├── README.md              # The thought process and set up
├── requirements.txt       # Dependencies

```

---

## 🧪 How to Run the App

### 1. Clone or download the repository

```bash

git clone https://github.com/prodigy234/AI_Powered_Resume_Screener.git

```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

Or manually install:

```bash
pip install streamlit pandas numpy scikit-learn PyPDF2 docx2txt
```

### 3. Launch the app

```bash
streamlit run app.py
```

---

## 🏁 License

MIT License – feel free to use and customize this for your business or learning projects.

---
