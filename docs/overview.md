##Overview of Tvheadend

###Welcome to Tvheadend!

Tvheadend is a lightweight, easily-configured, general-purpose TV/video 
streaming server and recorder (PVR/DVR) for GNU/Linux, FreeBSD and Android.
It supports input from:

* **Satellite**: DVB-S/S2
* **Cable**: DVB-C
* **Terrestrial/OTA**: DVB-T/T2, ATSC
* **LAN**: IPTV, SAT>IP, HDHomeRun and general-purpose MPEG-TS `pipe://`

As well as being able to record the input, Tvheadend also offers it up to
client applications via HTTP (VLC, MPlayer), HTSP (Kodi, Movian) and SAT>IP
streaming.

Analogue video (V4L) is no longer supported directly. If you still need this,
or need to input signals from video cameras or other non-broadcast sources,
use `pipe://`.

The code is hosted at [github](https://github.com/tvheadend/tvheadend).
Please use github's features if you want to provide patches. Contributions and improvements are always welcome.
