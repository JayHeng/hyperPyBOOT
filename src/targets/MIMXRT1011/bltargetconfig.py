#!/usr/bin/env python

# Copyright (c) 2014 Freescale Semiconductor, Inc.
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without modification,
# are permitted provided that the following conditions are met:
#
# o Redistributions of source code must retain the above copyright notice, this list
#   of conditions and the following disclaimer.
#
# o Redistributions in binary form must reproduce the above copyright notice, this
#   list of conditions and the following disclaimer in the documentation and/or
#   other materials provided with the distribution.
#
# o Neither the name of Freescale Semiconductor, Inc. nor the names of its
#   contributors may be used to endorse or promote products derived from this
#   software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
# ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR
# ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
# (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
# LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON
# ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
# SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import sys, os
sys.path.append(os.path.abspath(".."))
from boot.memoryrange import MemoryRange
from ui import RTyyyy_uidef
from ui import RTyyyy_uidef_efuse
from ui import uidef

cpu = 'MIMXRT1011'
board = 'EVK'
compiler = 'iar'
build = 'Release'

availablePeripherals = 0x11
romUsbVid = '0x1FC9'
romUsbPid = '0x0145'
hasSdpReadRegisterCmd = False
flashloaderUsbVid = '0x15A2'
flashloaderUsbPid = '0x0073'
flashloaderLoadAddr = 0x20205800
flashloaderJumpAddr = 0x20205800
availableCommands = 0x5EFDF
supportedPeripheralSpeed_uart = [4800, 9600, 19200, 57600, 115200] # @todo Verify
availableSecureBootTypes = [RTyyyy_uidef.kSecureBootType_Development,
                            RTyyyy_uidef.kSecureBootType_HabAuth,
                            RTyyyy_uidef.kSecureBootType_OtfadCrypto
                            ]
hasRemappedFuse = False
availableBootDevices = [RTyyyy_uidef.kBootDevice_FlexspiNor]
flexspiNorDevice = uidef.kFlexspiNorDevice_Adesto_AT25SF128A
flexspiNorMemBase = 0x60000000
xspiNorCfgInfoOffset = 0x400
flexspiNorEfuseBootCfg0Bits = 3
isNonXipImageAppliableForXipableDeviceUnderClosedHab = True
isSipFlexspiNorDevice = False
isEccTypeSetInFuseMiscConf = False
isSwEccSetAsDefaultInNandOpt = None

quadspiNorDevice = None
quadspiNorMemBase = None

efusemapIndexDict = RTyyyy_uidef_efuse.efusemapIndexDict_RT10yy

