import os
import discord
from discord.ext import commands
from discord.ui import Select, View, Modal, TextInput
from dotenv import load_dotenv

load_dotenv()
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="/", intents=intents)

TOKEN = os.getenv('DISCORD_TOKEN')

if not TOKEN:
    raise ValueError("DISCORD_TOKEN не найден в переменных окружения")

# -------------------- Событие при запуске бота --------------------
@bot.event
async def on_ready():
    print(f"Бот {bot.user} запущен и готов к работе!")
    # Восстанавливаем persistent View при перезапуске
    bot.add_view(RoleSelectView())
    bot.add_view(PurchaseRoleSelectView())
    bot.add_view(FoxProposeSelectView())
    try:
        synced = await bot.tree.sync()
        print(f"Синхронизировано {len(synced)} команд")
    except Exception as e:
        print(f"Ошибка синхронизации: {e}")

# -------------------- МОДАЛИ --------------------
class AdminApplicationModal(Modal, title="Заявка на роль Admin"):
    def __init__(self):
        super().__init__(timeout=300)
        
        self.name_age = TextInput(
            label="Как вас зовут и сколько вам лет?", 
            placeholder="Миша, 20", 
            required=True, 
            max_length=100
        )
        
        self.time_played = TextInput(
            label="Время игры на нашем проекте?", 
            placeholder="", 
            required=True, 
            max_length=20
        )
        
        self.about = TextInput(
            label="О себе", 
            placeholder="Расскажите о себе", 
            style=discord.TextStyle.paragraph, 
            required=True, 
            max_length=1000
        )
        
        self.experience = TextInput(
            label="Был ли опыт администрирования? Где?", 
            placeholder="Расскажите подробнее", 
            style=discord.TextStyle.paragraph, 
            required=True, 
            max_length=1000
        )
        
        self.motivation = TextInput(
            label="Почему хотите на эту должность?", 
            placeholder="Мотивация", 
            style=discord.TextStyle.paragraph, 
            required=True, 
            max_length=1000
        )
        
        self.add_item(self.name_age)
        self.add_item(self.time_played)
        self.add_item(self.about)
        self.add_item(self.experience)
        self.add_item(self.motivation)

    async def on_submit(self, interaction: discord.Interaction):
        # Проверка полей
        for field in self.children:
            if not field.value.strip():
                await interaction.response.send_message(f"❌ Поле '{field.label}' не может быть пустым.", ephemeral=True)
                return

        # Отправляем ответ пользователю
        await interaction.response.send_message("✅ Ваша заявка на роль Admin отправлена!", ephemeral=True)

        # Отправляем заявку в канал
        try:
            channel = bot.get_channel(1436873561632538708)
            if channel:
                embed = discord.Embed(
                    title="📨 Новая заявка на Admin", 
                    color=0x00ff00, 
                    timestamp=discord.utils.utcnow()
                )
                embed.add_field(name="Имя и возраст", value=self.name_age.value, inline=True)
                embed.add_field(name="Время игры", value=self.time_played.value, inline=True)
                embed.add_field(name="ℹО себе", value=self.about.value, inline=False)
                embed.add_field(name="Опыт", value=self.experience.value, inline=False)
                embed.add_field(name="Мотивация", value=self.motivation.value, inline=False)
                embed.set_footer(text=f"ID пользователя: {interaction.user.id} | {interaction.user.display_name}")
                await channel.send(embed=embed)
        except Exception as e:
            print(f"Ошибка отправки заявки: {e}")

