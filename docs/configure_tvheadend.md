##Configure Tvheadend

This section gives a high-level overview of the steps needed to get Tvheadend up and running. For more detailed
information, please consult the rest of this guide - much of it is arranged in the same order as the tabs on the
Tvheadend interface so you know where to look.

You can also consult the in-application help text, which mirrors this guide to a very great extent.

####1. Ensure tuners are available for use

*tvheadend web interface: _Configuration -> DVB Inputs -> TV Adapters_*

On this tab, you'll see a tree structure, with the Linux device list at the top level (e.g. `/dev/dvb/adapter0`)

Individual tuners are then the next level down (e.g. `DiBcom 7000PC : DVB-T #0`)

Click on each tuner that you want tvheadend to use, and ensure "Enabled" is checked in the 'Parameters' list

If anything is obviously wrong at this point, you probably have a driver/firmware error which you'll need to resolve before going any further.

####2. Set up relevant network(s)

*tvheadend web interface: _Configuration -> DVB Inputs -> Networks_*

Create a network of the appropriate type here. You can have multiple networks of the same type as necessary, e.g. to have two DVB-T networks defined, one with HD muxes, one without.

The creation process allows you to select from a series of pre-defined mux lists for common DVB sources. These are maintained outside of tvheadend, and are downloaded from linuxtv - but they do go out of date as broadcasters move services around and national authorities change entire pieces of spectrum. As such, you should try the pre-defined values, but you may need to add muxes manually.

<div class="admonition warning">
<p class="admonition-title">Critical Configuration Items</p>
<p>Critical configuration items at this stage: <........></p>
</div>

####3. Associate the network with the respective tuner(s)

*tvheadend web interface: _Configuration -> DVB Inputs -> TV Adapters_*

Associate each of your tuners with the correct network through _Parameters -> Basic Settings_. 

This can be as simple or as complex as necessary. You may simply have, for example, a single DVB-S2 network defined and then associate this with all DVB-S2 tuners. Or, you might have multiple networks defined - different satellites, different encoding. So, as further examples, you might define and then associate an HD DVB-T2 (e.g. H.264) network with HD tuners, while having a separate SD network associated with an independent SD (e.g. MPEG-2) tuner. 

<div class="admonition warning">
<p class="admonition-title">Critical Configuration Items</p>
<p>Critical configuration items at this stage: <........></p>
</div>

At this point, your tuners now know what networks to use: one network can appear on multiple tuners (many-to-one), and one tuner can have multiple networks.

#### 4. If necessary, manually add muxes to the network

*tvheadend web interface: _Configuration -> DVB Inputs -> Muxes_*

Ideally, this is where you'll see a list of the pre-populated muxes as created when you set up your initial network. However, should there be any issues, this is where you can manually add missing muxes. You only really need to worry about this if the pre-defined list didn't work (e.g. because of out-of-date data - damn those broadcasters, re-arranging their services without telling anyone...) or because automatic detection hasn't successfully found all the muxes over time. 

If you do need to add something manually, you'll need to search the Internet for details of the appropriate transmitter and settings: satellites tend not to change much and are universal over a large area, but terrestrial muxes tend to be very localised and you'll need to know which specific transmitter you're listening to. 

Good sources of transmitter/mux information include:

* [KingofSat](http://en.kingofsat.net) for all European satellite information

* [ukfree.tv](http://www.ukfree.tv/maps/freeview) for UK DVB-T transmitters

* [Interactive EU DVB-T map](http://www.dvbtmap.eu/mapmux.html) for primarily central and northern Europe

> other major sources....?

You can also use [dvbscan](http://www.linuxtv.org/wiki/index.php/Dvbscan) to force a scan and effectively ask your tuner what it can see.
 
<div class="admonition warning">
<p class="admonition-title">Critical Configuration Items</p>
<p>Critical configuration items at this stage: <........></p>
</div>

#### 5. Scan for services

*tvheadend web interface: _Configuration -> DVB Inputs -> Services_*

This is where the services will appear as your tuners tune to the muxes based on the network you told them to look on. Again, remember what's happening: the tvheadend software is telling your tuner hardware (via the drivers) to sequentially tune to each mux it knows about, and then see what 'programmes' it can see on that mux, each of which is identified by a series of unique identifiers that describe the audio stream(s), the video stream(s), the subtitle stream(s) and language(s), and so on.

> To force a scan ...

#### 6. Map services to channels

Once scanning for services is complete, you need to map the services to channels so your client can actually request them (i.e. so you can watch or record). You can do this in two places:

*tvheadend web interface: _Configuration -> DVB Inputs -> Services_*

Press the "Map All" button

*tvheadend web interface: _Configuration -> Channel/EPG -> Channels_*

Press the "Map Services" button

> Any explanation on how a channel can map to multiple services <......>

> Anything about using bouquets

#### 7. Watch TV

That's it - you're done. You should now have a working basic tvheadend installation with channels mapped and ready for use!

As required, you may now wish to look into:

* Setting up different EPGs (inc. localised character sets and timing offsets)
* Setting up channel icons
* Setting up recording profiles
* Setting up streaming profiles (including transcoding)
* Arranging your channels into groups (channel tags)
* Setting up softcams for descrambling
* Setting up access control rules for different client types/permission levels
