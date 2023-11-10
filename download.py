import requests
from use_google_scholar import get_paper_url
import time

def download_papers(titles):
    for paper in titles:
        print(paper)
        paper_url = get_paper_url(paper)
        print(paper_url)
        # download the pdf from paper url into data
        data = requests.get(paper_url).content
        # write the data to a file
        with open(f"data/{paper}.pdf", 'wb') as handler:
            handler.write(data)
        time.sleep(1)
        print()