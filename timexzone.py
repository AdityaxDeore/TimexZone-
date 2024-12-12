from datetime import datetime

def calculate_time_difference(country1, country2):
    
    utc_offsets = {
         "USA": -5,  # New York
        "India": 5.5,  # New Delhi
    "China": 8,  # Beijing
    "Japan": 9,  # Tokyo
    "UK": 0,  # London
    "Australia": 10,  # Sydney
    "Germany": 1,  # Berlin
    "France": 1,  # Paris
    "Canada": -5,  # Toronto
    "Brazil": -3,  # Brasília
    "Russia": 3,  # Moscow
    "South Africa": 2,  # Johannesburg
    "Mexico": -6,  # Mexico City
    "Italy": 1,  # Rome
    "Spain": 1,  # Madrid
    "Argentina": -3,  # Buenos Aires
    "New Zealand": 13,  # Wellington
    "South Korea": 9,  # Seoul
    "Netherlands": 1,  # Amsterdam
    "Sweden": 1,  # Stockholm
    "Turkey": 3,  # Istanbul
    "Egypt": 2,  # Cairo
    "Saudi Arabia": 3,  # Riyadh
    "Thailand": 7,  # Bangkok
    "Vietnam": 7,  # Hanoi
    "Philippines": 8,  # Manila
    "Singapore": 8,  # Singapore
    }

    offset1 = utc_offsets.get(country1)
    offset2 = utc_offsets.get(country2)

    if offset1 is None or offset2 is None:
        return None, None

    total_difference = offset2 - offset1
    hours = int(total_difference)
    minutes = int((total_difference - hours) * 60)

    return hours, minutes   


def main():
    country1 = input("Enter the first country: ")
    country2 = input("Enter the second country: ")

    hours, minutes = calculate_time_difference(country1, country2)

    # Determine the sign of the time difference
    sign = '+' if hours >= 0 else '-'
    
    print(f"The time difference between {country1} and {country2} is {sign}{abs(hours)} hours and {minutes} minutes.")

if __name__ == "__main__":
    main()