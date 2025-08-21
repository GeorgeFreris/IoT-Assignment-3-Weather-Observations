import requests
from statistics import mean
import urllib3

# Disable SSL warnings
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# BOM JSON URL
url = "https://www.bom.gov.au/fwo/IDW60801/IDW60801.94610.json"

# Add headers to mimic a browser
headers = {
    "User-Agent": "Mozilla/5.0"
}

# Fetch data from BOM
response = requests.get(url, headers=headers, verify=False)

# Check if the response is valid
if response.status_code == 200:
    data = response.json() #convert json to python
    records = data["observations"]["data"] #accesses list of observation records

    # Extract values for a given statistic
    def extract(statistic):
        return [r[statistic] for r in records if statistic in r]

    # Calculate stats
    def report_stats(values):
        return {
            "max": max(values),
            "min": min(values),
            "avg": round(mean(values), 2)
        }

    # Build stats dictionary
    stats = {
        "Pressure (hPa)": report_stats(extract("press")),
        "Temperature (°C)": report_stats(extract("air_temp")),
        "Relative Humidity (%)": report_stats(extract("rel_hum")),
        "Wind Speed (km/h)": report_stats(extract("wind_spd_kmh"))
    }


return stats
