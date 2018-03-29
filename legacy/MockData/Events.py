from datetime import datetime
from django.utils import timezone
from nintinder.models import Game
from nintinder.models import Event

start_2018 = datetime(2018, 3, 30, 16, 30, 1, tzinfo=timezone.utc)
end_2018 = datetime(2018, 3, 30, 21, 30, 1, tzinfo=timezone.utc)
gameIDObj = Game.objects.get(id='c464e2b5-eedf-488a-a53c-56fd067c0ee4')
Event.objects.create(id = 'e8b83077d06e48eb82903e1c5a122787', game = gameIDObj, start_time = start_2018, end_time = end_2018)

start_2018 = datetime(2018, 4, 30, 16, 30, 1, tzinfo=timezone.utc)
end_2018 = datetime(2018, 4, 30, 21, 30, 1, tzinfo=timezone.utc)
gameIDObj = Game.objects.get(id='a3b0a58c-010b-4076-8b00-313e537013ad')
Event.objects.create(id = 'aa259b37e2674ab09b6bbdde3350bc4f', game = gameIDObj, start_time = start_2018, end_time = end_2018)

start_2018 = datetime(2018, 3, 03, 15, 30, 1, tzinfo=timezone.utc)
end_2018 = datetime(2018, 3, 03, 20, 30, 1, tzinfo=timezone.utc)
gameIDObj = Game.objects.get(id='94f53507-184d-4d15-849e-814f90864e9a')
Event.objects.create(id = '52b111955c2b4ef5ba1569a08b6b3faf', game = gameIDObj, start_time = start_2018, end_time = end_2018)

start_2018 = datetime(2018, 5, 23, 18, 30, 1, tzinfo=timezone.utc)
end_2018 = datetime(2018, 5, 23, 21, 30, 1, tzinfo=timezone.utc)
gameIDObj = Game.objects.get(id='8c8b100e-4367-4ae3-b6e1-63a892a62e48')
Event.objects.create(id = '52608ad5061f4e0e98b5bfa0abbf4781', game = gameIDObj, start_time = start_2018, end_time = end_2018)

start_2018 = datetime(2018, 4, 15, 17, 30, 1, tzinfo=timezone.utc)
end_2018 = datetime(2018, 4, 15, 21, 30, 1, tzinfo=timezone.utc)
gameIDObj = Game.objects.get(id='42880d2a-af71-416f-90ba-fae0ef52f0ff')
Event.objects.create(id = '6502f1d13eca4a2f818072249c8df2ae', game = gameIDObj, start_time = start_2018, end_time = end_2018)

start_2018 = datetime(2018, 7, 12, 16, 30, 1, tzinfo=timezone.utc)
end_2018 = datetime(2018, 7, 12, 21, 30, 1, tzinfo=timezone.utc)
gameIDObj = Game.objects.get(id='c52cfb32-3042-4fc3-9d78-6a93328b8317')
Event.objects.create(id = '23e3c0760db14f92a096eb1733bc49c2', game = gameIDObj, start_time = start_2018, end_time = end_2018)