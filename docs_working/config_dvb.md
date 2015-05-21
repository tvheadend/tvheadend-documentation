<div class="hts-doc-text">

General tab
The general tab contains information and some per-adapter global
configuration.
Add DVB Network by location…
Pressing this button will popup a window that allows the user to select
a DVB network based on location. The adapter will be populated with
multiplexes from these networks and immediately start to scan for
services.
Map DVB services to channels…
Pressing this button will start a process that scans all services on all
multiplexes and tries to verify if the service is actually a working TV
channel. If so, the channel will be created and mapped to this service.
You can start mapping services to channels once all muxes have been
processed. Until then the option will be disabled.
Adapter name
You can change the display name for the adapter. This is highly
recommended for multi-adapter setups with adapters that report the same
name to avoid confusion.
Autodetect muxes
The DVB transmissions contains information about other muxes available
on the same network. If this checkbox is enabled, Tvheadend will
automatically create new muxes as it receives configuration for them via
the DVB networks.
Skip initial scan
By default Tvheadend will rescan all muxes before more detailed
background scanning (including EPG scans) can be properly started. This
is to verify all muxes are still valid.\
 This will not stop the ability to watch live TV, however for most
setups this option can be checked.
Idle scanning
When nothing else happens Tvheadend will continuously rotate among all
muxes and tune to them to verify that they are still working. If your
adapter have problems with lots of tuning, try to disable this.
Close device handle when idle
This will attempt to close all available device handles. This can be
necessary to allow some devices to go into low power states.\
 However, this option has been known to cause problems with some
multi-tuner DVB cards. If you have signal problems, try disabling this
option.\
 Note: this option has no effect if idle scanning is enabled.
Skip service availability check when mapping
By default Tvheadend will validate that a service can be correctly
received (including any descrambling) when mapping channels. You can
disable this checking by enabling this option.
Use SID as channel number during mapping
If you enable this option then the initial mapping of channels will use
the service ID as the channel number, should no local channel number be
provided in the service information tables.
Monitor signal quality
If you enable this option Tvheadend will attempt to monitor signal
quality of a mux using an internal metric. If the calculated quality
falls to low the mux/adapter will generally be ignored.
Disable PMT monitoring
This disable monitoring Program Map Table (PMT) for all services on a
mux.\
 Most people should not require this, but because this involves creating
a lot of table filters, some DVB cards have problems and report errors
related to too many open file descriptors. If this happens try enabling
this option.
Write full DVB MUX to disk
If this is enabled, Tvheadend will store the full mux stream to disk for
debugging and development purposes. Don’t enable this unless you know
what you’re doing.
Original Network ID
If you experience problems caused by overlaps between multiple network
providers this option can be used to filter which network ID is received
by a given adapter.
Extra priority
This field can be used to define a priority ordering for adapters. This
will be used when determining which adapter to use to service a
subscription request. It could be used for example to prefer a DVB-S
adapter over a DVB-T one.
DiSEqC version (DVB-S only)
If you’re using a DiSEqC switch, then specify the version here.
Turn off LNB when idle
This option can be enabled to disable the power to the LNB when the
adapter is not in use. This can reduce power consumption, however for
poorly shielded multi-tuner setups you may have some interference when
the LNB is re-enabled.
Multiplexes tab
All multiplexes on the currently selected adapter are listed and can be
edited in a grid.
-   To edit a cell, double-click on it. After a cell is changed it will
    flags one of its corner to red to indicated that it has been
    changed. To commit these changes back to Tvheadend press the ‘Save
    changes’ button. In order to change a Checkbox cell you only have to
    click once in it.
-   To delete one or more entries, select the lines (by clicking once on
    them), and press the ‘Delete selected’ button. A popup will ask you
    to confirm your request. Note, that if you have automatic mux
    discovery enabled the mux will probably come back quite soon.

