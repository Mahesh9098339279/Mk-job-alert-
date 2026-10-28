import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse

HEADERS = {
"User-Agent": "Mozilla/5.0 (compatible; MKJobAlert/1.0)"
}

def check_website(url):
try:
response = requests.get(
url,
headers=HEADERS,
timeout=15
)
response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    title = soup.title.get_text(" ", strip=True) if soup.title else urlparse(url).netloc

    print(f"\nWebsite: {title}")
    print(f"URL: {url}")
    print("Website accessible: Yes")
    print("Note: This checks website access only, not new vacancies.")

except requests.RequestException as error:
    print(f"\nWebsite: {url}")
    print(f"Could not check: {error}")

def main():
with open("job_sources.txt", "r", encoding="utf-8") as file:
urls = [
line.strip()
for line in file
if line.strip().startswith("https://")
]

for url in urls:
    check_website(url)

if name == "main":
main()
