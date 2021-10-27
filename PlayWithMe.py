import discord
from discord import guild
from discord import channel
from discord import message
from discord import reaction
from discord.colour import Color
import discord.ext.commands as cmds
import os
from discord.ext.commands import bot
from discord.ext.commands.core import check
from discord.ext.commands.help import HelpCommand
from discord.flags import Intents
import dotenv
import random
import keep_alive

dotenv.load_dotenv()

intents = discord.Intents.default()
intents.members = True
intents.reactions = True

client = cmds.Bot(command_prefix = '~', intents = intents)
client.remove_command("help")

TOKEN = os.getenv('DIS_TOKEN')

BMDia_Movie = {"Parampara. Pratishtha. Anushasan. Yeh is gurukul ke teen stambh hai":"mohabbatein",
"Filmein Sirf Teen Cheezon Ki Wajah Se Chalti Hain … Entertainment, Entertainment, Entertainment … Aur Main Entertainment Hoon!":"the dirty picture",
"Tumse naa ho payega": "gangs of wasseypur",
"Uska toh na bad luck hi kharab hai":"rangeela",
"Adrak ho gaya hai yeh aadmi, kahi se bhi badh raha hai!":"tanu weds manu 2",}

BMDia_Artist = {"Mogambo Khush Hua":"amrish puri",
"How's the josh?!":"vicky kaushal",
"Tension lene ka nahi, sirf dene ka.":"sanjay dutt",
"Mere Karan Arjun Ayenge":"rakhee gulzar"}

BMSce = {"http://2.bp.blogspot.com/-aN-xYQOsq7o/VVKe-C4lf2I/AAAAAAAAAzU/ZvP9pAozv7Q/s320/G0629.jpg":"golmal",
"https://www.firstpost.com/wp-content/uploads/2015/06/maxresdefault2.jpg":"sholay",
"https://nettv4u.com/fileman/Uploads/Top-10-Bollywood-movies-for-the-wanderluster-in-you/YJHD_16_.jpg":"yeh jawaani hai deewani",
"https://i.pinimg.com/originals/46/1d/4f/461d4fdcb2e4f6cc6d0fa135f6917b2b.jpg":"phir hera pheri"}

Eng_wrd = {"GMEA":"GAME","MONTER":"MENTOR","NESBIGNRE":"BEGINNERS"}
Eng_sen = {"so / to / itchy / is / that / I / wait / My / off. / uniform / can’t / take / it":"My uniform is so itchy that I can’t wait to take it off.",
"want / Do / me / see / you / you / at / to / the / airport? / off":"Do you want me to see you off at the airport?",
"backwardness / wanted / immediately / cultural / Gandhiji / and / social / seeing / the / do / something /to":"Gandhiji immediately wanted to do something seeing the social and cultural backwardness."}
Eng_ant = {"Attack":"defend", "Marvelous":"terrible", "Tragic":"comic", "Partial":"complete", "Brave":"cowardly", "Arrogant":"humble", "Crazy":"sane", "Divide":"unite", "Timid":"bold"}
Eng_one = {"Study of Stars":"astronomy",
"The practice of writing dictionaries":"lexicography",
"A series of stars":"constellation",
"The one who does not believe in God.":"atheist",
"Someone who walks by foot.":"pedestrian",
"Something which can be copied":"immitable",
"Make someone feel young":"rejuvenate"}

Puzz_img = {"https://www.mathsisfun.com/puzzles/images/b-circles.gif":"I want to know how many of the circles you need to cover the whole square. Is 2 enough? Or do you need 3? Or 4? Or more?",
"https://i.stack.imgur.com/GZgel.png":"How many triangles are there in this diagram?"}

Puzz_ans = ['4','75']

Puzz = {"Find a 10-digit number where the first digit is how many zeros in the number, the second digit is how many 1s in the number etc. until the tenth digit which is how many 9s in the number.":"6210001000",  #number puzzle
"ABCD × E = DCBA \n (Replace letters with digits and have the answer be true. A,B,C,D and E are all different digits.) \n Answer format: same as equation.": "2178 × 4 = 8712",
"Two ladies played cards for candy; the winner received one piece per game from the loser. When it was time for one of the ladies to go home, one lady had won three games, while the other lady had a profit of three pieces of candy.\nHow many individual games had they played?":"9",
"What mathematical symbol can be put between 5 and 9, to get a number bigger than 5 and smaller than 9?":"'.' that is 5.9",
"You are in a dark room with a candle, a wood stove and a gas lamp. You only have one match, so what do you light first?":"match",
"What occurs once in every minute,\ntwice in every moment,\nbut never in a thousand years?":"The letter 'm'",
"1 is 3.\n3 is 5.\n5 is 4.\n4 is 4.\nWhat is 7?":"7 is 5.\nBecause 'seven' has 5 letters.",
"I’m tall when I’m young, and I’m short when I’m old. What am I?":"candle"}

