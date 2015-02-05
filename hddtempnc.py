#!/usr/bin/python
 
# HDDtempNC
# Version 01.00.00
# Date: 2015-02-05

# Program to provide numeric string output of HDD temperature using netcat,
# so non-root user can query HDD temperature
 
# Depends on //netcat//, //hddtemp// (daemon on port)

# Copyright 2015 Vihar Malviya

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#    http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
 

# st__ : String variable
# nm__ : Numeric (integer or float) variable
# ar__ : Array variable (associative arrays are dictionaries, non-associative are lists or tuples )
# ak__ : Array key
# ss__ : Status variable
# bl__ : Boolean variable
# ag__ : Arguments
# ob__ : Object
 
import sys , getopt
import subprocess
 
# Initialise exit status
ss__ExitStatus = 1
 
# Define the main function
def main ( ag__ArgList ) :
 
  # Initialise the working variables, tweak as per need
  ar__Netcat = {
    "ak__Bin" : "/bin/netcat" ,
    "ak__Host" : "localhost" ,
    "ak__Port" : "7634" }
# st__NetcatBin = "/bin/netcat"
# st__NetcatHost = "localhost"
# st__NetcatPort = "7634"
 
  # Initialise internal variables
  bl__DiskFound = False
  st__DiskRequest = ""
 
  # Scan for script arguments
  try :
    # Parse the supplied arguments
    ar__ArgOption , ar__ArgRemainder = getopt.getopt ( ag__ArgList , "hd:" , [ "help" , "disk=" ] )
    # Call help if no aruments supplied
    if len ( ar__ArgOption ) == 0 :
      fn__Help ( )
  # Call help if confused
  except getopt.GetoptError :
    fn__Help ( )
 
  # Check supplied arguments/parameters
  for st__ArgParam , st__ArgValue in ar__ArgOption :
    # Call help if requested so
    if st__ArgParam in ( "-h" , "--help" ) :
      fn__Help ( )
    # Read disk request
    elif st__ArgParam in ( "-d" , "--disk" ) :
      st__DiskRequest = st__ArgValue
 
  # Run //netcat// using the supplied working variables
  st__HddtempProc = subprocess.Popen (
    [
      ar__Netcat [ "ak__Bin" ] ,
      ar__Netcat [ "ak__Host" ] ,
      ar__Netcat [ "ak__Port" ] ] ,
    stdout = subprocess.PIPE ,
    stderr = subprocess.STDOUT ,
    universal_newlines = True )
  # Store the output of //netcat//
  st__HddtempRaw = st__HddtempProc.stdout.read ( )
  # Notify if the requested disk is not found in the //netcat// output
  if st__HddtempRaw.find ( st__DiskRequest ) == -1 :
    fn__NotFound ( )
  # Finally, start parsing the raw //netcat// output
  else :
    # //netcat// splits each disk info with a double pipe symbol
    # use it split the output into list of disks
    ar__DisksTemp = st__HddtempRaw.split ( "||" )
    # Go through each disk in the list
    for st__DiskInfo in ar__DisksTemp :
      # Search for the requested disk in the list item
      if st__DiskInfo.find ( st__DiskRequest ) != -1 :
        # If requested disk found, then split further using //netcat//'s default delimited (|)
        ar__DiskInfo = st__DiskInfo.split ( "|" )
        # Go through each fragment of output for the current disk from the list of disks found
        for st__DiskInfoFragment in ar__DiskInfo :
          # Check if the requested disk matches at least one of the fragments; it should.
          if st__DiskInfoFragment == st__DiskRequest :
            # If any one fragment matches, then set the flag for disk found
            bl__DiskFound = True
        # If the disk is found if one of the fragments is "C" (Celsius)
        if bl__DiskFound and "C" in ar__DiskInfo :
          # Locate "C"
          nm__CelsiusLocation = ar__DiskInfo.index ( "C" )
          # The temperature is the item just before "C"
          print ( ar__DiskInfo [ nm__CelsiusLocation - 1 ] )
          # Set exit status success flag
          ss__ExitStatus = 0
        else :
          fn__NotFound ( )
  return ss__ExitStatus
 
def fn__Help ( ) :
  print ( "Usage:" , sys.argv [ 0 ] , "-d <disk> (--disk=<disk>)" )
  sys.exit ( 2 )
 
def fn__NotFound ( ) :
  print ( "Disk not found" )
  sys.exit ( 3 )
 
if __name__ == "__main__" :
# main ( sys.argv [ 1: ] )
  sys.exit ( main ( sys.argv [ 1: ] ) )

