<div class="hts-doc-text">

SDTV and HDTV support
H264 and MPEG2 video supported. AC-3, AAC(-HE) and MP2 audio supported.
DVB subtitles supported.
Input sources

DVB-T, DVB-C, DVB-S, DVB-S2, ATSC and SAT\>IP. 
:   Multiple adapters are supported. Each adapter can receive all
    programs available on the currently tuned mux simultaneously.

Multicasted IPTV. 
:   Both raw transport streams in UDP and transport stream in RTP in UDP
    is supported. The presence of RTP is autodetected.

Analog TV 
:   The IPTV extension URL - pipe:// allow to process any MPEG-TS input.
    FFMPEG or LIBAV library can be used to produce analog to digital
    conversion.

Output targets
HTTP (Web Protocol), supported by [VLC](http://www.videolan.org/vlc/),
[MPlayer](http://www.mplayerhq.hu)
HTSP (Home TV Streaming Protocol), supported by [Movian Media
player](http://movian.tv) and [Kodi](http://kodi.tv/)
SAT\>IP Server
The Built-in Digital Video Recorder
Modern web user interface
Entire application loaded into browser. No page refreshes or slow
updates. Based on [ExtJS](http://www.extjs.com/).
Easy to administrate and configure
All setup and configuration is done from the built in web user
interface. Even so, all settings are stored in human readable text
files.
Fully integrated with HTS Movian Media player or Kodi HTS PVR addon.
All channel data and their grouping, EPG and TV streaming is conducted
over a single TCP connection.
Digital Video Recorder
Built in video recorder stores recorded programs as either [Matroska
(.mkv)](http://www.matroska.org/) or MPEG TS (.ts) files. Multiple
simultaneous recordings are supported. All original streams (multiple
audio tracks, etc) are recorded.
Electronic Program Guide
Imports data from DVB and Internet providers such as
[XMLTV](http://www.xmltv.org). Searchable from the web user interface.
Results can be scheduled for recording with a single click.
Automatic recordings
Create rule-sets manually or based on EPG queries that will record all
future programs matching the query. Great for recording your favorite
TV-show(s).
Easy DVB setup
Tvheadend includes list of all major DVB-T, DVB-C and DVB-S networks
around the globe. Just pick your location from a list. Next, it can scan
all services and only map those which can be correctly decoded. Avoids
having lots of unusable channels in your Media player.
Multi-user support
Grant access to various system features based on username / password
and/or IP address.
Software based CSA descrambling
Requires a card server (newcamd and capmt protocol is supported).
Hardware based CSA descrambling
Requires the standard dvben50221 linuxdvb library.
Internationalization
All text is encoded in UTF-8 to provide full international support. All
major character encodings in DVB is supported.

</div>