class ModerApplicationModal(Modal, title="Заявка на роль Moderator"):
    def __init__(self):
        super().__init__(timeout=300)
        
        self.name_age = TextInput(
            label="Как вас зовут и сколько вам лет?", 
            placeholder="Миша, 20", 
            required=True, 
            max_length=100
        )
        
        self.device = TextInput(
            label="Ваше устройство для работы?", 
            placeholder="ПК", 
            style=discord.TextStyle.paragraph, 
            required=True, 
            max_length=50
        )
        
        self.experience = TextInput(
            label="Есть опыт работы модератором? Какой?", 
            placeholder="Расскажите подробнее", 
            style=discord.TextStyle.paragraph, 
            required=True, 
            max_length=1000
        )
        
        self.rules_knowledge = TextInput(
            label="Знание правил сервера/платформы?", 
            placeholder="8/10", 
            style=discord.TextStyle.paragraph, 
            required=True, 
            max_length=500
        )
        
        self.video_recording = TextInput(
            label="Умеете делать видеофиксацию нарушений?", 
            placeholder="Да/нет", 
            style=discord.TextStyle.paragraph, 
            required=True, 
            max_length=50
        )
        
        self.add_item(self.name_age)
        self.add_item(self.device)
        self.add_item(self.experience)
        self.add_item(self.rules_knowledge)
        self.add_item(self.video_recording)

    async def on_submit(self, interaction: discord.Interaction):
        # Проверка полей
        for field in self.children:
            if not field.value.strip():
                await interaction.response.send_message(f"❌ Поле '{field.label}' не может быть пустым.", ephemeral=True)
                return

        # Отправляем ответ пользователю
        await interaction.response.send_message("✅ Ваша заявка на роль Moderator отправлена!", ephemeral=True)

        # Отправляем заявку в канал
        try:
            channel = bot.get_channel(1436873561632538708)
            if channel:
                embed = discord.Embed(
                    title="📨 Новая заявка на Moderator", 
                    color=0xffff00, 
                    timestamp=discord.utils.utcnow()
                )
                embed.add_field(name="Имя и возраст", value=self.name_age.value, inline=True)
                embed.add_field(name="Устройство", value=self.device.value, inline=True)
                embed.add_field(name="Опыт работы", value=self.experience.value, inline=False)
                embed.add_field(name="Знание правил", value=self.rules_knowledge.value, inline=False)
                embed.add_field(name="Видеофиксация", value=self.video_recording.value, inline=False)
                embed.set_footer(text=f"ID пользователя: {interaction.user.id} | {interaction.user.display_name}")
                await channel.send(embed=embed)
        except Exception as e:
            print(f"Ошибка отправки заявки: {e}")

# -------------------- VIEW --------------------
class RoleSelect(Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Administrator", description="Подать заявку на роль администратора", value="admin", emoji="👑"),
            discord.SelectOption(label="Moderator", description="Подать заявку на роль модератора", value="moder", emoji="⚡"),
        ]
        super().__init__(
            placeholder="Подать заявку", 
            min_values=1, 
            max_values=1, 
            options=options,
            custom_id="role_select"
        )

    async def callback(self, interaction: discord.Interaction):
        try:
            if self.values[0] == "admin":
                modal = AdminApplicationModal()
                await interaction.response.send_modal(modal)
            elif self.values[0] == "moder":
                modal = ModerApplicationModal()
                await interaction.response.send_modal(modal)
        except Exception as e:
            print(f"Ошибка в callback: {e}")
            if not interaction.response.is_done():
                await interaction.response.send_message("❌ Произошла ошибка. Попробуйте еще раз.", ephemeral=True)
            else:
                await interaction.followup.send("❌ Произошла ошибка. Попробуйте еще раз.", ephemeral=True)

class RoleSelectView(View):
    def __init__(self):
        # timeout=None ОБЯЗАТЕЛЬНО для persistent View
        super().__init__(timeout=None)
        self.add_item(RoleSelect())

