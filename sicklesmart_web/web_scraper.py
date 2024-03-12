#!/usr/bin/python3

import requests
from bs4 import BeautifulSoup


def fetch_educational_resources():
    url = 'https://medlineplus.gov/sicklecelldisease.html'
    response = requests.get(url)
    if response.status_code != 200:
        return None

    soup = BeautifulSoup(response.text, 'html.parser')
    resources = []

    # Find the section containing the educational resources
    resource_sections = soup.find_all('div', class_='section-body')
    for resource_section in resource_sections:
        # Find the <ul> element with the class 'bulletlist'
        # directly under the resource section
        ul_element = resource_section.find('ul', class_='bulletlist')
        if ul_element:
            # Iterate through each list item under the <ul> element
            for li in ul_element.find_all('li'):
                # Extract the main title from the anchor tag
                title = li.find('a').text.strip()
                link = li.find('a')['href']
                resources.append({'title': title, 'link': link})

    return resources
