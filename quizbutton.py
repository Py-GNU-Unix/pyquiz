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

import button

class QuizButton(button.StandardButton):
    def __init__(self, win, color, is_right, text="Example Text"):
        button.StandardButton.__init__(self, win, color, text=text, button_size=(300, 100))
        self.is_right = is_right
