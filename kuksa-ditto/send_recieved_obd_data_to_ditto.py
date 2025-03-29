import asyncio
from kuksa_client.grpc.aio import VSSClient
import time

# Asynchronous main function to connect to Kuksa Databroker and retrieve OBD data
async def main():

	# Establish an asynchronous connection to the Kuksa Databroker at the specified IP and port
	async with VSSClient('127.0.0.1' , 55555) as client:

    	# Repeat Infinitely
    	while True:
       	 
        	# Retrieve the current values of the specified OBD features from the Databroker
        	# using the 'get_current_values' function
        	values = await client.get_current_values([
            	'Vehicle.OBD.VehicleSpeed', 'Vehicle.OBD.CoolantTemperature' ,
            	'Vehicle.OBD.ThrottlePosition' , 'Vehicle.OBD.EngineSpeed'
        	])

        	# Extract the individual feature values from the retrieved data
        	VehicleSpeed = values['Vehicle.OBD.VehicleSpeed'].value
        	EngineSpeed = values['Vehicle.OBD.EngineSpeed'].value
        	ThrottlePosition = values['Vehicle.OBD.ThrottlePosition'].value
        	CoolantTemperature = values['Vehicle.OBD.CoolantTemperature'].value

        	# Print the value for each feature
        	print('VehicleSpeed = ' , VehicleSpeed)
        	print('EngineSpeed = ' , EngineSpeed)
        	print('ThrottlePosition = ' , ThrottlePosition)
        	print('coolantTemperature = ' , CoolantTemperature)

        	# Pause for 1 second
        	time.sleep(1)

        	print('-----------------------------')

# Run the asynchronous main function
asyncio.run(main())
