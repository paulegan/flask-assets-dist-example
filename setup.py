#!/usr/bin/env python
import sys
import os
import glob
from distutils.cmd import Command
from distutils.command.build import build
from setuptools.command.install import install
from setuptools import setup, find_packages


class build_static_assets(Command):
    def initialize_options(self):
        self.build_dir = None

    def finalize_options(self):
        self.set_undefined_options('build', ('build_lib', 'build_dir'))

    def run(self):
        sys.path.insert(0, self.build_dir)
        from myapp import run
        status = run(*'assets --parse-templates build --production --no-cache'.split())
        sys.path.remove(self.build_dir)
        if status:
            sys.exit(status)
build.sub_commands.append(('build_static_assets', None))


class install_static_assets(Command):
    def initialize_options(self):
        self.install_dir = None

    def finalize_options(self):
        self.set_undefined_options('install_lib', ('install_dir', 'install_dir'))

    def run(self):
        staticfile = lambda f: os.path.join(self.install_dir, 'myapp/static', f)
        self.outfiles = [staticfile('.webassets-manifest')] + glob.glob(staticfile('gen/*'))

    def get_outputs(self):
        return self.outfiles
install.sub_commands.append(('install_static_assets', None))


setup(
    name="test project",
    version=0.1,
    author="Paul Egan",
    author_email="paulegan@mail.com",
    description="Test project",
    license="BSD",
    zip_safe=False,
    packages=find_packages(),
    package_data={
        '': ['templates/*.html', 'static/*.js']
    },
    entry_points={
        'console_scripts': ['myapp-manage = myapp:run']
    },
    install_requires=['Flask', 'Flask-Script', 'Flask-Assets'],
    cmdclass={
        'build_static_assets': build_static_assets,
        'install_static_assets': install_static_assets,
    },
)