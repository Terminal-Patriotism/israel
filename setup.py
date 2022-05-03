from setuptools import setup

setup(
    name = "israel",
    version = "0.1.0",
    description = "Prints Israel flag",
    author = "AitzazImtiaz",
    url = "https://github.com/AitzazImtiaz/israel",
    packages = ["israel"],
    entry_points = {
        'console_scripts': [
            'israel = israel.__main__:main'
        ]
    },
)
