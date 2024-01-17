from sys import version
import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()
setuptools.setup(
    name="SNS_diffusion_simulator",
    version="0.0.1",
    author="Ryutaro_Umehara",
    author_email="s2122007@stu.musashino-u.ac.jp",
    description="Simulator for estimating the spread of SNS",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="???",
    project_urls={
        "Bug Tracker":"???",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"":"src"},
    py_modules=['SNS_diffusion_simulator'],
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.7",
    entry_points = {
        'console_scripts':[
            'SNS_diffusion_simulator = SNS_diffusion_simulator:main'
        ]
    },
)