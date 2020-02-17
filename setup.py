from setuptools import setup, Extension


# Get the relative zopflipng source location
def get_zopflipng_source(items):
    return list(map(lambda item: "zopfli/src/" + item, items))


# zopflipng sources
zopflipng_src = get_zopflipng_source([
    'zopfli/blocksplitter.c',
    'zopfli/cache.c',
    'zopfli/deflate.c',
    'zopfli/gzip_container.c',
    'zopfli/hash.c',
    'zopfli/katajainen.c',
    'zopfli/lz77.c',
    'zopfli/squeeze.c',
    'zopfli/tree.c',
    'zopfli/util.c',
    'zopfli/zlib_container.c',
    'zopfli/zopfli_lib.c',
    'zopflipng/lodepng/lodepng_util.cpp',
    'zopflipng/lodepng/lodepng.cpp',
    'zopflipng/zopflipng_lib.cc'
])

# include header file
include_file = get_zopflipng_source([
    'zopfli/blocksplitter.h',
    'zopfli/cache.h',
    'zopfli/deflate.h',
    'zopfli/gzip_container.h',
    'zopfli/hash.h',
    'zopfli/katajainen.h',
    'zopfli/lz77.h',
    'zopfli/squeeze.h',
    'zopfli/symbols.h',
    'zopfli/tree.h',
    'zopfli/util.h',
    'zopfli/zlib_container.h',
    'zopfli/zopfli.h',
    'zopflipng/lodepng/lodepng_util.h',
    'zopflipng/lodepng/lodepng.h',
    'zopflipng/zopflipng_lib.h'
])

# python wrapper
zopflipng_src.extend([
    'src/py_zopflipng.cc'
])

# define module
module_zopflipng = Extension('zopflipng._clib',
                             language="c++",
                             sources=zopflipng_src,
                             include_file=include_file, )

setup(name='zopflipng',
      version='1.0.1',
      description='zopflipng wrapper for python',
      author ='hhoy',
      license='Apache',
      author_email='utf-16@qq.com',
      url="https://github.com/hhoy/python-zopflipng.git",
      long_description_content_type='text/markdown',
      long_description=open('README.md', encoding='utf-8').read(),
      ext_modules=[module_zopflipng],
      include_package_data=True,
      package_dir={'': 'src'},
      packages =['zopflipng'],
      platforms="any")
