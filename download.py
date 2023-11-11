import requests
import time
from pdfminer.high_level import extract_text
from typing import List
from semanticscholar import SemanticScholar
import pandas as pd

sch = SemanticScholar()

def convert_pdf_to_txt(pdf_path:str) -> str:
    """Converts a pdf file to a text file

    Args:
        pdf_path (str): path to a local file path

    Returns:
        str: output text file path
    """
    extracted_text = extract_text(pdf_path)
    text_path  = pdf_path[:-4] + '.txt'
    with open(text_path, 'w') as f:
        f.write(extracted_text)

    return text_path

def get_paper_url(title:str) -> str:
    """Given  a paper title, searches semantic scholar, returns the arxiv url to the paper 

    Args:
        title (str): Paper title

    Returns:
        str: Returns the arxiv url to the paper
    """
    results = sch.search_paper(title)
    if('ArXiv' not in results.items[0]['externalIds']):
        print(f'No arxiv link found for {title}')
        return None
    pdf_url = f"https://arxiv.org/pdf/{results.items[0]['externalIds']['ArXiv']}.pdf"
    return pdf_url


def get_paper_urls(titles:List[str]):
    """Gets URLs to pdfs of papers, given their titles and creates a CSV with the titles and URLs

    Args:
        titles (List[str]): Titles of papers to download
    """
    df = pd.DataFrame(columns=['title', 'url'])
    for paper in titles:
        paper_url = get_paper_url(paper)
        # if URL not found, only add the title
        next_item = {'title': paper, 'url': paper_url}
        df = df._append(next_item, ignore_index=True)

    df.to_csv('data/papers.csv')


def download_papers(paper_urls:List[str], paper_titles: List[str]) -> List[str]:
    """
    Downloads papers from google scholar into data folder

    Args:
        titles (str): String of paper titles that 

    Returns:
        list(str): the list of local paths for the downloaded PDfs
    """
    output_files = []
    for paper_url, paper_title in zip(paper_urls, paper_titles):
        data = requests.get(paper_url).content
        output_pdf = f"data/{paper_title}.pdf"
        with open(output_pdf, 'wb') as handler:
            handler.write(data)
        output_files.append(output_pdf)
        print(f"Saved {paper_title} to {output_pdf}")

    return output_files