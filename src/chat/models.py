from django.db import models
from django.conf import settings
from core.utils.mixins.base import BaseMixin

class PublicChatRoom(BaseMixin):
    title = models.CharField(max_length=255, unique=True, blank=False)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, help_text="Usuários conectados ao chat")

    def __str__(self):
        return self.title

    def conect_user(self, user):
        '''
        return true if user is added to the users list
        '''
        is_user_added = False
        if not user in self.users.all():
            self.users.add(user)
            self.save()
            is_user_added = True
        elif user in self.users.all():  
            is_user_added = True
        return is_user_added


    def disconnect_user(self, user):
        '''
        return true if user is added to the users list
        '''
        is_user_removed = False
        if user in self.users.all():
            self.users.remove(user)
            self.save()
            is_user_removed = True
        return is_user_removed

    @property
    def group_name(self):
        """
        Return the channels group name that sockets should 
        subscribe to and get sent messages as they are generated
        """
        return f"PublicChatRoom-{self.id}"


class PublicRoomChatMessageManager(BaseMixin):
    def by_room(self, room):
        qs = PublicRoomChatMessage.objects.filter(room=room).order_by("-registration")
        return qs

    
class PublicRoomChatMessage(BaseMixin):
    """
    Chat message created by a user inside a PublicChatRoom (ForeignKey)
    """
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(PublicChatRoom, on_delete=models.CASCADE)
    content = models.TextField(unique=False, blank=False, max_length=5000)

    objects = PublicRoomChatMessageManager()    

    def __str__(self):
        return self.content
