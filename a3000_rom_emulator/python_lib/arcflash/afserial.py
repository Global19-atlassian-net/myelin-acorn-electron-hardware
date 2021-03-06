from __future__ import print_function
# Copyright 2017 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import glob
import os
import serial
import serial.tools.list_ports

def guess_port():
    # Look for modern ARCFLASH_PORT env var
    port = os.environ.get("ARCFLASH_PORT")
    if port:
        print("Using %s from ARCFLASH_PORT environment variable" % port)
        return port

    # Look for old-style ROM_PORT env var
    port = os.environ.get("ROM_PORT")
    if port:
        print("Using %s from ROM_PORT environment variable" % port)
        return port

    # Try to detect a connected Arcflash or Circuit Playground
    arcflash_port = circuitplay_port = None
    for port in serial.tools.list_ports.comports():
        print(port.device,
            port.product,
            port.hwid,
            port.vid,
            port.pid,
            port.manufacturer,
        )
        if port.vid == 0x1209 and port.pid == 0xFE07:
            print("Found an Arcflash at %s" % port.device)
            arcflash_port = port.device
        elif port.vid == 0x239A and port.pid in (0x0018, 0x8018):
            print("Found a Circuit Playground Express at %s" % port.device)
            circuitplay_port = port.device

    if arcflash_port:
        print("Detected an Arcflash on %s" % arcflash_port)
        return arcflash_port

    if circuitplay_port:
        print("Detected a Circuit Playground (probably an Arcflash) on %s" % circuitplay_port)
        return circuitplay_port

    raise Exception("Could not find a connected Arcflash")

class Port:
    def __init__(self):
        port = guess_port()
        if not port:
            raise Exception("Could not guess serial port")

        print("Opening port %s" % port)
        self.ser = serial.Serial(port, timeout=0)
        print("Serial port opened: %s" % repr(self.ser))

    def __enter__(self):
        return self.ser

    def __exit__(self, type, value, traceback):
        self.ser.close()
