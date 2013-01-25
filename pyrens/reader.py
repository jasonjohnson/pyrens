class Reader(object):
    def __init__(self, text):
        self.text = text

        self.padded = None
        self.exploded = None
        self.cleaned = None
        self.scanned = None
        self.collapsed = None

    def get(self):
        self.pad()
        self.explode()
        self.clean()
        self.scan()
        self.collapse()

        return self.finalize()

    def pad(self):
        text = self.text
        subs = [
            ("(", " ( "),
            (")", " ) "),
            ("\n", "  "),
            ("\t", "  ")
        ]

        for org, new in subs:
            text = text.replace(org, new)

        self.padded = text

    def explode(self):
        self.exploded = self.padded.split(" ")

    def clean(self):
        self.cleaned = filter(None, self.exploded)

    def scan(self):
        self.scanned = []
        start = []

        for i, symbol in enumerate(self.cleaned):
            if symbol is '(':
                start.append(i)
            elif symbol is ')':
                self.scanned.append((start.pop(),i+1))

    def collapse(self):
        self.collapsed = list(self.cleaned)

        for start, end in self.scanned:
            self.collapsed[start:end] = [self.collapsed[start:end]] + \
                                        [None] * (end - start - 1)

    def finalize(self):
        stack = [self.collapsed]

        while stack:
            target = stack.pop()
            items = []

            for i, item in enumerate(target):
                if item is None:
                    items.append(i)
                if isinstance(item, list):
                    stack.append(item)

            items.reverse()

            for i in items:
                target.pop(i)

            try:
                target.remove('(')
                target.remove(')')
            except ValueError:
                pass

        return self.collapsed.pop()

