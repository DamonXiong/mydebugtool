# setup.py 

from distutils.core import setup
import py2exe

setup(windows = [{"script": "debugtool.py", "icon_resources": [(1, "debugtool.ico")] }],
	data_files=[("",[".\debugtool.ico"])])