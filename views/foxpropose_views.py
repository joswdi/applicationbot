import discord
from discord.ui import Select, View
from forms.foxpropose_forms import FoxGoldApplicationModal, ServerProposeModal

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
        super().__init__(timeout=None)
        self.add_item(FoxProposeSelect())