# -------------------- КОМАНДА --------------------
@bot.command()
async def набор(ctx):
    embed = discord.Embed(title="🔮 | НАБОР НА РОЛЬ ADMIN / MODER", color=0x3498db)
    embed.add_field(
        name="⚠️ Требования:",
        value=(
            "```\n"
            "- Уделять серверу не менее 3-х часов.\n"
            "- Быть старше 16 лет.\n"
            "- Адекватность и стрессоустойчивость.\n"
            "- Знания правил проекта.\n"
            "```"
        ),
        inline=False
    )
    embed.add_field(
        name="⚠️ Вы получите:",
        value=(
            "```\n"
            "- Права Fox-Gold.\n"
            "- Права Admin [Для Admin].\n"
            "- Резервный слот.\n"
            "- Имунитет от кика/бана.\n"
            "```"
        ),
        inline=False
    )
    embed.set_image(url="https://www2.online-converting.com/upload/api_71abdc6d62/result.jpg")
    await ctx.send(embed=embed, view=RoleSelectView())

class PurchaseFoxVipModal(Modal, title="Покупка Fox-Vip"):
    def __init__(self):
        super().__init__(timeout=300)
        
        self.time = TextInput(
            label="Количество месяцев?", 
            placeholder="2", 
            required=True, 
            max_length=50
        )
        
        self.add_comment = TextInput(
            label="Дополнительный комментарий", 
            placeholder=" ", 
            required=True, 
            max_length=20
        )
        
        self.add_item(self.time)
        self.add_item(self.add_comment)

    async def on_submit(self, interaction: discord.Interaction):
        # Проверка полей
        for field in self.children:
            if not field.value.strip():
                await interaction.response.send_message(f"❌ Поле '{field.label}' не может быть пустым.", ephemeral=True)
                return

        # Отправляем ответ пользователю
        await interaction.response.send_message("✅ Ваша заявка на покупку отправлена!", ephemeral=True)

        # Отправляем заявку в канал
        try:
            channel = bot.get_channel(1437115914280767498)
            if channel:
                embed = discord.Embed(
                    title="📨 Новая заявка на покупку Fox-Vip", 
                    color=0x00ff00, 
                    timestamp=discord.utils.utcnow()
                )
                embed.add_field(name="Количество месяцев", value=self.time.value, inline=True)
                embed.add_field(name="Доп. комментарий", value=self.add_comment.value, inline=True)
                embed.set_footer(text=f"ID пользователя: {interaction.user.id} | {interaction.user.display_name}")
                await channel.send(embed=embed)
        except Exception as e:
            print(f"Ошибка отправки заявки: {e}")

class PurchaseFoxGoldModal(Modal, title="Покупка Fox-Gold"):
    def __init__(self):
        super().__init__(timeout=300)
        
        self.time = TextInput(
            label="Количество месяцев?", 
            placeholder="2", 
            required=True, 
            max_length=50
        )
        
        self.add_comment = TextInput(
            label="Дополнительный комментарий", 
            placeholder=" ", 
            required=True, 
            max_length=20
        )
        
        self.add_item(self.time)
        self.add_item(self.add_comment)

    async def on_submit(self, interaction: discord.Interaction):
        # Проверка полей
        for field in self.children:
            if not field.value.strip():
                await interaction.response.send_message(f"❌ Поле '{field.label}' не может быть пустым.", ephemeral=True)
                return

        # Отправляем ответ пользователю
        await interaction.response.send_message("✅ Ваша заявка на покупку отправлена!", ephemeral=True)

        # Отправляем заявку в канал
        try:
            channel = bot.get_channel(1437115914280767498)
            if channel:
                embed = discord.Embed(
                    title="📨 Новая заявка на покупку Fox-Gold", 
                    color=0x00ff00, 
                    timestamp=discord.utils.utcnow()
                )
                embed.add_field(name="Количество месяцев", value=self.time.value, inline=True)
                embed.add_field(name="Доп. комментарий", value=self.add_comment.value, inline=True)
                embed.set_footer(text=f"ID пользователя: {interaction.user.id} | {interaction.user.display_name}")
                await channel.send(embed=embed)
        except Exception as e:
            print(f"Ошибка отправки заявки: {e}")