The columns have the following functions:
Enabled
Uncheck this if a multiplex is of no interest to you or otherwise
temporary broken
Network
Network name as given in the DVB stream. Cannot be changed
Frequency
Center frequency for the mux. Cannot be changed
Modulation
Information about the modulation used on the mux. Cannot be changed
Polarisation
Information about the polarisation used on the mux. Cannot be changed
Satellite config (DVB-S only)
The satellite configuration in use on this mux. Cannot be changed.
Frontend status
The status of the frontend signal last time the mux was tuned. Cannot be
changed
Mux id
Unique ID for this mux in the dvb network. Cannot be changed
Quality
Tvheadend’s estimated quality for the mux.
Services tab
All services on the currently selected adapter are listed and can be
edited in a grid.
-   To edit a cell, double-click on it. After a cell is changed it will
    flags one of its corner to red to indicated that it has been
    changed. To commit these changes back to Tvheadend press the ‘Save
    changes’ button. In order to change a Checkbox cell you only have to
    click once in it.
-   Service cannot be deleted since they are directly inherited /
    discovered from a mux they will reappear in just a few seconds
    should one delete them.

The columns have the following functions:

Enabled
Uncheck this if a service is of no interest to you or otherwise
temporary broken
Service name
Service name as given in the DVB stream. Cannot be changed
Play
Open the VLC plugin window to play this service.
Channel name
Double-click on this column to map the service to a channel.
DVB default charset
According to “ETSI EN 300 468”, the default character set for EIT data
is ISO6937. Unfortunately, some broadcasters actually use ISO-8859-x
encodings but fail to correctly announce it. To fix this you can set the
default charset to use when none is specified by the broadcaster.
EPG
Uncheck this if EPG data should not be retrieved for this service.
Type
Type of service. Cannot be changed
Provider
Provider as given in the DVB stream. Cannot be changed
Network
Network name for the mux this service resides on
Multiplex
Center frequency for the multiplex this service resides on
Information button
Press this to get a popup with more information about the service
Satellite config (DVB-S only)
Satellite configurations in use on this adapter (for controlling switch
equipment). The default entry will work fine for non-switched setups.
-   To edit a cell, double-click on it. After a cell is changed it will
    flags one of its corner to red to indicated that it has been
    changed. To commit these changes back to Tvheadend press the ‘Save
    changes’ button. In order to change a Checkbox cell you only have to
    click once in it.
-   To delete one or more entries, select the lines (by clicking once on
    them), and press the ‘Delete selected’ button. A popup will ask you
    to confirm your request. Note, that if you have automatic mux
    discovery enabled the mux will probably come back quite soon.

The columns have the following functions:
Name
Descriptive name for this configuration
Switchport
Port number to select for this configuration (numbering begins at 0).
In DiSEqC 1.0/2.0 mode, ports 0-3 are valid.
In DiSEqC 1.1/2.1 mode, ports 0-63 are valid.
Use numbers 0-3 for LNBs behind first input on the uncommitted switch,
then 4-7 and so on to support up to 64 ports using DiSEqC 1.1/2.1.
LNB type
Select the LNB type from the list of supported LNBs. If your LNB is not
supported please contact the Tvheadend team.
Comment
General comment to remind you what this is for.
A word about DVB adapters
-------------------------

A DVB adapter represents a piece of hardware attached to the system. DVB
receivers with dual tuners will present themselves as two adapters to
the Tvheadend application. Tvheadend support DVB-T, DVB-C and DVB-S
adapters.

There is currently no way of adding a new adapter to Tvheadend when
running. If a new adapter is plugged into the system Tvheadend needs to
be restarted in order to detect it.

If Tvheadend has configuration for an adapter and the adapter is missing
upon start-up the configuration will be left untouched in case the
adapter will be back in the future. There is currently no way to remove
configuration for a no longer present adapter.

Warning: Unplugging an DVB adapter (USB, etc) during operation (i.e when
Tvheadend is running) can result in deadlocking the kernel USB
subsystem, most likely requiring a system restart.

Warning2: Suspending a system is (from a USB driver perspective)
equivalent to a unplug/insert event. Thus, suspending a system running
Tvheadend with USB adapters is not recommended at the moment.

</div>
