class ExecutionFlowMidlleware(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        print('This line printed at pre-processing of request')
        response=self.get_response(request)
        print('This line printed at post-processing of request')
        return response

from django.http import HttpResponse
class AppMaintenanceMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        return HttpResponse('<h1>Currently the Application is under maintenance Please try after sometimes</h1>')

class ErrorMessageMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self,request):
        response=self.get_response(request)
        return response
    def process_exception(self,request,exception):
        s='<h1>Currently we are facing some technical issue please try after sometime</h1>'
        return HttpResponse(s)

class FirstMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        print('This line printed at first middleware pre-processing of request')
        response=self.get_response(request)
        print('This line printed at first post-processing of request')
        return response
class SecondMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        print('This line printed at second middleware pre-processing of request')
        response=self.get_response(request)
        print('This line printed at second post-processing of request')
        return response
class ThirdMiddleware(object):
    def __init__(self,get_response):
        self.get_response=get_response
    def __call__(self,request):
        print('This line printed at third middleware pre-processing of request')
        response=self.get_response(request)
        print('This line printed at third post-processing of request')
        return response
