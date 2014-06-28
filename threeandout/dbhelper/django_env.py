#import this module to set-up DJANGO settings properly
#we parse command line and look for any --settings=val
#and that is what we use for our django settings
from optparse import OptionParser
import os

import sys
sys.path.append('..')
if not os.environ.has_key('DJANGO_SETTINGS_MODULE'):
  parser = OptionParser()
  parser.add_option("", "--settings", dest="settings",
                  help="which settings to use.  default is dev", default="")
  
  (options, args) = parser.parse_args()
  if options.settings=="":
    options.settings='dev'
    print "WARNING:  No --settings flag given on the command line.  defaulting to %s" %options.settings
  os.environ['DJANGO_SETTINGS_MODULE'] = 'threeandout.settings.%s' %options.settings

from threeandout.apps.ff_core import models

