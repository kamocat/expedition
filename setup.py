from setuptools import find_packages, setup

package_name = 'expedition'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools', 'rclpy', 'numpy', 'nav_msgs'],
    zip_safe=True,
    maintainer='marshal',
    maintainer_email='kamocat@gmail.com',
    description='To boldly go where no bot has gone before',
    license='Apache 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'expedition = expedition.expedition:main'
        ],
    },
)
