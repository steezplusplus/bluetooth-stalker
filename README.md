### Detect Airpods

Using `PyBluez` it is possible to stalk nearby Bluetooth devices and retrieve a list of their MAC addresses. This simple script listens for bluetooth devices to enter its range, and returns the device's name and MAC address.

## Requirements
This project was created with Python 3.7.6 and on MacOS Mojave. If your system is similar, you need the following. 
```
$ pip3 install pybluez
$ pip3 install pyobjc
```
Then, download xcode off of the app store.

If your system is different, you may require different dependencies to use PyBluez. See the installation guide here `https://pybluez.readthedocs.io/en/latest/install.html`.

# Usage
```
$ python3 main.py
```

