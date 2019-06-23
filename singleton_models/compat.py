from django.utils import encoding

# ugly hack required for Python 2/3 compat
if hasattr(encoding, 'force_unicode'):
    force_unicode = encoding.force_unicode
elif hasattr(encoding, 'force_text'):
    force_unicode = encoding.force_text
else:
    force_unicode = lambda x: x
