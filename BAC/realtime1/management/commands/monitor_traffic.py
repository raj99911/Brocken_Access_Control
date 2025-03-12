from django.core.management.base import BaseCommand
from scapy.all import sniff
from realtime1.utils import packet_callback

class Command(BaseCommand):
    help = "Start real-time packet monitoring"

    def handle(self, *args, **kwargs):
        self.stdout.write("Starting packet monitoring...")
        sniff(prn=packet_callback, store=False)
