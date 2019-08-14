from setuptools import setup, find_packages


def install_deps():
    """Reads requirements.txt and preprocess it
    to be feed into setuptools.

    Returns:
         list of packages and dependency links.
    """
    default = open('requirements.txt', 'r').readlines()
    new_pkgs = []
    links = []
    for resource in default:
        if 'git+https' in resource:
            pkg = resource.split('#')[-1]
            links.append(resource.strip())
            new_pkgs.append(pkg.replace('egg=', '').rstrip())
        else:
            new_pkgs.append(resource.strip())
    return new_pkgs, links

pkgs, new_links = install_deps()

setup(name='dl',
      version='1.0',
      description='Deep learning utilities',
      url='https://github.com/sforazz/dl.git',
      python_requires='>=3.5',
      author='Francesco Sforazzini',
      author_email='f.sforazzini@dkfz.de',
      license='Apache 2.0',
      zip_safe=False,
      install_requires=pkgs,
      dependency_links=new_links,
      packages=find_packages(exclude=['*.tests', '*.tests.*', 'tests.*', 'tests']),
      classifiers=[
          'Intended Audience :: Science/Research',
          'Programming Language :: Python',
          'Topic :: Scientific/Engineering',
          'Operating System :: Unix'
      ]
      )
