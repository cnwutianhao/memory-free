# Memory Free

### Description
Memory Free is a standalone application designed to facilitate efficient memory management and memory release on Windows, Linux, and macOS operating systems. This repository provides the complete source code and resources necessary to build and run the Memory Free application.

### Packaging

> Before proceeding with the packaging, please ensure that the Python environment on your computer is properly configured.

+ Windows
  ```
  pip install psutil
  pip install pyinstaller
  pyinstaller -F --name MemoryFree ./main.py
  ```

+ Linux
  ```
  sudo pip install psutil
  sudo pip install pyinstaller
  pyinstaller -F --name MemoryFree main.py
  ```

+ macOS
  ```
  TODO
  ```
