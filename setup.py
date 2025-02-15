
import os
from setuptools import setup, find_packages

version = '0.0.104'

dir_ = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(dir_, 'README.md')) as f:
    long_description = f.read()

with open(os.path.join(dir_, 'requirements.txt')) as f:
    install_requires = f.read()

setup(
    name='iconify',
    version=version,
    description="An icon and image library for Qt that lets you use svg's "
                "from common packs like FontAwesome, MateriallDesign etc.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Jason Gilholme',
    author_email='jasongilholme@gmail.com',
    license='GPLv3',
    url='https://github.com/jasongilholme/iconify',
    keywords=['Qt', 'icons', 'svg', 'PySide', 'PyQt'],
    packages=find_packages(),
    install_requires=install_requires,
    include_package_data=True,
    data_files=[('requirements', ['requirements.txt'])],
    platforms=['OS-independent'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: X11 Applications :: Qt',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: User Interfaces',
    ],
    entry_points={
        'console_scripts': [
            'iconify-browser=iconify.browser:run',
            'iconify-fetch=iconify.fetch:fetch',
            'iconify-fetch-font-awesome=iconify.fetch:FontAwesome.fetch',
            'iconify-fetch-material-design=iconify.fetch:MaterialDesign.fetch',
            'iconify-fetch-elusive=iconify.fetch:Elusive.fetch',
            'iconify-fetch-dash=iconify.fetch:Dash.fetch',
            'iconify-fetch-feather=iconify.fetch:Feather.fetch',
            'iconify-fetch-google-emojis=iconify.fetch:GoogleEmojis.fetch',
            'iconify-fetch-emojione-legacy=iconify.fetch:EmojioneLegacy.fetch',
        ],
    }
)
