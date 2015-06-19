# HDDtempNC

[![Version][mg_BadgeVersion]][ln_ReleaseLatest]
[![Issues][mg_BadgeIssues]][ln_Issues]

[![Language][mg_BadgeCodeLang]][ln_CodeLang]
[![License][mg_BadgeLicense]][ln_License]

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
The script is available in the [code][ln_ReleaseLatest].

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

Licensed under the BSD 3-Clause License. You may obtain a copy of the License at http://opensource.org/licenses/BSD-3-Clause

[mg_BadgeLicense]: https://img.shields.io/github/license/viharm/HDDtempNC.svg?style=flat-square
[mg_BadgeVersion]: https://img.shields.io/github/release/viharm/HDDtempNC.svg?style=flat-square
[mg_BadgeIssues]: https://img.shields.io/github/issues/viharm/HDDtempNC.svg?style=flat-square
[mg_BadgeCodeLang]: https://img.shields.io/badge/language-python-yellowgreen.svg?style=flat-square
[ln_ReleaseLatest]: https://github.com/viharm/HDDtempNC/releases/latest
[ln_License]: https://github.com/viharm/HDDtempNC/blob/master/LICENCE
[ln_Issues]: https://github.com/viharm/HDDtempNC/issues
[ln_CodeLang]: https://www.python.org/
