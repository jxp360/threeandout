import sys

def application(environ, start_response):
    status = '200 OK'

    name = repr(environ['mod_wsgi.process_group'])
    output = 'mod_wsgi.process_group = %s' % name 

    response_headers = [('Content-type', 'text/plain'),
                        ('Content-Length', str(len(output)))]
    start_response(status, response_headers)

    return [output]
