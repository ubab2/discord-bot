import discord

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

    # if message.content.startswith("<고추>"):
    #     await message.channel.send("")

    # if message.content.startswith("거절"):
    #     await message.channel.send("거절은 안되")
    # if message.content.startswith("!수학"):
    #     await message.channel.send("https://hoc39.ebssw.kr/jyh1541/hmpg/hmpgAlctcrDetailView.do?menuSn=344031&alctcrSn=172070")
    # if message.content.startswith("!영어"):
    #     await message.channel.send("https://hoc39.ebssw.kr/wonjueng/hmpg/hmpgAlctcrDetailView.do?menuSn=348377&alctcrSn=158650")
    # if message.content.startswith("!과학"):
    #     await message.channel.send("https://hoc39.ebssw.kr/whs11/hmpg/hmpgAlctcrDetailView.do?menuSn=385700&alctcrSn=172241")
    # if message.content.startswith("!정보"):
    #     await message.channel.send("https://hoc39.ebssw.kr/jungbowjg/hmpg/hmpgAlctcrDetailView.do?menuSn=391168&alctcrSn=170004")
    # if message.content.startswith("!체육"):
    #     await message.channel.send("https://hoc39.ebssw.kr/wonjugope/hmpg/hmpgAlctcrDetailView.do?menuSn=381867&alctcrSn=170738")
    # if message.content.startswith("!한국사"):
    #     await message.channel.send("https://hoc39.ebssw.kr/wonjugohistory/hmpg/hmpgAlctcrDetailView.do?menuSn=383426&alctcrSn=171966")
    # if message.content.startswith("!진로"):
    #     await message.channel.send("https://hoc39.ebssw.kr/urasil/hmpg/hmpgAlctcrDetailView.do?menuSn=385886&alctcrSn=179578")
    # if message.content.startswith("!미술"):
    #     await message.channel.send("https://hoc39.ebssw.kr/miso0414/hmpg/hmpgAlctcrDetailView.do?menuSn=387657&alctcrSn=177340")
    # if message.content.startswith("!사회"):
    #     await message.channel.send("https://hoc39.ebssw.kr/wonjugotongsa/hmpg/hmpgAlctcrDetailView.do?menuSn=382318&alctcrSn=177262")
     # bee봇과 연쇄 작용
    if message.content.startswith("왜~~!!"):
        await message.channel.send("넣~을~께~~~")
    if message.content.startswith("!꿀벌"):
        await message.channel.send(".야! 꿀벌")


    if message.content.startswith("!야 꿀벌"):
        await message.channel.send("야 꿀벌 왜 울고 있는거야.... 소난다.........       넣을께~~")


    if message.content.startswith("!이~"):
        await message.channel.send("https://www.youtube.com/watch?v=q6EoRBvdVPQ")

    if message.content.startswith("!관짝"):
        await message.channel.send("https://www.youtube.com/watch?v=CAkLamTFDK4")


client.run("NzEwMjgzMDExMTk4ODEyMTgx.Xryn5w.DuTCHQvibWM1DoLnKQbw40NxSEk")