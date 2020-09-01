import discord
import os
client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("ubab ready")
    game = discord.Game(">.<")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("월요일 시간표"):
        await message.channel.send("체육 음악 정보 영어 지구과학 국어 창체")
    if message.content.startswith("!월시"):
        await message.channel.send("체육 음악 정보 영어 지구과학 국어 창체")

    if message.content.startswith("!화요일 시간표"):
        await message.channel.send("실험 사회 정보2 수학 한국사 영어")
    if message.content.startswith("!화시"):
        await message.channel.send("실험 사회 정보2 수학 한국사 영어")

    if message.content.startswith("!수요일 시간표"):
        await message.channel.send("국어 음악 영어 수학 창체")
    if message.content.startswith("!수시"):
        await message.channel.send("국어 음악 영어 수학 창체")

    if message.content.startswith("!목요일 시간표"):
        await message.channel.send("물리 국어 영어 한국사 수학 체육 사회")
    if message.content.startswith("!목시"):
        await message.channel.send("물리 국어 영어 한국사 수학 체육 사회")

    if message.content.startswith("!금요일 시간표"):
        await message.channel.send("수학 한국사 화학 사회 생물 진로 국어")
    if message.content.startswith("!금시"):
        await message.channel.send("수학 한국사 화학 사회 생물 진로 국어")

   

access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
