import emoji

class AdvMessage():
    def __init__(self):
        self.list_of_elements = []
        self.em = emoji.emojize(":thumbs_up:")
        self.msg_text_repr = ""
    def append_element(self, elem):
        self.list_of_elements.append(elem)

    def concat_elements(self, list):
        return ''.join(list)








