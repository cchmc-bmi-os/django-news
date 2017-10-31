try:
    from setuptools import setup, find_packages
    from setuptools.command.test import test
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages
    from setuptools.command.test import test

setup(name = 'django-news',
      description = "Fork of CHOP's fork of monokrome's lightweight news app",
      author = 'Marcus Renno',
      author_email = 'marcus.renno@ccmc.org',
      version = '0.7.2',

      zip_safe = False,
      include_package_data = True,
      packages = find_packages(),
      url = 'https://github.com/cchmc-bmi-os/django-news',

      classifiers = [
          "Development Status :: 4 - Beta",
          "Environment :: Web Environment",
          "Intended Audience :: Developers",
          "Operating System :: OS Independant",
          "Programming Language :: Python",
          "Framework :: Django",
          "Topic :: Internet :: WWW/HTTP / :: Dynamic Content",
          "Topic :: Internet :: WWW/HTTP / :: Site Management",
      ],
)

