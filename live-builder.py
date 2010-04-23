#!/usr/bin/env python

# BimboTux builder

import os
import urllib
import fileinput

# General functions
def download(filename, destination):
    url = 'http://github.com/Stemby/BimboTux/raw/master/files/%s' % filename
    print 'Downloading %s from %s ...' % (filename, url)
    urllib.urlretrieve(url, destination + filename)
    print '... done'

def main():
    # live-helper configuration 
    options = {}

    options["--mirror-binary"] = '"http://ftp.it.debian.org/debian/"'
    options["--mirror-bootstrap"] = '"http://localhost:9999/debian/"'
    options["--debian-installer"] = 'live'
    options["--debian-installer-distribution=daily"] = ''
    options["--debian-installer-gui"] = 'disabled'

    lh_config = 'lh config'
    for option, value in options.iteritems():
        lh_config += ' %s %s' % (option, value)

    print lh_config
    os.system(lh_config)

    # Download the package list
    filename = 'bimbotuxpkg.list'
    destination = 'config/chroot_local-packageslists/'
    download(filename, destination)

    # Enable the package list
    for line in fileinput.input('config/chroot', inplace=1):
        if 'LH_PACKAGES_LISTS' in line:
            line = line.replace('standard', 'standard bimbotuxpkg')
        print line,

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

    # Download .gtkrc-2.0
    filename = '.gtkrc-2.0'
    destination = 'config/chroot_local-includes/etc/skel/'
    download(filename, destination)
    
    # Download Xwrapper.config
    filename = 'Xwrapper.config'
    destination = 'config/chroot_local-includes/etc/X11/'
    os.system('mkdir -p %s' % destination)
    download(filename, destination)

    # Download startx.sh
    filename = 'startx.sh'
    destination = 'config/chroot_local-includes/usr/bin/'
    os.system('mkdir -p %s' % destination)
    download(filename, destination)
    os.system('chmod +x %s' % destination + filename)

    # Download .bash_profile
    filename = '.bash_profile'
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
