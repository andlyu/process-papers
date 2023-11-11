import numpy as np
from download import download_papers, convert_pdf_to_txt
from download import get_paper_urls
import os
import pandas as pd
from pdfminer.high_level import extract_text

titles = [
    "Self-Supervised Object Detection from Egocentric Videos",
    "STEPs: Self-Supervised Key Step Extraction and Localization from Unlabeled Procedural Videos",
    "Masked Spatio-Temporal Structure Prediction for Self-supervised Learning on Point Cloud Videos",
    "Learning Trajectory-Word Alignments for Video-Language Tasks",
    "Spatio-Temporal Crop Aggregation for Video Representation Learning",
    "Progressive Spatio-Temporal Prototype Matching for Text-Video Retrieval",
    "Long-range Multimodal Pretraining for Movie Understanding",
    "MGMAE: Motion Guided Masking for Video Masked Autoencoding",
    "Learning to Ground Instructional Articles in Videos through Narrations",
    "Accurate and Fast Compressed Video Captioning",
    "Few-Shot Video Classification via Representation Fusion and Promotion Learning"
]

if __name__ == "__main__":
    # If we do not have papers_csv, we create them
    if(not os.path.exists('data/papers.csv')):
        get_paper_urls(titles)
        print("Created papers.csv, please update the urls manually and rerun the script")
        exit()

    # TODO: Some paper urls are not found in Semantic Scholar, so they need to be updated manually

    # download the papers
    paper_urls = pd.read_csv('data/papers.csv')
    pdfs_paths = download_papers(paper_urls['url'].values, paper_urls['title'].values)

    # convert the pdfs to text
    texts = []
    for paper in pdfs_paths:
        texts.append(extract_text(paper))

    # save the texts to a file
    with open('data/papers.txt', 'w') as f:
        for text in texts:
            f.write(text)
            f.write('\nTHIS IS THE END OF A PAPER AND A NEW ONE WILL BEGIN AFTERWARDS\n')


