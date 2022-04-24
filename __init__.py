from zim.plugins import PluginClass

class MyPlugin(PluginClass):

  plugin_info = {
    'name': _('My Plugin'),
    'description': _('My first plugin'),
    'author': 'Your Name',
  }
