import re
import requests
import folium

def extract_ip_addresses(log_file):
    ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'
    ip_addresses = []

    with open(log_file, 'r') as file:
        for line in file:
            matches = re.findall(ip_pattern, line)
            ip_addresses.extend(matches)

    return ip_addresses

def get_country(ip_address):
    url = f'http://ip-api.com/json/{ip_address}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            country = data.get('country')
            return country
    except requests.exceptions.RequestException:
        pass

    return 'Unknown'

def get_location(ip_address):
    url = f'http://ip-api.com/json/{ip_address}'
    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            latitude = data.get('lat')
            longitude = data.get('lon')
            return latitude, longitude
    except requests.exceptions.RequestException:
        pass

    return None, None

# Example usage
log_file = 'firewall.log'
source_ips = extract_ip_addresses(log_file)

# Print IP addresses and their countries
for ip_address in source_ips:
    country = get_country(ip_address)
    print(f"IP: {ip_address}, Country: {country}")

# Create an empty map
world_map = folium.Map()

# Iterate over the source IP addresses and add markers to the map
for ip_address in source_ips:
    country = get_country(ip_address)
    if country != 'Unknown':
        latitude, longitude = get_location(ip_address)
        if latitude is not None and longitude is not None:
            folium.Marker(
                location=[latitude, longitude],
                popup=f'IP: {ip_address}, Country: {country}',
                icon=folium.Icon(color='red', icon='info-sign')
            ).add_to(world_map)

# Save the map as an HTML file
world_map.save('world_map.html')
