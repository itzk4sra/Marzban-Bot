import os
import time
import uuid
import qrcode
import discord
from discord.ext import commands
from marzpy import Marzban
from marzpy.api.user import User

panel = Marzban("username","password","https://example.com:Port") # Example Url https://example.com:8000 8000 Is Defult Port Of Marzban
mytoken = panel.get_token()


class Config():
    Prefix = "" # Enter Bot Prefix Example m!
    Token = "" # Enter Bot Token
    s_Color = 0x7FFFD # Youre Favorit Success Color Hex Example 0x7FFFD4
    e_Color = 0xD70040 # Youre Favorit Error Color Hex Example 0x7FFFD4
    owner = 357233919285919746 # Owner id


client = commands.Bot(command_prefix=Config.Prefix)


@client.event
async def on_ready():
    admin = panel.get_current_admin(token=mytoken)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Bot Ready Success Full')
    print(f'Panel Login Data : {admin}')
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=f"Marzban Bot By Imk4sra"),status=discord.Status.dnd) 



def gigabytes_to_bytes(gigabytes):
    bytes_in_a_gb = 1024**3
    bytes_result = gigabytes * bytes_in_a_gb
    return bytes_result

class Buttons(discord.ui.View):
    def __init__(self, *, timeout=180):
        super().__init__(timeout=timeout)


@client.command()
async def Restart(ctx, username: str):
    try:
        if ctx.author.id == Config.owner:
            result = panel.restart_xray_core(token=mytoken)
            core_result = panel.get_xray_core(token=mytoken)
            Embed = discord.Embed(
                title = "**Marzban Bot**",
                description=f"**Core Restart\nServer Result:**\n```{result}```\n**Core Stat:**\n```{core_result}```",
                color= Config.s_Color
            )
            await ctx.reply(embed=Embed)
        else:
            Not_Embed = discord.Embed(
                title = "**Marzban Bot**",
                description=f"**Hi {ctx.author.mention}\nYoure Not Owner To Use This Command !**",
                color= Config.e_Color
            )
            await ctx.reply(embed=Not_Embed)
            
    except:
        Error_Embed = discord.Embed(
            title = "**Marzban Bot**",
            description=f"**Hi {ctx.author.mention}\nThis User Dos Not Exist !**",
            color= Config.e_Color
        )
        await ctx.reply(embed=Not_Embed)   


@client.command()
async def CreateAdmin(ctx, username: str, password: str):
    if ctx.author.id == Config.owner:
        if username is None or password is None:
            Error_embed = discord.Embed(
                title="**Marzban Bot**",
                description=f"**Username or password Can Not be None.\nExaple Usage:**\n```{Config.Prefix}CreateAdmin k4sra k4sra@123```",
                color=Config.e_Color
            )
            await ctx.reply(embed=Error_embed)
            return
        data = {
            'username':username,
            'password':password,
            'is_sudo':False
        }
        result = panel.create_admin(token=mytoken,data=data)
        Embed = discord.Embed(
            title = "**Marzban Bot**",
            description=f"**Account Created**\n**Panel Result :**\n```{result}```",
            color= Config.s_Color
        )
        await ctx.reply(embed=Embed)
    else:
        Not_Embed = discord.Embed(
            title = "**Marzban Bot**",
            description=f"**Hi {ctx.author.mention}\nYoure Not Owner To Use This Command !**",
            color= Config.e_Color
        )
        await ctx.reply(embed=Not_Embed)


@client.command()
async def RemoveAdmin(ctx, username: str):
    if ctx.author.id == Config.owner:
        if username is None:
            Error_embed = discord.Embed(
                title="**Marzban Bot**",
                description=f"**Username Can Not be None.\nExaple Usage:**\n```{Config.Prefix}RemoveAdmin k4sra```",
                color=Config.e_Color
            )
            await ctx.reply(embed=Error_embed)
            return
        result = panel.delete_admin(username=username,token=mytoken)

        Embed = discord.Embed(
            title = "**Marzban Bot**",
            description=f"**Account Deleted**\n**Panel Result :**\n```{result}```",
            color= Config.s_Color
        )
        await ctx.reply(embed=Embed)
    else:
        Not_Embed = discord.Embed(
            title = "**Marzban Bot**",
            description=f"**Hi {ctx.author.mention}\nYoure Not Owner To Use This Command !**",
            color= Config.e_Color
        )
        await ctx.reply(embed=Not_Embed)
    

