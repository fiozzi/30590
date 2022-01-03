"""
isc.py

classes for iCalendar management
"""

class Container():
    def __init__(self, name):
        self.name = name
        self.content = []
    
    def add_line(self, name, param={}, value=''):
        self.content.append([name, param, value])

    def add_raw_text(self, text):
        self.content.append(text)

    def add_container(self, container):
        self.content.append(container)

    def contentline(self,element):
        flat_content = element[0].upper()
        for param in element[1]:
            flat_content += ';' + param.upper() + '=' + element[1][param]
        flat_content += ':' + element[2].upper()
        return flat_content

    def build(self):
        disp_str = 'BEGIN:' + self.name.upper() + '\n'
        for element in self.content:
            if isinstance(element, list):
                disp_str += self.contentline(element) + '\n'
            elif isinstance(element, Container):
                disp_str += element.build()
            elif isinstance(element, str):
                disp_str += element
        disp_str += 'END:' + self.name.upper() + '\n'
        return disp_str
        
class Calendar(Container):
    def __init__(self):
        super().__init__('vcalendar')
    
class Event(Container):
    def __init__(self):
        super().__init__('vevent')

