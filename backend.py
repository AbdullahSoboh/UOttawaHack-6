import random

# Define drivers and days
drivers = ["Driver A", "Driver B", "Driver C", "Driver D", "Driver E"]
days = ["Day 1", "Day 2", "Day 3", "Day 4", "Day 5"]
speed_limits = [50, 70, 90, 110, 130]  # Possible speed limits

# Function to generate simulated driving data
def generate_simulated_data(drivers, days):
    data = {}
    for driver in drivers:
        driver_data = {}
        for day in days:
            average_speed = random.uniform(30, 130)
            speed_limit = random.choice(speed_limits)
            acceleration_force = round(random.uniform(-9.8, 3), 2)
            driver_data[day] = {
                "average_speed": round(average_speed, 2),
                "speed_limit": speed_limit,
                "acceleration_force": acceleration_force
            }
        data[driver] = driver_data
    return data

# Function to process and categorize the data
def process_data(data):
    for driver, driver_data in data.items():
        for day, stats in driver_data.items():
            speed_deviation = ((stats["average_speed"] - stats["speed_limit"]) / stats["speed_limit"]) * 100
            acceleration_category = "Unsafe" if abs(stats["acceleration_force"]) > 0.2 else "Optimal"
            stats["speed_deviation"] = round(speed_deviation, 2)
            stats["acceleration_category"] = acceleration_category

# Main function to run the simulation and processing
def main():
    simulated_data = generate_simulated_data(drivers, days)
    process_data(simulated_data)
    # Output processed data for verification or further use
    for driver, driver_data in simulated_data.items():
        print(f"{driver}:")
        for day, stats in driver_data.items():
            print(f"  {day}: {stats}")
        print()

if __name__ == "__main__":
    main()
