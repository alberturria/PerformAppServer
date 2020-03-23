class ConvertToDictionary(object):
    def __init__(self):
        pass

    def convert_object_to_dictionary(self, element):
        if isinstance(element, dict):
            data = {}
            for (k, v) in element.items():
                data[k] = self.convert_object_to_dictionary(v)
            return data
        elif hasattr(element, "__dict__"):
            data = dict([(key, self.convert_object_to_dictionary(value))
                         for key, value in element.__dict__.iteritems()])
            return data
        elif hasattr(element, "__iter__"):
            return [self.convert_object_to_dictionary(v) for v in element]
        else:
            return element
