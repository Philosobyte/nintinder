from nintinder.models import Interest, Game
from django.contrib.auth.models import User

userIDObj = User.objects.get(username='mememeister')
Interest.objects.create(id = 'dc6d358c-7d9a-4e64-9ec2-5b042071169c', game = Game.objects.get(id='42880d2a-af71-416f-90ba-fae0ef52f0ff'), user = userIDObj);
Interest.objects.create(id = 'e6a77eb3-c676-45ed-8a0e-e9ccfd01648e', game = Game.objects.get(id='c52cfb32-3042-4fc3-9d78-6a93328b8317'), user = userIDObj);
Interest.objects.create(id = 'b90abeac-b97a-4938-87d5-98c73dd1c73f', game = Game.objects.get(id='acd664fd-1c56-4a8e-b09f-62ae88236325'), user = userIDObj);

userIDObj = User.objects.get(username='dbzhang')
Interest.objects.create(id = '67f8cac2-87d0-49f4-869a-d3178445a72c', game = Game.objects.get(id='d94e2cbe-ab78-4762-95c8-5a4adfd8cd68'), user = userIDObj);

userIDObj = User.objects.get(username='Philosobyte')
Interest.objects.create(id = 'ec33b2d3-bfe1-4105-8900-1789054a5a66', game = Game.objects.get(id='42880d2a-af71-416f-90ba-fae0ef52f0ff'), user = userIDObj);
Interest.objects.create(id = '9d455eaa-4feb-4ff4-b078-af54f45c189f', game = Game.objects.get(id='c52cfb32-3042-4fc3-9d78-6a93328b8317'), user = userIDObj);

userIDObj = User.objects.get(username='Glass')
Interest.objects.create(id = 'ef3bc548-e283-4436-9adb-5879f7a15a8a', game = Game.objects.get(id='54fa90b3-729b-4766-ad69-125a40d3cf74'), user = userIDObj);

userIDObj = User.objects.get(username='kp4life')
Interest.objects.create(id = 'ce1b3d2d-004f-453e-94c8-b1a7b5c2ec8f', game = Game.objects.get(id='acd664fd-1c56-4a8e-b09f-62ae88236325'), user = userIDObj);
Interest.objects.create(id = '36856653-31c7-41bc-be3a-818870461e89', game = Game.objects.get(id='8285b3a8-847d-485d-8202-7d893c85cb22'), user = userIDObj);

userIDObj = User.objects.get(username='dangerouswoman')
Interest.objects.create(id = 'da69d3da-9ee4-4e7e-aa3e-ac0a852534a5', game = Game.objects.get(id='79da553b-3c15-4dc5-a07f-146097304b54'), user = userIDObj);

userIDObj = User.objects.get(username='nickiminaj')
Interest.objects.create(id = '37fc6fd8-efb6-4f6f-a550-c52ce2011a44', game = Game.objects.get(id='a3b0a58c-010b-4076-8b00-313e537013ad'), user = userIDObj);
Interest.objects.create(id = '47f7f3ed-0f3e-4766-980e-99cba1ad806a', game = Game.objects.get(id='94f53507-184d-4d15-849e-814f90864e9a'), user = userIDObj);
Interest.objects.create(id = 'c787e0b6-7807-4766-a138-62b4cf9fc5c5', game = Game.objects.get(id='8c8b100e-4367-4ae3-b6e1-63a892a62e48'), user = userIDObj);

userIDObj = User.objects.get(username='sarahlynn3')
Interest.objects.create(id = '781189c0-70b4-4064-8c10-aaf80f5f3e2f', game = Game.objects.get(id='2d9c199e-e854-441f-ab30-cce96c48f303'), user = userIDObj);
Interest.objects.create(id = '41ba9faf-6e8b-4402-b829-7457af72dcac', game = Game.objects.get(id='8621e3e9-c60b-40f6-a47d-a68902c70d41'), user = userIDObj);

userIDObj = User.objects.get(username='xman')
Interest.objects.create(id = '360fb769-06fe-4929-b19d-3c1ee72a1733', game = Game.objects.get(id='4f2af043-d511-452f-a350-a6ea37571df6'), user = userIDObj);
