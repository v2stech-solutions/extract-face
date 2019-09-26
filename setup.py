
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='extract_face',  
    version='0.6',
    author="V2STech Solutions PVT. LTD.",
    author_email="jayesht1996@gmail.com",
    description="A Package which can extract all human faces from provided image",
    long_description=long_description,
    long_description_content_type="text/markdown",     
    install_requires=['opencv-python'],    
    packages=setuptools.find_packages(),
    package_data={'extract_face': ['haarcascade_frontalface_default.xml']},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
 )