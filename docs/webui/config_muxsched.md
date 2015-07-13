##Configuration - DVB Inputs - Mux Schedulers

Mux Schedulers enable Tvheadend to automatically play channels. This is
useful to get EPG, services or access rights updates.

!['Mux Schedulers \'Add\' Dialog' Tab](docresources/configdvbmuxsched.png)

---

####Menu Bar/Buttons

The following functions are available:

Button             | Function
-------------------|---------
**Save**           | Save any changes made to the mux schedulers.
**Undo**           | Undo any changes made to the mux schedulers since the last save.
**Add**            | Add a new mux scheduler.
**Delete**         | Delete an existing mux scheduler.
**Edit**           | Edit an existing mux scheduler.
**Hide <option\>** | <font color=red>??????</font>. Options are Parent Disabled, All, None
**Help**           | Displays this help page. 

---

####Add/Edit Dialog Example

A common set of fields is used for the _Add_ or _Edit_ functions, most
of which can also be seen in the grid view:

!['Mux Schedulers \'Add\' Dialog' Tab](docresources/configdvbmuxsched1.png)

---

####Grid Items

The main grid items have the following functions:

**Enabled**
: If selected, schedule will be triggered. If unselected, schedule will be
  ignored.

**Mux**
: Select mux to be played from the available muxes.

**Cron**
: Schedule frequency, using cron syntax. *Example : every day at 2am is `0 2 \* \* \*`*

**Timeout**
: Time in seconds the selected mux will be played. *Example : 1 hour would be `3600`*