@client.command()
async def GetAllAdmin(ctx):
    if ctx.author.id == Config.owner:
        result = panel.get_all_admins(token=mytoken)

        Embed = discord.Embed(
            title = "**Marzban Bot**",
            description=f"**All Admin Result:**\n\n```{result[0]}```",
            color= Config.s_Color
        )
        await ctx.reply(embed=Embed)
    else:
        Not_Embed = discord.Embed(
            title = "**Marzban Bot**",
            description=f"**Hi {ctx.author.mention}\nYoure Not Owner To Use This Command !**",
            color= Config.e_Color
        )
        await ctx.reply(embed=Not_Embed)

@client.command()
async def GetInbounds(ctx):
    if ctx.author.id == Config.owner:
        result = panel.get_inbounds(token=mytoken)

        Embed = discord.Embed(
            title = "**Marzban Bot**",
            description=f"**Get Inbounds Result:**\n\n```{result}```",
            color= Config.s_Color
        )
        await ctx.reply(embed=Embed)
    else:
        Not_Embed = discord.Embed(
            title = "**Marzban Bot**",
            description=f"**Hi {ctx.author.mention}\nYoure Not Owner To Use This Command !**",
            color= Config.e_Color
        )
        await ctx.reply(embed=Not_Embed)

@client.command()
async def Remove(ctx, username: str):
    try:
        if ctx.author.id == Config.owner:
            result = panel.delete_user(username, token=mytoken)

            Embed = discord.Embed(
                title = "**Marzban Bot**",
                description=f"**Account Removed\nServer Result:**\n```{result}```",
                color= Config.s_Color
            )
            await ctx.reply(embed=Embed)
        else:
            Not_Embed = discord.Embed(
                title = "**Marzban Bot**",
                description=f"**Hi {ctx.author.mention}\nYoure Not Owner To Use This Command !**",
                color= Config.e_Color
            )
            await ctx.reply(embed=Not_Embed)
    except:
        Error_Embed = discord.Embed(
            title = "**Marzban Bot**",
            description=f"**Hi {ctx.author.mention}\nThis User Dos Not Exist !**",
            color= Config.e_Color
        )
        await ctx.reply(embed=Not_Embed)              


@client.command()
async def ResetData(ctx, username: str):
    try:
        if ctx.author.id == Config.owner:
            result = panel.reset_user_traffic(username, token=mytoken)
            user_result = panel.get_user_usage(username,token=mytoken)

            Embed = discord.Embed(
                title = "**Marzban Bot**",
                description=f"**Account Data Reseted\nServer Result:**\n```{result}```\n**User Data:**\n```{user_result}```",
                color= Config.s_Color
            )
            await ctx.reply(embed=Embed)
        else:
            Not_Embed = discord.Embed(
                title = "**Marzban Bot**",
                description=f"**Hi {ctx.author.mention}\nYoure Not Owner To Use This Command !**",
                color= Config.e_Color
            )
            await ctx.reply(embed=Not_Embed)
            
    except:
        Error_Embed = discord.Embed(
            title = "**Marzban Bot**",
            description=f"**Hi {ctx.author.mention}\nThis User Dos Not Exist !**",
            color= Config.e_Color
        )
        await ctx.reply(embed=Not_Embed)     
    
