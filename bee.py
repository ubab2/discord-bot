import discord
import os
client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("bee ready")
    game = discord.Game("ㅠ.ㅠ")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith(".야! 꿀벌"):
        await message.channel.send("왜~~!!")

    if message.content.startswith("!수학"):
        await message.channel.send("https://hoc39.ebssw.kr/jyh1541/hmpg/hmpgAlctcrDetailView.do?menuSn=344031&alctcrSn=172070")
    if message.content.startswith("!영어"):
        await message.channel.send("https://hoc39.ebssw.kr/wonjueng/hmpg/hmpgAlctcrDetailView.do?menuSn=348377&alctcrSn=158650")
    if message.content.startswith("!과학"):
        await message.channel.send("https://hoc39.ebssw.kr/whs11/hmpg/hmpgAlctcrDetailView.do?menuSn=385700&alctcrSn=172241")
    if message.content.startswith("!정보"):
        await message.channel.send("https://hoc39.ebssw.kr/jungbowjg/hmpg/hmpgAlctcrDetailView.do?menuSn=391168&alctcrSn=170004")
    if message.content.startswith("!체육"):
        await message.channel.send("https://hoc39.ebssw.kr/wonjugope/hmpg/hmpgAlctcrDetailView.do?menuSn=381867&alctcrSn=170738")
    if message.content.startswith("!한국사"):
        await message.channel.send("https://hoc39.ebssw.kr/wonjugohistory/hmpg/hmpgAlctcrDetailView.do?menuSn=383426&alctcrSn=171966")
    if message.content.startswith("!진로"):
        await message.channel.send("https://hoc39.ebssw.kr/urasil/hmpg/hmpgAlctcrDetailView.do?menuSn=385886&alctcrSn=179578")
    if message.content.startswith("!미술"):
        await message.channel.send("https://hoc39.ebssw.kr/miso0414/hmpg/hmpgAlctcrDetailView.do?menuSn=387657&alctcrSn=177340")
    if message.content.startswith("!사회"):
        await message.channel.send("https://hoc39.ebssw.kr/wonjugotongsa/hmpg/hmpgAlctcrDetailView.do?menuSn=382318&alctcrSn=177262")
    if message.content.startswith("!실험"):
        await message.channel.send("https://hoc39.ebssw.kr/kwh111/hmpg/hmpgAlctcrDetailView.do?menuSn=386226&alctcrSn=176390")
    if message.content.startswith("!국어"):
        await message.channel.send("https://hoc39.ebssw.kr/wongo1korean/hmpg/hmpgAlctcrDetailView.do?menuSn=385257&alctcrSn=176456")

        
access_token = os.environ["BOT_TOKEN"]
client.run(access_token)
