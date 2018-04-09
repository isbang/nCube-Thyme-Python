## Project title
nCube-Thyme-Python compatible with [Mobius-2.0.0](https://github.com/IoTKETI/Mobius/tree/Mobius-2.0.0)

## Motivation
There is a [nCube-Thyme-Nodejs](https://github.com/IoTKETI/nCube-Thyme-Nodejs), [nCube-Thyme-Arduino](https://github.com/IoTKETI/nCube-Thyme-Arduino), [nCube-Thyme-Java](https://github.com/IoTKETI/nCube-Thyme-Java), [nCube-Thyme-Android](https://github.com/IoTKETI/nCube-Thyme-Android), but ***NOT IN Python***

For Python lover like me, I made this nCube-Thyme-Python.


## How to use?
First, you should change conf.py (configuration file) about your AE. Check the commented line.

Second, check thyme.py and fix it whatever you want.

You can also refer my IoTCCTV code from branch [IoTCCTV](https://github.com/Holmes1st/nCube-Thyme-Python/tree/IoTCCTV)

For more fine tuning
 - mqtt_adn.py: The code for all requests to CSE
 - mqtt_app.py: The code for mqtt action

After all, run
```bash
$ python3 thyme.py
```

## Used
Core : [Python3](https://www.python.org/downloads/)

Wroking with : [Mobius-2.0.0](https://github.com/IoTKETI/Mobius/tree/Mobius-2.0.0)

Editor : [Atom Editor](https://atom.io/)

Style-Guide : [python-yapf atom plugin](https://github.com/blacktop/atom-python-yapf)

## Code Example
- [IoTCCTV](https://github.com/Holmes1st/nCube-Thyme-Python/tree/IoTCCTV)
- [Container Monitor](https://github.com/Holmes1st/nCube-Thyme-Python/tree/CNT_Monitor)

## Installation
Just for this nCube-Thyme-Python project, you need [paho-mqtt](https://pypi.python.org/pypi/paho-mqtt)
```bash
$ python3 -m pip install paho-mqtt
```

## API Reference
[Mobius-2.0.0](https://github.com/IoTKETI/Mobius/tree/Mobius-2.0.0)

[nCube-Thyme-Nodejs-2.0.0](https://github.com/IoTKETI/nCube-Thyme-Nodejs/tree/nCube-Thyme-Nodejs-2.0.0)

[oneM2M](http://onem2m.org/)


## Contribute
Inside of code, there are some TODO lists. Please check from code, and contribute this project.


## Code style
I use atom editor with python-yapf plugin.

- {based_on_style: google, column_limit: 120}

To install yapf:
```bash
$ python3 -m pip install yapf
```

## License
MIT © [Bang](https://github.com/Holmes1st)

## Thanks For
[Sujin Lee](https://github.com/sujinleeme) - [Readme Guide](https://gist.github.com/sujinleeme/ec1f50bb0b6081a0adcf9dd84f4e6271#file-readme-md)
