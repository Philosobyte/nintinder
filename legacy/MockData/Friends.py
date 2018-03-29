from datetime import datetime
from django.utils import timezone
from nintinder.models import User
from nintinder.models import Friend
import uuid

friendAIDObj = User.objects.get(id='6d55e696-acdc-49a7-9f40-e386d2d9a2f1')
friendBIDObj = User.objects.get(id='36d16720-81b7-43c6-9573-d4b8a1d215f3')
Friend.objects.create(id = uuid.uuid4(), friendA = friendAIDObj, friendB = friendBIDObj, status = 0)

friendAIDObj = User.objects.get(id='6d55e696-acdc-49a7-9f40-e386d2d9a2f1')
friendBIDObj = User.objects.get(id='8290ff1c-a5ac-461c-bebe-1dd23006632a')
Friend.objects.create(id = uuid.uuid4(), friendA = friendAIDObj, friendB = friendBIDObj, status = 1)

friendAIDObj = User.objects.get(id='8290ff1c-a5ac-461c-bebe-1dd23006632a')
friendBIDObj = User.objects.get(id='36d16720-81b7-43c6-9573-d4b8a1d215f3')
Friend.objects.create(id = uuid.uuid4(), friendA = friendAIDObj, friendB = friendBIDObj, status = 2)

friendAIDObj = User.objects.get(id='6d55e696-acdc-49a7-9f40-e386d2d9a2f1')
friendBIDObj = User.objects.get(id='360228da7-1c28-4645-a333-8acbd905f3c9')
Friend.objects.create(id = uuid.uuid4(), friendA = friendAIDObj, friendB = friendBIDObj, status = 1)

friendAIDObj = User.objects.get(id='8290ff1c-a5ac-461c-bebe-1dd23006632a')
friendBIDObj = User.objects.get(id='60228da7-1c28-4645-a333-8acbd905f3c9')
Friend.objects.create(id = uuid.uuid4(), friendA = friendAIDObj, friendB = friendBIDObj, status = 2)

friendAIDObj = User.objects.get(id='8290ff1c-a5ac-461c-bebe-1dd23006632a')
friendBIDObj = User.objects.get(id='360228da7-1c28-4645-a333-8acbd905f3c9')
Friend.objects.create(id = uuid.uuid4(), friendA = friendAIDObj, friendB = friendBIDObj, status = 3)

friendAIDObj = User.objects.get(id='af9e7b7b-c901-4b93-9adb-e84a392eef73')
friendBIDObj = User.objects.get(id='360228da7-1c28-4645-a333-8acbd905f3c9')
Friend.objects.create(id = uuid.uuid4(), friendA = friendAIDObj, friendB = friendBIDObj, status = 2)

friendAIDObj = User.objects.get(id='af9e7b7b-c901-4b93-9adb-e84a392eef73')
friendBIDObj = User.objects.get(id='e58f9032-364e-4b7d-95b6-1943efeb81c4')
Friend.objects.create(id = uuid.uuid4(), friendA = friendAIDObj, friendB = friendBIDObj, status = 3)

friendAIDObj = User.objects.get(id='8290ff1c-a5ac-461c-bebe-1dd23006632a')
friendBIDObj = User.objects.get(id='76e19198-853f-4b92-ad27-8acbc70f07a9')
Friend.objects.create(id = uuid.uuid4(), friendA = friendAIDObj, friendB = friendBIDObj, status = 2)