##Configuration - Debugging

!['Debugging' Tab](docresources/configtvhlog.png)

This tab is used to configure various debugging options in tvheadend.

---

####Menu Bar/Buttons

The following functions are available:

Button     | Function
-----------|---------
**Button** |
**Button** |
**Button** |


---

####Configuration options:

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
