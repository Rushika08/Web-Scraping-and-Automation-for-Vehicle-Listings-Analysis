# Import necessary libraries
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas as pd
import os
import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

# Set up the browser
driver = webdriver.Chrome()

# Initialize lists to store values
years = []
mileages = []
locations = []
prices = []

# Iterate through the first two pages
for page in range(1, 4):
    # Navigate to ikman.lk search results page
    url = f"https://ikman.lk/en/ads/sri-lanka/motorbikes?query=CT-100&page={page}"
    driver.get(url)

    # Wait for the page to load
    driver.implicitly_wait(10)

    # Parse HTML content with BeautifulSoup
    soup = BeautifulSoup(driver.page_source, "html.parser")

    # Extract information for each listing
    for listing in soup.find_all('li', class_='normal--2QYVk gtm-normal-ad'):
        year = listing.find('h2', class_='heading--2eONR heading-2--1OnX8 title--3yncE block--3v-Ow').get_text().split()[-1]
        location = listing.find('div', class_='description--2-ez3').text.split(', ')[0]
        details_div = listing.find('div', class_='content--3JNQz')
        div_element = details_div.find('div')
        mileage = div_element.find('div').get_text().split()[0]
        price = listing.find('div', class_='price--3SnqI').span.text.split()[1]

        # Append values to respective lists
        years.append(year)
        mileages.append(mileage)
        locations.append(location)
        prices.append(price)

# Keeping the first 50 elements only
years = years[:50]
mileages = mileages[:50]
locations = locations[:50]
prices = prices[:50]

# Close the browser
driver.quit()

# Sample code to save data into CSV
data = {"Location": locations, "Price": prices, "Year of Manufacture": years, "Mileage": mileages}

df = pd.DataFrame(data)
df.index += 1
df.to_csv("CT-100_ikman_results.csv", index_label="Row No")

# Print the path where the CSV file has been stored
csv_path = os.path.abspath("ikman_results.csv")
print(f"CSV file has been saved at: {csv_path}\n")

df["Price"] = df["Price"].str.replace(",", "").astype(float)

# Group data by location and calculate average price
average_price_by_location = df.groupby("Location")["Price"].mean().round(2)

# Convert the average prices to a formatted string for email body
formatted_prices = average_price_by_location.to_string(header=False)


# Function to send email with analysis report
def send_email(sender_email, receiver_email, password, average_price_by_location, csv_filename="CT-100_ikman_results.csv"):
    # Checking whether the inputs are correctly provided
    if sender_email == " " or receiver_email == " " or password == " ":
        print("Email credentials cannot be empty. Please provide valid email addresses and password.")
        sys.exit()
     
    # Create the email content
    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = receiver_email
    msg["Subject"] = "Ikman.lk CT-100 Motorcycle Listings Analysis Report"

    # Include the average prices in the email body
    email_body = f"Average Vehicle Price by Location:\n\n{formatted_prices}"
    msg.attach(MIMEText(email_body, "plain"))

    # Attach the CSV file
    with open(csv_filename, "rb") as file:
        attachment = MIMEApplication(file.read(), _subtype="csv")
        attachment.add_header("Content-Disposition", "attachment", filename=csv_filename)
        msg.attach(attachment)

    # Send the email
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")


# Replace these values with necessary information
sender_email = " "
receiver_email = " "
password = " "


# Call the function with the necessary parameters
send_email(sender_email, receiver_email, password, average_price_by_location)
