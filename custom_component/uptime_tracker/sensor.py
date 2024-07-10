import logging
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from homeassistant.components.sensor import PLATFORM_SCHEMA
from homeassistant.const import CONF_NAME
from homeassistant.helpers.entity import Entity
from datetime import datetime

_LOGGER = logging.getLogger(__name__)

DOMAIN = 'uptime_tracker'

PLATFORM_SCHEMA = PLATFORM_SCHEMA.extend({
    vol.Optional(CONF_NAME): cv.string,
})

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    _LOGGER.debug("Setting up platform")
    name = config.get(CONF_NAME)

    sensors = [
        LastOfflineDurationSensor(hass, name),
        LastOnlineSensor(hass, name),
    ]

    async_add_entities(sensors, update_before_add=True)

class UptimeTrackerSensor(Entity):
    def __init__(self, hass, name, sensor_name):
        self._hass = hass
        self._name = name or sensor_name
        self._state = None
        self._initialized = False  # Flag to track if sensor has been initialized
        _LOGGER.debug(f"{sensor_name} initialized")

    async def async_update(self):
        _LOGGER.debug(f"Updating {self._name}")
        self._update_state()

    def _update_state(self):
        raise NotImplementedError

    @property
    def name(self):
        return self._name

    @property
    def state(self):
        return self._state

class LastOfflineDurationSensor(UptimeTrackerSensor):
    def __init__(self, hass, name):
        super().__init__(hass, name, 'Last Offline Duration')

    def _update_state(self):
        if not self._initialized:
            last_online_state = self._hass.states.get('sensor.uptime_tracker_last_online')
            if last_online_state and last_online_state.state:
                last_online_time = datetime.fromisoformat(last_online_state.state)
                current_time = datetime.now()
                duration_seconds = (current_time - last_online_time).total_seconds()
                self._state = round(duration_seconds)
                self._hass.states.async_set('sensor.uptime_tracker_last_offline_duration', self._state, {"friendly_name": "Last Offline Duration"})
                self._initialized = True
            else:
                self._state = None
            _LOGGER.debug(f"{self._name} state updated to: {self._state}")

class LastOnlineSensor(UptimeTrackerSensor):
    def __init__(self, hass, name):
        super().__init__(hass, name, 'Last Online')

    def _update_state(self):
        self._state = datetime.now().isoformat()
        self._hass.states.async_set('sensor.uptime_tracker_last_online', self._state, {"friendly_name": "Last Online"})
        _LOGGER.debug(f"{self._name} state updated to: {self._state}")