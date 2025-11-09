import discord
from discord.ui import Modal, TextInput
from config import get_bot 

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
            bot = get_bot()
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
            bot = get_bot()
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
            bot = get_bot()
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