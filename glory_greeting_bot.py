import asyncio
import discord
import logging

client = discord.Client()

#token
token = 'Your Token'

#봇 구동
@client.event
async def on_ready():
    logging.info("Logged in as")
    logging.info("bot name : %s", client.user.name)
    logging.info("bot id : %s", client.user.id)
    
    #봇 상태 출력
    await client.change_presence(game=discord.Game(name='인사', type=1))

@client.event
async def on_member_join(member):
    fmt = '''
    {1.name}에 오신걸 환영합니다! {0.mention}님!
1. 간단하게 자기소개 해주세요!
Ex)나이/성별/별명/접속시간대/접률(일주일에접속횟수)등
2. 닉네임은 저희랑 맞춰서 바꿔주시면 감사하겠습니다!
3. 공지사항 한번씩 읽어주시는 것을 권장합니다!'''
    channel = member.server.get_channel('Your Channel ID')
    await client.send_message(channel, fmt.format(member, member.server))

@client.event
async def on_member_remove(member):
    channel = member.server.get_channel('Your Channel ID')
    fmt = '{0.mention}님이 서버에서 나가셨습니다!'
    await client.send_message(channel, fmt.format(member, member.server))

client.run(token)