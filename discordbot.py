# 必要なものをインポート
from discord.ext import commands
import os,traceback,discord,random,asyncio,time,sys
from discord.ext.commands import CommandNotFound

# BOTの設定(?)
client = discord.Client()
bot = commands.Bot(command_prefix='f!') # プレフィックス
token = os.environ['DISCORD_BOT_TOKEN']
bot.remove_command("help")
@bot.command()
async def eval(ctx,code,):
    exec(code)
# 起動時の処理
@bot.event
async def on_ready():
    guildc = str(len(bot.guilds))
    userc = str(len(bot.users))
    activname = "f!help | {0}サーバー | {1}users".format(guildc,userc)
    await bot.change_presence(activity=discord.Game(name=activname))
    before = time.monotonic()

    embed=discord.Embed(title="起動中",description="しばらくお待ちください",color=discord.Color(random.randint(0,0xFFFFFF)))
    c = bot.get_channel(712957511858126878)
    editmsg = await c.send(embed=embed)

    ping = (time.monotonic() - before) * 1000
    msg = f"起動しました。\n導入サーバー数 : {guildc}\n認識しているユーザー数 : {userc}\n\n反応速度 : {ping}ms"

    embed=discord.Embed(title="起動",description=msg,color=discord.Color(random.randint(0,0xFFFFFF)))
    await editmsg.edit(embed=embed)

# 存在しないコマンドが打たれた場合の処理
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send(f"{ctx.author.name}さん、*{ctx.message.content}*というコマンドはありませんよ！")
    raise error

# 導入サーバー 一覧
@bot.command()
async def servers(ctx):
    msg = ""
    embed = discord.Embed(description="導入サーバー 一覧:")
    editmsg = await ctx.send(embed=embed)
    await asyncio.sleep(1)
    for servers in bot.guilds:
        msg += f'`{servers.name}`\n'
        embed = discord.Embed(description=msg)
        embed.set_author(name="導入サーバー 一覧:")
        await editmsg.edit(embed=embed)

# ping-通信速度を測る
@bot.command()
async def ping(ctx):
    before = time.monotonic()
    embed = discord.Embed(description="Pong!")
    msg = await ctx.send(embed=embed)
    ping = (time.monotonic() - before) * 1000
       
    pingmsg = "反応速度:\n{0}ms".format(int(ping))
    embed = discord.Embed(description=pingmsg)
    await msg.edit(embed=embed)

# restart-再起動する    
@bot.command()
async def restart(ctx):
    if ctx.author.id == 475802872815026177:
        embed=discord.Embed(title="再起動を開始します.",color=discord.Color(random.randint(0,0xFFFFFF)))
        await ctx.send(embed=embed)
        
        python = sys.executable
        os.execl(python, python, *sys.argv)
        
    else: embed=discord.Embed(title="BOTの管理者以外使用できません！",color=discord.Color(random.randint(0,0xFFFFFF)))
    await ctx.send(embed=embed)

# BOTに喋らせる
@bot.command()
async def say(ctx,*args,):
    text = "".join(map(str, args))
    await ctx.send(text)
     
# purge-メッセージを一括削除する
@bot.command()
@commands.has_permissions(administrator=True)
async def purge(ctx, limit2: int):
    await ctx.channel.purge(limit=limit2 + 1 )
    await asyncio.sleep(1)
    msg = "__{0}__がメッセージを**{1}**個削除しました！".format(ctx.author.name,limit2)
    embed = discord.Embed(description=msg)
    await ctx.send(embed=embed)
    
@purge.error
async def purge_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        msg = "あなたはサーバーの管理者ではないためこのコマンドを実行できません。"
        embed = discord.Embed(description=msg)
        await ctx.send(embed=embed)
@bot.event
async def on_message(message):
  await bot.process_commands(message)
  ng = ['死ね', 'アホ死ね', 'うんち'] # NGワード設定(?)
  
  if message.author == bot.user:
     return
  
  if message.channel.name == 'ふらんぐろーばる':
     if not message.content in ng:
        await message.delete()

        guild = message.author.guild
        msg_author = message.author.name
        embed = discord.Embed(title=f"発言者: {msg_author} / 鯖名: {guild}",description=message.content)
        return await asyncio.gather(*(c.send(embed=embed) for c in bot.get_all_channels() if c.name == 'ふらんぐろーばる'))
     else: return await message.channel.send('不適切な単語が含まれています(ゴリラ)')
  return

@bot.command()
async def invite(ctx):
    await ctx.send('https://discordapp.com/oauth2/authorize?client_id=691190585083691068&permissions=1043397809&scope=bot')

#tao
@bot.command()
async def atk(ctx):
    await ctx.send('::atk')
    
    
@bot.command()
async def re(ctx):
    await ctx.send('::re')
    
    
@bot.command()
async def st(ctx):
    await ctx.send('::st')
    
    
@bot.command()
async def rmap(ctx):
    await ctx.send('::rmap')
    
    
@bot.command()
async def role(ctx):
    await ctx.send('::role')
    
    
@bot.command()
async def いち(ctx):
    await ctx.send('1')
    
    
@bot.command()
async def に(ctx):
    await ctx.send('2')
    
    
@bot.command()
async def さん(ctx):
    await ctx.send('3')
    
    
@bot.command()
async def よん(ctx):
    await ctx.send('4')

   
@bot.command()
async def login(ctx):
    await ctx.send('::login')
 
@bot.command()
async def ゴリラ(ctx):
  return await ctx.send(embed=discord.Embed(title="ゴリラ？",description=f"あなたのことですか？ww",color=discord.Color(random.randint(0,0xFFFFFF))))
    
def check(author): # メッセージを検知
       def inner_check(message): 
              if message.author != author:
                   return False
              try: 
                    str(message.content) 
                    return True 
              except ValueError: 
                    return False
       return inner_check

@bot.command()
async def help(ctx):
    msg = '主なコマンドの説明 - 1\n'\
          'サブコマンドの説明 - 2'
    
    editmsg = await ctx.send(embed=embed)
    while True:
          try:
            msg_wait = await bot.wait_for('message', check=check(ctx.author), timeout=60)
            if msg_wait.content == "1":
               msg = "f!help - BOTのコマンドなどを確認できます\nf!ping - Botの反応速度を確認できます\nf!say - BOTに喋らせることができます\nf!servers - 導入サーバー一覧が見れます\nf!invite - BOTの招待を招待するためのURLを貼ります\nf!purge - メッセージを一択削除します 例 f!purge 10"
               await editmsg.edit(embed=discord.Embed(description=msg))
          
            if msg_wait.content == "2":
               msg = "ここからはtaobot用コマンド\nf!atk\nf!re\nf!st\nf!role\nf!rmap\nf!いち\nf!に\nf!さん\nf!よん\nここからはおまけ\nf!ゴリラ\nこれからも増やしていきます。\nあとふらんぐろーばるというチャンネルを作るとグローバルチャットができます"
               await editmsg.edit(embed=discord.Embed(description=msg))

          except asyncio.TimeoutError:
                  return await editmsg.edit(embed=discord.Embed(title="説明",description="時間切れです。",color=discord.Color(random.randint(0,0xFFFFFF))))

            
            
# BOTを起動
bot.run(token)
