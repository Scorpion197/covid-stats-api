import django

django.setup()


from covidAPI.models import Country
from covidAPI.scraper import Scrapper

def populate_db():

    scrap = Scrapper()
    scrap.extract()
    scrap.process()
    results = scrap.get_results()

    for i in range(len(results)):

        new_country = Country (

        country_name = results[i][1],
        new_cases = results[i][3],
        total_cases = results[i][2],
        total_deaths = results[i][4],
        total_recovered = results[i][6],
        new_deaths = results[i][5],
        new_recovered = results[i][7],
        active_cases = results[i][8]

        )

        new_country.save()

if __name__ == "__main__":

    populate_db()
