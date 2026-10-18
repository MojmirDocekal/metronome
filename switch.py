#!/usr/bin/env python3
#-*- coding: utf-8 -*-
'''
    the switchable_object should have a run() function, and a running flag.
    the run() function should have a
        while self.running:
    condition in it
'''

from threading import Thread
from getch import getch

class Switch():
    def __init__(self, switchable_object, switchable_object_args=(), **kwargs):
        target = switchable_object
        while True:
            runner = Thread(target=target, args=switchable_object_args)
            runner.start()
            stop_key = getch()
            target.running = False
            #runner.join()
            if stop_key == 'q':
                if hasattr(target, 'stop'):
                    target.stop()
                print('quitting, letting ' + str(target) + ' finish loop.')
                raise SystemExit
            else:
                if hasattr(target, 'stop'):
                    target.stop()
                del(runner)
                start_key = getch()
                if start_key == 'q':
                    raise SystemExit
                continue


