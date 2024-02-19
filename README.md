# 1. Purpose:

The purpose of this program is to scrape motorcycle listings from “ikman.lk”, analyze the data, and send an email with an analysis report containing average prices by location.

# 2. Functionalities:
### a. Web Scraping:
- The program is using Selenium and BeautifulSoup for web scraping.

### b. Data Processing:
- Extracted data includes year of manufacture, mileage, location, and price for each motorcycle.
- Only the first 50 listings are considered to avoid excessive data.

### c. Data Storage:
- The program saves the extracted data into a CSV file named "CT-100_ikman_results.csv".
- The CSV file includes columns for Location, Price, Year of Manufacture, and Mileage.

### d. Data Analysis:
- Calculates the average price for motorcycles in each location.
- The analysis is based on the first 50 listings.

### e. Email Functionality:
- A function is implemented to send an email with the analysis report.
- The email includes the average prices by location in the body.
- Attaches the CSV file to the email for detailed reference.


# 3. Non-Functional Features:
### a. Security:
- The email credentials (sender's email and password) are securely handled.

### b. Usability:
- The program provides informative console outputs, including the path where the CSV file is saved and successful messages after the email is sent.
- Error messages are clear and concise.

### c. Reliability:
- Implemented error handling to gracefully manage potential issues during web scraping, data processing, or email sending.

### d. Scalability:
- The program is able to handle a larger number of listings or pages if needed in the future.


# 4. Installation and Execution:
### a. Required Libraries:
- Install the necessary libraries using the following command:
"pip install beautifulsoup4 selenium pandas"

### b. WebDriver:
- Download the Chrome WebDriver from https://www.google.com/chrome/ and ensure it's in your system PATH.

### c. Replace Email Credentials:
- Open the script in a text editor.
- Replace the placeholder values for "sender_email", "receiver_email", and "password" with your own email credentials.

### d. Run the Code:
- Execute the Python script containing the provided code.
"python script_name.py"
