import random
import time
import asyncio
from kuksa_client.grpc.aio import VSSClient
from kuksa_client.grpc import Datapoint

# Asynchronous main function to connect to Kuksa Databroker and retrieve OBD data
______ def main():
    
	# Establish an asynchronous connection to the Kuksa Databroker at the IP: 127.0.0.1 and port 55555
	async with VSSClient('________' , ______) as client:

    	# Repeat Infinitely
    	while True:
        	# Generate random values for each feature with the defined ranges
        	VehicleSpeed = random.randint(0,255)
        	EngineSpeed = random.randint(0,1000)
        	ThrottlePosition = random.randint(0,200)
        	CoolantTemperature = random.randint(0,500)
        
        	# Send the generated values to the Kuksa Databroker with the
        	# corresponding vehicle data paths using the 'set_current_values' function
        	values = await client.___________({
            	'Vehicle.OBD.VehicleSpeed' : Datapoint(__________),
            	'Vehicle.OBD.CoolantTemperature': Datapoint(__________),
            	'Vehicle.OBD.ThrottlePosition':Datapoint(__________),
            	'Vehicle.OBD.EngineSpeed' : Datapoint(__________),
        	})

        	# Print the value for each feature
        	print('Vehicle Speed = ' , VehicleSpeed)
        	print('Engine Speed = ' , EngineSpeed)
        	print('Throttle Position = ' , ThrottlePosition)
        	print('coolant Temperature = ' , CoolantTemperature)

        	# Pause for 1 second
        	time.sleep(1)

        	print('-----------------------------')

# Run the main function
asyncio.run(main())
