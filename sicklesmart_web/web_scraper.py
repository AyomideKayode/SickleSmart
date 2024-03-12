#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup


def fetch_educational_resources():
    """Fetch educational resources related to sickle cell disease from a specific URL.
    Returns:
        list: A list of dictionaries containing titles and links to the resources.
            Each dictionary has keys 'title' and 'link'.
            Returns None if unable to fetch resources.
    """
    # URL of the webpage containing educational resources
    url = 'https://medlineplus.gov/sicklecelldisease.html'

    # Send a GET request to the URL
    response = requests.get(url)
    # Check if the request was successful (status code 200)
    if response.status_code != 200:
        return None

    # Parse the HTML content of the webpage using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    # List to store the extracted resources
    resources = []

    # Find sections containing educational resources
    resource_sections = soup.find_all('div', class_='section-body')
    for resource_section in resource_sections:
        # Find the unordered list (ul) element with class 'bulletlist'
        ul_element = resource_section.find('ul', class_='bulletlist')
        if ul_element:
            # Iterate through each list item (li) under the ul element
            for li in ul_element.find_all('li'):
                # Extract the title from the anchor tag
                title = li.find('a').text.strip()
                # Extract the link from the anchor tag's 'href' attribute
                link = li.find('a')['href']
                # Add the title and link to the resources list as a dictionary
                resources.append({'title': title, 'link': link})

    return resources
