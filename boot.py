# IDENTIFIER# IDENTIFIER# IDENTIFIER
# IDENTIFIER

# This file is executed on every boot (including wake-boot from deepsleep)
#import esp
#esp.osdebug(None)
#import webrepl
#webrepl.start()
import machine
from main.ota_updater import OTAUpdater


def download_and_install_update_if_available():
    credentials = ['aa','12345678']
    ota_updater = OTAUpdater('https://github.com/TheNameIsSamSamuelson/esp32', credentials)
    try:
        if ota_updater.check_for_update_to_install_during_next_reboot():
            machine.restart()
    except:
        pass
    ota_updater.download_and_install_update_if_available()

def start():

    # Start Main Loop ....
    import main.start
    # your custom code goes here. Something like this: ...
    # from main.x import YourProject

def boot():
    download_and_install_update_if_available()
    start()

boot()

# IDENTIFIER

#999999999999999999999999999
#6.0