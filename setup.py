from setuptools import setup

APP = ['cpu_tray.py']
OPTIONS = {
    'iconfile': 'blue.png',
    'packages': ['psutil', 'rumps']
}

setup(
    app=APP,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
)
