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

class Grid:
    def __init__(self, elements, max_line_len=2):
        self.elements = elements
        self.max_line_len = max_line_len
        self.row = 0; self.column = 0

    def __iter__(self):
        count = 0
        while count < self.elements:
            yield self.get_values()
            self.next_step()
            count += 1


    def next_step(self):
        self.column += 1
        self.check_newline()

    def check_newline(self):
        if self.need_newline():
            self.insert_newline()

    def need_newline(self):
        return self.column == self.max_line_len

    def insert_newline(self):
        self.column = 0
        self.row += 1

    def get_values(self):
        return self.row, self.column