efuse_0x460_bit6     = {'BL_UART_INT':               ['0 - Enabled', '1 - Disabled']}
efuse_0x460_bit13_12 = {'OTFAD_KEY0_SEL':            ['00 - From OTPMK[127:0]', '01 - From OTPMK[255:128]', '10 - From SW-GP2', '11 - From SW-GP2']}
efuseDescDiffDict = {'0x400_lock_bit7' :        RTyyyy_uidef_efuse.efuse_temp_reserved1,
                     '0x400_lock_bit14':        RTyyyy_uidef_efuse.efuse_temp_reserved1,
                     '0x400_lock_bit15':        RTyyyy_uidef_efuse.efuse_temp_reserved1,
                     '0x400_lock_bit17':        RTyyyy_uidef_efuse.efuse_temp_reserved1,
                     '0x400_lock_bit20':        RTyyyy_uidef_efuse.efuse_temp_reserved1,
                     '0x400_lock_bit25_24':     RTyyyy_uidef_efuse.efuse_temp_reserved2,

                     '0x460_bootcfg1_bit6'    : efuse_0x460_bit6,
                     '0x460_bootcfg1_bit13_12': efuse_0x460_bit13_12,
                     '0x460_bootcfg1_bit15_14': RTyyyy_uidef_efuse.efuse_temp_reserved2,
                     '0x460_bootcfg1_bit24'   : RTyyyy_uidef_efuse.efuse_temp_reserved1,
                     '0x460_bootcfg1_bit29'   : RTyyyy_uidef_efuse.efuse_temp_reserved1,
                     '0x460_bootcfg1_bit31_30': RTyyyy_uidef_efuse.efuse_temp_reserved2,

                     '0x470_bootcfg2_bit0':     RTyyyy_uidef_efuse.efuse_temp_reserved1,
                     '0x470_bootcfg2_bit3':     RTyyyy_uidef_efuse.efuse_temp_reserved1,
                     '0x470_bootcfg2_bit5':     RTyyyy_uidef_efuse.efuse_temp_reserved1,
                     '0x470_bootcfg2_bit6':     RTyyyy_uidef_efuse.efuse_temp_reserved1,
                     '0x470_bootcfg2_bit7':     RTyyyy_uidef_efuse.efuse_temp_reserved1,
                     '0x470_bootcfg2_bit8':     RTyyyy_uidef_efuse.efuse_temp_reserved1,
                     '0x470_bootcfg2_bit9':     RTyyyy_uidef_efuse.efuse_temp_reserved1,
                     '0x470_bootcfg2_bit11':    RTyyyy_uidef_efuse.efuse_temp_reserved1,
                     '0x470_bootcfg2_bit12':    RTyyyy_uidef_efuse.efuse_temp_reserved1,
                     '0x470_bootcfg2_bit13':    RTyyyy_uidef_efuse.efuse_temp_reserved1,
                     '0x470_bootcfg2_bit14':    RTyyyy_uidef_efuse.efuse_temp_reserved1,
                     '0x470_bootcfg2_bit15':    RTyyyy_uidef_efuse.efuse_temp_reserved1,
                     '0x470_bootcfg2_bit30_24': RTyyyy_uidef_efuse.efuse_temp_reserved7,
                     '0x470_bootcfg2_bit31':    RTyyyy_uidef_efuse.efuse_temp_reserved1,

                     '0x6d0_miscconf0_bit11_8': RTyyyy_uidef_efuse.efuse_temp_reserved4,
                     '0x6d0_miscconf0_bit19_16':RTyyyy_uidef_efuse.efuse_0x6d0_flexramPartion128KB,
                     '0x6d0_miscconf0_bit24':   RTyyyy_uidef_efuse.efuse_temp_reserved1,
                     '0x6d0_miscconf0_bit26_25':RTyyyy_uidef_efuse.efuse_temp_reserved2,
                     '0x6d0_miscconf0_bit27':   RTyyyy_uidef_efuse.efuse_temp_reserved1,
                     '0x6d0_miscconf0_bit29_28':RTyyyy_uidef_efuse.efuse_temp_reserved2,
                     '0x6d0_miscconf0_bit31_30':RTyyyy_uidef_efuse.efuse_temp_reserved2,

                     '0x6e0_miscconf1_bit0':    RTyyyy_uidef_efuse.efuse_temp_reserved1,
                     '0x6e0_miscconf1_bit3_1':  RTyyyy_uidef_efuse.efuse_temp_reserved3,
                     '0x6e0_miscconf1_bit5_4':  RTyyyy_uidef_efuse.efuse_temp_reserved2,
                     '0x6e0_miscconf1_bit6':    RTyyyy_uidef_efuse.efuse_temp_reserved1,
                     '0x6e0_miscconf1_bit11_8': RTyyyy_uidef_efuse.efuse_temp_reserved4,
                     '0x6e0_miscconf1_bit15_12':RTyyyy_uidef_efuse.efuse_temp_reserved4,
                     '0x6e0_miscconf1_bit23_16':RTyyyy_uidef_efuse.efuse_temp_reserved8,
                     '0x6e0_miscconf1_bit31_24':RTyyyy_uidef_efuse.efuse_temp_reserved8,
                    }

# memory map
memoryRange = {
    # ITCM, 128KByte
    'itcm' : MemoryRange(0x00000000, 0x20000, 'state_mem0.dat'),
    # DTCM, 128KByte
    'dtcm' : MemoryRange(0x20000000, 0x20000, 'state_mem1.dat'),
    # OCRAM, 128KByte
    'ocram' : MemoryRange(0x20200000, 0x20000, 'state_mem2.dat'),

    # FLASH, 64KByte / 512MByte
    'flash': MemoryRange(0x00000000, 0x20000000, 'state_flash_mem.dat', True, 0x10000)
}

reservedRegionDict = {   # new
    # OCRAM, 22KB
    'ram' : [0x20200000, 0x202057FF]
}

