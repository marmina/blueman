from blueman.Constants import *
import gtk
import re

def get_icon(name, size=24):
	ic = gtk.icon_theme_get_default()
	if not ICON_PATH in ic.get_search_path():
		ic.prepend_search_path(ICON_PATH)
		ic.prepend_search_path(ICON_PATH + "/devices")
		ic.prepend_search_path(ICON_PATH + "/signal")
	try:
		icon = ic.load_icon(name, size, 0) 
	except:
		icon = ic.load_icon("bluetooth", size, 0) 

	
	return icon
	
def adapter_path_to_name(path):
	return re.search(".*(hci[0-9]*)", path).groups(0)[0]