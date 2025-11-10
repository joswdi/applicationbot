import discord
from discord.ui import Modal, TextInput
from config import get_bot 

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
            bot = get_bot()
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
        for field in self.children:
            if not field.value.strip():
                await interaction.response.send_message(f"❌ Поле '{field.label}' не может быть пустым.", ephemeral=True)
                return

        await interaction.response.send_message("✅ Ваша заявка на роль Moderator отправлена!", ephemeral=True)

        try:
            bot = get_bot()
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

class ContentMakerApplicationModal(Modal, title="Заявка на роль Content Maker"):
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
            label="Есть опыт работы контент мейкером? Какой?", 
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
        
        self.add_item(self.name_age)
        self.add_item(self.device)
        self.add_item(self.experience)
        self.add_item(self.rules_knowledge)

    async def on_submit(self, interaction: discord.Interaction):
        for field in self.children:
            if not field.value.strip():
                await interaction.response.send_message(f"❌ Поле '{field.label}' не может быть пустым.", ephemeral=True)
                return

        await interaction.response.send_message("✅ Ваша заявка на роль Content Maker отправлена!", ephemeral=True)

        try:
            bot = get_bot()
            channel = bot.get_channel(1436873561632538708)
            if channel:
                embed = discord.Embed(
                    title="📨 Новая заявка на Content Maker", 
                    color=0xffff00, 
                    timestamp=discord.utils.utcnow()
                )
                embed.add_field(name="Имя и возраст", value=self.name_age.value, inline=True)
                embed.add_field(name="Устройство", value=self.device.value, inline=True)
                embed.add_field(name="Опыт работы", value=self.experience.value, inline=False)
                embed.add_field(name="Знание правил", value=self.rules_knowledge.value, inline=False)
                embed.set_footer(text=f"ID пользователя: <@{interaction.user.id}>")
                await channel.send(embed=embed)
        except Exception as e:
            print(f"Ошибка отправки заявки: {e}")

class EventerApplicationModal(Modal, title="Заявка на роль Eventer"):
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
            label="Есть опыт работы ивентёром? Какой?", 
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
        
        self.microphone = TextInput(
            label="Хороший ли у вас микрофон?", 
            placeholder="Да/нет", 
            style=discord.TextStyle.paragraph, 
            required=True, 
            max_length=50
        )
        
        self.add_item(self.name_age)
        self.add_item(self.device)
        self.add_item(self.experience)
        self.add_item(self.rules_knowledge)
        self.add_item(self.microphone)

    async def on_submit(self, interaction: discord.Interaction):
        for field in self.children:
            if not field.value.strip():
                await interaction.response.send_message(f"❌ Поле '{field.label}' не может быть пустым.", ephemeral=True)
                return

        await interaction.response.send_message("✅ Ваша заявка на роль Eventer отправлена!", ephemeral=True)

        try:
            bot = get_bot()
            channel = bot.get_channel(1436873561632538708)
            if channel:
                embed = discord.Embed(
                    title="📨 Новая заявка на Eventer", 
                    color=0xffff00, 
                    timestamp=discord.utils.utcnow()
                )
                embed.add_field(name="Имя и возраст", value=self.name_age.value, inline=True)
                embed.add_field(name="Устройство", value=self.device.value, inline=True)
                embed.add_field(name="Опыт работы", value=self.experience.value, inline=False)
                embed.add_field(name="Знание правил", value=self.rules_knowledge.value, inline=False)
                embed.add_field(name="Хороший микрофон", value=self.microphone.value, inline=False)
                embed.set_footer(text=f"ID пользователя: <@{interaction.user.id}>")
                await channel.send(embed=embed)
        except Exception as e:
            print(f"Ошибка отправки заявки: {e}")