import discord
from discord.ui import Modal, TextInput
from config import get_bot 

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

        await interaction.response.send_message("✅ Ваша заявка на Fox-Gold отправлена!", ephemeral=True)

        try:
            bot = get_bot()
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
            bot = get_bot()
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