class PurchaseAdminModal(Modal, title="Покупка Admin"):
    def __init__(self):
        super().__init__(timeout=300)
        
        self.time = TextInput(
            label="Количество месяцев?", 
            placeholder="2", 
            required=True, 
            max_length=50
        )
        
        self.add_comment = TextInput(
            label="Дополнительный комментарий", 
            placeholder=" ", 
            required=True, 
            max_length=20
        )
        
        self.add_item(self.time)
        self.add_item(self.add_comment)

    async def on_submit(self, interaction: discord.Interaction):
        # Проверка полей
        for field in self.children:
            if not field.value.strip():
                await interaction.response.send_message(f"❌ Поле '{field.label}' не может быть пустым.", ephemeral=True)
                return

        # Отправляем ответ пользователю
        await interaction.response.send_message("✅ Ваша заявка на покупку отправлена!", ephemeral=True)

        # Отправляем заявку в канал
        try:
            channel = bot.get_channel(1437115914280767498)
            if channel:
                embed = discord.Embed(
                    title="📨 Новая заявка на покупку Admin", 
                    color=0x00ff00, 
                    timestamp=discord.utils.utcnow()
                )
                embed.add_field(name="Количество месяцев", value=self.time.value, inline=True)
                embed.add_field(name="Доп. комментарий", value=self.add_comment.value, inline=True)
                embed.set_footer(text=f"ID пользователя: {interaction.user.id} | {interaction.user.display_name}")
                await channel.send(embed=embed)
        except Exception as e:
            print(f"Ошибка отправки заявки: {e}")

class PurchaseRoleSelect(Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Fox-Vip", description="Приобрести привилегию Fox-Vip", value="vip", emoji="💫"),
            discord.SelectOption(label="Fox-Gold", description="Приобрести привилегию Fox-Gold", value="gold", emoji="👑"),
            discord.SelectOption(label="Admin", description="Приобрести привилегию Admin", value="admin-purchase", emoji="❤️"),
        ]
        super().__init__(
            placeholder="Выбрать привилегию", 
            min_values=1, 
            max_values=1, 
            options=options,
            custom_id="purchase_select"
        )

    async def callback(self, interaction: discord.Interaction):
        try:
            if self.values[0] == "vip":
                modal = PurchaseFoxVipModal()
                await interaction.response.send_modal(modal)
            elif self.values[0] == "gold":
                modal = PurchaseFoxGoldModal()
                await interaction.response.send_modal(modal)
            elif self.values[0] == "admin-purchase":
                modal = PurchaseAdminModal()
                await interaction.response.send_modal(modal)
        except Exception as e:
            print(f"Ошибка в callback: {e}")
            if not interaction.response.is_done():
                await interaction.response.send_message("❌ Произошла ошибка. Попробуйте еще раз.", ephemeral=True)
            else:
                await interaction.followup.send("❌ Произошла ошибка. Попробуйте еще раз.", ephemeral=True)

class PurchaseRoleSelectView(View):
    def __init__(self):
        # timeout=None ОБЯЗАТЕЛЬНО для persistent View
        super().__init__(timeout=None)
        self.add_item(PurchaseRoleSelect())

@bot.command()
async def покупка(ctx):
    embed = discord.Embed()
    embed.set_image(url="https://i.pinimg.com/736x/28/54/8a/28548a67d9a0212b3f2e88690b3d0220.jpg")
    await ctx.send(embed=embed, view=PurchaseRoleSelectView())

