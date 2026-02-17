from django.apps import AppConfig
import threading

class MonitoringConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'monitoring'

    def ready(self):
        from .mqtt_client import start_mqtt
        thread = threading.Thread(target=start_mqtt)
        thread.daemon = True
        thread.start()
