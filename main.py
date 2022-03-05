import keep_alive
import discord
from discord.ext import commands, tasks
import os
import time
import random
import asyncio

intents = discord.Intents.default()
intents.members=True
intents.invites=True

token=os.environ['token']

client=commands.Bot(command_prefix='=', intents=intents, pass_context=True)
client.remove_command('help')
ownerid=904682505104396329
officials=0
initiates=0
ally=0
welcomemsg="""**CONGRATS! (userhere)** We are pleased to welcome you as the newest member of __**Phantom Guild**__! <a:02Welcome:726382805214298143><a:01Welcome:726382816526598175>


*As you will notice, we members of the **PHG** have a family like atmosphere. You can speak and express yourself openly in the event of any problem and don't even be shy about it! Improvements and innovative ideas are always open and accepted. We hope you'll find staying here in our guild fun and rewarding!* <a:pepemusic:724969694075027506>

*To become an official, you must have "PHG" as your in-game prefix and your melee level must be at least 90.* <:emoji_161:939972830286708746>

***Goodluck and Godbless to you!*** <a:KirbyDance:723761655095230594>"""

@tasks.loop(minutes=5)
async def activity():
    for guild in client.guilds:
        if guild.id==672453244336734208:
            for member in guild.members:
                official_role=guild.get_role(927134963122470943)
                officials=len(official_role.members)
                initiate_role=guild.get_role(698500328169013258)
                initiates=len(initiate_role.members)
                await client.change_presence(activity = discord.Streaming(url="https://twitch.tv/#", name=f"with {initiates+officials} PHGs"))

@client.event
async def on_ready():
    keep_alive.keep_alive()
    activity.start()
    os.system('clear')
    print(f"Connected to {client.user}")
    # with open('invites.json', 'w+') as e:
        # for g in client.guilds:
            # if g.id==672453244336734208:
                # invites={}
                # for inv in (await g.invites()):
                    # invites[inv.code]=[inv.inviter.id, inv.uses]
                # json.dump(invites, e)
                # break

# @client.event
# async def on_invite_create(invite):
    # for g in client.guilds:
        # if g.id==672453244336734208:
            # mainserver=g
    # for g in client.guilds:
        # if g.id==672453244336734208:
            # for channel in g.channels:
                # if channel.id==927140051350061116:
                    # invite_logs=channel
    # if invite.max_uses==1:
        # try:
            # inviter=invite.inviter
            # await invite.delete()
            # await invite_logs.send(f'{inviter.mention} - Your invite has been deleted, you have to create an invite with more than 1 uses')
        # except Exception:
            # pass
    # else:  
            # for inv in (await mainserver.invites()):
                # if inv.inviter==invite.inviter:
                    # if inv==invite:
                        # pass
                    # else:
                        # await invite_logs.send(f'{inv.inviter.mention} - Your previous invite code `{inv.code}` is deleted')
                        # await inv.delete()
            
            # invites=await mainserver.invites()
            # em=discord.Embed(title="Invite Logger", description=f"New invite code `{invite.code}` created by {invite.inviter.mention} (<t:{int(datetime.timestamp(invite.created_at))}:R>)", colour=discord.Colour.blue())
            # age=invite.max_age
            # if age==0:
                # age="Never"
            # elif age!=0 and age<=1800:
                # age="30 Minutes"
            # elif age>1800 and age<=3600:
                # age="1 Hour"
            # elif age>3600 and age<=21600:
                # age="6 Hours"
            # elif age>21600 and age<=43200:
                # age="12 Hours"
            # elif age>43200 and age<=86400:
                # age="1 Day"
            # elif age>86400 and age<=604800:
                # age="7 Days"
            # if invite.max_uses==0:
                # max_uses="Infinite"
            # else:
                # max_uses=invite.max_uses
            # em.add_field(name="Max uses", value=f"`{max_uses}`", inline= True)
            # em.add_field(name="Expiry", value=f"`{age}`", inline= True)
            # em.add_field(name="Temporary", value=f"`{invite.temporary}`", inline= True)
            # em.add_field(name="Target channel", value=f"`{invite.channel.name}`", inline= True)
            # em.set_author(name=invite.inviter.name, icon_url=invite.inviter.avatar_url_as(format='png'))
            # await invite_logs.send(embed=em)
            # try:
                # invites={}
                # with open('invites.json', 'r+') as e:
                    # for f in (await mainserver.invites()):
                        # invites[f.code]=[f.inviter, f.uses]
                    # json.dump(invites ,e)
            # except Exception:
                # pass

