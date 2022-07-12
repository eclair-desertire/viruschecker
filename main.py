from http import client
import apikey # your own file with YOUR API KEY, you can get it on virustotal site
import vt
from tkinter import *

client=vt.Client(apikey.api_key)