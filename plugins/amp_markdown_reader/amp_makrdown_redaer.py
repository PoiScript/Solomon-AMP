import mistune
import json
import requests
from PIL import Image
from io import BytesIO
from pelican import signals
from pelican.readers import BaseReader
from pelican.utils import pelican_open


class AMPRenderer(mistune.Renderer):
    def image(self, src, title, text):
        src = mistune.escape_link(src)
        text = mistune.escape(text, quote=True)
        width, height = 0, 0
        # width, height = get_image_size(src)
        if title:
            title = mistune.escape(title, quote=True)
            html = '''<amp-img on="tap:lightbox1" role="button" tabindex="0" src="%s" alt="%s"
                        title="%s" layout="responsive" width="%s" height="%s">
                        <noscript>
                            <img src="%s" alt="%s" title="%s" width="%s" height="%s"/>
                        </noscript>
                    ''' % (src, text, title, width, height, src, text, title, width, height)
        else:
            html = '''<amp-img on="tap:lightbox1" role="button" tabindex="0" src="%s" alt="%s"
                        layout="responsive" width="%s" height="%s">
                        <noscript>
                            <img src="%s" alt="%s" width="%s" height="%s"/>
                        </noscript>
                    ''' % (src, text, width, height, src, text, width, height)
        return '%s</amp-img>' % html


renderer = AMPRenderer()
markdown = mistune.Markdown(renderer=renderer)


class AMPMarkdownReader(BaseReader):
    enabled = True
    file_extensions = ['md', 'markdown', 'mkd', 'mdown']

    def read(self, source_path):
        with pelican_open(source_path) as fp:
            text = list(fp.splitlines())

        meta = json.loads('\n'.join(text[text.index('```json') + 1:text.index('```')]))
        metadata = {}
        for k in meta:
            name, value = k, meta[k]
            metadata[name] = self.process_metadata(name, value)
        content = markdown('\n'.join(text[text.index('```') + 1:]))
        return content, metadata


def get_image_size(url):
    data = requests.get(url).content
    im = Image.open(BytesIO(data))
    return im.size


def add_reader(readers):
    for ext in AMPMarkdownReader.file_extensions:
        readers.reader_classes[ext] = AMPMarkdownReader


def register():
    signals.readers_init.connect(add_reader)
