from channels.generic.websocket import AsyncJsonWebsocketConsumer
from currency.models import CurrencyFaits
from channels.db import database_sync_to_async
import json

class FaitsConsumer(AsyncJsonWebsocketConsumer):
	
	async def connect(self):
		self.groupname = "dashboard"
		await self.channel_layer.group_add(
			self.groupname,
			self.channel_name,
			)

		await self.accept()

	async def disconnect(self,close_code):
		pass
		#await self.disconnect()

	async def receive(self,text_data):
		print('>>>>>>',text_data)
		# datapoint = json.loads(text_data)
		# val = datapoint['value']

		await self.channel_layer.group_send(
			self.groupname,
			{
				'type': 'sendFaits',
				'value': text_data,
			}
		)

		pass
		
	async def sendFaits(self,event):
		valOther = event['value']
		await self.send(text_data=json.dumps({"NewFait":valOther}))

