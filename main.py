import os
import signal
import sys
import platform
import psutil


def free_mem_win():
    print("Current operating system is Windows")

    confirm = input("Do you want to start memory cleanup? (y/n): ")
    if confirm != 'y':
        return

    # 程序本身占用的内存
    own_process = psutil.Process(os.getpid())
    own_mem_info = own_process.memory_info()
    own_mem_used = own_mem_info.rss

    # 释放前内存占用
    pre_free_mem = psutil.virtual_memory()
    pre_free_total = pre_free_mem.total
    pre_free_used = pre_free_mem.used - own_mem_used
    print(f"Before free: Used mem {pre_free_used / 1024 / 1024:.2f}MB / Total mem {pre_free_total / 1024 / 1024:.2f}MB")

    processes = psutil.process_iter()
    for proc in processes:
        status = proc.status()
        # 清理进程状态是 zombie 或 stopped
        if status in ['zombie', 'stopped']:
            print(f"{proc.name()} is currently {proc.status()}, mem usage {proc.memory_info().rss / 1024 / 1024:.2f}MB")
            proc.kill()

    # 释放后内存占用
    post_mem = psutil.virtual_memory()
    post_total = post_mem.total
    post_used = post_mem.used - own_mem_used
    print(f"After free: Used mem {post_used / 1024 / 1024:.2f}MB / Total mem {post_total / 1024 / 1024:.2f}MB")

    input("Memory Free completed. Press any key to exit...")


def free_mem_linux():
    print("Current operating system is Linux")

    confirm = input("Do you want to start memory cleanup? (y/n): ")
    if confirm != 'y':
        return

    # 程序本身占用的内存
    own_mem = psutil.Process(os.getpid()).memory_info().rss

    # 释放前内存占用
    pre_free_mem = psutil.virtual_memory()
    pre_free_total = pre_free_mem.total
    pre_free_used = pre_free_mem.used - own_mem
    print(f"Before free: Used mem {pre_free_used / 1024 / 1024:.2f}MB / Total mem {pre_free_total / 1024 / 1024:.2f}MB")

    # 解析/proc文件系统
    for pid in os.listdir('/proc'):
        # 检查pid是否只包含数字
        if not pid.isdigit():
            continue

        # 跳过pid小于等于100的进程
        if int(pid) <= 100:
            continue

        try:
            p = psutil.Process(int(pid))
            status = p.status()
            # 不清理进程状态是 running 或 sleeping 或 disk sleep
            if status in ['running', 'sleeping', 'disk sleep']:
                continue

            print(f"{p.name()} is currently {p.status()}, mem usage {p.memory_info().rss / 1024 / 1024:.2f}MB")
            os.kill(int(pid), signal.SIGKILL)
        except IOError:
            continue

    # 释放后内存占用
    post_mem = psutil.virtual_memory()
    post_total = post_mem.total
    post_used = post_mem.used - own_mem
    print(f"After free: Used mem {post_used / 1024 / 1024:.2f}MB / Total mem {post_total / 1024 / 1024:.2f}MB")

    input("Memory Free completed. Press any key to exit...")


def free_mem_mac():
    print("Current operating system is macOS")

    confirm = input("Do you want to start memory cleanup? (y/n): ")
    if confirm != 'y':
        return

    input("Memory Free completed. Press any key to exit...")


def get_platform():
    if sys.platform not in platform.platform:
        return sys.platform

    return platform.platform[sys.platform]


if __name__ == '__main__':
    platform = get_platform()
    if platform == 'Windows':
        free_mem_win()

    elif platform == 'Linux':
        free_mem_linux()

    elif platform == 'OS X':
        free_mem_mac()

    else:
        print('Unknown OS')
