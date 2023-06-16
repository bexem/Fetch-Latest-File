from homeassistant import config_entries

class FetchLatestFileConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="Fetch Latest File", data={})

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({}),
        )
