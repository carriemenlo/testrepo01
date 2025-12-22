from datetime import datetime

# Get the current date and time
now = datetime.now()

# Format the time into a readable string
# %H:%M:%S represents Hours:Minutes:Seconds
current_time = now.strftime("%H:%M:%S")

print(f"The current time is: {current_time}")
