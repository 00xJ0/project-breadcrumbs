import pandas as pd
import numpy as np
import random

# Number of records
num_records = 2000

# Device Types (Initial Inquiry)
device_types = ["Phone", "Tablet", "Smart Watch"]

# Initial Issue Categories (Expanded)
inquiry_categories = ["Cracked Screen", "Software Issue", "Network Issue", "Phone Setup/Restore", "Battery Problem", "Connectivity Issue", "Warranty Claim", "Slow Performance", "App Issue", "Other"]

# Secondary Device Types
secondary_device_types = [
    "Laptop", "Gaming System", "Smart Headphones", "Desktop", "Smart TV",
    "Smart Thermostat", "Smart Security Camera", "Printer", "Fitness Tracker", "Smart Speaker", "Sound Bar"
]

# Probing Questions/Statements (Refined)
probing_questions = [
    "While we're discussing your {initial_device}, have you had any issues with other tech in your home?",
    "Are you aware that HomeTech Protection can cover all your smart devices, from laptops to gaming consoles?",
    "Have you tried other products from X brand?",  # Replace X with brand
    "Besides yourself, what would be your most important piece of technology in your home?",
    "Many of our customers protect all their devices under one plan. Would you be interested in learning more about HomeTech Protection?",
    "Are you aware we offer comprehensive coverage for multiple devices in your home with HomeTech Protection?",
    "Protecting all your devices can save you a lot of money in the long run. Would you like to explore HomeTech Protection?",
    "What other tech do you have at home that you'd want protected?",
    "Our HomeTech Protection plan covers all your home tech. It's very cost-effective. Have you heard about it?",
    "Thinking about your tech at home, what's the one device you'd be most upset to lose or have damaged?",
    "Do you have any smart home devices, like a smart thermostat or security system?",
    "A lot of people are now working from home, do you have a home office setup with a computer or printer?",
    "Do you stream movies or play games at home? We can protect your Smart TV and gaming consoles too.",
    "Do you use smart headphones or a smart speaker? HomeTech Protection can cover those as well.",
    "Are you worried about accidental damage to your laptop or desktop? We can protect those under HomeTech Protection.",
    "Do you have a printer at home? Printers can be expensive to replace, and HomeTech Protection can cover them.",
    "HomeTech Protection can cover all your smart devices, including fitness trackers. It's a great way to protect your investment.",
    "With so many smart devices in a home these days, it makes sense to have one plan to cover them all. Have you considered HomeTech Protection?"
]

def generate_secondary_devices():
    num_secondary = random.randint(0, len(secondary_device_types))
    if num_secondary == 0:  # If no devices are chosen, explicitly return "None"
        return "None"
    else:
        owned_secondary = random.sample(secondary_device_types, num_secondary)
        return ", ".join(owned_secondary)

def choose_breadcrumb(initial_device, secondary_devices, probing_questions):
    if secondary_devices != "None":  # Check if secondary_devices is NOT "None"
        if "Laptop" in secondary_devices and "Gaming System" in secondary_devices:
            return random.choice([
                "I see you have a laptop and a gaming system. HomeTech Protection covers all your devices, even high-value ones like those. Would you be interested in learning more?",
                "With a laptop and a gaming system, you've got a great setup. HomeTech Protection can keep it all protected. Want to learn more?"
            ])
        elif "Smart TV" in secondary_devices:
            return random.choice([
                "Many of our customers bundle their Smart TVs with their other devices for complete home tech protection. It's very affordable. Would you like to explore that option?",
                "Protecting your Smart TV can be expensive. HomeTech Protection offers great coverage for entertainment devices. Interested?"
            ])
        elif "Printer" in secondary_devices and "Desktop" in secondary_devices:
            return random.choice([
                "With a desktop and printer, you've got a home office setup. HomeTech Protection can cover all your work-from-home tech. It's a great way to safeguard your productivity. Have you heard about it?",
                "Having a reliable home office is important. HomeTech Protection can cover your desktop and printer, giving you peace of mind. Want to learn more?"
            ])
        elif initial_device == "Smart Watch" and "Fitness Tracker" in secondary_devices:
            return random.choice([
                "It looks like you're into wearable tech! HomeTech Protection can cover both your Smart Watch and Fitness Tracker, and all your other devices too. Want to learn more?",
                "We can protect all your wearable tech, including your Smart Watch and Fitness Tracker, under one plan. It's very convenient. Interested?"
            ])
        elif initial_device == "Phone" and any(device in secondary_devices for device in ["Smart Speaker", "Sound Bar"]):
            return random.choice([
                "We can protect your phone and your smart speakers or sound bars at home under one plan. It's a really convenient way to go. What other devices do you have?",
                "HomeTech Protection covers your phone and your smart home audio too. It's a great way to protect your entertainment setup. Want to learn more?"
            ])
        elif "Smart Thermostat" in secondary_devices or "Smart Security Camera" in secondary_devices:
            return random.choice([
                "I see you have some smart home devices. HomeTech Protection can cover your smart thermostat and security cameras, along with all your other tech. Have you considered it?",
                "Protecting your smart home setup is important. HomeTech Protection offers comprehensive coverage for all your smart devices. Interested?"
            ])
        else:  # Generic
            return random.choice(probing_questions)  # Use any of the probing questions

    else:  # Default breadcrumbs (if no secondary devices are listed)
        return random.choice([
            "While we're discussing your {initial_device}, have you considered protecting it against accidental damage?",
            "We have affordable plans for your {initial_device}, would you be interested in learning more?"
        ])

# Create the DataFrame
data = []
for i in range(num_records):
    initial_device = random.choice(device_types)
    inquiry = random.choice(inquiry_categories)
    secondary_devices_owned = generate_secondary_devices()
    breadcrumb = choose_breadcrumb(initial_device, secondary_devices_owned, probing_questions)
    offer_presented = random.choice([True, False])
    offer_accepted = False
    if offer_presented:
        offer_accepted = np.random.choice([True, False], p=[0.3, 0.7])  # Adjust rate

    data.append([i, initial_device, inquiry, secondary_devices_owned, breadcrumb, offer_presented, offer_accepted])

df = pd.DataFrame(data, columns=["Customer ID", "Initial Device Inquiry", "Initial Issue Category", "Secondary Devices Owned", "Probing Question/Statement Used", "HomeTech Protection Offer Presented", "HomeTech Protection Offer Accepted"])

df.to_csv("home_tech_protection_data.csv", index=False)

print(df.head())
print("Data simulation complete. File saved as home_tech_protection_data.csv")