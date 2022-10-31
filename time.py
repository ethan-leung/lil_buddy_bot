from win32gui import GetWindowText, GetForegroundWindow
import time
import keyboard

if __name__ == '__main__':
    on_too_long = False
    timestamp_app = {}
    viewtime_app = {}
    prev_app = ""
    total = 0

    timestamp_tab = {}
    viewtime_tab = {}
    prev_tab = ""
    on = True
    while on is True:
        new_window = GetWindowText(GetForegroundWindow())
        window_length = len(new_window.split(' - '))
        new_app = new_window.split(' - ')[window_length - 1]
        new_tab = new_window.split(' - ')[window_length - 2]
        tab_length = len(new_tab.split(' | '))
        new_tab = new_tab.split(' | ')[tab_length - 1]
        possibleApps = ["Visual Studio Code", "Google Chrome", "Discord"]
        if new_app != prev_app:
            on_too_long = False
            if new_app not in timestamp_app.keys():
                viewtime_app[new_app] = 0
            if prev_app != "":
                time_spent_app = 1
                viewtime_app[prev_app] = viewtime_app[prev_app] + 1
            t0app = int(time.time())
            timestamp_app[new_app] = t0app
            prev_app = new_app
        else:
            viewtime_app[new_app] = viewtime_app[new_app] + 1
        if new_app == "Discord":
            if int(time.time() - timestamp_app[new_app]) > 5 and on_too_long == False:
                print ("you've been on", new_app, "for a bit too long!")
                on_too_long = True
        if new_app == "Google Chrome":
            if new_tab != prev_tab:
                tab_on_too_long = False
                if new_tab not in timestamp_tab.keys():
                    viewtime_tab[new_tab] = 0
                if prev_tab != "":
                    viewtime_tab[prev_tab] = viewtime_tab[prev_tab] + 1
                t0tab = int(time.time())
                timestamp_tab[new_tab] = t0tab
                prev_tab = new_tab
            else:
                viewtime_tab[new_tab] = viewtime_tab[new_tab] + 1
            if new_tab == "YouTube" or new_tab == "Twitch":
                if int(time.time() - timestamp_tab[new_tab]) > 5 and tab_on_too_long == False:
                    print("you've been on", new_tab, "for a bit too long!")
                    tab_on_too_long = True
        
        if keyboard.is_pressed("`"):
            on = False
        time.sleep(1)
    print ("time in seconds for each application:" + str(viewtime_app) + "\ntime in seconds for each tab:" + str(viewtime_tab))