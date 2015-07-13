##Digital Video Recorder - Upcoming/Current Recordings

This tab show your all upcoming/current recordings.

!['Upcoming/Current Recordings' Tab](docresources/upcomingrecordings1.png)

---

####Menu Bar/Buttons

The following functions are available:

Button     | Function
-----------|----------
**Save**   | Saves any changes made to the recording list.
**Undo**   | Undo any changes made since the last save.
**Add**    | Add and configure a recording event by hand as opposed to choosing something from the EPG. This is useful if you wish to record something that isn’t yet in the EPG, or record at a particular time that perhaps spans several EPG events.
**Delete** | Delete the selected recording event. You will be prompted for confirmation.
**Abort**  | Abort an already-underway recording. Note that this does not remove the (partial) recording file from disk.
**Edit**   | Manually edit an already-scheduled recording event. This uses the same fields as **Add**, but they’re obviously pre-populated with their current values.
**Help**   | Display this help page.

---

####Add/Edit Dialog Example

A common set of fields is used for the _Add_ or _Edit_ functions, most
of which can also be seen in the grid view:

![Add/Edit Upcoming Recording](docresources/upcomingrecordings3.png)

---

####Grid Items

The main grid items have the following functions:

**Details**
: Shows the status of the recording event:


Icon                                       | Description
-------------------------------------------|-------------
![Clock icon](icons/clock.png)             | the programme is scheduled (upcoming)
![Recording icon](icons/rec.png)           | the programme is active and underway (current)
![Information icon](icons/information.png) | click to display detailed information about the selected recording (upcoming or current)

The detailed information dialog is as follows:

![Detailed Recording Information](docresources/upcomingrecordings2.png)

**Rerun Of**
: If the recording is a repeat (rerun) this field will display the date
the programme was previously broadcast. Note that this field is dependent
on your epg source.

**Title**
: The title (name) of the recording. While this is copied from the EPG
when you create a recording, it’s not used to match the event itself and
is thus used here as the name of the event (see also: adding an event
manually with the **Add** button).

**Subtitle**
: The programme episode title if available. Note that some broadcasters
(especially in the UK on Freeview) incorrectly insert the programme synopsis
into the subtitle section of the OTA EPG data.

**Episode**
: The episode number of the recording (whether this is available depends
on your broadcaster and/or EPG data source).

**Priority**
: The priority of the recording: Not set, Important, High, Normal, Low,
Unimportant. If there is a clash, more important recordings will take priority over
less important ones.

**Scheduled Start Time**
:The date and time when the scheduled recording will start. Note that
this includes any extra time defined in the recording profile (e.g.
“start two minutes earlier than the EPG start time”).

**Scheduled Stop Time**
: The date and time when the scheduled recording will stop. Note that this
includes any extra time defined in the recording profile (e.g. “finish
recording five minutes after the EPG stop time”).

**Duration**
: The total duration of the scheduled recording, including any extra time
before or after.

**File Size**
: The current file size of the in-progress recording. This will continue
to increase until the recording is complete.

**Channel**
: The channel to be recorded.

**Owner**
: The logged-in user who created the recording. This will be blank if the
user can't be verified.

**Creator**
: The user who created the recording or the auto-recording source and IP
address if scheduled by a matching rule.

**DVR Configuration**
: The DVR configuration to be used for this recording.

**Schedule Status**
: The status of the recording (scheduled or recording).

**Errors**
: The number of transport stream errors encountered during the recording.

**Data Errors**
: The number of continuity errors encountered during the recording.

**Comment**
: This field allows you to enter a note about the recording; you can enter
whatever you like here. This field will automatically be filled if the
recording was created by an auto-recording rule, although you can still
change it if you wish.

