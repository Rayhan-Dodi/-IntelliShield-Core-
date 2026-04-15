# features_extraction.py
import re
import whois
from datetime import datetime
import urllib.parse

# ====================== FEATURE EXTRACTION FUNCTIONS ======================

def having_ip_address(url):
    """Returns -1 if URL contains IP address, else 1"""
    ip_pattern = re.compile(
        r'(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.|$){3}'
        r'(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)'
    )
    
    # Check for IPv4 and IPv6
    if re.search(ip_pattern, url) or re.search(r'([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}', url):
        return -1
    return 1


def shortening_service(url):
    """Returns -1 if URL uses shortening service, else 1"""
    shortening_services = [
        'bit.ly', 'goo.gl', 'tinyurl', 't.co', 'ow.ly', 'is.gd', 'cli.gs',
        'tr.im', 'tiny.cc', 'url4.eu', 'twurl.nl', 'snipurl.com', 'x.co'
    ]
    for service in shortening_services:
        if service in url:
            return -1
    return 1


def url_length(url):
    """Returns -1 if length > 75, 0 if between 54-75, 1 if < 54"""
    length = len(url)
    if length < 54:
        return 1
    elif length >= 54 and length <= 75:
        return 0
    else:
        return -1


def having_at_symbol(url):
    """Returns -1 if @ symbol is present, else 1"""
    if "@" in url:
        return -1
    return 1


def get_hostname_from_url(url):
    """Extract hostname from URL"""
    try:
        parsed = urllib.parse.urlparse(url)
        return parsed.netloc if parsed.netloc else parsed.path.split('/')[0]
    except:
        return ""


def domain_registration_length(domain):
    """Returns -1 if domain expires in less than 1 year, else 1"""
    try:
        expiration_date = domain.expiration_date
        if isinstance(expiration_date, list):
            expiration_date = expiration_date[0]
        if (expiration_date - datetime.now()).days < 365:
            return -1
        return 1
    except:
        return -1  # If whois fails, treat as suspicious


def having_sub_domain(url):
    """Returns -1 if has sub-domain, else 1"""
    hostname = get_hostname_from_url(url)
    if hostname.count('.') >= 2:
        return -1
    return 1


# ====================== PREDICTION FUNCTION ======================

def get_prediction_from_url(url):
    """Simple prediction based on features (You can expand this later)"""
    features = []
    
    features.append(having_ip_address(url))
    features.append(shortening_service(url))
    features.append(url_length(url))
    features.append(having_at_symbol(url))
    features.append(having_sub_domain(url))
    
    # Simple rule-based prediction (can be replaced with ML model later)
    score = sum(features)
    
    if score <= 0:
        return -1  # Phishing / Malicious
    else:
        return 1   # Legitimate


# ====================== TEST HELPER ======================

def get_prediction_from_url_test(url):
    """For unit testing compatibility"""
    return get_prediction_from_url(url)