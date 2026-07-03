from setuptools import find_packages, setup

package_name = 'add_two_ints'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='akshat',
    maintainer_email='akshatmdnr@gmail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'add_two_ints_server = add_two_ints.add_two_ints_server:main',
            'add_two_ints_client = add_two_ints.add_two_ints_client:main',
        ],
    },
)
