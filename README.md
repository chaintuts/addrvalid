## General
____________

### Author
* Josh McIntyre

### Website
* jmcintyre.net

### Overview
* AddrVal is a library for cryptocurrency address validation

## Development
________________

### Git Workflow
* master for releases (merge development)
* development for bugfixes and new features

### Building
* make build
Build the application
* make clean
Clean the build directory

### Features
* Validate a Digibyte address

### Requirements
* Requires Python

### Platforms
* Windows
* MacOSX
* Linux

## Usage
____________

### Library Usage
* `import addrvalid`
* `valid = addrvalid.validate_digibyte(<address>)`

### Run unit tests
* Run `python -m pytest <test file>`