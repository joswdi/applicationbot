import discord
from discord.ui import Select, View
from forms.admin_forms import AdminApplicationModal, ModerApplicationModal, ContentMakerApplicationModal, EventerApplicationModal

class RoleSelect(Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="Administrator", description="Подать заявку на роль администратора", value="admin", emoji="👑"),
            discord.SelectOption(label="Moderator", description="Подать заявку на роль модератора", value="moder", emoji="⚡"),
            discord.SelectOption(label="Content Maker", description="Подать заявку на роль контент мейкера", value="content_maker", emoji="🦋"),
            discord.SelectOption(label="Eventer", description="Подать заявку на роль ивентёра", value="eventer", emoji="🎲"),
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
            elif self.values[0] == "content_maker":
                modal = ContentMakerApplicationModal()
                await interaction.response.send_modal(modal)
            elif self.values[0] == "eventer":
                modal = EventerApplicationModal()
                await interaction.response.send_modal(modal)
        except Exception as e:
            print(f"Ошибка в callback: {e}")
            if not interaction.response.is_done():
                await interaction.response.send_message("❌ Произошла ошибка. Попробуйте еще раз.", ephemeral=True)
            else:
                await interaction.followup.send("❌ Произошла ошибка. Попробуйте еще раз.", ephemeral=True)

class RoleSelectView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.add_item(RoleSelect())