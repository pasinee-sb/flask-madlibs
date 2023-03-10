from stories import Story


class Story2(Story):
    def __init__(self,words,text):
        super().__init__(words,text)

story2 = Story2(    ["place", "noun", "verb", "adjective", "plural_noun"],
    """At {place}, where there was a tiny {adjective} {noun}. It likes to {verb} {plural_noun}."""
       )