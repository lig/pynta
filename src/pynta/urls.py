class Registry(object):
    
    patterns = list()
    
    def __add__(self, patterns):
        self.patterns += patterns
        return self
    
    def __unicode__(self):
        return unicode(self.patterns)
    
    def __str__(self):
        return str(self.patterns)
