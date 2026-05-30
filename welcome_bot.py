import discord
from discord.ext import commands
import traceback
import os

TOKEN = os.getenv("DISCORD_TOKEN")
WELCOME_CHANNEL_ID = 1084599010796519474
RULES_CHANNEL_ID   = 1231906406177701919
EMBED_COLOR        = 0xC8860A

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot online come {bot.user} (ID: {bot.user.id})")

@bot.event
async def on_member_join(member: discord.Member):
    try:
        channel = bot.get_channel(WELCOME_CHANNEL_ID)
        if channel is None:
            print(f"Canale non trovato (ID: {WELCOME_CHANNEL_ID})")
            return
        rules_channel = bot.get_channel(RULES_CHANNEL_ID)
        rules_mention = rules_channel.mention if rules_channel else "#statuto"
        avatar_url = member.display_avatar.url
        embed = discord.Embed(
            title=f"🤠 Benvenuto/a, Pistolero {member.display_name}!",
            description=(
                f"Ehi straniero {member.mention}, sei arrivato nel saloon giusto! 🌵\n\n"
                f"Prima di sederti al tavolo da gioco, dai un'occhiata a {rules_mention} "
                f"per conoscere le leggi di queste terre.\n\n"
                f"Speriamo che tu ti trovi bene — qui si spara solo a chi se lo merita! 🔫"
            ),
            color=EMBED_COLOR,
        )
        embed.set_thumbnail(url=avatar_url)
        embed.set_footer(text=f"Sei il pistolero numero {member.guild.member_count}!")
        await channel.send(embed=embed)
    except Exception as e:
        print(f"Errore: {e}")
        traceback.print_exc()

try:
    bot.run(TOKEN)
except Exception as e:
    print(f"Errore avvio: {e}")
    traceback.print_exc()
    input("Premi Invio per chiudere...")
