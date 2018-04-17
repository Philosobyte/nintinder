from nintinder.models import EarnedAchievement, Achievement
from django.contrib.auth.models import User

userIDObj = User.objects.get(username='mememeister')
EarnedAchievement.objects.create(id = '43f03deb-4e79-4a90-b783-6bf17fbf09c5', user = userIDObj, achievement = Achievement.objects.get(id='2d6b2f91-e15b-415f-8652-09d0b1cd9b71'));
EarnedAchievement.objects.create(id = 'b73bef17-264f-4349-a17e-80d6f5a4b9ee', user = userIDObj, achievement = Achievement.objects.get(id='8d762592-5665-41ad-b2b9-a511a821fa51'));
EarnedAchievement.objects.create(id = 'ff11ca20-c805-4f93-b65a-8fa78f658e07', user = userIDObj, achievement = Achievement.objects.get(id='9023ee64-7097-4dfd-abe2-67cf467292da'));

userIDObj = User.objects.get(username='dbzhang')
EarnedAchievement.objects.create(id = '1ed4f624-8999-46f5-9452-586003c4d033', user = userIDObj, achievement = Achievement.objects.get(id='881fb3ac-ee16-4ded-82ac-dae615687d6a'));
EarnedAchievement.objects.create(id = '794f9b24-1d0d-4052-9a8b-a7250df828af', user = userIDObj, achievement = Achievement.objects.get(id='bc14ce0c-5237-47ff-bc34-29d80dad2ff2'));

userIDObj = User.objects.get(username='Philosobyte')
EarnedAchievement.objects.create(id = '94a0991a-f003-4d4e-8da0-15345aa55cfc', user = userIDObj, achievement = Achievement.objects.get(id='8d762592-5665-41ad-b2b9-a511a821fa51'));

userIDObj = User.objects.get(username='kp4life')
EarnedAchievement.objects.create(id = '26edda37-bbed-4c97-bd90-1f5b4e46aef8', user = userIDObj, achievement = Achievement.objects.get(id='b5530ced-73ec-4687-a3b0-316c5082ac7c'));
EarnedAchievement.objects.create(id = '661533c0-4012-466e-99c4-2473844d402e', user = userIDObj, achievement = Achievement.objects.get(id='465246d7-8e64-454c-a0b5-13c5c8bdb037'));
EarnedAchievement.objects.create(id = '1a6fdab5-8163-4199-bb2a-58c13db5d107', user = userIDObj, achievement = Achievement.objects.get(id='c00f89bb-305a-4955-895e-de319a8912fa'));

userIDObj = User.objects.get(username='nickiminaj')
EarnedAchievement.objects.create(id = '5dc019c7-2455-4731-8a53-4e860d1d2600', user = userIDObj, achievement = Achievement.objects.get(id='34f7e14b-5e76-4994-b4cc-e6bdcf419cad'));
EarnedAchievement.objects.create(id = '705687a3-ff6f-476f-b5cc-b2f4403bd562', user = userIDObj, achievement = Achievement.objects.get(id='3eb8b2c6-1839-4453-a474-960f57cf5a39'));

userIDObj = User.objects.get(username='sarahlynn3')
EarnedAchievement.objects.create(id = '101f603e-467a-4714-9cff-6396ab4a6630', user = userIDObj, achievement = Achievement.objects.get(id='e117caa6-51ff-4c79-a709-20b5760b33c1'));
EarnedAchievement.objects.create(id = 'ab0c67b7-307e-4d49-a03d-d827a1aeb71e', user = userIDObj, achievement = Achievement.objects.get(id='27425025-2501-45c3-9cc0-e43c118e8077'));
EarnedAchievement.objects.create(id = 'dc4a5d3e-9cb4-4a12-9fdd-99fff0bb8228', user = userIDObj, achievement = Achievement.objects.get(id='dbc837cd-9636-4439-8a1f-a87dcd8e1b7e'));

userIDObj = User.objects.get(username='xman')
EarnedAchievement.objects.create(id = 'f40f706b-1e11-4d38-baca-1c52295ee9ee', user = userIDObj, achievement = Achievement.objects.get(id='24a18714-b700-48ef-8d48-12aef6cc973f'));
EarnedAchievement.objects.create(id = 'c3cbf2c9-723d-4f86-b444-13ab5b204b20', user = userIDObj, achievement = Achievement.objects.get(id='647a94e9-d05f-4b02-98a6-92932eed34fb'));
