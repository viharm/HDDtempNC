#!/usr/bin/python
 
# HDDtempNC
# Version 01.00.03
# Date: 2015-02-14

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
 
def fn__Help ( ) :
  print ( "Usage:" , sys.argv [ 0 ] , "-d <disk> (--disk=<disk>)" )
  sys.exit ( 2 )
 
def fn__NotFound ( ) :
  print ( "Disk not found" )
  sys.exit ( 3 )

def fn__Debug ( ag__DebugTag , ag__DebugMessage ) :
  global bl__Debug
  if bl__Debug :
    print ag__DebugTag + ": " + ag__DebugMessage 

# Configure debug mode
bl__Debug = False
fn__Debug ( "Debugging enabled" , bl__Debug )

# Initialise exit status
ss__ExitStatus = 1
fn__Debug ( "Initial exit status" , ss__ExitStatus )

# Define the main function
def main ( ag__ArgList ) :
 
  # Initialise the working variables, tweak as per need
  ar__Netcat = {
    "ak__Bin" : "/bin/netcat" ,
    "ak__Host" : "localhost" ,
    "ak__Port" : "7634" }
  
  fn__Debug ( "Netcat array" , ar__Netcat )
  
  # Initialise internal variables
  bl__DiskFound = False
  fn__Debug ( "Initial disk found" , bl__DiskFound )

  st__DiskRequest = ""
  fn__Debug ( "Initial disk request" , "blank" )

  # Scan for script arguments
  try :
    # Parse the supplied arguments
    ar__ArgOption , ar__ArgRemainder = getopt.getopt ( ag__ArgList , "hd:" , [ "help" , "disk=" ] )
    # Call help if no aruments supplied
    if len ( ar__ArgOption ) == 0 :
      fn__Debug ( "No arguments" , "seeking help" )
      fn__Help ( )
  # Call help if confused
  except getopt.GetoptError :
    fn__Debug ( "Argument parse error" , "seeking help" )
    fn__Help ( )
 
  # Check supplied arguments/parameters
  fn__Debug ( "Checking arguments" , "cycling through each" )
  for st__ArgParam , st__ArgValue in ar__ArgOption :
    # Call help if requested so
    if st__ArgParam in ( "-h" , "--help" ) :
      fn__Debug ( "Help requested" , "seeking help" )
      fn__Help ( )
    # Read disk request
    elif st__ArgParam in ( "-d" , "--disk" ) :
      st__DiskRequest = st__ArgValue
      fn__Debug ( "Requested disk" , st__DiskRequest )

  # Run //netcat// using the supplied working variables
  fn__Debug ( "Ready" , "Now running netcat" )
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
  fn__Debug ( "Raw HDDtemp output" , st__HddtempRaw )
  
  # Notify if the requested disk is not found in the //netcat// output
  if st__HddtempRaw.find ( st__DiskRequest ) == -1 :
    fn__Debug ( "Disk not found" , "calling function" )
    fn__NotFound ( )
  # Finally, start parsing the raw //netcat// output
  else :
    fn__Debug ( "Requested disk found" , "splitting disks" )
    # //netcat// splits each disk info with a double pipe symbol
    # use it split the output into list of disks
    ar__DisksTemp = st__HddtempRaw.split ( "||" )
    fn__Debug ( "Disks split as follows" , ar__DisksTemp )
    # Go through each disk in the list
    for st__DiskInfo in ar__DisksTemp :
      fn__Debug ( "Disk dump" , st__DiskInfo )
      # Search for the requested disk in the list item
      fn__Debug ( "Current disk dump" , "Comparing with request" )
      if st__DiskInfo.find ( st__DiskRequest ) != -1 :
        # If requested disk found, then split further using //netcat//'s default delimited (|)
        fn__Debug ( "Current disk dump is requested" , "splitting parameters and values" )
        ar__DiskInfo = st__DiskInfo.split ( "|" )
        # Go through each fragment of output for the current disk from the list of disks found
        for st__DiskInfoFragment in ar__DiskInfo :
          fn__Debug ( "Checking fragment" , st__DiskInfoFragment )
          # Check if the requested disk matches at least one of the fragments; it should.
          if st__DiskInfoFragment == st__DiskRequest :
            fn__Debug ( "Checking fragment" , "Comparing with request" )
            # If any one fragment matches, then set the flag for disk found
            fn__Debug ( "Fragment match" , "Current disk dump match" )
            bl__DiskFound = True
            fn__Debug ( "Disk found flag" , bl__DiskFound )
        # If the disk is found if one of the fragments is "C" (Celsius)
        if bl__DiskFound and "C" in ar__DiskInfo :
          # Locate "C"
          fn__Debug ( "Disk found" , "Locating Celsius symbol C" )
          nm__CelsiusLocation = ar__DiskInfo.index ( "C" )
          # The temperature is the item just before "C"
          fn__Debug (
            "Temperature value is the preceding fragment from C symbol" ,
            "Locating numeric value of temperature" )
          print ( ar__DiskInfo [ nm__CelsiusLocation - 1 ] )
          # Set exit status success flag
          ss__ExitStatus = 0
          fn__Debug ( "Setting success flag" , ss__ExitStatus )
        else :
          fn__NotFound ( )
  return ss__ExitStatus

  if __name__ == "__main__" :
# main ( sys.argv [ 1: ] )
  sys.exit ( main ( sys.argv [ 1: ] ) )

