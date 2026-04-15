# Purpose: Extract features from a webpage for phishing/malicious detection
# 1 = Legitimate, 0 = Suspicious, -1 = Phishing

import re
import socket
import whois
import time
from datetime import datetime
from bs4 import BeautifulSoup
import sys

# Import patterns (create patterns.py if not exists)
try:
    from patterns import *
except ImportError:
    print("Warning: patterns.py not found. Using default patterns.")
    # Default patterns if file is missing
    ipv4_pattern = r'(\b25[0-5]|\b2[0-4][0-9]|\b[01]?[0-9][0-9]?)(\.|$){3}'
    ipv6_pattern = r'([0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}'
    shortening_services = r'bit\.ly|goo\.gl|tinyurl|t\.co|ow\.ly|is\.gd|cli\.gs|tr\.im|tiny\.cc'
    http_https = r'^https?://'


def get_hostname_from_url(url):
    """Extract hostname from URL"""
    pattern = r"https?://(www\.)?|www\."
    hostname = re.sub(pattern, '', url, flags=re.IGNORECASE)
    hostname = hostname.split('/')[0]
    return hostname


def having_ip_address(url):
    ip_address_pattern = ipv4_pattern + "|" + ipv6_pattern
    match = re.search(ip_address_pattern, url)
    return -1 if match else 1


def url_length(url):
    length = len(url)
    if length < 54:
        return 1
    elif 54 <= length <= 75:
        return 0
    else:
        return -1


def shortening_service(url):
    match = re.search(shortening_services, url, re.IGNORECASE)
    return -1 if match else 1


def having_at_symbol(url):
    return -1 if "@" in url else 1


def double_slash_redirecting(url):
    last_double_slash = url.rfind('//')
    return -1 if last_double_slash > 6 else 1


def prefix_suffix(domain):
    return -1 if '-' in domain else 1


def having_sub_domain(url):
    if having_ip_address(url) == -1:
        return -1
    num_dots = url.count('.')
    if num_dots <= 3:
        return 1
    elif num_dots == 4:
        return 0
    else:
        return -1


def domain_registration_length(domain):
    try:
        expiration_date = domain.expiration_date
        if isinstance(expiration_date, list):
            expiration_date = expiration_date[0]
        today = datetime.now()
        registration_length = (expiration_date - today).days
        return -1 if registration_length / 365 <= 1 else 1
    except:
        return -1


def main(url):
    try:
        # Read HTML saved by PHP
        with open('markup.txt', 'r', encoding='utf-8', errors='ignore') as f:
            html_content = f.read()
        
        soup = BeautifulSoup(html_content, 'html.parser')
        hostname = get_hostname_from_url(url)

        status = []

        # 1-7 Basic URL features
        status.append(having_ip_address(url))
        status.append(url_length(url))
        status.append(shortening_service(url))
        status.append(having_at_symbol(url))
        status.append(double_slash_redirecting(url))
        status.append(prefix_suffix(hostname))
        status.append(having_sub_domain(url))

        # DNS & Domain features
        try:
            domain_info = whois.query(hostname)
            dns = 1
        except:
            domain_info = None
            dns = -1

        status.append(-1 if dns == -1 else domain_registration_length(domain_info))

        # Content-based features (HTML analysis)
        # Note: Some functions simplified due to complexity and reliability issues
        status.append(1)   # Favicon - Simplified
        status.append(-1 if "http:" in url else 1)  # HTTPS Token
        status.append(1)   # Request URL - Simplified
        status.append(1)   # URL of Anchor - Simplified
        status.append(1)   # Links in Tags - Simplified
        status.append(1)   # SFH
        status.append(1)   # Submitting to Email

        status.append(-1 if dns == -1 else 1)           # Abnormal URL
        status.append(1)                                # iFrame
        status.append(-1 if dns == -1 else 1)           # Age of Domain
        status.append(dns)                              # DNS Record
        status.append(1)                                # Web Traffic (Alexa is dead)
        status.append(1)                                # Google Index - Simplified
        status.append(1)                                # Statistical Report

        print("\n=== Feature Vector ===")
        print(status)
        print(f"Total Features: {len(status)}")
        
        return status

    except Exception as e:
        print(f"Error analyzing page: {e}")
        return [-1] * 22   # Return phishing score on error


# ====================== Standalone Execution ======================
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python features_extraction.py <URL>")
        sys.exit(1)
    
    test_url = sys.argv[1]
    print(f"Analyzing: {test_url}")
    result = main(test_url)
    print("Final Result:", result)