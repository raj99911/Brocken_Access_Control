import json
from channels.generic.websocket import AsyncWebsocketConsumer

class PacketMonitorConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("packet_monitor", self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("packet_monitor", self.channel_name)

    async def send_packet(self, event):
        await self.send(text_data=json.dumps(event["packet"]))
