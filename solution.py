def minimum_runtime(battery_capacity, initial_battery, tasks, charge_rate):
    battery = float(initial_battery)
    total_time = 0.0

    for duration, drain_rate in tasks:
        required = duration * drain_rate

        # Impossible if task needs more battery than capacity
        if required > battery_capacity:
            return -1

        # Charge if needed
        if battery < required:
            needed = required - battery
            idle_time = needed / charge_rate

            total_time += idle_time
            battery += needed

            if battery > battery_capacity:
                battery = battery_capacity

        # Execute task
        total_time += duration
        battery -= required

    return round(total_time, 1)


# Example Test
if __name__ == "__main__":
    battery_capacity = 100
    initial_battery = 50
    tasks = [
        [10, 4],   # consumes 40
        [5, 8]     # consumes 40
    ]
    charge_rate = 2

    print(minimum_runtime(
        battery_capacity,
        initial_battery,
        tasks,
        charge_rate
    ))
