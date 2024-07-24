import requests
from bs4 import BeautifulSoup
import random
import pandas as pd

# Defining the URL for the webpage containing country information
url = "https://www.scrapethissite.com/pages/simple/"

# Sending a request to fetch the webpage
response = requests.get(url)
response.raise_for_status()  # Check that the request was successful

# Parsing the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Finding the divs containing country information
countries_divs = soup.find_all('div', class_='col-md-4 country')

# Creating a list to store the country data
countries_data = []

# Looping through the country divs and extracting details
for country_div in countries_divs:
    name = country_div.find('h3', class_='country-name').text.strip()
    capital = country_div.find('span', class_='country-capital').text.strip()
    population = int(country_div.find('span', class_='country-population').text.strip().replace(',', ''))
    area = float(country_div.find('span', class_='country-area').text.strip().replace(',', ''))

    # Calculating population density
    population_density = population / area if area != 0 else 0

    # Appending the extracted data to the list
    countries_data.append({
        'Name': name,
        'Capital': capital,
        'Population': population,
        'Area': area,
        'Population Density': population_density
    })

# Randomly selecting ten countries
selected_countries = random.sample(countries_data, 10)

# Displaying the selected countries
for country in selected_countries:
    print(f"Country: {country['Name']}")
    print(f"Capital: {country['Capital']}")
    print(f"Population: {country['Population']}")
    print(f"Area: {country['Area']} km²")
    print(f"Population Density: {country['Population Density']:.2f} people per km²")
    print('')

# Saving the selected countries to a CSV file
df = pd.DataFrame(selected_countries)
df.to_csv('random_countries_with_density.csv', index=False)

print("Country information is in the file 'random_countries_with_density.csv'")