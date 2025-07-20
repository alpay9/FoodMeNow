def scrape_restaurants_service(request):
    # There would be logic here to scrape restaurant
    print(f"Scraping started for {request.location} with filters: {request.filters}")
    # Start the scraping process, possibly triggering another service if needed
    return "Scraping started"