# @client.event
# async def on_invite_delete(invite):
    # for g in client.guilds:
        # if g.id==672453244336734208:
            # mainserver=g
    # invites={}
    # for inv in (await mainserver.invites()):
        # invites[inv.code]=[inv.inviter.id, inv.uses]
    # with open('invites.json', 'w+') as e:
        # json.dump(invites, e)

# @client.event
# async def on_member_join(member):
    # for g in client.guilds:
        # if g.id==672453244336734208:
            # mainserver=g
    # for g in client.guilds:
        # if g.id==672453244336734208:
            # for channel in g.channels:
                # if channel.id==927140051350061116:
                    # invite_logs=channel
    # if member.bot:
        # return
    # else:
        # if (datetime.now() - member.created_at).total_seconds()<86400:
            # mention=True
        # else:
            # mention=False
        # temoinv=await mainserver.invites()
        # tempinv={}
        # for inv in temoinv:
            # tempinv[inv.code]=[inv.inviter.id, inv.uses]
        # with open('invites.json') as e:
            # invites=json.load(e)
        # if not len(tempinv.keys())==len(invites.keys()):
            # print(tempinv)
            # print(invites)
            # em=discord.Embed(title='Invite Logger', description=f'I cannot determine how `{member}` joined', colour=discord.Colour.red())
            # await invite_logs.send(embed=em)
        # else:
            # for invb in invites.keys():
                # for inva in tempinv.keys():
                    # if str(invb)==str(inva):
                        # if invites[invb][1]< tempinv[inva][1]:
                            # em=discord.Embed(name='Invite Logger', description=f'***`{member}`* was invited by <@{tempinv[inva][0]}>**', colour=discord.Colour.green())
                            # await invite_logs.send(embed=em)
                            # if mention:
                                # await invite_logs.send(f"⚠️ <@{tempinv[inva][0]}> `{member}`'s account is made less than a day ago")
                            # with open('invites.json', 'w+') as e:
                                # invites={}
                                # for inv in (await mainserver.invites()):
                                    # invites[inv.code]=[inv.inviter.id, inv.uses]
                                # json.dump(invites, e)

@client.event
async def on_message(msg):
    if msg.author==client.user:
        return
    if msg.channel.id==927140051350061116:
        await msg.delete()
    else:
        if msg.content.lower()=="blank" or msg.content==client.get_user(ownerid).mention:
            image=random.choice(['gd.gif', 'hd.gif', 'he.gif', 'an.gif', 'ap.gif'])
            file=discord.File("images/"+image, filename="Blank.gif")
            reply=random.choice(['Blan...you mean, Kami sama!? He gave me life 🥲', "You can't become cool like him 😏", 'I worship him every day 🙏', 'Call him Blank sama 🙂', "He resides in my aura 🥰", "No Blank, No life 😋"])
            em=discord.Embed(color=discord.Color.random()).set_image(url="attachment://Blank.gif")
            await msg.reply(content=reply,file=file, embed=em)
    
    await client.process_commands(msg)

@client.command(aliases=['tw', 'test', 'wt'])
async def testwelcome(ctx, user:discord.Member=None):
    if ctx.author.guild_permissions.manage_messages:
        await ctx.send(welcomemsg.replace("(userhere)", f"{user.mention}"))
            
@client.command()
async def members(ctx):
    official_role=ctx.guild.get_role(927134963122470943)
    officials=len(official_role.members)
    initiate_role=ctx.guild.get_role(698500328169013258)
    initiates=len(initiate_role.members)
    ally_role=ctx.guild.get_role(698504816858497066)
    ally=len(ally_role.members)
    others=(len(ctx.guild.members))-(officials+initiates+ally)
    em=discord.Embed(title="Phantom Guild Members", colour=discord.Colour.random())
    em.set_thumbnail(url="https://media.discordapp.net/attachments/810810787684941854/908067532206907432/PhantomGuildLogoNew.gif")
    em.add_field(name="**🧊 `Total Members`**", value=f"**{len(ctx.guild.members)} Members**", inline=False)
    em.add_field(name="**🧊 `Phantom Officials`**", value=f"**{officials} Officials**", inline=False)
    em.add_field(name="**🧊 `Phantom Initiates`**", value=f"**{initiates} Initiates**", inline=False)
    em.add_field(name="**🧊 `Allies`**", value=f"**{ally} Allies**", inline=False)
    em.add_field(name="**🧊 `Others`**", value=f"**{others} Others**", inline=False)
    await ctx.reply(embed=em)

