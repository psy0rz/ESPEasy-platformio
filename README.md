# ESPEasy-platformio

This is an ESPEasy build environment for the next 2.0.0 release of ESPEasy (formally called ESPEasyMega).

Current automated build status: [![Build Status](https://travis-ci.org/letscontrolit/ESPEasy-platformio.svg?branch=mega)](https://travis-ci.org/letscontrolit/ESPEasy-platformio)

The src is pointing to the mega-branch in the normal ESPEasy repository (its a git submodule), so thats where the actual sourcecode is.

Issues that still need to be fixed before releasing: https://github.com/letscontrolit/ESPEasy/milestone/1

## Steps

### 1. Clone the repository with these options:
```
$ git clone --recursive -b mega https://github.com/letscontrolit/ESPEasy-platformio.git
```

### 2. Start atom:

```
$ atom ESPEasy-platformio 
```

### 3. Press F7 to build and upload.

You can select the version you want as well. (mini/normal/testing/dev)

Easy isnt it? :)

