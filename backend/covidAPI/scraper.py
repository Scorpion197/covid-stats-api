import requests
from bs4 import BeautifulSoup
from .models import Country

class Scrapper:

    def __init__(self):

        self.url = "https://www.worldometers.info/coronavirus/"
        self.page = requests.get(self.url)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')
        self.results = []

    def extract(self):

        table = self.soup.table
        table_rows = table.find_all('tr')

        for tr in table_rows:

            td = tr.find_all('td')
            data = [item.text for item in td]

            self.results.append(data)


    def remove_empty_arrays(self):

        for arr in self.results:

            if (len(arr) == 0):

                self.results.remove(arr)

    def remove_bad_chars(self):

        """
            remove spaces and new lines
        """

        for arr in self.results:

            for i in range(len(arr)):

                arr[i] = arr[i].replace('\n', '').replace(' ', '')

    def process(self):

        self.remove_empty_arrays()
        self.remove_bad_chars()

    def get_results(self):

        return self.results
