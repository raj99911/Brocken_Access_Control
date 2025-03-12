import threading

from .packets import start_sniffing


def run_sniffer():
    sniffer_thread = threading.Thread(target=start_sniffing, daemon=True)
    sniffer_thread.start()
