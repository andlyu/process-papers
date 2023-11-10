import requests
from bs4 import BeautifulSoup

def get_paper_url(title):
    # Replace spaces with '+' for the query
    query = '+'.join(title.split())
    url = f"https://scholar.google.com/scholar?q={query}"

    headers = {'User-Agent': 'Mozilla/5.0'}
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        # Parse the response using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find the link to the paper (this will depend on the structure of the page)
        # This is an example and might not work as Google Scholar's layout changes
        div_gs_or_ggsm = soup.find('div', class_='gs_or_ggsm')

        # Check if the div is found and it contains an <a> tag
        if div_gs_or_ggsm and div_gs_or_ggsm.find('a'):
            # Extract the href attribute
            link = div_gs_or_ggsm.find('a')['href']
            return link
        else:
            print("The link could not be found.")
    else:
        print(f"Failed to retrieve results: Status code {response.status_code}")