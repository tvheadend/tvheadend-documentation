##Configuration - Debugging

!['Debugging' Tab](docresources/configtvhlog.png)

This tab is used to configure various debugging options in tvheadend.

##NOTE:<font color=red>Rename this and the html to config_degugging for consistency</font>
---

####Menu Bar/Buttons

The following functions are available:

Button     | Function
-----------|---------
**Apply Configuration (run-time only)** | Saves any changes made to the debugging configuration. Changes will be lost on a restart.
**Help** | Display this help page


---

####Configuration Options

**Debug log path**
: text   

**Debug to syslog**
: text   

**Debug trace (low-level stuff)**
: text

**Debug subsystems**
: text   

**Trace subsystems**
: text   

Changes to any of these settings must be confirmed by pressing the ‘Save
configuration’ button before taking effect.

Note that the settings is not saved to a storage. It is available only
until the actual tvheadend process is running. If you like to change the
default behaviour permanently, use the command line options like `-l`,
`–debug`, `–trace`. This configuration is stored usually in the
/etc/sysconfig tree (depending on the distribution) or an init script.
