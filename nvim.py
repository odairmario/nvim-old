from parser import parser
import argparse
import os
import re
import yaml

class Nvim(object):

    """Class to represent nvim config"""

    _vimrc_lines = []
    def __init__(self,output,**kwargs):
        """TODO: to be defined. """
        self._output = output
        self._delimiter = kwargs.get("delimiter","|")
        self._delimiter_endline = kwargs.get("delimiter_end_line","\n")
        self._general_setting = {
                "header":kwargs.get("GeneralSettings:header","### general settings"),
                    "command_col":kwargs.get("GeneralSettings:command_col","Command"),
                    "description_col":kwargs.get("GeneralSettings:description_col","Description")
                    }
        self._plugins = {
            "header":kwargs.get("Plugin:header","## My plugins"),
            "name_col":kwargs.get("Plugin:name_col","Name"),
            "description_col":kwargs.get("Plugin:description_col","Description"),
            "url_col":kwargs.get("Plugin:url_col","Url"),
            "start_plugin":kwargs.get("Plugin:start_plugin","call plug#begin()"),
            "end_plugin":kwargs.get("Plugin:end_plugin","call plug#end()")
            }
        self._plugin_settings = {
            "header":kwargs.get("PluginSettings:header","### Plugins settings"),
            "command_col":kwargs.get("PluginSettings:command_col","Command"),
            "description_col":kwargs.get("PluginSettings:description_col","Description"),
            "plugin_col":kwargs.get("PluginSettings:plugin_col","Plugin") }
        self._document_file = kwargs.get("document_file","README.md")
        self._other_configs = kwargs.get("other_configs","config.d")
        with open(self._document_file,"r") as f:
            self._lines = f.readlines()
        
        
    def load_settings(self):
        settings = parser(
                self._general_setting["header"],
                self._delimiter,
                self._delimiter_endline,
                self._lines)
        for setting in settings:
            _setting = re.split("\`(.*?)\`",setting[self._general_setting["command_col"]])[1]
            self._vimrc_lines.append("{}\n".format(_setting))
    def load_plugins(self):
        """load plugins 
        :returns: TODO

        """
        plugins = parser(
                self._plugins["header"],
                self._delimiter,
                self._delimiter_endline,
                self._lines)
        self._vimrc_lines.append("{}\n".format( self._plugins["start_plugin"]))
        for plugin in plugins:
            plugi_url = re.split("\[(.*?)\]",plugin[self._plugins["url_col"]])[1]
            self._vimrc_lines.append("Plug '{}'\n".format(plugi_url))
        self._vimrc_lines.append("{}\n".format(self._plugins["end_plugin"]))

    def load_plugin_settings(self):
        settings = parser(
                self._plugin_settings["header"],
                self._delimiter,
                self._delimiter_endline,
                self._lines)
        for setting in settings:
            _setting = re.split("\`(.*?)\`",setting[self._plugin_settings["command_col"]])[1]
            self._vimrc_lines.append("{}\n".format(_setting))
    def load_other_settings(self):
        """TODO: Docstring for load_other_settings.
        :returns: TODO

        """
        files = os.listdir(self._other_configs)
        for _file in files:
            with open(os.path.join(self._other_configs,_file),"r") as f:
                lines = f.readlines()
                for line in lines:
                    self._vimrc_lines.append(line)

            
    def dump(self):
        """TODO: Docstring for dump.
        :returns: TODO

        """

        self.load_settings()
        self.load_plugins()
        self.load_plugin_settings()
        self.load_other_settings()
        with open(self._output,"w") as f:
            f.writelines(self._vimrc_lines)
        
def handle_cmd_line():
    """handle cmd line
    :returns: TODO

    """
    _parser = argparse.ArgumentParser()
    _parser.add_argument("-o","--output",dest="output",default="./nvimrc.vim")
    _parser.add_argument("-c","--config",dest="config_file",default="./config.yml")
    return _parser.parse_args()

def config(config_file):
    """TODO: Docstring for config.
    :returns: TODO

    """
    if os.path.exists(config_file):
        with open(config_file,"r") as f:
            conf = yaml.load(f,yaml.FullLoader)
        return conf
    return {}
    
def main():
    """Main of program
    :returns: TODO

    """
    args = handle_cmd_line()
    conf = config(args.config_file)
    nvim = Nvim(args.output,**conf)
    nvim.dump()
if __name__ == "__main__":
    main()
