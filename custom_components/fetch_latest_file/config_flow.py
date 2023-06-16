from homeassistant import config_entries

DOMAIN = "latest"

class FetchLatestFileConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1
    CONNECTION_CLASS = config_entries.CONN_CLASS_LOCAL_PUSH

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            return self.async_create_entry(title="Fetch Latest File", data={})

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema({}),
        )
