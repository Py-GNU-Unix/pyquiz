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

import yaml

class YamlParser:
    def __init__(self, yaml_filename):
        self.load_file(yaml_filename)

    @staticmethod
    def open_yaml(filename):
        with open(filename, "r") as yaml_file:
            root_dict = yaml.safe_load(yaml_file)

        return root_dict
    
    def load_file(self, yaml_filename):
        self.root = self.open_yaml(yaml_filename)
        self.questions_list = self.root["quiz"]["questions"]
        self.root_properties = self.root["quiz"].get("properties")
 

    def get_root(self):
        return self.root

    def get_questions(self):
        return self.questions_list

    def get_root_properties(self):
        return self.root_properties


if __name__ == "__main__":
    par = YamlParser("basedata.yml")
    print(par.get_questions())
    print(par.get_root_properties())
    print(par.get_questions())
