from ast import Not
import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from channels.layers import get_channel_layer
from core.core_auth.models import CoreUser

from .models import Notification


@database_sync_to_async
def get_user(user_id):
    try:        
        return CoreUser.objects.get(id=user_id)
    except:
        print("Couldn't find user")

@database_sync_to_async
def get_notification(receiver):
    query = Notification.objects.filter(user_receiver=receiver).filter(status="unread")
    return("Query")

class NotificationConsumer(AsyncWebsocketConsumer):

    async def websocket_connect(self, event):
        # print(self.scope["url_route"]['kwargs']['client_id'])

        user_id = self.scope['user'].pk
        self.group_name = f"{user_id}"

        #Joining room group 
        await self.channel_layer.group_add(
            self.group_name,
            self.channel_name
        )

        await self.accept()
        
        self.send({
            "type": "websocket.send",
            "text":"room made"
        })

    # Receive message from WebSocket
    async def websocket_receive(self,event):
        print(">"*50)
        print(event)
        data_to_get = json.loads(event['text'])        
        user_to_get = await get_user(int(data_to_get))
        print(user_to_get)
        get_of = await get_notification(user_to_get)  
        print(get_of)      
        self.room_group_name=f"{data_to_get}"        
        channel_layer=get_channel_layer()
        await (channel_layer.group_send)(
            self.room_group_name, 
            {
                "type":"send_notification",
                "value":json.dumps(get_of)
            }
        )
        
    
    async def websocket_disconnect(self, event):
        # Leave room group
        await self.channel_layer.group_discard(
            self.group_name,
            self.channel_name
        )
        print('disconnect', event)
    
    async def send_notification(self, event):
        await self.send(json.dumps({
            "type": "websocket.send",
            "data": event
        }))
        print(' I am here ')
        print(event)

    


