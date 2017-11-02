#!/usr/bin/env python
# *-* coding:utf8 *-*
# Auther : seekabc

import psutil
memory = psutil.virtual_memory()
print(str(memory.total/1024//1024)+"M", str(memory.used/1024//1024)+"M")


cpu = psutil.cpu_times()
print(cpu)