import requests
from bs4 import BeautifulSoup


def get_phone_number_info(phone_number):
    url = f"https://phonenumberinfo.net/{phone_number}"
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            # Find the relevant details in the HTML
            country = soup.find('td', {'class': 'country'}).text.strip()
            location = soup.find('td', {'class': 'location'}).text.strip()
            carrier = soup.find('td', {'class': 'carrier'}).text.strip()

            return {
                'Country': country,
                'Location': location,
                'Carrier': carrier
            }
        except AttributeError:
            return "Information not found."
    else:
        return "Error: Unable to fetch data."


# Example usage
phone_number = "numbr"  # Replace with the phone number you want to check
info = get_phone_number_info(phone_number)
print(info)
