# Copyright (c) 2010-2012 Robin Jarry
#
# This file is part of EVE Corporation Management.
#
# EVE Corporation Management is free software: you can redistribute it and/or
# modify it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at your
# option) any later version.
#
# EVE Corporation Management is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY
# or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for
# more details.
#
# You should have received a copy of the GNU General Public License along with
# EVE Corporation Management. If not, see <http://www.gnu.org/licenses/>.

from __future__ import with_statement

__date__ = '2012 3 24'
__author__ = 'diabeteman'

import sys
from os import path
from ConfigParser import SafeConfigParser
from optparse import OptionParser

from ecm.lib.subcommand import Subcommand
from ecm.admin.util import get_logger
from ecm.lib.daemon import Daemon

#------------------------------------------------------------------------------
def sub_command():
    cmd = Subcommand('start', aliases=('stop', 'restart', 'status'),
                     parser=OptionParser(usage='%prog [OPTIONS] instance_dir'),
                     help='Control the embedded server of an existing ECM instance.',
                     callback=run)
    return cmd

#------------------------------------------------------------------------------
def run(command, global_options, options, args):
    if not args:
        command.parser.error('Missing instance directory.')
    instance_dir = args[0]

    log = get_logger()

    config = SafeConfigParser()
    settings_file = path.join(instance_dir, 'settings.ini')
    if not config.read([settings_file]):
        command.parser.error('Settings file "%s" not found.' % settings_file)

    pidfile = config.get('misc', 'pid_file') or 'ecm.pid'
    address = config.get('misc', 'server_bind_ip') or '127.0.0.1'
    port = config.get('misc', 'server_bind_port') or 8888

    if not path.isabs(pidfile):
        pidfile = path.abspath(path.join(instance_dir, pidfile))

    real_command = sys.argv[1]

    if real_command == 'status':
        if path.isfile(pidfile):
            with open(pidfile, 'r') as pf:
                pid = pf.read()
            log.info('Instance is running with PID: %s' % pid.strip())
        else:
            log.info('Instance is stopped')
        sys.exit(0)
    else:
        daemon = GEventWSGIDaemon(pidfile, address, port)
        if real_command == 'start':
            log.info('Instance starting...')
            daemon.start()
            with open(pidfile, 'r') as pf:
                pid = pf.read()
            log.info('Instance is running with PID: %s' % pid.strip())
        elif real_command == 'stop':
            log.info('Instance is shutting down...')
            daemon.stop()
            log.info('Instance is stopped')
        elif real_command == 'restart':
            log.info('Instance restarting...')
            daemon.restart()
            with open(pidfile, 'r') as pf:
                pid = pf.read()
            log.info('Instance is running with PID: %s' % pid.strip())

#------------------------------------------------------------------------------
class GEventWSGIDaemon(Daemon):

    def __init__(self, pidfile, address, port):
        Daemon.__init__(self, pidfile)
        self.address = address
        self.port = port

    def run(self):
        self._setup_environ()
        try:
            from gevent.pywsgi import WSGIServer
        except ImportError:
            print >>sys.stderr, 'Please install "gevent" to run this command.'
            sys.exit(1)
        import django.core.handlers.wsgi
        application = django.core.handlers.wsgi.WSGIHandler()
        server = WSGIServer((self.address, self.port), application)
        server.serve_forever()

    def _setup_environ(self):
        instance_dir = path.abspath(path.dirname(__file__))
        sys.path.insert(0, instance_dir)

        import settings #@UnresolvedImport

        from django.core import management

        management.setup_environ(settings)
        utility = management.ManagementUtility()
        command = utility.fetch_command('runserver')
        command.validate()

        from django.conf import settings as django_settings
        from django.utils import translation
        translation.activate(django_settings.LANGUAGE_CODE)
