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
            myEmbed.add_field(name="Version",value="1.0", inline=False)

            await message.channel.send(embed=myEmbed)
            return

        elif user_message.lower() == 'thank muthu paandi' :
            await message.channel.send(f'chellom thanks!')
            return    

        elif user_message.lower() == 'bye':
            await message.channel.send(f'see you later {username}!')
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
            myEmbed.add_field(name="Ultimate Ability",value=" From the Shadows(7 Ult. Points)", inline=False)

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

client.run(TOKEN)




