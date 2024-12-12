# Funcional Proxy Using Playwright. Might be slow at times as it comes under a non paid api

def fetch_proxy():
    with sync_playwright() as p:
        # Launch browser (headless=True or False, depending on your needs)
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        # Fetch the proxy data by sending an HTTP GET request
        response = page.request.get('https://gimmeproxy.com/api/getProxy')
        
        # Ensure the request was successful
        if response.status != 200:
            print("Failed to get proxy data.")
            return None

        # Parse the JSON response
        proxy_data = response.json()

        # Extract IP and Port from the response JSON
        proxy_ip = proxy_data.get('ip')
        proxy_port = proxy_data.get('port')


        if proxy_ip and proxy_port:
            browser.close()
            return f"http://{proxy_ip}:{proxy_port}"
        else:
            print("Proxy data is incomplete.")
            browser.close()
      
            
