import discord
from discord import player
from discord.channel import VoiceChannel
from discord.ext import commands
from discord.ext.commands.core import command
from discord import FFmpegPCMAudio



TOKEN = 'OTIwMTkzMDQ0NjgxMjA3ODA4.Ybgyjg.52r9t0JhsWfX-DA0O8BWbPPsczg'

client = discord.Client()

@client.event
async def on_ready():
    print('we have logged in as {0.user}' .format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author == client.user:
        return

    if message.channel.name == 'valo_bot' or message.channel.name == 'general-⌨' or message.channel.name == 'valbot':
        
        if user_message.lower() == 'hello':
            await message.channel.send(f'Hello {username}!')

            myEmbed = discord.Embed(title="User guide", description="The VALORANT encyclopedia", colour =0xFF0833)
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/e/e6/Site-logo.png/revision/latest?cb=20210620062038')
            myEmbed.add_field(name="For Agents",value="!(agent name)", inline=False)
            myEmbed.add_field(name="For Maps",value="!(map name)", inline=False)
            myEmbed.add_field(name="For Abilities",value="!(ability name)", inline=False)
            myEmbed.add_field(name="For Weapons",value="!(weapon name)", inline=False)
            myEmbed.add_field(name="Version",value="2.0", inline=False)
            myEmbed.set_image(url='https://media.giphy.com/media/sZ9LvwOqWkxaAOiS11/giphy.gif')

            await message.channel.send(embed=myEmbed)
            return

        elif user_message.lower() == 'thank muthu paandi' :
            await message.channel.send(f'PODA LSU')
            return    

        elif user_message.lower() == 'bye':
            await message.channel.send(f'GET LOST {username}!')
            return  







        elif user_message.lower() == '!brimstone':

            myEmbed = discord.Embed(title="Brimstone", description="ROLE: Controller", colour =0xFF6000)
            myEmbed.set_image(url='https://static.wikia.nocookie.net/valorant/images/3/37/Brimstone_artwork.png/revision/latest/scale-to-width-down/587?cb=20200602020239')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/e/e6/Site-logo.png/revision/latest?cb=20210620062038')
            myEmbed.add_field(name="Basic Abilities",value="Incendiary and Stim Beacon", inline=False)
            myEmbed.add_field(name="Signature Abilities",value="Sky Smoke(3)", inline=False)
            myEmbed.add_field(name="Ultimate Ability",value="Orbital Strike(7 Ult. Points)", inline=False)

            await message.channel.send(embed=myEmbed)
            return

        elif user_message.lower() == '!viper':

            myEmbed = discord.Embed(title="Viper", description="ROLE: Controller", colour =0x00FF00)
            myEmbed.set_image(url='https://static.wikia.nocookie.net/valorant/images/9/91/Viper_artwork.png/revision/latest/scale-to-width-down/326?cb=20200602020322')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/e/e6/Site-logo.png/revision/latest?cb=20210620062038')
            myEmbed.add_field(name="Basic Abilities",value="Snake Bite and Poison Cloud", inline=False)
            myEmbed.add_field(name="Signature Abilities",value="Toxic Screen", inline=False)
            myEmbed.add_field(name="Ultimate Ability",value="Viper's Pit(7 Ult. Points)", inline=False)

            await message.channel.send(embed=myEmbed)
            return

        elif user_message.lower() == '!omen':

            myEmbed = discord.Embed(title="Omen", description="ROLE: Controller", colour =0x32127a)
            myEmbed.set_image(url='https://static.wikia.nocookie.net/valorant/images/0/06/Omen_artwork.png/revision/latest/scale-to-width-down/326?cb=20200602020233')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/e/e6/Site-logo.png/revision/latest?cb=20210620062038')
            myEmbed.add_field(name="Basic Abilities",value="Shrouded Step and Paranoia", inline=False)
            myEmbed.add_field(name="Signature Abilities",value="Dark Cover", inline=False)
            myEmbed.add_field(name="Ultimate Ability",value="From the Shadows(7 Ult. Points)", inline=False)

            await message.channel.send(embed=myEmbed)
            return

        elif user_message.lower() == '!astra':

            myEmbed = discord.Embed(title="Astra", description="ROLE: Controller", colour =0xBF40BF)
            myEmbed.set_image(url='https://static.wikia.nocookie.net/valorant/images/8/8a/Astra_artwork.png/revision/latest/scale-to-width-down/326?cb=20210302170140')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/e/e6/Site-logo.png/revision/latest?cb=20210620062038')
            myEmbed.add_field(name="Basic Abilities",value="Gravity Well, Nova Pulse and Nebula / Dissipate", inline=False)
            myEmbed.add_field(name="Signature Abilities",value=" Astral Form", inline=False)
            myEmbed.add_field(name="Ultimate Ability",value=" Cosmic Divide(7 Ult. Points)", inline=False)

            await message.channel.send(embed=myEmbed)
            return    
         
        elif user_message.lower() == '!jett':

            myEmbed = discord.Embed(title="Jett", description="ROLE: Duelists", colour =0xADD8E6)
            myEmbed.set_image(url='https://static.wikia.nocookie.net/valorant/images/7/79/Jett_artwork.png/revision/latest/scale-to-width-down/326?cb=20200602020209')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/e/e6/Site-logo.png/revision/latest?cb=20210620062038')
            myEmbed.add_field(name="Passive Ability",value=" Drift", inline=False)
            myEmbed.add_field(name="Basic Abilities",value="Cloudburst and Updraft", inline=False)
            myEmbed.add_field(name="Signature Abilities",value=" Tailwind", inline=False)
            myEmbed.add_field(name="Ultimate Ability",value=" Blade Storm(7 Ult. Points)", inline=False)

            await message.channel.send(embed=myEmbed)
            return

        elif user_message.lower() == '!phoenix':

            myEmbed = discord.Embed(title="Phoenix", description="ROLE: Duelists", colour =0xfdad5c)
            myEmbed.set_image(url='https://static.wikia.nocookie.net/valorant/images/f/fa/Phoenix_artwork.png/revision/latest/scale-to-width-down/326?cb=20200602020246')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/e/e6/Site-logo.png/revision/latest?cb=20210620062038')
            myEmbed.add_field(name="Basic Abilities",value=" Blaze and Curveball", inline=False)
            myEmbed.add_field(name="Signature Abilities",value=" Hot Hands", inline=False)
            myEmbed.add_field(name="Ultimate Ability",value="Run It Back(6 Ult. Points)", inline=False)

            await message.channel.send(embed=myEmbed)
            return 

        elif user_message.lower() == '!raze':

            myEmbed = discord.Embed(title="Raze", description="ROLE: Duelists", colour =0xFFA500)
            myEmbed.set_image(url='https://static.wikia.nocookie.net/valorant/images/c/c4/Raze_artwork.png/revision/latest/scale-to-width-down/326?cb=20200602020217')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/e/e6/Site-logo.png/revision/latest?cb=20210620062038')
            myEmbed.add_field(name="Basic Abilities",value=" Boom Bot and  Blast Pack", inline=False)
            myEmbed.add_field(name="Signature Abilities",value=" Paint Shells", inline=False)
            myEmbed.add_field(name="Ultimate Ability",value="Showstopper(8 Ult. Points)", inline=False)

            await message.channel.send(embed=myEmbed)
            return
            
        elif user_message.lower() == '!reyna':

            myEmbed = discord.Embed(title="Reyna", description="ROLE: Duelists", colour =0x491e3c)
            myEmbed.set_image(url='https://static.wikia.nocookie.net/valorant/images/4/41/Reyna_artwork.png/revision/latest/scale-to-width-down/326?cb=20200602020340')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/e/e6/Site-logo.png/revision/latest?cb=20210620062038')
            myEmbed.add_field(name="Basic Abilities",value=" Leer", inline=False)
            myEmbed.add_field(name="Signature Abilities",value=" Devour and Dismiss", inline=False)
            myEmbed.add_field(name="Ultimate Ability",value="Empress(6 Ult. Points)", inline=False)

            await message.channel.send(embed=myEmbed)
            return

        elif user_message.lower() == '!yoru':

            myEmbed = discord.Embed(title="Yoru", description="ROLE: Duelists", colour =0x0096FF)
            myEmbed.set_image(url='https://static.wikia.nocookie.net/valorant/images/1/1a/Yoru_artwork.png/revision/latest/scale-to-width-down/326?cb=20210112180407')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/e/e6/Site-logo.png/revision/latest?cb=20210620062038')
            myEmbed.add_field(name="Basic Abilities",value="Fakeout and Blindside", inline=False)
            myEmbed.add_field(name="Signature Abilities",value="Gatecrash", inline=False)
            myEmbed.add_field(name="Ultimate Ability",value=" Dimensional Drift(6 Ult. Points)", inline=False)

            await message.channel.send(embed=myEmbed)
            return            
                   
        elif user_message.lower() == '!breach':

            myEmbed = discord.Embed(title="Breach", description="ROLE: Initiators", colour =0x006400)
            myEmbed.set_image(url='https://static.wikia.nocookie.net/valorant/images/5/5c/Breach_artwork.png/revision/latest/scale-to-width-down/326?cb=20200602020225')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/e/e6/Site-logo.png/revision/latest?cb=20210620062038')
            myEmbed.add_field(name="Basic Abilities",value="Aftershock and Flashpoint", inline=False)
            myEmbed.add_field(name="Signature Abilities",value=" Fault Line", inline=False)
            myEmbed.add_field(name="Ultimate Ability",value=" Rolling Thunder(7 Ult. Points)", inline=False)

            await message.channel.send(embed=myEmbed)
            return                   
                   
        elif user_message.lower() == '!kayo':

            myEmbed = discord.Embed(title="Kayo", description="ROLE: Initiators", colour =0x5C5CFF)
            myEmbed.set_image(url='https://static.wikia.nocookie.net/valorant/images/a/a9/KAYO_artwork.png/revision/latest/scale-to-width-down/326?cb=20210622163116')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/e/e6/Site-logo.png/revision/latest?cb=20210620062038')
            myEmbed.add_field(name="Basic Abilities",value=" FRAG/ment and FLASH/drive", inline=False)
            myEmbed.add_field(name="Signature Abilities",value="ZERO/point", inline=False)
            myEmbed.add_field(name="Ultimate Ability",value="  NULL/cmd(7 Ult. Points)", inline=False)

            await message.channel.send(embed=myEmbed)
            return 

        elif user_message.lower() == '!skye':

            myEmbed = discord.Embed(title="Skye", description="ROLE: Initiators", colour =0x01796f)
            myEmbed.set_image(url='https://static.wikia.nocookie.net/valorant/images/d/d6/Skye_artwork.png/revision/latest/scale-to-width-down/326?cb=20201013182515')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/e/e6/Site-logo.png/revision/latest?cb=20210620062038')
            myEmbed.add_field(name="Basic Abilities",value=" Regrowth and Trailblazer", inline=False)
            myEmbed.add_field(name="Signature Abilities",value=" Guiding Light", inline=False)
            myEmbed.add_field(name="Ultimate Ability",value=" Seekers(7 Ult. Points)", inline=False)

            await message.channel.send(embed=myEmbed)
            return 

        elif user_message.lower() == '!sova':

            myEmbed = discord.Embed(title="Sova", description="ROLE: Initiators", colour =0x0f52ba)
            myEmbed.set_image(url='https://static.wikia.nocookie.net/valorant/images/6/61/Sova_artwork.png/revision/latest/scale-to-width-down/326?cb=20200602020314')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/e/e6/Site-logo.png/revision/latest?cb=20210620062038')
            myEmbed.add_field(name="Basic Abilities",value=" Owl Drone and  Shock Bolt", inline=False)
            myEmbed.add_field(name="Signature Abilities",value=" Recon Bolt", inline=False)
            myEmbed.add_field(name="Ultimate Ability",value="  Hunter's Fury(8 Ult. Points)", inline=False)

            await message.channel.send(embed=myEmbed)
            return 

        elif user_message.lower() == '!chamber':

            myEmbed = discord.Embed(title="Chamber", description="ROLE: Sentinels", colour =0xA38A00)
            myEmbed.set_image(url='https://static.wikia.nocookie.net/valorant/images/5/5d/Chamber_artwork.png/revision/latest/scale-to-width-down/326?cb=20211031124636')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/e/e6/Site-logo.png/revision/latest?cb=20210620062038')
            myEmbed.add_field(name="Basic Abilities",value=" Trademark and  Headhunter", inline=False)
            myEmbed.add_field(name="Signature Abilities",value="Rendezvous", inline=False)
            myEmbed.add_field(name="Ultimate Ability",value=" Tour De Force(7 Ult. Points)", inline=False)

            await message.channel.send(embed=myEmbed)
            return 

        elif user_message.lower() == '!cypher':

            myEmbed = discord.Embed(title="Cypher", description="ROLE: Sentinels", colour =0xC9AE5D)
            myEmbed.set_image(url='https://static.wikia.nocookie.net/valorant/images/b/bb/Cypher_artwork.png/revision/latest/scale-to-width-down/326?cb=20200602020329')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/e/e6/Site-logo.png/revision/latest?cb=20210620062038')
            myEmbed.add_field(name="Basic Abilities",value=" Trapwire and  Cyber Cage", inline=False)
            myEmbed.add_field(name="Signature Abilities",value="Spycam", inline=False)
            myEmbed.add_field(name="Ultimate Ability",value=" Neural Theft(6 Ult. Points)", inline=False)

            await message.channel.send(embed=myEmbed)
            return 

        elif user_message.lower() == '!killjoy':

            myEmbed = discord.Embed(title="Killjoy", description="ROLE: Sentinels", colour =0xFFFF00)
            myEmbed.set_image(url='https://static.wikia.nocookie.net/valorant/images/6/6b/Killjoy_artwork.png/revision/latest/scale-to-width-down/220?cb=20200729134445')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/e/e6/Site-logo.png/revision/latest?cb=20210620062038')
            myEmbed.add_field(name="Basic Abilities",value="Alarmbot and Nanoswarm", inline=False)
            myEmbed.add_field(name="Signature Abilities",value=" Turret", inline=False)
            myEmbed.add_field(name="Ultimate Ability",value="Lockdown(7 Ult. Points)", inline=False)

            await message.channel.send(embed=myEmbed)
            return 

        elif user_message.lower() == '!sage':

            myEmbed = discord.Embed(title="Sage", description="ROLE: Sentinels", colour =0x75E6DA)
            myEmbed.set_image(url='https://static.wikia.nocookie.net/valorant/images/1/1e/Sage_artwork.png/revision/latest/scale-to-width-down/326?cb=20200602020306')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/e/e6/Site-logo.png/revision/latest?cb=20210620062038')
            myEmbed.add_field(name="Basic Abilities",value="Barrier Orb and Barrier Orb", inline=False)
            myEmbed.add_field(name="Signature Abilities",value=" Healing Orb", inline=False)
            myEmbed.add_field(name="Ultimate Ability",value=" Resurrection(8  Ult. Points)", inline=False)

            await message.channel.send(embed=myEmbed)
            return 

        elif user_message.lower() == '!neon':

            myEmbed = discord.Embed(title="Neon", description="ROLE: Duelist", colour =0x0047AB)
            myEmbed.set_image(url='https://static.wikia.nocookie.net/valorant/images/a/ad/Neon_artwork.png/revision/latest/scale-to-width-down/326?cb=20220112155550')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/e/e6/Site-logo.png/revision/latest?cb=20210620062038')
            myEmbed.add_field(name="Basic Abilities",value="Fast Lane and  Relay Bolt", inline=False)
            myEmbed.add_field(name="Signature Abilities",value="High Gear", inline=False)
            myEmbed.add_field(name="Ultimate Ability",value="Overdrive(7 Ult. Points)", inline=False)

            await message.channel.send(embed=myEmbed)
            return







        elif user_message.lower() == '!fracture':

            myEmbed = discord.Embed(title="Fracture", description="Type: Standard", colour =0x75E6DA)
            myEmbed.set_image(url='https://static.wikia.nocookie.net/valorant/images/1/18/Fracture_minimap.png/revision/latest/scale-to-width-down/350?cb=20210908143612')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/f/fc/Loading_Screen_Fracture.png/revision/latest/scale-to-width-down/200?cb=20210908143656')
            myEmbed.add_field(name="Real Location",value="Santa Fe, New Mexico, USA", inline=False)
            myEmbed.add_field(name="Spike Sites",value=" A/B", inline=False)
            myEmbed.add_field(name="Dynamic Element(s)",value="Automatic door,One-way automatic,ziplines,Rope ascenders", inline=False)

            await message.channel.send(embed=myEmbed)
            return   
    
        elif user_message.lower() == '!breeze':

            myEmbed = discord.Embed(title="Breeze", description="Type: Standard", colour =0x75E6DA)
            myEmbed.set_image(url='https://static.wikia.nocookie.net/valorant/images/7/78/Breeze_minimap.png/revision/latest/scale-to-width-down/350?cb=20210423171259')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/1/10/Loading_Screen_Breeze.png/revision/latest/scale-to-width-down/350?cb=20210427160616')
            myEmbed.add_field(name="Real Location",value="Atlantic Ocean", inline=False)
            myEmbed.add_field(name="Spike Sites",value=" A/B", inline=False)
            myEmbed.add_field(name="Dynamic Element(s)",value="Mechanical door,One-way chute,Rope ascenders", inline=False)

            await message.channel.send(embed=myEmbed)
            return   
    
        elif user_message.lower() == '!icebox':

            myEmbed = discord.Embed(title="Icebox", description="Type: Standard", colour =0x75E6DA)
            myEmbed.set_image(url='https://static.wikia.nocookie.net/valorant/images/c/cf/Icebox_minimap.png/revision/latest/scale-to-width-down/350?cb=20210712171153')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/1/13/Loading_Screen_Icebox.png/revision/latest/scale-to-width-down/350?cb=20201015084446')
            myEmbed.add_field(name="Real Location",value="Bennett Island, Sakha, Russia", inline=False)
            myEmbed.add_field(name="Spike Sites",value=" A/B", inline=False)
            myEmbed.add_field(name="Dynamic Element(s)",value="Ziplines,Rope ascenders", inline=False)

            await message.channel.send(embed=myEmbed)
            return   
    
        elif user_message.lower() == '!bind':

            myEmbed = discord.Embed(title="Bind", description="Type: Standard", colour =0x75E6DA)
            myEmbed.set_image(url='https://static.wikia.nocookie.net/valorant/images/e/e6/Bind_minimap.png/revision/latest/scale-to-width-down/350?cb=20210611144252')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/2/23/Loading_Screen_Bind.png/revision/latest/scale-to-width-down/350?cb=20200620202316')
            myEmbed.add_field(name="Real Location",value="Rabat, Morocco", inline=False)
            myEmbed.add_field(name="Spike Sites",value=" A/B", inline=False)
            myEmbed.add_field(name="Dynamic Element(s)",value="One-way teleporters", inline=False)

            await message.channel.send(embed=myEmbed)
            return   
    
        elif user_message.lower() == '!haven':

            myEmbed = discord.Embed(title="Haven", description="Type: Standard", colour =0x75E6DA)
            myEmbed.set_image(url='https://static.wikia.nocookie.net/valorant/images/2/25/Haven_minimap.png/revision/latest/scale-to-width-down/350?cb=20210611144435')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/7/70/Loading_Screen_Haven.png/revision/latest/scale-to-width-down/350?cb=20200620202335')
            myEmbed.add_field(name="Real Location",value="Thimphu, Bhutan", inline=False)
            myEmbed.add_field(name="Spike Sites",value=" A/B/C", inline=False)
            myEmbed.add_field(name="Dynamic Element(s)",value="Destructible doors", inline=False)

            await message.channel.send(embed=myEmbed)
            return   
   
        elif user_message.lower() == '!split':

            myEmbed = discord.Embed(title="Split", description="Type: Standard", colour =0x75E6DA)
            myEmbed.set_image(url='https://static.wikia.nocookie.net/valorant/images/f/ff/Split_minimap.png/revision/latest/scale-to-width-down/350?cb=20210517144018')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/d/d6/Loading_Screen_Split.png/revision/latest/scale-to-width-down/350?cb=20200620202349')
            myEmbed.add_field(name="Real Location",value="Shinjuku, Tokyo, Japan", inline=False)
            myEmbed.add_field(name="Spike Sites",value=" A/B", inline=False)
            myEmbed.add_field(name="Dynamic Element(s)",value="Rope ascenders", inline=False)

            await message.channel.send(embed=myEmbed)
            return   
   
        elif user_message.lower() == '!ascent':

            myEmbed = discord.Embed(title="Ascent", description="Type: Standard", colour =0x75E6DA)
            myEmbed.set_image(url='https://static.wikia.nocookie.net/valorant/images/0/04/Ascent_minimap.png/revision/latest/scale-to-width-down/350?cb=20210713101708')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/e/e7/Loading_Screen_Ascent.png/revision/latest/scale-to-width-down/350?cb=20200607180020')
            myEmbed.add_field(name="Real Location",value=" San Marco, Venice, Italy", inline=False)
            myEmbed.add_field(name="Spike Sites",value=" A/B", inline=False)
            myEmbed.add_field(name="Dynamic Element(s)",value="Irreversible bomb doors", inline=False)

            await message.channel.send(embed=myEmbed)
            return   

        elif user_message.lower() == '!range':

            myEmbed = discord.Embed(title="Range", description="Type: Practice", colour =0x75E6DA)
            myEmbed.set_image(url='https://static.wikia.nocookie.net/valorant/images/7/7b/Range_mini-map.png/revision/latest/scale-to-width-down/350?cb=20200412002707')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/3/37/Loading_Screen_Range.png/revision/latest/scale-to-width-down/350?cb=20200607180003')
            myEmbed.add_field(name="Real Location",value=" San Marco, Venice, Italy", inline=False)
            await message.channel.send(embed=myEmbed)
            return   







        elif user_message.lower() == '!incendiary':

            myEmbed = discord.Embed(title="Incendiary", description="Brimstone", colour =0xFF6000)
            myEmbed.set_image(url='https://media.giphy.com/media/C71Rn3G3j2U0eeb9vY/giphy.gif')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/2/26/Incendiary.png/revision/latest/scale-to-width-down/128?cb=20200405205403')
            myEmbed.add_field(name="Q",value=" EQUIP an incendiary grenade launcher. FIRE to launch a grenade that detonates as it comes to a rest on the floor, creating a lingering fire zone that damages players within the zone.", inline=False)
            await message.channel.send(embed=myEmbed)
            return

        elif user_message.lower() == '!stim beacon':

            myEmbed = discord.Embed(title="Stim Beacon", description="Brimstone", colour =0xFF6000)
            myEmbed.set_image(url='https://media.giphy.com/media/u45ZL2Lh7W0uKskps4/giphy.gif')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/a/ad/Stim_Beacon.png/revision/latest/scale-to-width-down/128?cb=20200405205447')
            myEmbed.add_field(name="C",value=" EQUIP a stim beacon. FIRE to toss the stim beacon in front of Brimstone. Upon landing, the stim beacon will create a field that grants players RapidFire.", inline=False)
            await message.channel.send(embed=myEmbed)
            return           

        elif user_message.lower() == '!sky smoke':

            myEmbed = discord.Embed(title="Sky Smoke(3)", description="Brimstone", colour =0xFF6000)
            myEmbed.set_image(url='https://media.giphy.com/media/BYF606qEfpW4z8G17l/giphy-downsized-large.gif')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/7/71/Sky_Smoke.png/revision/latest/scale-to-width-down/126?cb=20200405205417')
            myEmbed.add_field(name="E",value=" EQUIP a tactical map. FIRE to set locations where Brimstone’s smoke clouds will land. ALTERNATE FIRE to confirm, launching long-lasting smoke clouds that block vision in the selected area", inline=False)
            await message.channel.send(embed=myEmbed)
            return

        elif user_message.lower() == '!orbital strike':

            myEmbed = discord.Embed(title="Orbital Strike(7 Ult. Points)", description="Brimstone", colour =0xFF6000)
            myEmbed.set_image(url='https://media.giphy.com/media/WZbX2S08n0YHnIExUN/giphy-downsized-large.gif')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/6/61/Orbital_Strike.png/revision/latest/scale-to-width-down/128?cb=20200405205426')
            myEmbed.add_field(name="X",value="EQUIP a tactical map. FIRE to launch a lingering orbital strike laser at the selected location, dealing high damage-over-time to players caught in the selected area", inline=False)
            await message.channel.send(embed=myEmbed)
            return

        elif user_message.lower() == '!poison cloud':

            myEmbed = discord.Embed(title="Poison Cloud", description="Viper", colour =0x00FF00)
            myEmbed.set_image(url='https://media.giphy.com/media/kfUPDq4hzBPwll2iUc/giphy-downsized-large.gif')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/8/81/Poison_Cloud.png/revision/latest/scale-to-width-down/128?cb=20200405224117')
            myEmbed.add_field(name="Q",value="EQUIP a gas emitter. FIRE to throw the emitter that perpetually remains throughout the round. RE-USE the ability to create a toxic gas cloud at the cost of fuel. This ability can be RE-USED more than once and can be picked up to be REDEPLOYED.", inline=False)
            await message.channel.send(embed=myEmbed)
            return

        elif user_message.lower() == '!snake bite':

            myEmbed = discord.Embed(title="Snake Bite", description="Viper", colour =0x00FF00)
            myEmbed.set_image(url='https://media.giphy.com/media/9MsLoqpOCyvUsgpRnm/giphy-downsized-large.gif')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/a/a2/Snake_Bite.png/revision/latest/scale-to-width-down/128?cb=20200405224128')
            myEmbed.add_field(name="C",value="EQUIP a chemical launcher. FIRE to launch a canister that shatters upon hitting the floor, creating a lingering chemical zone that damages and slows enemies.", inline=False)
            await message.channel.send(embed=myEmbed)
            return

        elif user_message.lower() == '!toxic screen':

            myEmbed = discord.Embed(title="Toxic Screen", description="Viper", colour =0x00FF00)
            myEmbed.set_image(url='https://media.giphy.com/media/8r9vjPTsABTv2dO4QB/giphy-downsized-large.gif')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/c/cd/Toxic_Screen.png/revision/latest/scale-to-width-down/128?cb=20200405224110')
            myEmbed.add_field(name="E",value="EQUIP a gas emitter launcher. FIRE to deploy a long line of gas emitters. RE-USE the ability to create a tall wall of toxic gas at the cost of fuel. This ability can be RE-USED more than once.", inline=False)
            await message.channel.send(embed=myEmbed)
            return

        elif user_message.lower() == "!viper's pit":

            myEmbed = discord.Embed(title="Viper's Pit(7 Ult. Points)", description="Viper", colour =0x00FF00)
            myEmbed.set_image(url='https://media.giphy.com/media/DQOrB5IUJSKtmkV72M/giphy.gif')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/a/ab/Viper%E2%80%99s_Pit.png/revision/latest/scale-to-width-down/128?cb=20200405224059')
            myEmbed.add_field(name="X",value="EQUIP a chemical sprayer. FIRE to spray a chemical cloud in all directions around Viper, creating a large cloud that reduces the vision range and maximum health of players inside of it.", inline=False)
            await message.channel.send(embed=myEmbed)
            return

        elif user_message.lower() == "!shrouded step":

            myEmbed = discord.Embed(title="Shrouded Step", description="Omen", colour =0x32127a)
            myEmbed.set_image(url='https://media.giphy.com/media/lXN5OZ3UwidKihFwaB/giphy-downsized-large.gif')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/8/80/Shrouded_Step.png/revision/latest/scale-to-width-down/115?cb=20200405212629')
            myEmbed.add_field(name="C",value="EQUIP a shadow walk ability and see its range indicator. FIRE to begin a brief channel, then teleport to the marked location.", inline=False)
            await message.channel.send(embed=myEmbed)
            return

        elif user_message.lower() == "!paranoia":

            myEmbed = discord.Embed(title="Paranoia", description="Omen", colour =0x32127a)
            myEmbed.set_image(url='https://media.giphy.com/media/UGxWadTTvTQVuczkD0/giphy.gif')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/8/8d/Paranoia.png/revision/latest/scale-to-width-down/115?cb=20200405212616')
            myEmbed.add_field(name="Q",value="INSTANTLY fire a shadow projectile forward, briefly reducing the vision range of all players it touches. This projectile can pass straight through walls.", inline=False)
            await message.channel.send(embed=myEmbed)
            return

        elif user_message.lower() == "!dark cover":

            myEmbed = discord.Embed(title="Dark Cover", description="Omen", colour =0x32127a)
            myEmbed.set_image(url='https://media.giphy.com/media/iF6F6B2Pce6FyBkS61/giphy-downsized-large.gif')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/2/2c/Dark_Cover.png/revision/latest/scale-to-width-down/115?cb=20200405212635')
            myEmbed.add_field(name="E",value="EQUIP a shadow orb and see its range indicator. FIRE to throw the shadow orb to the marked location, creating a long-lasting shadow sphere that blocks vision. HOLD ALTERNATE FIRE while targeting to move the marker further away. HOLD the ability key with targeting to move the marker closer.", inline=False)
            await message.channel.send(embed=myEmbed)
            return

        elif user_message.lower() == "!from the shadows":

            myEmbed = discord.Embed(title="From the Shadows(7 Ult. Points)", description="Omen", colour =0x32127a)
            myEmbed.set_image(url='https://media.giphy.com/media/NB1Ljlioat0QHOs2ZU/giphy.gif')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/0/0e/From_the_Shadows.png/revision/latest/scale-to-width-down/115?cb=20200405212650')
            myEmbed.add_field(name="X",value="EQUIP a tactical map. FIRE to begin teleporting to the selected location. While teleporting, Omen will appear as a Shade that can be destroyed by an enemy to cancel his teleport.", inline=False)
            await message.channel.send(embed=myEmbed)
            return   

        elif user_message.lower() == "!gravity well":

            myEmbed = discord.Embed(title="Gravity Well", description="Astra", colour =0xBF40BF)
            myEmbed.set_image(url='https://media.giphy.com/media/dSRbLl6ywHfyceYo0R/giphy-downsized-large.gif')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/4/41/Gravity_Well.png/revision/latest/scale-to-width-down/115?cb=20210302170436')
            myEmbed.add_field(name="C",value="Place Stars in Astral Form (X) ACTIVATE a Star to form a Gravity Well. Players in the area are pulled toward the center before it explodes, making all players still trapped inside fragile.", inline=False)
            await message.channel.send(embed=myEmbed)
            return

        elif user_message.lower() == "!nova pulse":

            myEmbed = discord.Embed(title="Nova Pulse", description="Astra", colour =0xBF40BF)
            myEmbed.set_image(url='https://media.giphy.com/media/InhSyPyJjavwSOyBXP/giphy-downsized-large.gif')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/5/51/Nova_Pulse.png/revision/latest/scale-to-width-down/115?cb=20210302170417')
            myEmbed.add_field(name="Q",value="Place Stars in Astral Form (X) ACTIVATE a Star to detonate a Nova Pulse. The Nova Pulse charges briefly then strikes, concussing all players in its area.", inline=False)
            await message.channel.send(embed=myEmbed)
            return

        elif user_message.lower() == "!nebula":

            myEmbed = discord.Embed(title="Nebula", description="Astra", colour =0xBF40BF)
            myEmbed.set_image(url='https://media.giphy.com/media/FLXdr0y4hfThn6CzKP/giphy-downsized-large.gif')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/8/8b/Nebula_-_Dissipate.png/revision/latest/scale-to-width-down/115?cb=20210302170357')
            myEmbed.add_field(name="E",value="Place Stars in Astral Form (X) ACTIVATE a Star to transform it into a Nebula (smoke). Use (F) on a Star to Dissipate it, returning the star to be placed in a new location after a delay. Dissipate briefly forms a fake Nebula at the Star’s location before returning..", inline=False)
            await message.channel.send(embed=myEmbed)
            return   
                                 
        elif user_message.lower() == "!astral form":

            myEmbed = discord.Embed(title="ASTRAL FORM / COSMIC DIVIDE", description="Astra", colour =0xBF40BF)
            myEmbed.set_image(url='https://media.giphy.com/media/5Mue1nFYUIFYsegXUT/giphy-downsized-large.gif')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/f/f4/Cosmic_Divide.png/revision/latest/scale-to-width-down/115?cb=20210302170328')
            myEmbed.add_field(name="X",value="ACTIVATE (X) to enter Astral Form where you can place Stars with PRIMARY FIRE. Stars can be reactivated later, transforming them into a Nova Pulse, Nebula, or Gravity Well. When Cosmic Divide is charged, use SECONDARY FIRE in Astral Form to begin aiming it, then PRIMARY FIRE to select two locations. An infinite Cosmic Divide connects the two points you select. Cosmic Divide blocks bullets and heavily dampens audio.", inline=False)
            await message.channel.send(embed=myEmbed)
            return
                        
        elif user_message.lower() == "!blindside":

            myEmbed = discord.Embed(title="Blindside", description="Yoru", colour =0x0096FF)
            myEmbed.set_image(url='https://media.giphy.com/media/yGBuLe3BzGmr6LwBMY/giphy.gif')
            myEmbed.set_thumbnail(url='https://static.wikia.nocookie.net/valorant/images/2/2f/Blindside.png/revision/latest/scale-to-width-down/115?cb=20210112180620')
            myEmbed.add_field(name="Q",value="EQUIP to rip an unstable dimensional fragment from reality. FIRE to throw the fragment, activating a flash that winds up once it collides with a hard surface in world.", inline=False)
            await message.channel.send(embed=myEmbed)
            return                        


client.run(TOKEN)