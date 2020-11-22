#!/usr/bin/python
import notify2
import sched
import time


def notify(sc):
    notify2.init("Cryptocurrency rates notifier")
    n = notify2.Notification("Rest the vision",
                             icon='/home/bonilla/Desktop/PythonProjects/notification_builder/focus.png')
    n.set_urgency(notify2.URGENCY_NORMAL)

    n.set_timeout(5000)

    n.update("Rest the vision", 'Look to the infinity for 2 minutes')
    n.show()

    s.enter(60 * 30, 1, notify, (sc,))


s = sched.scheduler(time.time, time.sleep)
s.enter(60 * 30, 1, notify, (s,))
s.run()
