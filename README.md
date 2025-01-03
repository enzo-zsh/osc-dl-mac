
# Open Shop Channel DL for Mac [![Actions Status](https://github.com/dhtdht020/osc-dl/workflows/Build/badge.svg)](https://github.com/dhtdht020/osc-dl/actions) [![Discord Server](https://img.shields.io/discord/426478571389976577.svg)](https://discord.gg/by6mR5N) [![Downloads](https://img.shields.io/github/downloads/dhtdht020/osc-dl/total)](https://github.com/dhtdht020/osc-dl/releases) [![License](https://img.shields.io/badge/Open%20Source-GPL--3.0-lightgrey.svg)](https://github.com/dhtdht020/osc-dl/blob/master/LICENSE)

OSCDL is a cross platform desktop client for the Open Shop Channel homebrew repository, in Python 3 and Qt.

OSCDL for Mac is the Python 3 and Qt app but buildable as a macOS application using PyInstaller.

With OSCDL, you can download hundreds of homebrew apps and themes to your computer send them directly to the Wii through the network or through USB Gecko.

![Preview](https://user-images.githubusercontent.com/18469146/144217304-b690eba3-4c71-4791-9705-6dd36c0a1fcd.png)

## Installing OSCDL-for-Mac

I recommend obtaining the latest release from [here](https://github.com/enzo-zsh/osc-dl-mac/releases) if you are a macOS user.

#### Manual Download:

1. `git clone https://github.com/enzo-zsh/osc-dl-mac.git`
2. `cd osc-dl-mac`
2. `pip install pyinstaller`
3. `pyinstaller osc-dl-mac.spec`
4. Go to `dist`folder and run`OSC-DL for Mac.app`

#### USBGecko setup:

See [USBGecko information on WiiBrew](https://wiibrew.org/wiki/USB_Gecko) for device details.

When downloading drivers (if necessary), please use the COM (VCP) drivers instead of the D2XX API.

##### Licences:

All right reserved at dhtdht020 the creator of OSC-DL.