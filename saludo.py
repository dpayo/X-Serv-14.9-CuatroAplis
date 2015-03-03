#!/usr/bin/python

import webapp

class Serv_sal(webapp.app):
    def parse(self, request, rest):
        """Parse the received request, extracting the relevant information.

        request: HTTP request received from the client
        rest:    rest of the resource name after stripping the prefix
        """
        recurso=rest[1]
        print recurso
        return recurso

    def process(self, recurso):
        """Process the relevant elements of the request.

        Returns the HTTP code for the reply, and an HTML page.
        """
        if recurso == '/hola':
            respuesta = 'Hola!'
        elif recurso == '/adios':
            respuesta = ' Adios'
        else:
            respuesta = ' Introduce /hola o /adios'
            
        return ("200 OK", "<html><body><h1>API Saludos </h1><p> "+respuesta + "<p></body></h>")
