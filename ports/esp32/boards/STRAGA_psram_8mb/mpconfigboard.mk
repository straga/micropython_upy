
SDKCONFIG += boards/sdkconfig.base
SDKCONFIG += boards/sdkconfig.spiram

SDKCONFIG += boards/STRAGA_board/sdkconfig.mod
PART_SRC = boards/STRAGA_board/8mb/partitions.csv
FROZEN_MANIFEST = boards/STRAGA_board/manifest_psram.py