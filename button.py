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
import pygame


class BaseButton(oop.Object):
    def __init__(self, win, color, text):
        oop.Object.__init__(self, win)
        self.generate_images(color, text)
        self.set_image(self.normal_image)

    def generate_images(self, color, text):
        self.normal_image = self.create_button_surface(color, text)

    def create_button_surface(self, color, text):
        color_surface = self.create_color_surface(color)
        border_surface = self.create_border_surface()
        text_surface = self.create_text_surface(text)
        base_surface = self.create_base_surface(color_surface, border_surface, text_surface)

        return base_surface
 
    @staticmethod
    def create_color_surface(color):
        color_surface = pygame.Surface((850, 250))
        color_surface.fill(color)

        return color_surface

    @staticmethod
    def create_text_surface(text):
        text = oop.Text(None, text, color=(30, 30, 30),
                font=pygame.font.SysFont(None, 90),padding=(60, 60))

        image = text.get_image()

        return image
    
    @staticmethod
    def create_border_surface():
        return oop.image_tools.load_image("images/button-base.png")
    
    @staticmethod
    def create_base_surface(color_surface, border_surface, text_surface):
        base_surface = pygame.Surface((900, 300))
        base_surface.set_colorkey([0,0,0])
        base_surface.blit(color_surface, (25,25))
        base_surface.blit(border_surface, (0,0))
        base_surface.blit(text_surface, (0,0))
        return base_surface


class StandardButton(BaseButton):
    def __init__(self, win, color, text, button_size):
        self.button_size=button_size
        BaseButton.__init__(self, win, color, text)
        self.add_demons()

    def generate_images(self, color, text):
        BaseButton.generate_images(self, color, text)

        color_lighter_image = oop.colors.make_lighter(color, 100)
        self.active_image = self.create_button_surface(color_lighter_image, text)

    def add_demons(self):
        self.generate_actions()
        self.add_under_cursors_demons()
        self.add_on_click_demon()

    def generate_actions(self):
        self.under_cursor_action = lambda: self.set_image(self.active_image)
        self.on_not_under_cursor_action = lambda: self.set_image(self.normal_image)
        self.on_click_action = lambda: None

    def add_under_cursors_demons(self):
        self.on_under_cursor_demon = oop.demons.OnObjectUnderCursor(self, self.under_cursor_action)
        self.on_not_under_cursor_demon = oop.demons.OnObjectNotUnderCursor(self, self.on_not_under_cursor_action)

        self.master_window.add_demon(self.on_not_under_cursor_demon)
        self.master_window.add_demon(self.on_under_cursor_demon)

    def add_on_click_demon(self):
        self.on_click_demon = oop.demons.OnObjectClick(self, self.on_click_action)
        self.master_window.add_demon(self.on_click_demon)

    def set_on_click_action(self, func):
        self.on_click_action = lambda: func(self)
        self.on_click_demon.set_action(self.on_click_action)

    def create_button_surface(self, color, text):
        base_surface = BaseButton.create_button_surface(self, color, text)
        base_surface = oop.image_tools.scale_image(base_surface, self.button_size)
        return base_surface


if __name__ == "__main__":
    win = oop.Window(flags = 0, bg_color = oop.colors.white)
    b = StandardButton(win, (255, 0, 0), button_size=(300,300),
                        text="Something that is gonna be write on our red button")

    while True:
        win.do_routine()
