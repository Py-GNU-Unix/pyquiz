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
import quizbutton
import banner
import grid


class Scene:
    def __init__(self, buttons, master_window, background_filename=None):
        self.buttons = buttons
        self.master_window = master_window
        self.background_filename = background_filename
        if background_filename:
            self.place_background()
        self.place_buttons()
        self.set_button_actions()
        self.esit = None

    def place_buttons(self, max_line_len=2):
        buttons_grid = grid.Grid(len(self.buttons), max_line_len)

        for (row, column), button in zip(buttons_grid, self.buttons):
            pos = column*300, 400+row*100
            button.set_pos(pos)

    def set_button_actions(self):
        for button in self.buttons:
            button.set_on_click_action(lambda button: self.on_button_pressure(button.is_right))

    def on_button_pressure(self, esit):
        if self.esit != None:
            return 0

        self.esit = esit
        b = banner.ResponseBanner(self.master_window, esit)

        while not b.clicked:
            self.master_window.do_routine()

        self.die()


    def place_background(self):
        background_surface = oop.image_tools.load_image(self.background_filename)
        window_size = self.master_window.get_window_size()
        background_surface = oop.image_tools.scale_image(background_surface, window_size)
        background = oop.Object(self.master_window, image=background_surface, depth_level = -1)
        
        return background

    def die(self):
        self.master_window.objects[0] = []
    
    def is_die(self):
        return self.is_the_result_right



if __name__ == "__main__":
    win = oop.Window(size=(600,600), bg_color=(255,255,255))
    b1 = quizbutton.QuizButton(win, oop.colors.red, True)
    b2 = quizbutton.QuizButton(win, oop.colors.green, False)
    b3 = quizbutton.QuizButton(win, oop.colors.blue, False)
    b4 = quizbutton.QuizButton(win, oop.colors.orange, False)

    Scene((b1, b2, b3, b4), win, background_filename="images/background.jpeg")
    while True:

        win.do_routine()
