from datetime import datetime
from django.utils import timezone
from nintinder.models import Game
from nintinder.models import Event
from nintinder.models import User
from nintinder.models import Participant
import uuid

start_2018 = datetime(2018, 3, 30, 16, 30, 1, tzinfo=timezone.utc)
end_2018 = datetime(2018, 3, 30, 21, 30, 1, tzinfo=timezone.utc)
eventIDObj = Event.objects.get(id='e8b83077d06e48eb82903e1c5a122787')
userIDObj = User.objects.get(id='6d55e696-acdc-49a7-9f40-e386d2d9a2f1')
Participant.objects.create(id = uuid.uuid4(), event = eventIDObj, user = userIDObj, start_time = start_2018, end_time = end_2018)

start_2018 = datetime(2018, 4, 30, 16, 30, 1, tzinfo=timezone.utc)
end_2018 = datetime(2018, 4, 30, 21, 30, 1, tzinfo=timezone.utc)
eventIDObj = Event.objects.get(id='aa259b37e2674ab09b6bbdde3350bc4f')
userIDObj = User.objects.get(id='8290ff1c-a5ac-461c-bebe-1dd23006632a')
Participant.objects.create(id = uuid.uuid4(), event = eventIDObj, user = userIDObj, start_time = start_2018, end_time = end_2018)

start_2018 = datetime(2018, 3, 03, 15, 30, 1, tzinfo=timezone.utc)
end_2018 = datetime(2018, 3, 03, 20, 30, 1, tzinfo=timezone.utc)
eventIDObj = Event.objects.get(id='52b111955c2b4ef5ba1569a08b6b3faf')
userIDObj = User.objects.get(id='8290ff1c-a5ac-461c-bebe-1dd23006632a')
Participant.objects.create(id = uuid.uuid4(), event = eventIDObj, user = userIDObj, start_time = start_2018, end_time = end_2018)

start_2018 = datetime(2018, 5, 23, 18, 30, 1, tzinfo=timezone.utc)
end_2018 = datetime(2018, 5, 23, 21, 30, 1, tzinfo=timezone.utc)
eventIDObj = Event.objects.get(id='52608ad5061f4e0e98b5bfa0abbf4781')
userIDObj = User.objects.get(id='36d16720-81b7-43c6-9573-d4b8a1d215f3')
Participant.objects.create(id = uuid.uuid4(), event = eventIDObj, user = userIDObj, start_time = start_2018, end_time = end_2018)

start_2018 = datetime(2018, 4, 15, 17, 30, 1, tzinfo=timezone.utc)
end_2018 = datetime(2018, 4, 15, 21, 30, 1, tzinfo=timezone.utc)
eventIDObj = Event.objects.get(id='6502f1d13eca4a2f818072249c8df2ae')
userIDObj = User.objects.get(id='36d16720-81b7-43c6-9573-d4b8a1d215f3')
Participant.objects.create(id = uuid.uuid4(), event = eventIDObj, user = userIDObj, start_time = start_2018, end_time = end_2018)

start_2018 = datetime(2018, 7, 12, 16, 30, 1, tzinfo=timezone.utc)
end_2018 = datetime(2018, 7, 12, 21, 30, 1, tzinfo=timezone.utc)
eventIDObj = Event.objects.get(id='23e3c0760db14f92a096eb1733bc49c2')
userIDObj = User.objects.get(id='60228da7-1c28-4645-a333-8acbd905f3c9')
Participant.objects.create(id = uuid.uuid4(), event = eventIDObj, user = userIDObj, start_time = start_2018, end_time = end_2018)