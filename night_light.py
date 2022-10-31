import subprocess, time, datetime

if __name__ == '__main__':
    def data_bytes(enabled, nl_start_hour, nl_start_min, nl_end_hour, nl_end_min, nl_temp):
        data = (0x43, 0x42, 0x01, 0x00, 0x0A, 0x02, 0x01, 0x00, 0x2A, 0x06)
        offset_time = datetime.datetime.now()
        epochTime = int(time.mktime(offset_time.timetuple()))
        data += (epochTime & 0x7F | 0x80,)
        data += ((epochTime >> 7) & 0x7F | 0x80,)
        data += ((epochTime >> 14) & 0x7F | 0x80,)
        data += ((epochTime >> 21) & 0x7F | 0x80,)
        data += (epochTime >> 28,)
        data += (0x2A, 0x2B, 0x0E, 0x1D, 0x43, 0x42, 0x01, 0x00)
        if enabled:
            data += (0x02, 0x01)
        data += (0xCA, 0x14, 0x0E)
        data += (nl_start_hour,)
        data += (0x2E,)
        data += (nl_start_min,)
        data += (0x00, 0xCA, 0x1E, 0x0E)
        data += (nl_end_hour,)
        data += (0x2E,)
        data += (nl_end_min,)
        data += (0x00, 0xCF, 0x28)
        data += ((nl_temp & 0x3F) * 2 + 0x80,)
        data += ((nl_temp >> 6),)
        data += (0xCA, 0x32, 0x00, 0xCA, 0x3C, 0x00, 0x00, 0x00, 0x00, 0x00)

        return f"Set-ItemProperty -Path 'HKCU:\SOFTWARE\Microsoft\Windows\CurrentVersion\CloudStore\Store\DefaultAccount\Current\default$windows.data.bluelightreduction.settings\windows.data.bluelightreduction.settings' -Name 'Data' -Value ([byte[]]{data}) -Type Binary"

    def run(cmd):
        subprocess.run(["powershell", "-Command", cmd])

    run(data_bytes(False, 21, 0, 7, 0, 3000))
    time.sleep(0.5)

    while True:
        if datetime.time(21, 0, 0) <= datetime.datetime.now().time() or datetime.datetime.now().time() <= datetime.time(7, 0, 0):
            run(data_bytes(True, 21, 0, 7, 0, 3000))
        else:
            run(data_bytes(False, 21, 0, 7, 0, 3000))
