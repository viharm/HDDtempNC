# HDDtempNC
*HDDtempNC* is a tool to acquire hard disk drive temperature from *hddtemp*'s network interface.

It is *Python* script and requires a working *Python* environment. It depends a configured and working *hddtemp* daemon on the system whose HDD temperatures are required.

## Usage ##
*HDDtempNC* can be used either from the command line or by calling it in another script/program

### Command syntax ###
```
hddtempnc.py --param1=value1 [ --param2=value2 [ --param3 ] ]
```

Following parameters are available:

* `-d <disk> (--disk=<disk>)`

  Specify disk to interrogate (full device path, e.g. /dev/sda)
  
* `-t <host> (--target=<host>)`

  Specify target host to interrogate (optional, default localhost)
  
* `-p <port> (--port=<port>)`

  Specify target port to interrogate (optional, default 7634)
  
* `-g (--debug)`

  Enable debugging to console/stdout
  
* `-h (--help)`

  Show help
  
The sequence of parameters is not important.

### Examples ###
Command examples

#### Long parameters ####
```
/usr/bin/python3 hddtempnc.py --disk=/dev/sda`
/usr/bin/python3 hddtempnc.py --target=192.168.0.20 --disk=/dev/sdb
/usr/bin/python hddtempnc.py --port=7630 --disk=/dev/sdc
/usr/bin/python hddtempnc.py --disk=/dev/sda --port=9000 --target=10.65.0.65
```

#### Short parameters ####
```
/usr/bin/python3 hddtempnc.py -d /dev/sda
/usr/bin/python3 hddtempnc.py -t 192.168.0.20 -d /dev/sdb
/usr/bin/python hddtempnc.py -p 7630 -d /dev/sdc
/usr/bin/python hddtempnc.py -d /dev/sda -p 9000 -t 10.65.0.65
```

## Download ##
The script is available in the [code](https://github.com/viharm/HDDtempNC/blob/master/hddtempnc.py "HDDtempNC").

## Discussion & issues ##
Feature requests, bugs, issues and other comments can be created in [Issues](https://github.com/viharm/HDDtempNC/issues).

## Links ##
* *hddtemp* home
  http://www.guzu.net/linux/hddtemp.php
* *hddtemp* on *[Savannah](http://savannah.gnu.org/)*
  https://savannah.nongnu.org/projects/hddtemp/
* *hddtemp* guide on *Arch* wiki
  https://wiki.archlinux.org/index.php/Hddtemp

## License

Copyright (c) 2015, Vihar Malviya
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.