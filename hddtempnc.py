#!/usr/bin/python
 
# HDDtempNC
# Version 01.01.04
# Date: 2015-02-15

# Program to provide numeric string output of HDD temperature using netcat,
# so non-root user can query HDD temperature
 
# Depends on //hddtemp// running as daemon on known port (default 7634) on known target host (default localhost)

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

# Import necessary modules 
import sys
import getopt
import socket
import subprocess

# Configure debug mode
bl__Debug = False

# Initialise exit status
ss__ExitStatus = 1


# Define the debugging function
def fn__Debug ( ag__DebugTag , ag__DebugMessage ) :
  # Re-define global variables to be re-used
  global bl__Debug

  if bl__Debug :
    print ( repr ( ag__DebugTag ) + ": " + repr ( ag__DebugMessage ) )

# Define the help function
def fn__Help ( ) :
  # Re-define global variables to be re-used
  global ss__ExitStatus , bl__Debug

  # Set exit status
  ss__ExitStatus = 2
  fn__Debug ( "Exit status" , ss__ExitStatus )
  
  # Print help
  print ( "Usage:" , sys.argv [ 0 ] , "--param=value" )
  print ( "-d <disk> (--disk=<disk>)" , "Specify disk to interrogate" )
  print ( "-t <host> (--target=<host>)" , "Specify target host to interrogate (optional, default localhost)" )
  print ( "-p <port> (--port=<port>)" , "Specify target port to interrogate (optional, default 7634)" )
  print ( "-g (--debug)" , "Enable debugging to console/stdout" )
  print ( "-h (--help)" , "Show (this) help" )
  
  # Exit gracefully
  sys.exit ( ss__ExitStatus )

# Define set of actions when disk not found
def fn__NotFound ( ) :
  # Re-define global variables to be re-used
  global ss__ExitStatus , bl__Debug

  # Set exit status
  ss__ExitStatus = 3
  fn__Debug ( "Exit status set" , ss__ExitStatus )
  
  # Notify of failure
  print ( "Disk not found" )
  
  # Exit gracefully
  sys.exit ( ss__ExitStatus )

# Define function for reading socket
def fn__SocketRead ( ag__Host = "localhost" , ag__Port = "7634" ) :

  # Re-define global variables to be re-used
  global ss__ExitStatus , bl__Debug
  
  fn__Debug ( "Checking host" , ag__Host )
  fn__Debug ( "Checking port" , ag__Port )
  
  # Clear connection  
  ob__Socket = None
  fn__Debug ( "Connection object" , "cleared" )
  
  # Analyse target to fetch socket information
  fn__Debug ( "Preparing" , "Analysing target" )
  for nm__LoopCounter01 in socket.getaddrinfo (
    ag__Host ,
    ag__Port ,
    socket.AF_UNSPEC ,
    socket.SOCK_STREAM ) :
    nm__SocketFamily , nm__SocketType , nm__SocketProtocol , st__HostCanonname , ar__SocketAddress = nm__LoopCounter01
    
    # Debug output
    fn__Debug ( "Socket family" , nm__SocketFamily )
    fn__Debug ( "Socket type" , nm__SocketType )
    fn__Debug ( "Socket protocol" , nm__SocketProtocol )
    fn__Debug ( "Canonical host name" , st__HostCanonname )
    fn__Debug ( "Socket address parameters" , ar__SocketAddress )
    
    try :
      ob__Socket = socket.socket ( nm__SocketFamily , nm__SocketType , nm__SocketProtocol )
      fn__Debug ( "Object" , ob__Socket )
    except OSError as msg :
      ob__Socket = None
      fn__Debug ( "Error creating socket object" , "Object cleared" )
      continue
    
    try :
      ob__Socket.connect ( ar__SocketAddress )
    except socket.error as msg :
      # Clear object on failure
      ob__Socket = None
      fn__Debug ( "Socket error" , "Object cleared" )
      
      # Set exit status
      ss__ExitStatus = 111
      fn__Debug ( "Exit status" , ss__ExitStatus )
      continue
    break
  # Check for null object
  if ob__Socket is None :
    fn__Debug ( "Null socket object" , "Could not open socket" )
    print ( 'Could not open socket' )
    
    # Exit gracefully
    sys.exit ( ss__ExitStatus )
  
  # Read data from target and save to return variable
  rt__SocketOutput = ob__Socket.recv ( 4096 )
  fn__Debug ( "Data from target" , rt__SocketOutput )
  
  # Close socket
  ob__Socket.close ( )
  fn__Debug ( "Socket" , "closed" )
  
  # Return data to calling routine
  return repr ( rt__SocketOutput )


# Define the main function
def main ( ag__ArgList ) :
 
  # Re-define global variables to be re-used
  global ss__ExitStatus , bl__Debug

  # Initialise the working variables
  st__TargetHost = "localhost"
  st__TargetPort = "7634"
  
  # Initialise internal variables
  bl__DiskFound = False
  fn__Debug ( "Initial disk found" , bl__DiskFound )

  st__DiskRequest = ""
  fn__Debug ( "Initial disk request" , "blank" )

  # Scan for script arguments
  try :
    # Parse the supplied arguments
    ar__ArgOption , ar__ArgRemainder = getopt.getopt ( ag__ArgList , "hgt:p:d:" , [ "help" , "debug" , "target=" , "port=" , "disk=" ] )
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
    
    # Check if debugging is requested
    if st__ArgParam in ( "-g" , "--debug" ) :
      bl__Debug = True
      fn__Debug ( "Debug request" , bl__Debug )

    # Check if target host is specified
    if st__ArgParam in ( "-t" , "--target" ) :
      st__TargetHost = st__ArgValue
      fn__Debug ( "Target host" , st__TargetHost )
      
    # Check if target port is specified
    if st__ArgParam in ( "-p" , "--port" ) :
      st__TargetPort = st__ArgValue
      fn__Debug ( "Target port" , st__TargetPort )
      
  
  # Call function to read Hddtemp
  fn__Debug ( "Ready" , "Now reading socket" )
  st__HddtempRaw = fn__SocketRead ( st__TargetHost , st__TargetPort )

  fn__Debug ( "Raw HDDtemp output" , st__HddtempRaw )
  
  # Notify if the requested disk is not found in the //hddtemp// output
  if st__HddtempRaw.find ( st__DiskRequest ) == -1 :
    fn__Debug ( "Disk not found" , "calling function" )
    fn__NotFound ( )
    
  # Finally, start parsing the raw //hddtemp// output
  else :
    fn__Debug ( "Requested disk found" , "splitting disks" )
    # //hddtemp// splits each disk info with a double pipe symbol
    # use it split the output into list of disks
    ar__DisksTemp = st__HddtempRaw.split ( "||" )
    fn__Debug ( "Disks split as follows" , ar__DisksTemp )
    # Go through each disk in the list
    for st__DiskInfo in ar__DisksTemp :
      fn__Debug ( "Disk dump" , st__DiskInfo )
      # Search for the requested disk in the list item
      fn__Debug ( "Current disk dump" , "Comparing with request" )
      if st__DiskInfo.find ( st__DiskRequest ) != -1 :
        # If requested disk found, then split further using //hddtemp//'s default delimiter (|)
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
  sys.exit ( main ( sys.argv [ 1: ] ) )