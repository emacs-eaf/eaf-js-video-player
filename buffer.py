#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Copyright (C) 2018 Andy Stewart
#
# Author:     Andy Stewart <lazycat.manatee@gmail.com>
# Maintainer: Andy Stewart <lazycat.manatee@gmail.com>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from core.utils import PostGui
from core.webengine import BrowserBuffer
from PyQt6.QtCore import QTimer


class AppBuffer(BrowserBuffer):
    def __init__(self, buffer_id, url, arguments):
        BrowserBuffer.__init__(self, buffer_id, url, arguments, False)

        self.buffer_widget.loadFinished.connect(self.init_path)
        self.load_index_html(__file__)

    @PostGui()
    def init_path(self):
        self.buffer_widget.eval_js("init(\"{}\");".format(self.url))

    def save_session_data(self):
        return str(self.buffer_widget.execute_js("getCurrentTime();"))

    def restore_session_data(self, session_data):
        self.position = session_data
        QTimer.singleShot(600, self.restore_seek_position)

    def restore_seek_position(self):
        self.buffer_widget.eval_js("setCurrentTime('{}');".format(self.position))
