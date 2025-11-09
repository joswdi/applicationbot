import discord
from discord.ui import Select, View
from forms.purchaserole_forms import PurchaseFoxVipModal, PurchaseFoxGoldModal, PurchaseAdminModal

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
        super().__init__(timeout=None)
        self.add_item(PurchaseRoleSelect())