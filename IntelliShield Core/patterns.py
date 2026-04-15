# patterns.py
# Common regular expression patterns used by features_extraction.py

# ==================== URL Patterns ====================

# IPv4 Pattern
ipv4_pattern = r"(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)"

# IPv6 Pattern (Simplified & More Reliable)
ipv6_pattern = r"(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|(?:[0-9a-fA-F]{1,4}:){1,7}:|(?:[0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|" \
               r"(?:[0-9a-fA-F]{1,4}:){1,5}(?::[0-9a-fA-F]{1,4}){1,2}|(?:[0-9a-fA-F]{1,4}:){1,4}(?::[0-9a-fA-F]{1,4}){1,3}|" \
               r"(?:[0-9a-fA-F]{1,4}:){1,3}(?::[0-9a-fA-F]{1,4}){1,4}|(?:[0-9a-fA-F]{1,4}:){1,2}(?::[0-9a-fA-F]{1,4}){1,5}|" \
               r"[0-9a-fA-F]{1,4}:(?::[0-9a-fA-F]{1,4}){1,6}|:(?::[0-9a-fA-F]{1,4}){1,7}|::"

# Shortening Services
shortening_services = r"bit\.ly|goo\.gl|tinyurl\.com|t\.co|ow\.ly|is\.gd|cli\.gs|tr\.im|tiny\.cc|url4\.eu|twurl\.nl|" \
                      r"snipurl\.com|x\.co|bit\.do|lnkd\.in|db\.tt|qr\.ae|adf\.ly|cur\.lv|ity\.im|q\.gs|po\.st|" \
                      r"bc\.vc|twitthis\.com|u\.to|j\.mp|buzurl\.com|cutt\.us|yourls\.org|prettylinkpro\.com|" \
                      r"v\.gd|link\.zip\.net|shorte\.st|go2l\.ink|yfrog\.com|migre\.me|ff\.im|su\.pr"

# HTTP/HTTPS Token
http_https = r"^https?://"

# Other useful patterns
at_symbol = r"@"
dash_symbol = r"-"