SciTech = {"Which space agency has confirmed the presence of water on the surface of moon?":"nasa",
"Which social media giant has delayed the implementation of a new privacy policy by 3 months?":"whatsapp",
"Which tech major has announced the proprietary technology of charging multiple electronic devices in wireless mode?":"xiaomi",
"Which is the second largest part of the body in human beings?":"liver",
"What is the name of the first ‘Quantum Computer Simulator Toolkit’ of India?":"qsim",
"What is the name of NASA’s robotic spacecraft, launched to reach Jupiter’s asteroids, named the Trojans?":"lucy",
"Who invented telescope?":"hans lipperhey",
"What is the rarest blood type?":"ab-",
"This planet spins the fastest, completing one whole rotation in just 10 hours. Which planet is it?":"jupiter",
"How many hearts does an octopus have?":"3",
"True or false: your hair and your nails are made from the same material.":"true",
"Who directed Solo: A Star Wars Story?":"ron howard",
"Which author wrote the bestseller Jurassic Park which “hatched” into the successful film franchise?":"michael crichton",
"Published in 1895, who wrote The Time Machine?":"h.g. wells"}

wrong = ["https://www.scrolldroll.com/wp-content/uploads/2020/06/3-Idiots-Memes-Aise-do-words-hote-hi-nahi-hai.jpg",
"https://indianmemetemplates.com/wp-content/uploads/2019/01/rajus-home-768x343.jpg",
"https://i.pinimg.com/564x/1e/b1/bc/1eb1bc3055bdf79d674f09631a7fae4d.jpg",
"https://allmemetemplates.files.wordpress.com/2020/02/img_20200712_121339.jpg",
"https://humornama.com/wp-content/uploads/2021/01/Clear-Bol-Clear-Meme-Template-of-Tiwari-Seth-758x426.jpg",
"https://www.scrolldroll.com/wp-content/uploads/2020/04/Hera-Pheri-Memes-19.jpg",
"https://www.memestemplates.com/wp-content/uploads/2021/01/Disappointed-Cricket-Fan-14122020090952.jpg",
"https://pbs.twimg.com/media/EdNmAb5UcAIxHMp.jpg",
"https://i.pinimg.com/564x/ff/2a/9f/ff2a9f7e8fe52cc7a3c3c6d009ea267f.jpg",
"https://memegenerator.net/img/instances/71468293.jpg",
"https://memegenerator.net/img/instances/75664507.jpg"]

correct = ["https://allmemetemplates.files.wordpress.com/2020/02/img_20200712_121337.jpg",
"https://dontgetserious.com/wp-content/uploads/2021/01/Abhi-maza-ayega-na-bhidu-meme.jpg",
"https://www.memestemplates.com/wp-content/uploads/2020/06/aaaaahh-kadak-hai-1536x753.jpg",
"https://indianmemetemplates.com/wp-content/uploads/2019/01/salary-kitna-loge-discuss-karle-1-768x401.jpg",
"https://indianmemetemplates.com/wp-content/uploads/2019/02/bhaisahab-yeh-kis-line-mein-aa-gaye-aap-768x392.jpg",
"https://indianmemetemplates.com/wp-content/uploads/2019/03/miracle-miracle-768x361.jpg",
"https://indianmemetemplates.com/wp-content/uploads/2019/02/bhaisahab-yeh-kis-line-mein-aa-gaye-aap-768x392.jpg",
"https://c.tenor.com/lYx8DiK-dioAAAAM/waah-amir.gif",
"https://c.tenor.com/E6WSW38Kn94AAAAM/kbc-great.gif",
"https://c.tenor.com/uwpK6yZgT9MAAAAd/amitabh-bachchan-big-b.gif",
"https://media.makeameme.org/created/yes-you-got-572e7n.jpg"]

flag = 0

