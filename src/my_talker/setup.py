from setuptools import setup

package_name = 'my_talker'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools'],
    entry_points={
        'console_scripts': [
            'my_node = my_talker.my_node:main',     # talker — already there from pkg create
            'listener = my_talker.listener:main',   # ← add this line
        ],
    },
)