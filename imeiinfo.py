import requests
from bs4 import BeautifulSoup

def check_imei(imei):
    url = f"https://imei.info/{imei}/"  # IMEI.info lookup page

    # Send GET request to the IMEI lookup page
    try:
        response = requests.get(url)

        # Handle response status
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            # Extract device information (you may need to adjust this based on the site's structure)
            device_info_section = soup.find('div', {'class': 'details'})

            if device_info_section:
                details = device_info_section.get_text(strip=True)
                return details
            else:
                return "Device information not found or the IMEI is invalid."
        elif response.status_code == 404:
            return "Error: Page not found. The IMEI may not exist in the database."
        else:
            return f"Error: Unable to fetch data (status code: {response.status_code})"
    except Exception as e:
        return f"An error occurred: {str(e)}"

# Replace with the IMEI number you want to check
imei_number = "numbr"  # Example IMEI number

# Get IMEI information
imei_info = check_imei(imei_number)

# Print the result
print(imei_info)
