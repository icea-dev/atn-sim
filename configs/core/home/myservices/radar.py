#
# CORE
# Copyright (c)2010-2012 the Boeing Company.
# See the LICENSE file included in this distribution.
#
''' Sample user-defined service.
'''

import os

from core.service import CoreService, addservice
from core.misc.ipaddr import IPv4Prefix, IPv6Prefix

class Radar(CoreService):
    ''' This is a sample user-defined service. 
    '''
    # a unique name is required, without spaces
    _name = "Radar"
    # you can create your own group here
    _group = "Aviation"
    # list of other services this service depends on
    _depends = ()
    # per-node directories
    _dirs = ()
    # generated files (without a full path this file goes in the node's dir,
    #  e.g. /tmp/pycore.12345/n1.conf/)
    _configs = ('radar.cfg', 'radar.sh')
    # this controls the starting order vs other enabled services
    _startindex = 50
    # list of startup commands, also may be generated during startup
    _startup = ('sh radar.sh',)
    # list of shutdown commands
    _shutdown = ()

    @classmethod
    def generateconfig(cls, node, filename, services):
        ''' Return a string that will be written to filename, or sent to the
            GUI for user customization.
        '''
        if filename == "radar.sh":
            cfg = "#!/bin/sh\n"
            cfg += "# auto-generated by Radar (radar.py)\n"
            cfg += "python -m atn.surveillance.radar.radar\n"

            return cfg


        if filename == "radar.cfg":
            cfg = "[Location]\n"
            cfg += "; Latitude of radar (in decimal degrees)\n"
            cfg += "latitude = -15.870969\n"
            cfg += "\n"
            cfg += "; Longitude of radar (in decimal degrees)\n"
            cfg += "longitude = -47.917024\n"
            cfg += "\n"
            cfg += "; Altitude of radar (in meters)\n"
            cfg += "altitude = 2681\n"
            cfg += "\n"
            cfg += "[PSR]\n"
            cfg += "\n"
            cfg += "; The maximum horizontal distance of a detectable object (in NM)\n"
            cfg += "psr_horizontal_coverage = 80\n"
            cfg += "\n"
            cfg += "; The maximum altitude of a detectable object (in FT)\n"
            cfg += "vertical_coverage = 60000\n"
            cfg += "\n"
            cfg += "; Minimum elevation angle of detectable objects (in degrees)\n"
            cfg += "min_angle = 0\n"
            cfg += "\n"
            cfg += "; Maximum elevation angle of detectable objects (in degrees)\n"
            cfg += "max_angle = 85\n"
            cfg += "\n"
            cfg += "; The maximum horizontal distance of Secundary SSR (in NM)\n"
            cfg += "ssr_horizontal_coverage = 200\n"
            cfg += "\n"
            cfg += "; The time it takes to sweep the entire 360 degrees horizon (in seconds)\n"
            cfg += "sweep_time = 4.0\n"
            cfg += "\n"
            cfg += "[Network]\n"
            cfg += "\n"
            cfg += "; IP address of the receiver of radar plots (e.g. ATC system)\n"
            cfg += "destination = 172.16.0.255\n"
            cfg += "\n"
            cfg += "; Transport layer port of the destination\n"
            cfg += "port = 65000\n"
            cfg += "\n"
            cfg += "; Mode of transmission: unicast or broadcast\n"
            cfg += "mode = broadcast\n"
            cfg += "\n"
            cfg += "; Radar protocol to be used\n"
            cfg += "protocol = icea\n"

            return cfg




    @staticmethod
    def subnetentry(x):
        ''' Generate a subnet declaration block given an IPv4 prefix string
            for inclusion in the config file.
        '''
        if x.find(":") >= 0:
            # this is an IPv6 address
            return ""
        else:
            net = IPv4Prefix(x)
            return 'echo "  network %s"' % (net)

# this line is required to add the above class to the list of available services
addservice(Radar)