@client.event
async def on_ready():  #the bot is online for 1-2 mins always after use-->discord feature
    print("Online")
    print(client.user.name)
    print(client.user.id)
    print("............")


@client.event
async def on_raw_reaction_add(payload):
    # gld = client.get_guild(payload.guild_id)
    # player = discord.utils.get(guild.roles, name = "Player")
    # await payload.member
    msg = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
    # reaction = discord.utils.get(message.Emoji.name)
    score = 0
    reaction = payload.emoji.name
    # player = payload.member
    while(reaction == '1️⃣'):
        for i in BMDia_Movie:
            embd = discord.Embed(title = "Movie?", description = i)
            # embd.add_field(name = "Type:", value = "'next' to play more \n 'quit' to exit")
            await msg.channel.send(embed = embd)
            msg2 = await client.wait_for('message', check = check)
            print(msg2.content)
            if(msg2.content.lower() == BMDia_Movie[i]):
                score += 1
                # await msg2.channel.send("Great work!")
                embd1 = discord.Embed(title = "Great Work!")
                embd1.set_image(url = random.choice(correct))
                embd1.add_field(name = "Type:", value = "'next' to play more \n 'quit' to exit")
                await msg2.channel.send(embed = embd1)
                msg3 = await client.wait_for('message', check = check)
                if(msg3.content == "next"):
                    flag = 0
                    continue
                elif(msg3.content == "quit"):
                    flag = 1
                    break
            else:
                # await msg2.channel.send("Wrong answer, try next")
                embd1 = discord.Embed(title = "Wrong answer, try next!")
                embd1.add_field(name = "Type:", value = "'next' to play more \n 'quit' to exit")
                embd1.set_image(url = random.choice(wrong))
                await msg2.channel.send(embed = embd1)
                msg3 = await client.wait_for('message', check = check)
                if(msg3.content == "next"):
                    flag = 0
                    continue
                elif(msg3.content == "quit"):
                    flag = 1
                    break
        await msg.channel.send("Congo, done great!")
        await msg.channel.send(f"Your score is: {score}") 
        if(flag == 1):
            break
        for i in BMDia_Artist:
            embd = discord.Embed(title = "Delivered by?", description = i)
            # embd.add_field(name = "Type:", value = "'next' to play more \n 'quit' to exit")
            await msg.channel.send(embed = embd)
            msg2 = await client.wait_for('message', check = check)
            print(msg2.content)
            if(msg2.content.lower() == BMDia_Artist[i]):
                score += 1
                # await msg2.channel.send("Great work!")
                embd1 = discord.Embed(title = "Great Work!")
                embd1.add_field(name = "Type:", value = "'next' to play more \n 'quit' to exit")
                embd1.set_image(url = random.choice(correct))
                await msg2.channel.send(embed = embd1)
                msg3 = await client.wait_for('message', check = check)
                if(msg3.content == "next"):
                    flag = 0
                    continue
                elif(msg3.content == "quit"):
                    flag = 1
                    break
            else:
                # await msg2.channel.send("Wrong answer, try next")
                embd1 = discord.Embed(title = "Wrong answer, try next!")
                embd1.add_field(name = "Type:", value = "'next' to play more \n 'quit' to exit")
                embd1.set_image(url = random.choice(wrong))
                await msg2.channel.send(embed = embd1)
                msg3 = await client.wait_for('message', check = check)
                if(msg3.content == "next"):
                    flag = 0
                    continue
                elif(msg3.content == "quit"):
                    flag = 1
                    break
        await msg.channel.send("Congo, done great!")
        await msg.channel.send(f"Your score is: {score}")
        if(flag == 1):
            break
        for i in BMSce:
            embd = discord.Embed(title = "Movie?")
            embd.set_image(url = i)
            # embd.add_field(name = "Type:", value = "'next' to play more \n 'quit' to exit")
            await msg.channel.send(embed = embd)
            msg2 = await client.wait_for('message', check = check)
            print(msg2.content)
            if(msg2.content.lower() == BMSce[i]):
                score += 1
                # await msg2.channel.send("Great work!")
                embd1 = discord.Embed(title = "Great Work!")
                embd1.add_field(name = "Type:", value = "'next' to play more \n 'quit' to exit")
                embd1.set_image(url = random.choice(correct))
                await msg2.channel.send(embed = embd1)
                msg3 = await client.wait_for('message', check = check)
                if(msg3.content == "next"):
                    flag = 0
                    continue
                elif(msg3.content == "quit"):
                    flag = 1
                    break
            else:
                # await msg2.channel.send("Wrong answer, try next")
                embd1 = discord.Embed(title = "Wrong answer, try next!")
                embd1.add_field(name = "Type:", value = "'next' to play more \n 'quit' to exit")
                embd1.set_image(url = random.choice(wrong))
                await msg2.channel.send(embed = embd1)
                msg3 = await client.wait_for('message', check = check)
                if(msg3.content == "next"):
                    flag = 0
                    continue
                elif(msg3.content == "quit"):
                    flag = 1
                    break
        await msg.channel.send("Congo, done great!")
        await msg.channel.send(f"Your score is: {score}")
        if(flag == 1):
            break
    while(reaction == '2️⃣'):
        for i in Eng_wrd:
            embd = discord.Embed(title = "UNJUMBLE to find Meaningful Word", description = i)
            # embd.add_field(name = "Type:", value = "'next' to play more \n 'quit' to exit")
            await msg.channel.send(embed = embd)
            msg2 = await client.wait_for('message', check = check)
            print(msg2.content)
            if(msg2.content.upper() == Eng_wrd[i]):
                score += 1
                # await msg2.channel.send("Great work!")
                embd1 = discord.Embed(title = "Great Work!")
                embd1.set_image(url = random.choice(correct))
                embd1.add_field(name = "Type:", value = "'next' to play more \n 'quit' to exit")                
                await msg2.channel.send(embed = embd1)
                msg3 = await client.wait_for('message', check = check)
                if(msg3.content == "next"):
                    flag = 0
                    continue
                elif(msg3.content == "quit"):
                    flag = 1
                    break
            else:
                # await msg2.channel.send("Wrong answer, try next")
                embd1 = discord.Embed(title = "Wrong answer, try next!")
                embd1.add_field(name = "Type:", value = "'next' to play more \n 'quit' to exit")
                embd1.set_image(url = random.choice(wrong))
                await msg2.channel.send(embed = embd1)
                msg3 = await client.wait_for('message', check = check)
                if(msg3.content == "next"):
                    flag = 0
                    continue
                elif(msg3.content == "quit"):
                    flag = 1
                    break
        await msg.channel.send("Congo, done great!")
        await msg.channel.send(f"Your score is: {score}") 
        if(flag == 1):
            break
        for i in Eng_sen:
            embd = discord.Embed(title = "UNJUMBLE to find Meaningful Sentence", description = i)
            # embd.add_field(name = "Type:", value = "'next' to play more \n 'quit' to exit")
            await msg.channel.send(embed = embd)
            msg2 = await client.wait_for('message', check = check)
            print(msg2.content)
            if(msg2.content.lower() == Eng_sen[i]):
                score += 1
                # await msg2.channel.send("Great work!")
                embd1 = discord.Embed(title = "Great Work!")
                embd1.add_field(name = "Type:", value = "'next' to play more \n 'quit' to exit")
                embd1.set_image(url = random.choice(correct))
                await msg2.channel.send(embed = embd1)
                msg3 = await client.wait_for('message', check = check)
                if(msg3.content == "next"):
                    flag = 0
                    continue
                elif(msg3.content == "quit"):
                    flag = 1
                    break
            else:
                # await msg2.channel.send("Wrong answer, try next")
                embd1 = discord.Embed(title = "Wrong answer, try next!")
                embd1.add_field(name = "Type:", value = "'next' to play more \n 'quit' to exit")
                embd1.set_image(url = random.choice(wrong))
                await msg2.channel.send(embed = embd1)
                msg3 = await client.wait_for('message', check = check)
                if(msg3.content == "next"):
                    flag = 0
                    continue
                elif(msg3.content == "quit"):
                    flag = 1
                    break
        await msg.channel.send("Congo, done great!")
        await msg.channel.send(f"Your score is: {score}")
        if(flag == 1):
            break
        for i in Eng_ant:
            embd = discord.Embed(title = "ANTONYM?")
            await msg.channel.send(embed = embd)
            msg2 = await client.wait_for('message', check = check)
            print(msg2.content)
            if(msg2.content.lower() == Eng_ant[i]):
                score += 1
                # await msg2.channel.send("Great work!")
                embd1 = discord.Embed(title = "Great Work!")
                embd1.add_field(name = "Type:", value = "'next' to play more \n 'quit' to exit")
                embd1.set_image(url = random.choice(correct))
                await msg2.channel.send(embed = embd1)
                msg3 = await client.wait_for('message', check = check)
                if(msg3.content == "next"):
                    flag = 0
                    continue
                elif(msg3.content == "quit"):
                    flag = 1
                    break
            else:
                # await msg2.channel.send("Wrong answer, try next")
                embd1 = discord.Embed(title = "Wrong answer, try next!")
                embd1.add_field(name = "Type:", value = "'next' to play more \n 'quit' to exit")
                embd1.set_image(url = random.choice(wrong))
                await msg2.channel.send(embed = embd1)
                msg3 = await client.wait_for('message', check = check)
                if(msg3.content == "next"):
                    flag = 0
                    continue
                elif(msg3.content == "quit"):
                    flag = 1
                    break
        await msg.channel.send("Congo, done great!")
        await msg.channel.send(f"Your score is: {score}")
        if(flag == 1):
            break
        for i in Eng_one:
            embd = discord.Embed(title = "Give one word for...", description = i)
            # embd.add_field(name = "Type:", value = "'next' to play more \n 'quit' to exit")
            await msg.channel.send(embed = embd)
            msg2 = await client.wait_for('message', check = check)
            print(msg2.content)
            if(msg2.content.lower() == Eng_sen[i]):
                score += 1
                # await msg2.channel.send("Great work!")
                embd1 = discord.Embed(title = "Great Work!")
                embd1.add_field(name = "Type:", value = "'next' to play more \n 'quit' to exit")
                embd1.set_image(url = random.choice(correct))
                await msg2.channel.send(embed = embd1)
                msg3 = await client.wait_for('message', check = check)
                if(msg3.content == "next"):
                    flag = 0
                    continue
                elif(msg3.content == "quit"):
                    flag = 1
                    break
            else:
                # await msg2.channel.send("Wrong answer, try next")
                embd1 = discord.Embed(title = "Wrong answer, try next!")
                embd1.add_field(name = "Type:", value = "'next' to play more \n 'quit' to exit")
                embd1.set_image(url = random.choice(wrong))
                await msg2.channel.send(embed = embd1)
                msg3 = await client.wait_for('message', check = check)
                if(msg3.content == "next"):
                    flag = 0
                    continue
                elif(msg3.content == "quit"):
                    flag = 1
                    break
        await msg.channel.send("Congo, done great!")
        await msg.channel.send(f"Your score is: {score}")
        if(flag == 1):
            break
    while(reaction == '3️⃣'):
        for i in Puzz_img:
            embd = discord.Embed(title = "SHAPES", description = Puzz_img[i])
            embd.set_image(url = i)
            # embd.add_field(name = "Type:", value = "'next' to play more \n 'quit' to exit")
            await msg.channel.send(embed = embd)
            msg2 = await client.wait_for('message', check = check)
            print(msg2.content)
            if(msg2.content.lower() in Puzz_ans):
                score += 1
                # await msg2.channel.send("Great work!")
                embd1 = discord.Embed(title = "Great Work!")
                embd1.set_image(url = random.choice(correct))
                embd1.add_field(name = "Type:", value = "'next' to play more \n 'quit' to exit")
                await msg2.channel.send(embed = embd1)
                msg3 = await client.wait_for('message', check = check)
                if(msg3.content == "next"):
                    flag = 0
                    continue
                elif(msg3.content == "quit"):
                    flag = 1
                    break
            else:
                # await msg2.channel.send("Wrong answer, try next")
                embd1 = discord.Embed(title = "Wrong answer, try next!")
                embd1.add_field(name = "Type:", value = "'next' to play more \n 'quit' to exit")
                embd1.set_image(url = random.choice(wrong))
                await msg2.channel.send(embed = embd1)
                msg3 = await client.wait_for('message', check = check)
                if(msg3.content == "next"):
                    flag = 0
                    continue
                elif(msg3.content == "quit"):
                    flag = 1
                    break
        await msg.channel.send("Congo, done great!")
        await msg.channel.send(f"Your score is: {score}") 
        if(flag == 1):
            break
        for i in Puzz:
            embd = discord.Embed(title = "Tricky!", description = i)
            # embd.add_field(name = "Type:", value = "'next' to play more \n 'quit' to exit")
            await msg.channel.send(embed = embd)
            msg2 = await client.wait_for('message', check = check)
            print(msg2.content)
            if(msg2.content.lower() == Puzz[i]):
                score += 1
                # await msg2.channel.send("Great work!")
                embd1 = discord.Embed(title = "Great Work!")
                embd1.set_image(url = random.choice(correct))
                embd1.add_field(name = "Type:", value = "'next' to play more \n 'quit' to exit")
                await msg2.channel.send(embed = embd1)
                msg3 = await client.wait_for('message', check = check)
                if(msg3.content == "next"):
                    flag = 0
                    continue
                elif(msg3.content == "quit"):
                    flag = 1
                    break
            else:
                # await msg2.channel.send("Wrong answer, try next")
                embd1 = discord.Embed(title = "Wrong answer, try next!")
                embd1.add_field(name = "Type:", value = "'next' to play more \n 'quit' to exit")
                embd1.set_image(url = random.choice(wrong))
                await msg2.channel.send(embed = embd1)
                msg3 = await client.wait_for('message', check = check)
                if(msg3.content == "next"):
                    flag = 0
                    continue
                elif(msg3.content == "quit"):
                    flag = 1
                    break
        await msg.channel.send("Congo, done great!")
        await msg.channel.send(f"Your score is: {score}") 
        if(flag == 1):
            break
    while(reaction == '4️⃣'):
        for i in SciTech:
            embd = discord.Embed(title = "For Sci-Tech Freaks!", description = i)
            # embd.add_field(name = "Type:", value = "'next' to play more \n 'quit' to exit")
            await msg.channel.send(embed = embd)
            msg2 = await client.wait_for('message', check = check)
            print(msg2.content)
            if(msg2.content.lower() in list(SciTech.values())):
                score += 1
                # await msg2.channel.send("Great work!")
                embd1 = discord.Embed(title = "Great Work!")
                embd1.set_image(url = random.choice(correct))
                embd1.add_field(name = "Type:", value = "'next' to play more \n 'quit' to exit")
                await msg2.channel.send(embed = embd1)
                msg3 = await client.wait_for('message', check = check)
                if(msg3.content == "next"):
                    flag = 0
                    continue
                elif(msg3.content == "quit"):
                    flag = 1
                    break
            else:
                # await msg2.channel.send("Wrong answer, try next")
                embd1 = discord.Embed(title = "Wrong answer, try next!")
                embd1.add_field(name = "Type:", value = "'next' to play more \n 'quit' to exit")
                embd1.set_image(url = random.choice(wrong))
                await msg2.channel.send(embed = embd1)
                msg3 = await client.wait_for('message', check = check)
                if(msg3.content == "next"):
                    flag = 0
                    continue
                elif(msg3.content == "quit"):
                    flag = 1
                    break
        await msg.channel.send("Congo, done great!")
        await msg.channel.send(f"Your score is: {score}") 
        if(flag == 1):
            break
    
 
