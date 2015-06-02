##Overview of Tvheadend

###Welcome to Tvheadend!

Tvheadend is a lightweight, easily-configured, general-purpose TV/video streaming server and recorder (PVR/DVR) for GNU/Linux, FreeBSD and Android. It supports input from:

* **Satellite**: DVB-S, DVB-S2
* **Cable**: DVB-C
* **Terrestrial/OTA**: DVB-T, ATSC
* **LAN**: IPTV, SAT>IP, HDHomeRun and general-purpose MPEG-TS _pipe://_

As well as being able to record the input, Tvheadend also offers it up to client applications via HTTP (VLC, MPlayer), HTSP (Kodi, Movian) and SAT>IP streaming.

Analogue video (V4L) was supported directly in previous versions of Tvheadend, up to version 3.4. However, due to the death of analogue signals in many places, this has now been deprecated.

Instead, in recent versions, you can use a pipe:// source to input an analogue signal that's been exterally remuxed into MPEG-TS (e.g. with ffmpeg/libav from a V4L device). You can also use this to input signals from video cameras and other non-broadcast sources. Please see the user guide for more information.

The code is hosted at [github](https://github.com/tvheadend/tvheadend).
Please use github's features if you want to provide patches. Contributions and improvements are always welcome.

###Basic Requirements

Tvheadend runs on **Linux** - pre-built binaries are available for most 
Debian-based distributions (Debian itself, Ubuntu, Mint...) and RPMs for
Fedora.

You will only need **c. 30MB disk space** for the application and associated
files, and maybe anything up to **1GB** for your configuration - depending on 
how many tuners of what type you have, how many channels you receive, your
choice of programme guide, and so on. You'll clearly need much more for
your recordings, though: as a guide, an hour of SD MPEG-2 video will take
about 1GB, while high bitrate HD H.264 will easily consume 5GB+ per hour.

Tvheadend is intended to be lightweight, so it will run on a NAS or similar
**low-powered CPU**. Note that the exception here is transcoding: if you want
to convert high-definition video in real time then you will need a powerful,
multi-core system. It will happily run in less than **1GB of RAM**, and many
people run it successfully on original Raspberry Pis with perhaps only 256MB
of usable free memory. This does depend on what else you're using the computer
for, though, as a GUI will drain your system as will any serious file serving.

And, of course, you'll need one or more **TV tuners** if you want to receive
regular broadcast television - otherwise, you're limited to IP sources.

It's perfectly possible to install and run Tvheadend as a single-seat installation,
with the software running on the same system as any client software (e.g. Kodi),
with all files stored locally.
