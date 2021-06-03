import config
import importlib

def anim_start(anim_name,all_lines,chosen_line):
    anim_module = importlib.import_module('ui_console.animations.'+anim_name+'.start','.')
    anim_module.anim(all_lines, chosen_line)
