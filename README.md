# Memory Free

On Windows, Linux, and macOS operating systems, Memory Free is a standalone tool created to aid effective memory management and memory release. The whole source code and materials required to create and execute the Memory Free program are available in this repository.

## Packaging

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
  pip install psutil
  pip install pyinstaller
  pyinstaller -F --name MemoryFree main.py
  ```

## Run

+ Windows
  ```
  Current operating system is Windows
  Do you want to start memory free? (y/n): y
  Before free: Used mem 2245.92MB / Total mem 8999.05MB
  backgroundTaskHost.exe is currently stopped, mem usage 29.00MB
  SearchApp.exe is currently stopped, mem usage 185.90MB
  backgroundTaskHost.exe is currently stopped, mem usage 28.35MB
  SystemSettings.exe is currently stopped, mem usage 49.37MB
  backgroundTaskHost.exe is currently stopped, mem usage 49.62MB
  After free: Used mem 2063.30MB / Total mem 8999.05MB
  Memory Free completed. Press Enter key to exit...
  ```

+ Linux
  ```
  wutianhao@ubuntu:~/Desktop/MemoryFree/dist$ ./MemoryFree
  Current operating system is Linux
  Do you want to start memory free? (y/n): y
  Before free: Used mem 1119.88MB / Total mem 19488.50MB
  ...
  nbound is currently idle, mem usage 0.00MB
  kworker/u256:11-events_unbound is currently idle, mem usage 0.00MB
  kworker/u256:12-events_unbound is currently idle, mem usage 0.00MB
  kworker/u256:13-events_unbound is currently idle, mem usage 0.00MB
  kworker/u256:14-events_unbound is currently idle, mem usage 0.00MB
  ...
  After free: Used mem 1009.88MB / Total mem 19488.50MB
  Memory Free completed. Press Enter key to exit...
  ```

+ macOS
  ```
  TODO
  ```

## License

```
MIT License

Copyright (c) 2023 Tyhoo Wu

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```
