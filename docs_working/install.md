<div class="hts-doc-text">

Parts of this documentation is also available in the Tvheadend man page.

Starting Tvheadend
If you already have Tvheadend up and running you can skip this part.
Command line options:

-f
Fork and become a background process (daemon). Default no.
-u username
Run as ‘username’. Only applicable if demonizing. Default is to use the
UID of 1 (daemon on most systems).
-g groupname
Run as group ‘groupname’. Only applicable if daemonizing. Default is to
use the ‘video’ group. If the ‘video’ group does not exist, GID 1
(daemon) will be used.
Default configuration
All configuration in Tvheadend is maintained via its embedded web server
running on port 9981. Just point your browser to:
http://hostname:9981/

By default **everyone (also from remote hosts)is allowed full access to
all features / settings** in the web user interface. If this is the
first time you setup Tvheadend you are most encouraged to enter the web
user interface, selected the ‘Configuration’ + ‘Access Control’ tab and
make reasonable changes. Further help / documentation can be obtained
inside the web interface.
Settings storage
Settings are loaded/stored in \$HOME/.hts/tvheadend.
Logging
All activity inside Tvheadend is logged to syslog using log facility.
Also, if logged in to the web interface you will receive the same log in
the bottom tab (System log).
Permission to access video adapters
In order for Tvheadend to control video adapters on the system it must
be granted access to those devices. Most systems have a ‘video’ group
with write access to the video adapter devices. When Tvheadend is
started as a daemon (if Tvheadend is installed from a distribution
package this is most likely the way it is) it will change its primary
group to ‘video’ in order to access these groups. If your system is
configured in a different way you can either change the group membership
of the video adapters (/dev/dvb, etc) or reconfigure the Tvheadend start
up parameters.
If Tvheadend is started without the ‘-f’ argument it will not demonize
nor change its primary UID/GID. Rather it will run with the permissions
granted to the user executing the binary. If that’s the case you must
make sure the current user is granted with access to the video devices.
Open ports
Tvheadend listens to the following TCP ports by default:
-   9981 - HTTP server (web interface)
-   9982 - HTSP server (Streaming protocol)

There is currently no way of disabling these TCP servers, nor bind the
services to specific interfaces or other ports. To limit access, please
read the section about ‘Access Control’ in the configuration chapter.

</div>
