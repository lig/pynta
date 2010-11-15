from pynta import views


# define view class
class view_name(views.View):
    
    # define response for GET method with default template rendering as result
    def GET(self):
        # render 'example_app/view_name.html' template
        return self.render()
    
    # define response for POST method with other template rendering as result
    def POST(self):
        # render 'result.html' template
        return self.render('result.html')


# define view with only GET method and default template
class view_name1(views.View):
    
    def GET(self):
        # provide string 'bar' as value for 'foo' template variable
        self.foo = 'bar'
        # render 'example_app/view_name1.html' template
        return self.render()


# define view with ajax support
class view_name2(views.View):
    
    def main(self, parameter):
        # provide data to template
        self.foo = 'bar'
    
    def GET(self, parameter):
        self.main(parameter)
        # render 'example_app/view_name2.html' template
        return self.render()
    
    def AJAX(self, parameter):
        self.main(parameter)
        # render 'example_app/view_name2.js' template
        return self.render()
