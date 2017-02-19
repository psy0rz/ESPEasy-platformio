# ESPEasy-platformio

This is an ESPEasy build environment that you can use to quickly compile ESPEasy with http://platformio.org

We also use this repository to automaticly build and release firmware.bin files for ESPEasy.

Automated build status: [![Build Status](https://travis-ci.org/letscontrolit/ESPEasy-platformio.svg?branch=master)](https://travis-ci.org/letscontrolit/ESPEasy-platformio)

## Steps

### 1. Clone the repository with the --recursive option:
```
psy@psypad ~ % git clone --recursive https://github.com/psy0rz/ESPEasy-platformio.git
Cloning into 'ESPEasy-platformio'...
remote: Counting objects: 89, done.
remote: Compressing objects: 100% (67/67), done.
remote: Total 89 (delta 11), reused 89 (delta 11), pack-reused 0
Receiving objects: 100% (89/89), 37.80 KiB | 0 bytes/s, done.
Resolving deltas: 100% (11/11), done.
Checking connectivity... done.
Submodule 'lib/ArduinoJson' (https://github.com/bblanchon/ArduinoJson.git) registered for path 'lib/ArduinoJson'
Submodule 'lib/IRremoteESP8266' (https://github.com/sebastienwarin/IRremoteESP8266.git) registered for path 'lib/IRremoteESP8266'
Submodule 'src' (https://github.com/psy0rz/ESPEasy.git) registered for path 'src'
Cloning into 'lib/ArduinoJson'...
remote: Counting objects: 7944, done.
remote: Compressing objects: 100% (62/62), done.
remote: Total 7944 (delta 18), reused 0 (delta 0), pack-reused 7881
Receiving objects: 100% (7944/7944), 2.49 MiB | 649.00 KiB/s, done.
Resolving deltas: 100% (5466/5466), done.
Checking connectivity... done.
Submodule path 'lib/ArduinoJson': checked out 'a498abc14afb98dc1de77bf1cf8bab44afafec0c'
Cloning into 'lib/IRremoteESP8266'...
remote: Counting objects: 68, done.
remote: Total 68 (delta 0), reused 0 (delta 0), pack-reused 68
Unpacking objects: 100% (68/68), done.
Checking connectivity... done.
Submodule path 'lib/IRremoteESP8266': checked out 'fee16e880b19807d46d410e4752d52d13b5e7330'
Cloning into 'src'...
remote: Counting objects: 1637, done.
remote: Total 1637 (delta 0), reused 0 (delta 0), pack-reused 1637
Receiving objects: 100% (1637/1637), 1.32 MiB | 305.00 KiB/s, done.
Resolving deltas: 100% (1237/1237), done.
Checking connectivity... done.
Submodule path 'src': checked out '5fe033bef882136e2860e6536d33494f13b0325d'
```

### 2. Start atom:

```
psy@psypad ~ % atom ESPEasy-platformio 
```

### 3. Press F7 to build and upload.

Easy isnt it? :)

