app_name="hrm"
rel_login_url="login"
import os
host_dir= ""
def on_authenticate(sender):
    return True
def on_get_language_resource_item(language,appname,view,key,value):
    return value