@client.command()
async def promote(ctx, user:discord.Member=None):
    if ctx.author.guild_permissions.manage_messages:
        if user is None:
            m=await ctx.reply("You cannot promote an empty user bruh!")
            time.sleep(4)
            try:
                await ctx.message.delete()
            except Exception:
                pass
            try:
                await m.delete()
            except Exception:
                pass
        elif user.bot:
            m=await ctx.reply("I don't think bots are here to be an official member")
            time.sleep(4)
            try:
                await ctx.message.delete()
            except Exception:
                pass
            try:
                await m.delete()
            except Exception:
                pass
        
        elif user==ctx.author:
            m=await ctx.reply("Trying to be smart, \😏 huh??")
            time.sleep(4)
            try:
                await ctx.message.delete()
            except Exception:
                pass
            try:
                await m.delete()
            except Exception:
                pass
        else:
            if user.top_role > ctx.author.top_role or user.top_role==ctx.author.top_role:
                m=await ctx.reply("Bruh, you cannot promote someone who has same or higher role than you")
                time.sleep(4)
                try:
                    await ctx.message.delete()
                except Exception:
                    pass
                try:
                    await m.delete()
                except Exception:
                    pass
            else:
                initiate_role=ctx.guild.get_role(698500328169013258)
                if initiate_role in user.roles:
                    try:
                        await user.remove_roles(initiate_role)
                        official_role=ctx.guild.get_role(927134963122470943)
                        await user.add_roles(official_role)
                        try:
                            await user.send(f'You have been promoted in {ctx.guild.name}!')
                        except Exception:
                            pass
                        m=await ctx.reply("👍")
                        time.sleep(4)
                        try:
                            await ctx.message.delete()
                        except Exception:
                            pass
                        try:
                            await m.delete()
                        except Exception:
                            pass
                    except discord.Forbidden:
                        m=await ctx.reply("that person is a mod/admin")
                        time.sleep(4)
                        try:
                            await ctx.message.delete()
                        except Exception:
                            pass
                        try:
                            await m.delete()
                        except Exception:
                            pass
                else:
                        m=await ctx.reply(f"Cannot find initiate role in {user.name}'s roles!")
                        time.sleep(4)
                        try:
                            await ctx.message.delete()
                        except Exception:
                            pass
                        try:
                            await m.delete()
                        except Exception:
                            pass
    else:
        await ctx.message.add_reaction('❎')
        await ctx.reply("You don't have permissions to use this command, you can use **`=help`** to see the commands you can use!")
        try:
            await ctx.author.send('https://tenor.com/view/rick-roll-rick-ashley-never-gonna-give-you-up-gif-22113173')
        except Exception:
            pass

@client.command()
async def welcome(ctx, user:discord.Member=None):
    if ctx.author.guild_permissions.manage_messages or 711897508401381428 in [i.id for i in ctx.author.roles]:
        if user is None:
            m=await ctx.reply("Woah, how can you think of welcoming no one?")
            time.sleep(4)
            try:
                await ctx.message.delete()
            except Exception:
                pass
            try:
                await m.delete()
            except Exception:
                pass
        elif user.bot:
            m=await ctx.reply("Sorry but bots don't care even if you welcome them...")
            time.sleep(4)
            try:
                await ctx.message.delete()
            except Exception:
                pass
            try:
                await m.delete()
            except Exception:
                pass
        elif user==ctx.author:
            m=await ctx.reply("You cannot welcome yourself!")
            time.sleep(4)
            try:
                await ctx.message.delete()
            except Exception:
                pass
            try:
                await m.delete()
            except Exception:
                pass
        elif user.top_role >= ctx.author.top_role:
            m=await ctx.reply("Bruh, you cannot welcome someone who is already in such a high rank!")
            time.sleep(4)
            try:
                await ctx.message.delete()
            except Exception:
                pass
            try:
                await m.delete()
            except Exception:
                pass
        else:
            visitor_role=ctx.guild.get_role(698500675306258452)
            if visitor_role in user.roles:
                try:
                    await user.remove_roles(visitor_role)
                    initiate_role=ctx.guild.get_role(698500328169013258)
                    await user.add_roles(initiate_role)
                    try:
                        await user.send(f'Congratulations! You are now a member of {ctx.guild.name}!')
                    except Exception:
                        pass
                    guildchat=client.get_channel(927136976765878303)
                    try:
                        if not user.display_name.lower().startswith('phg') and not user.display_name.startswith('ᴾᴴᴳ'):
                            await user.edit(nick=f"PHG {user.display_name}")
                    except Exception:
                        pass
                    await guildchat.send(welcomemsg.replace("(userhere)", f"{user.mention}"))
                    
             
                    m=await ctx.reply(f"check {guildchat.mention}")
                    time.sleep(4)
                    try:
                        await ctx.message.delete()
                    except Exception:
                        pass
                    try:
                        await m.delete()
                    except Exception:
                        pass
                except Exception:
                    m=await ctx.reply("That user is a mod/admin")
                    time.sleep(4)
                    try:
                        await ctx.message.delete()
                    except Exception:
                        pass
                    try:
                        await m.delete()
                    except Exception:
                        pass
            else:
                m=await ctx.reply("User doesn't have visitor role")
                time.sleep(4)
                try:
                    await ctx.message.delete()
                except Exception:
                    pass
                try:
                    await m.delete()
                except Exception:
                    pass
    else:
        await ctx.message.add_reaction('❎')
        await ctx.reply("You don't have permissions to use this command, you can use **`=help`** to see the commands you can use!")
        try:
            await ctx.author.send('https://tenor.com/view/rick-roll-rick-ashley-never-gonna-give-you-up-gif-22113173')
        except Exception:
            pass
                    
