#
# One of mysterious magic methods in Python is __getattr__(). It will be hit when the invoked method cannot be found
# You can run like this: python3 html_builder.py > html_builder_result.html
# Then open this generated file in browser to see the result
#


class HtmlNode(object):
    def __init__(self, name, children=None, attrs=None, parent=None):
        self.name = name
        self.children = []
        self.attrs = attrs
        self.parent = parent
        if attrs and 'content' in attrs:
            self.content = attrs['content']
            del self.attrs['content']
        else:
            self.content = ''

        if children:
            for c in children:
                self.children.append(c.node)
                c.node.parent = self

        if parent:
            parent.children.append(self)

    def __str__(self):
        if self.content:
            children_str = self.content
        else:
            children_str = ''.join([str(c) for c in self.children])

        if self.name == '':
            return children_str

        if self.attrs:
            attr_str = ' '.join(['{}="{}"'.format(k, v) for k, v in self.attrs.items()])
            return '<{} {}>{}</{}>'.format(self.name, attr_str, children_str, self.name)
        else:
            return '<{}>{}</{}>'.format(self.name, children_str, self.name)


class HtmlBuilder(object):
    def __init__(self, node=None):
        if node:
            self.node = node
        else:
            self.node = HtmlNode('')

    def __str__(self):
        root = self.node
        while root.parent:
            root = root.parent
        return str(root)

    def __getattr__(self, name):
        def _gen_html(*args, **kwargs):
            return HtmlBuilder(HtmlNode(name, args, kwargs, self.node))

        return _gen_html


if __name__ == '__main__':
    builder = HtmlBuilder()
    builder \
        .html() \
        .body() \
        .div(HtmlBuilder().h1(content='Hi'),
             HtmlBuilder().p(content='This is a test'),
             HtmlBuilder().img(src='some.png'),
             HtmlBuilder().p(content='Test ends')) \
        .div(HtmlBuilder().h2(content='COOL'))
    print(builder)
