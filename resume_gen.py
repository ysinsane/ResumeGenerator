from openai import OpenAI
from bs4 import BeautifulSoup
import requests

client = OpenAI()

# assistant = client.beta.assistants.create(
#   name="Resume Master",
#   instructions="You are an assitant that extract job descriptions from a webpage. You are going to be provided with a html file and you need to extract the job description from it. The output should be a plain text job description.",
#   tools=[],
#   model="gpt-4o",
# )
# print(assistant.id)

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
    thread = client.beta.threads.create()
    client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=f"<htmlcontent>{html_content}</htmlcontent>",
    )
    run = client.beta.threads.runs.create_and_poll(
    thread_id=thread.id,
    assistant_id="asst_9W7eVOEGXdVyLYNji2N2GMtj",
    )
    if run.status == 'completed':
        messages = client.beta.threads.messages.list(
            thread_id=thread.id
        )
        result = messages.data[0].content[0].text.value
        return result
    else:
        return None

def generate_resume(full_resume: str, job_description: str) -> str:
    thread = client.beta.threads.create()
    client.beta.threads.messages.create(
    thread_id=thread.id,
    role="user",
    content=f"<fullResume>{full_resume}</fullResume><jobDescription>{job_description}</jobDescription>",
    )
    run = client.beta.threads.runs.create_and_poll(
    thread_id=thread.id,
    assistant_id="asst_htGhAnAcQhqWBugHQcotVvWz",
    )
    if run.status == 'completed': 
        messages = client.beta.threads.messages.list(
            thread_id=thread.id
        )
        result = messages.data[0].content[0].text.value
        result = result.replace("```latex", "")
        result = result.replace("```", "")
        return result
    else:
        print(run.status)

if __name__ == "__main__":
    job_description = extract_job_description("https://www.dice.com/job-detail/d797e235-f7a1-4464-adc4-5d0d2a1794d0")
    generate_resume("testdata/JavaResume1.tex", job_description)