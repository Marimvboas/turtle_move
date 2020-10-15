from setuptools import setup

package_name = 'turtle_move'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Mariana Mota',
    maintainer_email='marivboas02@gmail.com',
    description='Moving in a Straight Line',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        	'moving = turtle_move.move2:main',
        ],
    },
)
