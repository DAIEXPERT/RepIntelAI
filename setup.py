from setuptools import find_packages, setup

LATEST_VERSION = "1.0.1"

exclude_packages = [
    "selenium",
    "webdriver",
    "fastapi",
    "fastapi.*",
    "uvicorn",
    "jinja2",
    "AI_core",
    "langgraph"
]

"""with open(r"README.md", "r", encoding="utf-8") as f:
    long_description = f.read()"""

with open("requirements.txt", "r") as f:
    reqs = [line.strip() for line in f if not any(pkg in line for pkg in exclude_packages)]

setup(
    name="AI_core",
    version=LATEST_VERSION,
    description="the AI-based reputation intelligence system by Magolnick Global. Gain insights into your online presence, analyze consumer sentiment, and uncover essential trends to help you manage and grow your brand.",
    package_dir={'AI_core': 'AI_core'},
    packages=find_packages(exclude=exclude_packages),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://www.magolnick.com/AI_core",
    author="Mike Magolnick",
    author_email="mike@magolnick.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Intended Audience :: Developers",
        "Intended Audience :: Education",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
    ],
    install_requires=reqs,


)