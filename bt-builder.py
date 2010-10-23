#!/usr/bin/env python

# BimboTux builder

import os
import urllib

# General functions
def download(filename, destination):
    url = 'http://github.com/Stemby/BimboTux/raw/master/files/%s' % filename
    print 'Downloading %s...\n\tfrom %s\n\tto %s' % (filename, url, destination)
    urllib.urlretrieve(url, destination + filename)
    print '... done'

def main():
    # live-build configuration
    options = {}
#    lcOptions = [] # live-config options
#    for i in (
#            'hostname=bimbotux',
#            'locales=it_IT.UTF-8',
#            'timezone=Europe/Rome',
#            'keyboard-layouts=it'
#            ):
#        lcOptions.append('live-config.%s' % i)
#    options['--bootappend-live'] = '"%s"' % ' '.join(lcOptions)
    options['--hostname'] = 'bimbotux'
    options['--bootappend-live'] = '"\
            locales=it_IT.UTF-8 \
            keyboard-layouts=it \
            timezone=Europe/Rome"'
    options['--language'] = '"it"'
    options['-d'] = 'squeeze'
#    options['--apt-recommends'] = 'false'
    options['-a'] = 'i386'
    options['-k'] = '686'
    options['--mirror-binary'] = '"http://ftp.it.debian.org/debian/"'
#    options['--mirror-chroot'] = '"http://ftp.it.debian.org/debian/"'
    options['--mirror-bootstrap'] = '"http://192.168.0.100:9999/debian/"'
    options['--debian-installer'] = 'live'
    options['--debian-installer-distribution'] = 'daily'
    options['--debian-installer-gui'] = 'disabled'
#    options['-r'] = 'live.debian.net' # workaround for bug #583485

    lb_config = 'lb config'
    for option, value in options.iteritems():
        lb_config += ' %s %s' % (option, value)

    print lb_config
    os.system(lb_config)

    # Download the package list
    filename = 'bimbotuxpkg.list'
    destination = 'config/chroot_local-packageslists/'
    download(filename, destination)

    # Download .fvwm2rc 
    filename = '.fvwm2rc'
    destination = 'config/chroot_local-includes/etc/skel/.fvwm/'
    os.system('mkdir -p %s' % destination)
    download(filename, destination)

    # Download sudoers, TODO: is there a better way? 
    filename = 'sudoers'
    destination = 'config/chroot_local-includes/etc/'
    download(filename, destination)
    os.system('chmod 440 %s' % destination + filename)

    # Download .profile, workaround for #585932
#    filename = '.profile'
#    destination = 'config/chroot_local-includes/etc/skel/'
#    download(filename, destination)

    # Download .gtkrc-2.0
    filename = '.gtkrc-2.0'
    destination = 'config/chroot_local-includes/etc/skel/'
    download(filename, destination)

    # Download supertux.desktop
    filename = 'supertux.desktop'
    destination = 'config/chroot_local-includes/usr/share/applications/'
    os.system('mkdir -p %s' % destination)
    download(filename, destination)

    # Download .ri-li.pref
    filename = '.ri-li.pref'
    destination = 'config/chroot_local-includes/etc/skel/'
    download(filename, destination)

if __name__ == '__main__':
    main()
