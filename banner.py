# This file is part of pyquiz.
#
# pyquiz is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# pyquiz is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with pyquiz.  If not, see <https://www.gnu.org/licenses/>.

# Copyright 2021 Py-GNU-Unix

import oopygame as oop
import button

class ResponseBanner(button.StandardButton):
    def __init__(self, win, esit):
        self.clicked = False
        text, color = self.calcolate_text_and_color(esit)
        button.StandardButton.__init__(self, win, color, text, button_size=(600, 200))
        self.set_on_click_action(self.set_clicked_to_true)

    @staticmethod
    def calcolate_text_and_color(esit):
        if esit:
            text = "U R RIGHT!"
            color = oop.colors.yellow
        else:
            text = "The next time\nwill be better."
            color = oop.colors.red

        return text, color

    def set_clicked_to_true(self, *_):
        self.clicked = True
