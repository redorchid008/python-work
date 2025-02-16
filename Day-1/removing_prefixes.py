google_url = "https://www.google.com/"
print(google_url)
print(f"Google URL is: {google_url}")

simple_url = google_url.removeprefix("https://").removesuffix("/")
print(simple_url)
print(f"Simplified Google URL is: {simple_url}")