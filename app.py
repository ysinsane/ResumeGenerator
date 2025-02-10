import os
import subprocess
from flask import Flask, render_template, request, send_file
from resume_gen_gemini import extract_job_description, generate_resume
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get input and textarea values from the form
        jd_url = request.form['jd_url']
        full_resume = request.form['user_textarea']
        jd = extract_job_description(jd_url)
        generated_text = generate_resume(full_resume, jd)
        # Save generated LaTeX content to a .tex file
        tex_filename = "generated_resume.tex"
        with open(tex_filename, "w", encoding="utf-8") as f:
            f.write(generated_text)

        # Run pdflatex to generate a PDF
        try:
            subprocess.run(["pdflatex", "-interaction=nonstopmode", tex_filename], check=True)
            pdf_filename = "generated_resume.pdf"
            return send_file(pdf_filename, as_attachment=True)
        except subprocess.CalledProcessError:
            return "Error: pdflatex failed to compile the document.", 500

    return render_template('index.html', generated_text=None)

if __name__ == '__main__':
    app.run(debug=True)
