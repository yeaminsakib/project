from datetime import datetime, timedelta

# Function to generate 1026 timestamps with continuous dates and incrementing times
def generate_dates(start_date, num_dates):
    dates = []
    current_date = start_date

    # Loop over to generate the requested number of dates and times
    for i in range(num_dates):
        # Format time to match the pattern, hours and minutes increment based on the loop
        hours = i % 24  # Loop through 24 hours
        minutes = i % 60  # Loop through 60 minutes
        
        # Format date and time into a single string in DD/MM/YYYY HH:MM format
        timestamp = current_date.replace(hour=hours, minute=minutes)
        dates.append(timestamp.strftime("%d/%m/%Y %H:%M"))

        # Once the hour reaches 23:59, increment the date
        if hours == 23 and minutes == 59:
            current_date += timedelta(days=1)

    return dates

# Starting date (01/01/2025)
start_date = datetime(2025, 1, 1)

# Generate 1026 timestamps
updated_dates = generate_dates(start_date, 1026)

# Save the output to a file
output_filename = "date.txt"

with open(output_filename, 'w') as file:
    for date in updated_dates:
        file.write(date + '\n')

print(f"Dates saved to {output_filename}")
