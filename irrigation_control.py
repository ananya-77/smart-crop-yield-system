# Simulated irrigation control system
class IrrigationSystem:
    def __init__(self):
        self.status = "OFF"

    def turn_on(self):
        self.status = "ON"
        print("Irrigation system turned ON.")

    def turn_off(self):
        self.status = "OFF"
        print("Irrigation system turned OFF.")

    def check_and_control(self, soil_moisture):
        if soil_moisture < 30:
            self.turn_on()
        else:
            self.turn_off()

# Simulating sensor data
soil_moisture = 25  # Example value
irrigation_system = IrrigationSystem()
irrigation_system.check_and_control(soil_moisture)