@client.command()
async def say(ctx, *, text=None):
    if text is None:
        return
    if ctx.author.id==ownerid:
        try:
            await ctx.message.delete()
        except Exception:
            pass
        await ctx.channel.send(text.strip())
    else:
        await ctx.message.add_reaction('❎')
        await ctx.reply("You don't have permissions to use this command, you can use **`=help`** to see the commands you can use!")
        try:
            await ctx.author.send('https://tenor.com/view/rick-roll-rick-ashley-never-gonna-give-you-up-gif-22113173')
        except Exception:
            pass
            
@client.command()
async def reply(ctx, msgid: int=None, *, text=None):
    if msgid is None:
        return
    if ctx.author.id==ownerid:
        channel=ctx.channel
        try:
            msg=await channel.fetch_message(msgid)
        except Exception:
            await ctx.send(f'Message ID: `{msgid}` not found', delete_after=2.0)
        try:
            await ctx.message.delete()
        except Exception:
            pass
        await msg.reply(text.strip())
    else:
        await ctx.message.add_reaction('❎')
        await ctx.reply("You don't have permissions to use this command, you can use **`=help`** to see the commands you can use!")
        try:
            await ctx.author.send('https://tenor.com/view/rick-roll-rick-ashley-never-gonna-give-you-up-gif-22113173')
        except Exception:
            pass

@client.command()
async def help(ctx):
    em=discord.Embed(title="PHG Bot", colour=discord.Colour.random())
    em.add_field(name="🧊 **`members`**", value="**Sends the number of members, officials, initiates and allies in Phantom Guild**", inline=False)
    if ctx.author.guild_permissions.manage_messages:
        em.add_field(name="🧊 **`promote <user>`**", value="**Promotes a phantom initiate to an official (also DMs the user)**", inline=False)
    if ctx.author.guild_permissions.manage_messages or 711897508401381428 in [i.id for i in ctx.author.roles]:
        em.add_field(name="🧊 **`welcome <user>`**", value="**Send the welcome message and promote the user to initiate rank and removes the visitor role (also DMs the user)**", inline=False)
    if ctx.author.id==ownerid:
        em.add_field(name="🧊 **`say <message>`**", value="**Make the bot say something**", inline=False)
        em.add_field(name="🧊 **`reply <messageid> <message>`**", value="**Makes the bot reply to a message in the channel**", inline=False)
    if ctx.author.guild_permissions.manage_messages:
        em.add_field(name="🧊 **`testwelcome <user>`**", value="**Can be used to test the welcome message on any user (it will not give any roles)**", inline=False)
    em.add_field(name="🧊 **`about`**", value="**Info about bot**", inline=False)
    await ctx.author.send(embed=em)
    await ctx.message.add_reaction('☑️')
        
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.errors.MemberNotFound):
        await ctx.reply('Member not found! Probably they don\'t have view channel permission in this channel.', delete_after=2.0)
        await asyncio.sleep(2)
        try:
            await ctx.message.delete()
        except Exception:
            pass
    elif isinstance(error, discord.ext.commands.errors.CommandNotFound):
        await ctx.reply('Command not found! Use **=help** for list of commands', delete_after=2.0)
        await asyncio.sleep(2)
        try:
            await ctx.message.delete()
        except Exception:
            pass
    else:
        print(error)

@client.command()
async def about(ctx):
    owner=client.get_user(ownerid)
    if owner is None:
        em=discord.Embed(description=f"**PHG BOT | Made by Blank**", colour=discord.Colour.random())
    else:
        em=discord.Embed(description=f"***PHG BOT | Made by {owner.mention}***", colour=discord.Colour.random())
    await ctx.reply(embed=em)
    
client.run(token)
