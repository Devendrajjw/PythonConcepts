# Sample data representing racks and devices with their health status
racks = {
    'R1': {
        'D1': 'Good',
        'D2': 'Critical',
        'D3': 'Good'
    },
    'R2': {
        'D1': 'Critical',
        'D2': 'Good',
        'D3': 'Critical'
    },
    'R3': {
        'D1': 'Good',
        'D2': 'Good',
        'D3': 'Critical'
    }
}

def check_health_status(racks):
    good_devices = {}
    critical_devices = {}

    for rack, devices in racks.items():
        for device, status in devices.items():
            if status == 'Good':
                if rack not in good_devices:
                    good_devices[rack] = []
                good_devices[rack].append(device)
            elif status == 'Critical':
                if rack not in critical_devices:
                    critical_devices[rack] = []
                critical_devices[rack].append(device)

    return good_devices, critical_devices

# Get the health status of devices in each rack
good_devices, critical_devices = check_health_status(racks)

# Print the results
print("Good Devices:")
for rack, devices in good_devices.items():
    print(f"Rack {rack}: Devices {', '.join(devices)}")

print("\nCritical Devices:")
for rack, devices in critical_devices.items():
    print(f"Rack {rack}: Devices {', '.join(devices)}")



# Good Devices:
# Rack R1: Devices D1, D3
# Rack R2: Devices D2
# Rack R3: Devices D1, D2
#
# Critical Devices:
# Rack R1: Devices D2
# Rack R2: Devices D1, D3
# Rack R3: Devices D3
