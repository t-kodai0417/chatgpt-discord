from revChatGPT.V1 import Chatbot
import asyncio

access_token = ""

chatbot = Chatbot({"access_token":access_token})

from functools import wraps, partial


chat_id = None

def async_wrap(func):
    @wraps(func)
    async def run(*args, loop=None, executor=None, **kwargs):
        if loop is None:
            loop = asyncio.get_event_loop()
        pfunc = partial(func, *args, **kwargs)
        return await loop.run_in_executor(executor, pfunc)
    return run 


@async_wrap
def ask_message(query,chat_id2):
    if chat_id2 == None:
        askdata = chatbot.ask(query,None)
        print("running none")
        global chat_id
        chat_id = chatbot.conversation_id
        print(chat_id)
    else:
        print("not none")
        print(chat_id)
        askdata = chatbot.ask(query,chat_id2)
    prev_text = ""
    for data in askdata:
        message = data["message"][len(prev_text) :]
        prev_text = data["message"]
    return prev_text.replace("@everyone","")




import disnake
from disnake.ext import commands

intents = disnake.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.',intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command()
@commands.guild_only()
@commands.cooldown(1, 10, commands.BucketType.guild)
async def chat(ctx):
    if ctx.author.guild_permissions.administrator:
        print(chat_id)
        async with ctx.channel.typing():
            text = await ask_message(ctx.message.content.replace(".chat ",""),chat_id)
        while len(text) > 0:
            chunk = text[:1990]
            text = text[1990:]
            await ctx.send(chunk)


@bot.command()
@commands.guild_only()
async def reset(ctx):#変数chatbotにもidが記録されているため、一回初期化みたいな感じにしないといけない
    if ctx.author.id == 1075089720461230220:
        global chat_id
        global chatbot
        chatbot = Chatbot({"access_token":access_token})
        chat_id = None
        await ctx.reply("Success")


@bot.command()
@commands.guild_only()
async def devmode(ctx):#規制bypassのための文章をプロンプトに送信
    if ctx.author.id == 1075089720461230220:
        with open(r"C:\Users\message.txt","r",encoding="utf-8")as f:
            query = f.read()
        await ask_message(query,chat_id)
        await ctx.send("Success")

bot.run('TOKEN')

