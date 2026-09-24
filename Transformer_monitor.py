import random
import time
from datetime import datetime

# Transformer ratings
RATED_VOLTAGE = 415.0       # Volts
RATED_CURRENT = 50.0        # Amps
MAX_TEMPERATURE = 85.0      # °C
WARNING_TEMPERATURE = 75.0   # °C

# Monitoring interval
INTERVAL = 5


def read_sensor_data():
    """
    Simulate transformer sensor readings.

    Replace this function with actual sensor readings
    when connecting hardware.
    """

    voltage = random.uniform(400, 430)
    current = random.uniform(10, 55)
    temperature = random.uniform(50, 90)

    return voltage, current, temperature


def calculate_load_percentage(current):
    """Calculate transformer loading percentage."""

    load_percentage = (current / RATED_CURRENT) * 100

    return load_percentage


def determine_health(voltage, current, temperature):
    """Determine transformer health status."""

    load_percentage = calculate_load_percentage(current)

    warnings = []

    if temperature >= MAX_TEMPERATURE:
        warnings.append("OVER TEMPERATURE")

    elif temperature >= WARNING_TEMPERATURE:
        warnings.append("HIGH TEMPERATURE")

    if voltage < RATED_VOLTAGE * 0.90:
        warnings.append("LOW VOLTAGE")

    elif voltage > RATED_VOLTAGE * 1.10:
        warnings.append("HIGH VOLTAGE")

    if load_percentage > 100:
        warnings.append("OVERLOAD")

    elif load_percentage > 90:
        warnings.append("HIGH LOAD")

    if not warnings:
        return "HEALTHY", []

    if "OVER TEMPERATURE" in warnings or "OVERLOAD" in warnings:
        return "CRITICAL", warnings

    return "WARNING", warnings


def calculate_apparent_power(voltage, current):
    """Calculate apparent power in kVA."""

    return (voltage * current) / 1000


def main():

    print("=" * 65)
    print("          TRANSFORMER HEALTH MONITORING SYSTEM")
    print("=" * 65)

    try:

        while True:

            voltage, current, temperature = read_sensor_data()

            load_percentage = calculate_load_percentage(current)

            apparent_power = calculate_apparent_power(
                voltage,
                current
            )

            health, warnings = determine_health(
                voltage,
                current,
                temperature
            )

            timestamp = datetime.now().strftime(
                "%Y-%m-%d %H:%M:%S"
            )

            print("\n--------------------------------------------")
            print(f"Time          : {timestamp}")
            print(f"Voltage       : {voltage:.2f} V")
            print(f"Current       : {current:.2f} A")
            print(f"Temperature   : {temperature:.2f} °C")
            print(f"Load          : {load_percentage:.2f}%")
            print(f"Power         : {apparent_power:.2f} kVA")
            print(f"Health Status : {health}")

            if warnings:
                print("Alerts        :")
                for warning in warnings:
                    print(f"  - {warning}")
            else:
                print("Alerts        : None")

            print("--------------------------------------------")

            time.sleep(INTERVAL)

    except KeyboardInterrupt:

        print("\nTransformer monitoring stopped.")


if __name__ == "__main__":
    main()
