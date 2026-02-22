import requests
import logging
from urllib3.exceptions import InsecureRequestWarning

# Configure logging
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

# Suppress certificate warnings
requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)


def get_public_ip(url: str) -> None:
    response = requests.get(url, verify=False)
    if response.status_code != 200:
        logger.info(f"Error fetching public IP: {response.status_code}")
        return None
    else:
        # logger.info(f"Public IP Address: {response.text}")
        return response.text


if __name__ == "__main__":
    # get_public_ip(ipify_url)
    ipify_url = "https://api.ipify.org"
    public_ip = get_public_ip(ipify_url)
    print(f"Public IP is: {public_ip}")
