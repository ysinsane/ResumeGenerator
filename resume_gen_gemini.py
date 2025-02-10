
from bs4 import BeautifulSoup
import requests
from google import genai

def download_html_content(url: str) -> str:
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        body_text = soup.body.get_text(separator="\n", strip=True)  # Extract text from <body>
        
        with open("webpage_text.txt", "w", encoding="utf-8") as file:
            file.write(body_text)
        print("Extracted text saved successfully!")
        return body_text
    else:
        print(f"Failed to retrieve webpage. Status code: {response.status_code}")


def extract_job_description(url: str) -> str:
    # download the html content the url
    html_content = download_html_content(url)
    client = genai.Client(api_key="AIzaSyDKV_lENriY6cxDQgNBbtwfvnezc7KRNdA")

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"Please extract JD from the following html content:<htmlcontent>{html_content}</htmlcontent>",
    )

    return response.text

def generate_resume(full_resume: str, job_description: str) -> str:
    client = genai.Client(api_key="AIzaSyDKV_lENriY6cxDQgNBbtwfvnezc7KRNdA")

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=f"You are professional career consultant. Generate a resume that fit individual job description base on my personal full resume. The output format should be Latex.<fullResume>{full_resume}</fullResume><jobDescription>{job_description}</jobDescription>"
    )

    return response.text
    

if __name__ == "__main__":
    job_description = extract_job_description("https://www.dice.com/job-detail/d797e235-f7a1-4464-adc4-5d0d2a1794d0")
    generate_resume("testdata/JavaResume1.tex", job_description)