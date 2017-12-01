from pkg_resources import get_distribution

pkg = get_distribution('pyft')
pkg_meta = {}
for meta in pkg._get_metadata(pkg.PKG_INFO):
    try:
        k, v = meta.split(': ', 1)
        pkg_meta[k] = v
    except ValueError:
        continue

__version__ = get_distribution('pyft').version
__author_email__ = pkg_meta['Author-email']
__url__ = pkg_meta['Home-page']