class FoxGoldApplicationModal(Modal, title="Заявка на Fox-Gold"):
    def __init__(self):
        super().__init__(timeout=300)
        
        self.name_age = TextInput(
            label="Имя и возраст?", 
            placeholder="Аня, 20", 
            required=True, 
            max_length=50
        )
        
        self.time = TextInput(
            label="Время игры на проекте?", 
            placeholder=" ", 
            required=True, 
            max_length=50
        )
        
        self.add_item(self.name_age)
        self.add_item(self.time)

    async def on_submit(self, interaction: discord.Interaction):
        # Проверка полей
        for field in self.children:
            if not field.value.strip():
                await interaction.response.send_message(f"❌ Поле '{field.label}' не может быть пустым.", ephemeral=True)
                return

        # Отправляем ответ пользователю
        await interaction.response.send_message("✅ Ваша заявка на Fox-Gold отправлена!", ephemeral=True)

        # Отправляем заявку в канал
        try:
            channel = bot.get_channel(1436873561632538708)
            if channel:
                embed = discord.Embed(
                    title="📨 Новая заявка на Fox-Gold", 
                    color=0x00ff00, 
                    timestamp=discord.utils.utcnow()
                )
                embed.add_field(name="Имя и возраст", value=self.name_age.value, inline=True)
                embed.add_field(name="Время игры", value=self.time.value, inline=True)
                embed.set_footer(text=f"ID пользователя: {interaction.user.id} | {interaction.user.display_name}")
                await channel.send(embed=embed)
        except Exception as e:
            print(f"Ошибка отправки заявки: {e}")

class ServerProposeModal(Modal, title="Предложение по серверу"):
    def __init__(self):
        super().__init__(timeout=300)
        
        self.name_age = TextInput(
            label="Имя?", 
            placeholder="Аня", 
            required=True, 
            max_length=50
        )
        
        self.time = TextInput(
            label="Время игры на проекте?", 
            placeholder=" ", 
            required=True, 
            max_length=50
        )

        self.propose = TextInput(
            label="Ваше предложение",
            placeholder="Расскажите подробнее",
            required=True,
            max_length=500
        )
        
        self.add_item(self.name_age)
        self.add_item(self.time)
        self.add_item(self.propose)

    async def on_submit(self, interaction: discord.Interaction):
        # Проверка полей
        for field in self.children:
            if not field.value.strip():
                await interaction.response.send_message(f"❌ Поле '{field.label}' не может быть пустым.", ephemeral=True)
                return

        # Отправляем ответ пользователю
        await interaction.response.send_message("✅ Ваше предложение по серверу отправлено!", ephemeral=True)

        # Отправляем заявку в канал
        try:
            channel = bot.get_channel(1437084045962903643)
            if channel:
                embed = discord.Embed(
                    title="📨 Новое предложение по серверу", 
                    color=0x00ff00, 
                    timestamp=discord.utils.utcnow()
                )
                embed.add_field(name="Имя", value=self.name_age.value, inline=True)
                embed.add_field(name="Время игры", value=self.time.value, inline=True)
                embed.add_field(name="Предложение:", value=self.propose.value, inline=True)
                embed.set_footer(text=f"ID пользователя: {interaction.user.id} | {interaction.user.display_name}")
                await channel.send(embed=embed)
        except Exception as e:
            print(f"Ошибка отправки заявки: {e}")

class FoxProposeSelect(Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Fox-Gold", description="Бесплатный VIP для девушек", value="fox_propose", emoji="💅"),
            discord.SelectOption(label="Предложение", description="Предложить свою идею", value="propose", emoji="🗒️"),
        ]
        super().__init__(
            placeholder="Выбрать нужное", 
            min_values=1, 
            max_values=1, 
            options=options,
            custom_id="foxpropose_select"
        )

    async def callback(self, interaction: discord.Interaction):
        try:
            if self.values[0] == "fox_propose":
                modal = FoxGoldApplicationModal()
                await interaction.response.send_modal(modal)
            elif self.values[0] == "propose":
                modal = ServerProposeModal()
                await interaction.response.send_modal(modal)
        except Exception as e:
            print(f"Ошибка в callback: {e}")
            if not interaction.response.is_done():
                await interaction.response.send_message("❌ Произошла ошибка. Попробуйте еще раз.", ephemeral=True)
            else:
                await interaction.followup.send("❌ Произошла ошибка. Попробуйте еще раз.", ephemeral=True)

class FoxProposeSelectView(View):
    def __init__(self):
        # timeout=None ОБЯЗАТЕЛЬНО для persistent View
        super().__init__(timeout=None)
        self.add_item(FoxProposeSelect())

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