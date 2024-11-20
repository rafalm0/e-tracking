import pytracking

# Define your base URL and secret key
secret_key = "ELIJGNEJNGL25DSKDSFNSDkvjasn25dkvjFJKNVndsvjnkSSVKDKJNSDJKCN1146"
pytracking_config = pytracking.Configuration(
    base_open_tracking_url="https://yourdomain.com/track",
    include_client_id=False,
    secret_key=secret_key
)
# Generate the tracking pixel
html_pixel = pytracking.get_open_tracking_pixel()

# Embed this HTML code in your email
print(html_pixel)
