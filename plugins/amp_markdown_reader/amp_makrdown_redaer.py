import mistune
from pelican import signals
from pelican.readers import BaseReader
from pelican.utils import pelican_open


class AMPRenderer(mistune.Renderer):
    def image(self, src, title, text):
        src = mistune.escape_link(src)
        text = mistune.escape(text, quote=True)
        if title:
            title = mistune.escape(title, quote=True)
            html = '<amp-img src="%s" alt="%s" title="%s" height="400" width="800" layout="responsive"'\
                   % (src, text, title)
        else:
            html = '<amp-img src="%s" alt="%s" height="400" width="800" layout="responsive"' % (src, text)
        return '%s></amp-img>' % html


renderer = AMPRenderer()
markdown = mistune.Markdown(renderer=renderer)


class AMPMarkdownReader(BaseReader):
    enabled = True
    file_extensions = ['md', 'markdown', 'mkd', 'mdown']

    def read(self, source_path):
        with pelican_open(source_path) as fp:
            text = list(fp.splitlines())

        metadata = {}
        for i, line in enumerate(text):
            kv = line.split(':', 1)
            if len(kv) == 2:
                name, value = kv[0].lower(), kv[1].strip()
                metadata[name] = self.process_metadata(name, value)
            else:
                content = "\n".join(text[i:])
                break

        content = markdown(content)
        return content, metadata


def add_reader(readers):
    for ext in AMPMarkdownReader.file_extensions:
        readers.reader_classes[ext] = AMPMarkdownReader


def register():
    signals.readers_init.connect(add_reader)
