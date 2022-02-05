def get_text_from_element(element):
    text_elements = [t.strip() for t in element.css('::text').getall() if t != '\n']
    text = ' '.join(text_elements)
    text = text.replace(' , ', ', ')
    text = text.replace(' . ', '. ')
    text = text.replace('( ', '(')
    text = text.replace(' )', ')')
    return text
