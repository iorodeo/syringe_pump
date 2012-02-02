"""
Copyright 2010  IO Rodeo Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from setuptools import setup, find_packages

setup(name='syringe_pump',
      version='0.1',
      description = 'serial interface to New Era Pump Systems NE-500, NE-501, and NE-1000 Syringe pumps',
      author = 'William Dickson, IO Rodeo Inc.',
      author_email = 'will@iorodeo.com',
      packages=find_packages(),
      )

