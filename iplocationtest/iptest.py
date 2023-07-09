import re
import geoip2.database

def extract_ip_addresses(paragraphs):
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    ip_addresses = []

    for paragraph in paragraphs:
        matches = re.findall(ip_pattern, paragraph)
        ip_addresses.extend(matches)

    return ip_addresses

def get_country(ip_address):
    reader = geoip2.database.Reader('GeoLite2-Country.mmdb')
    try:
        response = reader.country(ip_address)
        country = response.country.name
    except geoip2.errors.AddressNotFoundError:
        country = 'Unknown'

    reader.close()
    return country

# Example usage
paragraphs = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Source IP: 192.168.0.1, Destination IP: 10.0.0.1",
    "Nulla facilisi. Vestibulum a lacus at nisl ultrices lacinia. Source IP: 192.168.0.2, Destination IP: 10.0.0.2",
    "Praesent euismod elit a massa semper, a pulvinar ligula fringilla. Source IP: 192.168.0.3, Destination IP: 10.0.0.3"
]

ip_addresses = extract_ip_addresses(paragraphs)

with open('ip_addresses.txt', 'w') as file:
    for ip_address in ip_addresses:
        file.write(ip_address + '\n')

for ip_address in ip_addresses:
    country = get_country(ip_address)
    print(f"IP: {ip_address}, Country: {country}")
