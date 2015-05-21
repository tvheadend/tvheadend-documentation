##Overview of Tvheadend

####Welcome to Tvheadend!

Tvheadend is a lightweight, easily-configured, general-purpose TV/video streaming server and recorder (PVR/DVR) for GNU/Linux, FreeBSD and Android. It supports input from:

* **Satellite**: DVB-S, DVB-S2
* **Cable**: DVB-C
* **Terrestrial/OTA**: DVB-T, ATSC
* **LAN**: IPTV, SAT>IP, HDHomeRun and general-purpose MPEG-TS _pipe://_

As well as being able to record the input, Tvheadend also offers it up to client applications via HTTP (VLC, MPlayer), HTSP (Kodi, Movian) and SAT>IP streaming.

Analogue video (V4L) was supported directly in previous versions of Tvheadend, up to version 3.4. However, due to the death of analogue signals in many places, this has now been deprecated.

Instead, in recent versions, you can use a pipe:// source to input an analogue signal that's been exterally remuxed into MPEG-TS (e.g. with ffmpeg/libav from a V4L device). You can also use this to input signals from video cameras and other non-broadcast sources. Please see the user guide for more information.

The code is hosted at [github](https://github.com/tvheadend/tvheadend).
Please use github's features if you want to provide patches. Contributions and improvements are always welcome
