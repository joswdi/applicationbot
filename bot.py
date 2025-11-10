import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from config import set_bot
from views.role_views import RoleSelectView
from views.purchaserole_views import PurchaseRoleSelectView
from views.foxpropose_views import FoxProposeSelectView

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)
set_bot(bot)

TOKEN = os.getenv('DISCORD_TOKEN')

if not TOKEN:
    raise ValueError("DISCORD_TOKEN не найден в переменных окружения")

# -------------------- Событие при запуске бота --------------------
@bot.event
async def on_ready():
    print(f"Бот {bot.user} запущен и готов к работе!")
    bot.add_view(RoleSelectView())
    bot.add_view(PurchaseRoleSelectView())
    bot.add_view(FoxProposeSelectView())
    try:
        synced = await bot.tree.sync()
        print(f"Синхронизировано {len(synced)} команд")
    except Exception as e:
        print(f"Ошибка синхронизации: {e}")

@bot.command()
async def набор(ctx):
    embed = discord.Embed(title="🔮 | НАБОР В КОМАНДУ ПРОЕКТА", color=0x3498db)
    embed.add_field(
        name="⚠️ Требования:",
        value=(
            "```\n"
            "• Уделять серверу не менее 3-х часов в день.\n"
            "• Быть старше 16 лет.\n"
            "• Адекватность и стрессоустойчивость.\n"
            "• Знания правил проекта.\n"
            "```"
        ),
        inline=False
    )
    embed.add_field(
        name="⚠️ Вы получите:",
        value=(
            "```\n"
            "• Права Fox-Gold на нашем сервере [7 дней].\n"
            "• Права Admin на нашем сервере.\n"
            "• Резервный слот при входе на сервер.\n"
            "• Имунитет от кика/бана.\n"
            "• Интересное времяпровождение.\n"
            "• Отзывчивую Администрацию.\n"
            "• Дружелюбный коллектив.\n"
            "```"
        ),
        inline=False
    )
    embed.set_image(url="https://i.pinimg.com/736x/3d/2e/5f/3d2e5fc4c0c5480795de10bb829544a2.jpg")
    await ctx.send(embed=embed, view=RoleSelectView())

@bot.command()
async def покупка(ctx):
    embed = discord.Embed()
    embed.set_image(url="https://i.pinimg.com/736x/28/54/8a/28548a67d9a0212b3f2e88690b3d0220.jpg")
    await ctx.send(embed=embed, view=PurchaseRoleSelectView())

@bot.command()
async def предложения(ctx):
    embed = discord.Embed(title="🗨️ • ЗАЯВКИ / ПРЕДЛОЖЕНИЯ", color=0xFF50FC)
    embed.add_field(
        name="💕 • Требования FOX-GOLD для девушек:",
        value=(
            "```\n"
            "💄╰➤Наличие хорошего микрофона.\n"
            "💄╰➤Время игры на проекте более 3 дней.\n"
            "💄╰➤Адекватность.\n"
            "```"
        ),
        inline=False
    )
    embed.add_field(
        name="",
        value=(
            "```\n"
            "📃 • Также вы можете выдвинуть своё предложение по улучшению сервера и мы его рассмотрим. Возможно именно вашу идею мы сможем воплотить в жизнь. Принимаем предложения по добавлению своей музыки в конце раунда.\n"
            "```"
        ),
        inline=False
    )
    embed.set_image(url="https://i.pinimg.com/736x/54/ee/26/54ee2603ac19084e28bdd88a47864f57.jpg")
    await ctx.send(embed=embed, view=FoxProposeSelectView())

if __name__ == "__main__":
    bot.run(TOKEN)