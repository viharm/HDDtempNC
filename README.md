# HDDtempNC

|           |                                                 |
|:----------|:------------------------------------------------|
| Version   | 1.3.0                                           |
| Download  | https://github.com/viharm/HDDtempNC/releases    |
| Issues    | https://github.com/viharm/HDDtempNC/issues      |
| License   | Modified BSD (3-clause)                         |
| Language  | [Python](https://www.python.org)                |


*HDDtempNC* is a tool to acquire hard disk drive temperature from *hddtemp*'s network interface.

It is *Python* script and requires a working *Python* environment. It depends a configured and working *hddtemp* daemon on the system whose HDD temperatures are required.


## Install


### Pre-requisites

* Python 2.x or 3.x
* Working instance of *HDDtemp* running in daemon mode and listening on a TCP port (*HDDtemp* need not be running on the same host as the one running *HDDtempNC*, however must be reachable via TCP port)


## Download


### Package

Get the package from the download linked above.


### Git clone

Clone repository.

```
git clone --recurse-submodules \
https://github.com/viharm/phpAria2rpc.git
```

Remember to clone recursively (`--recurse-submodules`) to ensure cloning the submodules.


### PyPI

From version v1.3.0 onwards, *HDDtempNC* is available on *[PyPI](https://pypi.org/)* and can be installed with *pip* (or *pip3*)


### Deploy

Save the downloaded directory structure in your choice of path within your application (plugins, includes, etc.)


## Usage ##

*HDDtempNC* can be used either from the command line or by calling it in another script/program


### Command syntax ###

The command syntax using long semantic arguments is as follows

```
hddtempnc.py --disk=/dev/<diskpath> [ --target=<hostname> ] [ --port=<HDDtemp port> ] [ --debug ] [ --help ]
```

The command syntax using short *POSIX*-style arguments is as follows

```
hddtempnc.py -d /dev/<diskpath> [ -t <hostname> ] [ -p <HDDtemp port> ] [ -g ] [ -h ]
```

Following parameters are available:

|       Argument        |       Alternative argument        |                       Description                              | Optional |   Default   |
| --------------------- | --------------------------------- | -------------------------------------------------------------- |:--------:|:-----------:|
| `-g`                  | `--debug`                         |Debug to console/stdout                                         |   Yes    |    None     |
| `-t 192.168.0.30`     | `--target=server.local`           |Specify target host (IP address or resolvable host name)        |   Yes    | `localhost` |
| `-p 3378`             | `--port=3698`                     |Specify target host's port                                      |   Yes    |    `7634`   |
| `-d /dev/sda`         | `--disk=/dev/sda`                 |Specify disk to interrogate (full device path)                  |    No    |     None    |
| `-h`                  | `--help`                          |Show help                                                       |   Yes    |    None     |



#### Options

The above command options are explained below. The sequence of parameters is not important.


##### Disk

`-d <disk> (--disk=<disk>)`

Specify disk to interrogate by providing full path to the block device

Example: `/dev/sda`

Optional: No

Default value: None


##### Host

`-t <host> (--target=<host>)`

Specify target host to interrogate. *HDDtemp* must be running on this host (in daemon mode) and listening on a TCP port.

Examples: `192.168.0.30`, `server.local`, `server.domain.tld`

Optional: Yes

Default value: `localhost`


##### Port
  
`-p <port> (--port=<port>)`

Specify target port to interrogate. *HDDtemp* must be listening on this port.

Optional: Yes

Default value: `7634`


##### Debug

`-g (--debug)`

Enable debugging to console/stdout

Optional: Yes

Default value: None


##### Runtime help

`-h (--help)`

Show help and exit.

Optional: Yes

Default value: None


### Examples ###

Command examples


#### Long parameters ####

```
/usr/bin/python3 hddtempnc.py --disk=/dev/sda`
/usr/bin/python3 hddtempnc.py --target=192.168.0.20 --disk=/dev/sdb
/usr/bin/python hddtempnc.py --port=7630 --disk=/dev/sdc
/usr/bin/python hddtempnc.py --disk=/dev/sda --port=9000 --target=10.65.0.65
```


#### Short parameters

```
/usr/bin/python3 hddtempnc.py -d /dev/sda
/usr/bin/python3 hddtempnc.py -t 192.168.0.20 -d /dev/sdb
/usr/bin/python hddtempnc.py -p 7630 -d /dev/sdc
/usr/bin/python hddtempnc.py -d /dev/sda -p 9000 -t 10.65.0.65
```


## Support

Feature requests, bugs, issues and other comments can be created at the issues link provided at the top of this page.


# Contribute

Please feel free to clone/fork and contribute via pull requests. Donations also welcome, simply create an issue by using the link provided at the top of this page.

Please make contact for more information.


# Environments

Developed on..

* *Debian Wheezy*
* *Debian Jessie*
* *Debian Stretch*

Known to be working on 

* *Debian Wheezy*
* *Debian Jessie*
* *Debian Stretch*
* *FreeBSD* 11.2-RELEASE
* *Windows* 10
* *Python* 3.7


## Links ##

* *hddtemp* home
  http://www.guzu.net/linux/hddtemp.php
* *hddtemp* on *[Savannah](http://savannah.gnu.org/)*
  https://savannah.nongnu.org/projects/hddtemp/
* *hddtemp* guide on *Arch* wiki
  https://wiki.archlinux.org/index.php/Hddtemp


## License

Licensed under the modified BSD (3-clause) license.

A copy of the license is available...

* in the enclosed [`LICENSE`](LICENCE) file.
* at http://opensource.org/licenses/BSD-3-Clause


# Credits


#### Codiad

*Codiad* web based IDE (https://github.com/Codiad/Codiad), used under a MIT-style license.

Copyright (c) Codiad & Kent Safranski (codiad.com)


#### CodeGit

*CodeGit* *Git* plugin for *Codiad* (https://github.com/Andr3as/Codiad-CodeGit), used under a MIT-style license.

Copyright (c) Andr3as <andranode@gmail.com>


#### Ungit

*Ungit* client for *Git* (https://github.com/FredrikNoren/ungit) used under the MIT license

Copyright (C) Fredrik Norén


## GitHub

Hosted by *GitHub* code repository (github.com).

