##Configuration - CAs

Tvheadend support connecting to card clients via the cwc (newcamd) and
capmt (dvbapi) protocols for so-called 'softcam' descrambling.

!['CAs' Tab](docresources/configcwc.png)

---

####Menu Bar/Buttons

The following functions are available:

Button              | Function
--------------------|---------
**Save**            | Save any changes made to the CA client configuration
**Undo**            | Undo any changes made to the CA client configuration since the last save.
**Add**             | Add a new CA client configuration.
**Delete**          | Delete an existing CA client configuration.
**Move Up**         | Move the selected CA client configuration up in the list.
**Move Down**       | Move the selected CA client configuration down in the list.
**Show Passwords**  | Reveals any stored CA client passwords.
**Help**            | Display this help page.

---

####Grid Items

The main grid items have the following functions:

**Enabled**
: If selected, connection will be tried to be established and retained up.
  If unselected, Tvheadend will disconnect (if connected) and not try to
  reconnect.

**Hostname**
: Server hostname. DNS lookup is performed upon every connection attempt.

**Port**
: Server TCP port

**Username**
: Username to use.

**Password**
: Password to use.

**DES Key**
: Initial DES key.

**Update Card**
: Forward Entitlement Management Messages (EMMs) to the server.

**Update One**
: Forward EMMs only from one channel at a time.

**Comment**
: Allows the administrator to set a comment only visible in this editor.
  It does not serve any active purpose.

!['CAs Tab 2'](docresources/configcapmt.png)

The servers are listed / edited in a grid.

* To edit a cell, double click on it. After a cell is changed it will
  flags one of its corner to red to indicated that it has been
  changed. To commit these changes back to Tvheadend press the ‘Save
  changes’ button. In order to change a Checkbox cell you only have to
  click once in it.

* To add a new entry, press the ‘Add entry’ button. The new (empty)
  entry will be created on the server but will not be in its enabled
  state. You can now change all the cells to the desired values, check
  the ‘enable’ box and then press ‘Save changes’ to activate the new
  entry.

* To delete one or more entries, select the lines (by clicking once on
  them), and press the ‘Delete selected’ button. A pop up will ask you
  to confirm your request.

The columns have the following functions:

**Enabled**
: If selected, connection will be tried to be established and retained up.
  If unselected, Tvheadend will disconnect (if connected) and not try to
  reconnect.

**Camd.socket Filename / IP Address**
: Socket filename which is usually opened by cam client. Tvheadend tries
  to connect to this socket file.

 In mode 3 (TCP), enter the IP address of the oscam server. Tvheadend
tries to create a TCP connecting to this IP adress and *Connect port*.

**Listen / Connect port**
: If running on a so called full-featured DVB-Card this can be left empty.
  Running on Budget-Cards one has to use a dummy ca-device. This is
  emulated via capmt\_ca.so. This module has to be pre-loaded prior to the
  cam client.
  
*LD\_PRELOAD=/path/to/capmt\_ca.so cam\_client &*

This module will communicate the received control-words back to
Tvheadend via Port 9000

 In mode 3 (TCP), this port is used for the oscam connection. It must be
equal to the listen port in the oscam/dvbapi settings.

**OSCam mode**

* **mode 0 (LD\_PRELOAD)**
: LD\_PRELOAD hack is active

* **mode 1 (old OSCam)**
: If selected, connection will be made directly to oscam without using
  LD\_PRELOAD hack. Port 9000 will be used automatically.

<div class="admonition note">
<p class="admonition-title">Usage Note for Mode 1</p>
<p>The following lines are required in <strong>[dvbapi]</strong> section of oscam.conf
file:</p>
<code>boxtype = pc
 pmt_mode = 4</code>
</div>

* **mode 2 (new OSCam since revision 9095)**
: In this mode, no UDP connections are required. All communication is
  processed though the Camd.socket. The configuration for OSCam should be
  same as for mode 1.

* **mode 3 (new OSCam since revision 9574)**
: A TCP connection to server is created. All emm/ecm data are send to
  oscam using this connection without a requirement for the real linuxdvb
  devices in the system with OSCam. This mode is suitable for all DVB
  devices including SAT\>IP and IPTV.

<div class="admonition note">
<p class="admonition-title">Usage Note for Mode 3</p>
<p>The following lines are required in <strong>[dvbapi]</strong> section of oscam.conf
file:</p>
<code>boxtype = pc
 pmt_mode = 4
 listen_port = 9000 # or your preferred port</code>
</div>

* **mode 4 (new OSCam since revision 9754)**
: Similar to mode 3, but a Camd.socket connection is used instead of the
  TCP connection.

<div class="admonition note">
<p class="admonition-title">Usage Note for Mode 4</p>
<p>The following lines are required in <strong>[dvbapi]</strong> section of oscam.conf
file:</p>
<code>boxtype = pc-nodmx
 pmt_mode = 4</code>
</div>

* **mode 5 (new OSCam since revision 10087)**
: Similar to mode 3 (TCP), but uses a new network protocol which also
  added client/server greeting messages and protocol version information
  (to be able to smoothly detect enhancements in the future).

<div class="admonition tip">
<p class="admonition-title">Note</p>
<p>Mode 5 is currently the preferred mode - others may be removed in the future</p>
</div>


<div class="admonition note">
<p class="admonition-title">Usage Note for Mode 5</p>
<p>The following lines are required in <strong>[dvbapi]</strong> section of oscam.conf
file:</p>
<code>boxtype = pc
 pmt_mode = 4
 listen_port = 9000 # or your preferred port</code>
</div>

**Comment**
Allows the administrator to set a comment only visible in this editor.
It does not serve any active purpose.
