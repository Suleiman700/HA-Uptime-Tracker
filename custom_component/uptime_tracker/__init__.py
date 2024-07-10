"""Custom component for Uptime Tracker Sensors."""
DOMAIN = "uptime_tracker"

async def async_setup(hass, config):
    """Set up the Uptime Tracker Sensors component."""
    # Nothing needs to be done here for simple sensor components
    return True