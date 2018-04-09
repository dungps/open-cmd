import sublime
import sublime_plugin
import os


class CmdCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    file_name=self.view.file_name()
    path=file_name.split("\\")
    current_driver=path[0]
    path.pop()
    current_directory="\\".join(path)
    command= "cmd /K cd "+current_directory
    os.system(command)
