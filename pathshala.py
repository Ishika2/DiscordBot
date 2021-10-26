import discord
from discord import guild
from discord import channel
import discord.ext.commands as cmds
import os
from discord.ext.commands import bot
from discord.ext.commands.help import HelpCommand
from discord.flags import Intents
import dotenv

dotenv.load_dotenv()

intents = discord.Intents.default()
intents.members = True

client = cmds.Bot(command_prefix = '!32', intents = intents)
client.remove_command("help") # help_commands=None)  #change prefix to !32

#assign v32 role to students; role id = 899119393982783569

TOKEN = os.getenv('DISCORD_TOKEN')

# client = discord.Client()


# client = cmds.Bot(command_prefix = '.') #, intents = intent, HelpCommand = None)

# client = cmds.Bot(command_prefix = '.', Intents = intent)

# client.intents.all()

course = ['UG','PG','D']

UG = ['CSAI','CSE','ECAI','ECE','IT','MAE','EEE','CE']
PG = ['PD','AE','CH','CE','EE','ME','ED','MV','ER','QT','RAS','AI','CS','CP']
D = ['BE','CHE','CHEM','CE','AI','RAS','CS','CP','CG','CC','VLSI','EV','DES']

@client.event
async def on_ready():
    print("Online")
    print(client.user.name)
    print(client.user.id)
    print(".......")

@client.event
async def on_member_join(member):
    await member.send(f"{member.name.mention} Welcome to the Server!\n Type '!32help' to know bot commands")
  #  await channel1.send(f"{member.name} Welcome to the Server!\n Type '!32help' to know bot commands")


@client.event
async def on_message(message): #,ctx,user:discord.Member, role:discord.Role):
    #print(discord.Member.name)
    m = message.content.split('-')
    print(m)
    if(len(m) > 1):
        m[0] = int(m[0])
        if (m[0] >= 0 and m[0] <= 999) and (m[1] in course) and (m[2] in (UG or PG or D)):
            print("Success!")
            user = message.author
            print("Member: ", user)
            rl = discord.utils.get(message.guild.roles, name = "v32")
            await user.add_roles(rl)
            await message.channel.send(f"Well done! {user.mention} is verified and has been assigned {rl.mention} role successfully!")
        else:
            await message.channel.send("Oops! Wrong Admission Number Entered!")
    await client.process_commands(message)

@client.command()
async def help(ctx):
  #user = ctx.message.author.name
    #await ctx.channel.send("Working")
    embeding = discord.Embed(title = "HOW TO USE?", color = discord.Color.blue(), description = "My Username: Ishika Punchariya#2102")
    embeding.set_author(name = "Ishika Punchariya", url = "https://www.linkedin.com/in/ishika-punchariya-7a286121b", icon_url = ctx.author.avatar_url)  #"https://images.immediate.co.uk/remote/images.atlas.metabroadcast.com/pressassociation.com/webANXspongebob.jpg?quality=90&webp=true&resize=650,366"
    embeding.set_thumbnail(url = "https://e7.pngegg.com/pngimages/107/601/png-clipart-discord-logo-online-chat-computer-icons-web-browser-discord-thinking-text-logo-thumbnail.png")
    embeding.add_field(name = "Type your addmission number in the following format:", value = "Three-digit roll number-UG/PG/D-Branch-Year of graduation", inline = False)
    await ctx.channel.send(embed = embeding)

client.run(TOKEN)