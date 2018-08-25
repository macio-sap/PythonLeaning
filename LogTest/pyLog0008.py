#-*- coding:utf-8 -*-
import pyLog0006 as p6
import os
import os.path

def testP6log():
    Log = p6.Logger('create_log',logger_name=__name__)
    Log.outputLog()
    try:
        open('/path/to/does/not/exist', 'rb')
    # except (SystemExit, KeyboardInterrupt):
    #     raise
    # except Exception, e:
    except Exception:
        Log.outputLogInfo('Failed to open file')

if __name__ == '__main__':
    print(os.getcwd())
    Log = p6.Logger('create_log',logger_name=__name__)
    Log.outputLog()