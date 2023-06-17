from homeassistant import config_entries

class ConfigFlowHandler(config_entries.ConfigFlow, domain="fetch_latest_file"):
    async def async_step_import(self, user_input=None):
        return await self.async_step_user()

    async def async_step_user(self, user_input=None):
        if self._async_current_entries():
            return self.async_abort(reason='single_instance_allowed')
        return self.async_create_entry(title="Fetch latest File", data={})
