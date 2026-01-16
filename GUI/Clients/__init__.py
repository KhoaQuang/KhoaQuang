#Python default packages used in this lib.
import sys,os,time,logging

##Get framework base path from environment variable
##which is set in user .basrhrc file.

base_path = os.environ['PHOENIX_BASE_PATH']
##Lib PATH SET