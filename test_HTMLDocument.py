from test_GenericDocument import GenericDocument
from test_PartType import PartType


class HTMLDocument(GenericDocument):
    def render_paragraph(self, text: str) -> str:
        return f"<p>{text}</p>"

    def render_heading1(self, text: str) -> str:
        return f"<h1>{text}</h1>"

    def render_heading2(self, text: str) -> str:
        return f"<h2>{text}</h2>"

    def render_heading3(self, text: str) -> str:
        return f"<h3>{text}</h3>"

    def render_codeblock(self, text: str) -> str:
        return f"<pre><code>{text}</code></pre>"


def test_html_heading1():
    doc = HTMLDocument().add_heading1("Title")
    assert doc.render() == "<h1>Title</h1>"


def test_html_paragraph():
    doc = HTMLDocument().add_paragraph("This is a paragraph.")
    assert doc.render() == "<p>This is a paragraph.</p>"


# Lägg till fler testfall här
