
def application(environ, start_reponse):
	start_reponse('200 OK', [('Content-Type', 'text/html')])
	return '<h1>Hello, %s!!</h1>' % (environ['PATH_INFO'][1:] or 'web')