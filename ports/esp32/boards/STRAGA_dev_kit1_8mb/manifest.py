freeze('$(PORT_DIR)/modules',  ('_boot.py', 'flashbdev.py', 'inisetup.py'))
freeze('$(MPY_DIR)/tools', ('upip_utarfile.py'))
freeze('$(MPY_DIR)/ports/esp8266/modules', 'ntptime.py')
freeze('$(MPY_DIR)/drivers/onewire')


#freeze('$(MPY_DIR)/tools', ('upip.py', 'upip_utarfile.py'))
#freeze('$(MPY_DIR)/ports/esp8266/modules', 'ntptime.py')
#freeze('$(MPY_DIR)/ports/esp8266/modules', ('webrepl.py', 'webrepl_setup.py', 'websocket_helper.py',))
#freeze('$(MPY_DIR)/drivers/dht', 'dht.py')
#freeze('$(MPY_DIR)/drivers/onewire')
