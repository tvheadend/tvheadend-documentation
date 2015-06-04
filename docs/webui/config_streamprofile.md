##Configuration - Stream - Stream Profile

##NOTE: <font color=red>INTRO TEXT REQUIRED</font>

##NOTE: <font color=red>SCREENSHOT REQUIRED</font>

---

####Menu Bar/Buttons

The following functions are available:

Button     | Function
-----------|---------
**Save**   | Save any changes made to the stream profile configuration.
**Undo**   | Undo any changes made to the stream profile configuration since the last save.
**Add**    | Add a new stream profile.
**Delete** | Delete an existing stream profile. 
**Help**   | Display this help page.

---

####Configuration Options

####Stream Profile Types

**MPEG-TS Pass-through /build-in**
: MPEG-TS pass through muxer (built-in)

**Matroska (mkv) /build-in**
: Matroska/WebM muxer (built-in)

**HTSP Stream Profile**
: HTSP Default Stream Settings

**MPEG-TS /av-lib**
: MPEG-TS stream muxer (libav)

**Matroska /av-lib**
: Matroska/WebM muxer (libav)

**Transcode /av-lib**
: Transcode video/audio/subtitles to different codecs and containers

####Transcoding Settings

**Container**
: Container to use for transcoded streams.

**Resolution**
: Vertical resolution (height) of the output video stream. Horizontal resolution
  is adjusted automatically to preserve aspect ratio.

**Channels**
: Channel layout for audio streams.

**Language**
: Currently unused.

**Video Codec**
: Codec for video stream.

* **Do not use**
: Don't output a video stream.

* **Copy codec type**
: Pass through video stream without transcoding.

**Video Bitrate**
: Video quality/bitrate of the transcoded video stream.

* **0: Automatic Setting (target quality)**
: The automatic setting is dependent on the used codec. The respective
  values used, are 5 for MPEG2 and 15 for H.264 and VP8.

* **1-63: Target Quality**
: Use the given value to achieve average quality. A lower value results
  in better quality. The resulting bitrate is dependent on the complexity
  of the video stream.

* **>63: Target Bitrate**
: Use the given value to achieve average bitrate. The resulting quality
  is dependent on the complexity of the video stream.

**Audio Codec**
: Codec for audio streams.

* **Do not use**
: Don't output an audio stream.

* **Copy codec type**
: Pass through audio streams without transcoding.

* **Audio Bitrate**
: Audio bitrate of the transcoded audio streams.

**Subtitles Codec**
: Codec for subtitles.

* **Do not use**
: Don't output subtitles.

* **Copy codec type**
: Pass through subtitles without transcoding.
