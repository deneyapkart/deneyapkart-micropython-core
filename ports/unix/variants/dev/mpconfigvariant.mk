PROG ?= micropython-dev

FROZEN_MANIFEST ?= $(VARIANT_DIR)/manifest.py

MICROPY_ROM_TEXT_COMPRESSION = 1
MICROPY_VFS_FAT = 1
MICROPY_VFS_LFS1 = 1
MICROPY_VFS_LFS2 = 1

MICROPY_PY_BLUETOOTH ?= 1