folder_board = "STRAGA_factory_8mb"

freeze('$(PORT_DIR)/modules',  ('_boot.py', 'flashbdev.py','inisetup.py'))
freeze('$(MPY_DIR)/tools', ('upip_utarfile.py'))
freeze('$(MPY_DIR)/ports/esp8266/modules', 'ntptime.py')
freeze('$(MPY_DIR)/drivers/onewire')

freeze('$(PORT_DIR)/boards/modules/ftp_recovery')


#freeze('$(PORT_DIR)/boards/modules/upy_core')


# freeze('$(PORT_DIR)/boards/modules/boot',  ('inisetup.py'))

# freeze('$(PORT_DIR)/boards/{}/modules'.format(folder_board))


# freeze('$(PORT_DIR)/modules',  ('_boot.py', 'flashbdev.py', 'inisetup.py'))
#freeze('$(MPY_DIR)/tools', ('upip.py', 'upip_utarfile.py'))
#freeze('$(MPY_DIR)/ports/esp8266/modules', 'ntptime.py')
#freeze('$(MPY_DIR)/ports/esp8266/modules', ('webrepl.py', 'webrepl_setup.py', 'websocket_helper.py',))
#freeze('$(MPY_DIR)/drivers/dht', 'dht.py')
#freeze('$(MPY_DIR)/drivers/onewire')
