#
# This file is part of lmountd.
#
# lmountd is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# lmountd is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with lmountd.  If not, see <http://www.gnu.org/licenses/>.

from distutils.core import setup

setup(name='warwick.observatory.lmount',
      version='0',
      packages=['warwick.observatory.lmount'],
      author='Paul Chote',
      description='Common code for the Warwick L mount daemon',
      license='GNU GPLv3',
      author_email='p.chote@warwick.ac.uk',
      url="https://github.com/warwick-one-metre/lmountd")
