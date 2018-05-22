import sublime
import sublime_plugin
import os


class CmdCommand(sublime_plugin.TextCommand):
  def run(self, edit):
    directory, _ = os.path.split(self.view.file_name());
    os.chdir(directory)
    os.system('start cmd')
