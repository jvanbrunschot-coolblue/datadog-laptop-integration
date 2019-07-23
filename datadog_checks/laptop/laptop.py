from datadog_checks.base import AgentCheck
import psutil


class LaptopCheck(AgentCheck):
    def check(self, instance):
        tags = []
        custom_tags = instance.get('custom_tags', [])
        if not isinstance(custom_tags, list):
            raise Exception("Custom tags must be a list")

        tags.extend(custom_tags)

        battery = psutil.sensors_battery()

        self.gauge('laptop.battery_percentage', battery.percent, tags=[tags])

        self.service_check('laptop.health', self.OK)
