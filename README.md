<img src="img/logo.png" height=120 width=120>

# ExplorerOS
Completely free custom ROM for Google Glass **Explorer Edition**

# Introduction

I made this custom ROM to bring Google Glass back to life after more than 13 years. It's based on the latest XE24, with some optimization tweaks from me, plus a completely new launcher.

# Features

- XE apps support (like GlassTube)
- Updated certificates
- Brand new launcher
- Gemini integration
- Improved battery life
- Customization (15+ Glassfaces)
- Modern design

# Builds

| Title | Version | Channel | Download
|-------| --------|--------|---------|
| ExplorerOS 26.0 Public Beta 1 | 26.0 (200626PB1) | Stable | [Download](https://drive.google.com/drive/folders/1sthRXSZ63CTTSfoUvg8625V3FmW4pmbe?usp=sharing) |

# Installation (currently Windows only)

#### **Before installing**: see "Post-install"

1. Download this repository
2. Download an ExplorerOS build from "Builds"
3. Install ADB & Fastboot drivers (you can use my other tool - Glassy)
4. Unpack the ExplorerOS build into the ``builds/ExplorerOS-<version>`` folder
5. Enable USB Debugging on your Glass
6. Connect your Glass to the PC and run **ExplorerFlasher.exe**



# Post-install

1. Go to [Weather API](https://www.weatherapi.com) and get your API Key (free)
2. Go to [Open Router](https://openrouter.ai), add $5 to your balance, and get your API Key (paid)
3. To use AI, you need a Python Flask server. If you don't want to set it up, you can use my server instead.

# Server Setup

> [!TIP]
> If you don't want to buy a server, you can use my server completely free

1. Install Python on your Linux Server
2. Run: ``pip3 install flask requests`` (if you have any errors, add ``--break-system-packages``)
3. Download ``server/server.py`` on your server and run it: ``python3 server.py``

# Support

We have a discord server! [Join ExplorerOS Discord Server](https://discord.gg/DSkWE3JjG)


# System itself

##### Home screen:

<img src="img/screenshot1.png" width=320 height=180>

- Use the touchpad to navigate between cards
- Tap once to select a new Glassface
- Press the Camera button to activate Gemini

##### Weather Card:

<img src="img/screenshot2.png" width=320 height=180>

- Tap once to update the widget info

##### Gemini Demo:

<img src="img/screenshot3.png" width=320 height=180>

<img src="img/screenshot4.png" width=320 height=180>

- Press the Camera button to close Gemini
