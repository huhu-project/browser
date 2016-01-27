#!/usr/bin/env python
#-*- coding:utf-8 -*-

# huhu_browser
# https://github.com/huhu-project/huhu_browser

# Licensed under the MIT license:
# http://www.opensource.org/licenses/mit-license
# Copyright (c) 2016 Mehmet Kose mehmet@linux.com

from gi.repository import Gtk, GLib, WebKit

class HuhuBrowser:
    def __init__(self):
        window = Gtk.Window(type=Gtk.WindowType.TOPLEVEL)
        window.connect('delete-event', Gtk.main_quit)
        window.set_title("HuhuBrowser")
        window.show_all()

        self.view = WebKit.WebView()
        self.view.load_uri('http://huhu-project.github.io')

        window.add(self.view)
        window.fullscreen()
        window.show_all()

if __name__ == "__main__":
    HuhuBrowser()
    Gtk.main()