from threading import current_thread, main_thread

def do_somethong():
    print('Executing comething')
    print(current_thread().name)

do_somethong()