@client.command()
async def CreateUser(ctx, text, Data=None):
    try:
        if ctx.author.id == Config.owner:
            current_time = int(time.time())
            myuuid = uuid.uuid4()
            days_to_add = 30
            seconds_in_a_day = 86400
            
            if Data is not None:
                gigabytes = float(Data)
                bytes = gigabytes_to_bytes(gigabytes)
            else:
                bytes = 0

            img = qrcode.make(result.links[0])
            type(img)
            img.save("config_qrcode.png")

            user = User(
                username=text,
                proxies={
                    "vmess": {"id": str(myuuid), "flow": "xtls-rprx-vision"},
                    "vless": {"id": str(myuuid), "flow": "xtls-rprx-vision"},
                },
                inbounds={"vmess": ["VMess TCP"], "vless": ["VLESS TCP REALITY"]},
                expire=current_time + (days_to_add * seconds_in_a_day),
                data_limit=bytes,
                data_limit_reset_strategy="no_reset",
            )
            result = panel.add_user(user=user, token=mytoken) 


            Embed = discord.Embed(
                title = "**Marzban Bot**",
                description=f"**Account Created\nSub Link:\n```{result.subscription_url}```\nConfig Link:\n```{result.links[0]}```**",
                color= Config.s_Color
            )
            Embed.set_thumbnail('attachment://config_qrcode.png')
            Embed.set_footer(text="Marzpy Bot By Imk4sra")

            view=Buttons()
            view.add_item(discord.ui.Button(label="Creator Github",style=discord.ButtonStyle.link,url="https://github.com/imk4sra"))
            view.add_item(discord.ui.Button(label="Support Server",style=discord.ButtonStyle.link,url="https://discord.gg/52hz"))
            
            await ctx.reply(embed=Embed, file=discord.File("data/config_qrcode.png"),view=view)

        else:
            Not_Embed = discord.Embed(
                title = "**Marzban Bot**",
                description=f"**Hi {ctx.author.mention}\nYoure Not Owner To Use This Command !**",
                color= Config.e_Color
            )
            await ctx.reply(embed=Not_Embed)
    except:
        Error_Embed = discord.Embed(
            title = "**Marzban Bot**",
            description=f"**Hi {ctx.author.mention}\nThis User Already Exist !**",
            color= Config.e_Color
        )
        await ctx.reply(embed=Not_Embed)       







@client.command()
async def helpme(ctx):
    prefix = Config.Prefix 

    help_embed = discord.Embed(
        title="**Marzban Bot - Help**",
        description=f"Command Prefix: `{prefix}`",
        color=Config.s_Color
    )
    help_embed.add_field(
        name="Restart",
        value="Restarts the Core.",
        inline=False
    )
    help_embed.add_field(
        name="CreateAdmin",
        value="Creates an admin user.",
        inline=False
    )
    help_embed.add_field(
        name="RemoveAdmin",
        value="Removes an admin user.",
        inline=False
    )
    help_embed.add_field(
        name="GetAllAdmin",
        value="Gets a list of all admin users.",
        inline=False
    )
    help_embed.add_field(
        name="GetInbounds",
        value="Gets inbounds information.",
        inline=False
    )
    help_embed.add_field(
        name="Remove",
        value="Removes a specified item.",
        inline=False
    )
    help_embed.add_field(
        name="ResetData",
        value="Resets data (if applicable).",
        inline=False
    )
    help_embed.add_field(
        name="CreateUser",
        value="Create V2ray Server",
        inline=False
    )
    view=Buttons()
    view.add_item(discord.ui.Button(label="Creator Github",style=discord.ButtonStyle.link,url="https://github.com/imk4sra"))
    view.add_item(discord.ui.Button(label="Support Server",style=discord.ButtonStyle.link,url="https://discord.gg/52hz"))
    await ctx.send(embed=help_embed,view=view)

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
        description=f"{error}",
        color=0xFF7518	
        )
        await ctx.reply(embed=embed)
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
        description=f"{error}",
        color=0xFF7518	
        )
        await ctx.reply(embed=embed)
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
        description=f"{error}",
        color=0xFF7518	
        )
        await ctx.reply(embed=embed)
    if isinstance(error, commands.BotMissingPermissions):
        embed = discord.Embed(
        description=f"{error}",
        color=0xFF7518	
        )
        await ctx.reply(embed=embed)
    if isinstance(error, commands.MemberNotFound):
        embed = discord.Embed(
        description=f"{error}",
        color=0xFF7518	
        )
        await ctx.reply(embed=embed)
    if isinstance(error, commands.errors.NoPrivateMessage):
        embed = discord.Embed(
        description=f"{error}",
        color=0xFF7518	
        )
        await ctx.reply(embed=embed)

client.run(Config.Token)
