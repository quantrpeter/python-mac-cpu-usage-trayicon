import rumps
import psutil

class CpuUsageApp(rumps.App):
    def __init__(self):
        super(CpuUsageApp, self).__init__("CPU")
        self.timer = rumps.Timer(self.update, 1)
        self.timer.start()

    def update(self, _):
        cpu = psutil.cpu_percent()
        self.title = f"CPU: {cpu}%"

if __name__ == "__main__":
    CpuUsageApp().run()