@client.command()
async def help(ctx):
    embdh = discord.Embed(title = "Hi, there!", description = "I'm here to give you guidlines about the amazing PlayWithMe discord bot")
    embdh.set_author(name = "Ishika Punchariya", icon_url = ctx.author.avatar_url)
    embdh.set_thumbnail(url = "https://st2.depositphotos.com/6367796/9368/v/950/depositphotos_93685540-stock-illustration-pop-art-comics-icon-help.jpg")
    embdh.add_field(name = "Instructions", value = "1. To get started type '~play'.\n2. React with the respective emoji to play the desired game.\n3. Answer the given question.\n4. If your answer is correct, you'll be rewarded 1 point, otherwise 0.\n5. For next question type 'next'.\n6. To end the game type 'quit'.\n7. To switch the genre, you need to first end the game then restart it by '~play'.")
    embdh.add_field(name = "Commands", value = "'~play' --> to start playing\n '~help' --> to get help and see instructions")
    await ctx.channel.send(embed = embdh)

@client.command()
async def play(ctx):
    emb = discord.Embed(title = "WHAT TO PLAY?", color = discord.Color.gold() , description = "1️⃣ Bollywood Mania \n\n 2️⃣ English-Vinglish \n\n 3️⃣ Puzzles \n\n 4️⃣ Science & Technology \n\n Add respective reaction to play...")
    # guils = client.get_guild(guild.utils.)
    await ctx.channel.send(embed = emb)

keep_alive.keep_alive()
client.run(TOKEN)