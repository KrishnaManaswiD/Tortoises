from tortoise import Tortoise
from enums import Direction, SensorType

Name=Tortoise()

while True:

    touchSensorValue = Name.getSensorData(SensorType.proximity, 1)

    if touchSensorValue == 1:

        print("Touch sensor is being pressed")
        Name.setLEDValue(1, 1)

    else:

        print("Nothing is pressing the touch sensor")
        Name.setLEDValue(1, 0)
