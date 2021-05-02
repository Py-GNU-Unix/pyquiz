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

import time
import sys
import random
import pygame
import oopygame as oop
import button
import scene
import quizbutton
import yaml_reader

class Istance:
    def __init__(self, yaml_filename):
        self.parser = yaml_reader.YamlParser(yaml_filename)
        self.questions = self.parser.get_questions()

    def start_app(self):
        win_prop = self.get_win_prop()
        self.win = oop.Window(size=(600, 600), **win_prop)
        self.ask_questions()

    def get_win_prop(self):
        win_prop = self.parser.get_root_properties()
        win_prop["title"] = "pyquiz | made with <3 by the open-source community"
        win_prop["bg_color"] = oop.colors.white

        return win_prop

    def ask_questions(self):
        counter = 0
        start_time = time.time()

        while counter < 20:
            question = random.choice(list(self.questions.values()))
            self.create_question_text(question)
            buttons = list(self.create_buttons_for_question(question))
            s = scene.Scene(buttons, self.win)

            while s.esit is None:
                self.win.do_routine()

            if s.esit:
                counter += 1
            else:
                counter -= 3
                counter = max(counter, 0)
        
        end_time = time.time()
        elapsed_time = end_time - start_time
        button.StandardButton(self.win, oop.colors.white, 
                              f"You have finished in {elapsed_time} seconds", (600, 200))

        while True:
            self.win.do_routine()

        
    def create_question_text(self, question):
        oop.Text(self.win, question["text"], size=(600, 200), font=pygame.font.SysFont(None, 42))
        


    def create_buttons_for_question(self, question):
        buttons_dict = question["buttons"]

        for button_attrs in buttons_dict.values():
            color = eval(button_attrs.get("color", oop.colors.red), {}, {})
            yield quizbutton.QuizButton(self.win, color, is_right=button_attrs["value"], text=button_attrs["text"])



        
       

if __name__ == "__main__":
    target = sys.argv[1]
    Istance(target).start_app()
