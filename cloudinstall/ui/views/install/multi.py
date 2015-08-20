# Copyright 2015 Canonical, Ltd.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

""" Multi Install View

Diagram:

Ubuntu OpenStack Installer - Multi Install

                  Performing Multi Install...

[## Initializing Env ##][Creating Container][Initializing Container]

[#### Progress 20%                                                 ]

----------------------------- Output -------------------------------

Console logging...
etc etc...


"""

import logging
from urwid import WidgetWrap, Columns, Text, ListBox
from cloudinstall.ui.utils import Color, Padding


log = logging.getLogger("cloudinstall.u.v.i.multi")


class MultiInstallViewException(Exception):
    "Problem in Multi Install View"


class MultiInstallView(WidgetWrap):
    def __init__(self):
        body = [
            Padding.center_50(Color.body(
                Text("Performing Multi Install..."))),
            Padding.line_break(""),
            Padding.center_79(self._build_status_indicators())
        ]
        super().__init__(ListBox(body))

    def _build_status_indicators(self):
        """ Displays the status columns for each task running """
        col = [
            ("weight", 0.2, Color.body(Text("Bootstrapping Juju")))
        ]
        return Columns(col)