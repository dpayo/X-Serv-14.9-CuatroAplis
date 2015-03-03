#!/usr/bin/python

import webapp
import sys

class Serv_sum(webapp.app):
    def parse(self, request, rest):
        """Parse the received request, extracting the relevant information.

        request: HTTP request received from the client
        rest:    rest of the resource name after stripping the prefix
        """
        sumandos=rest.split('/')[1:]
        return sumandos

    def process(self, sumandos):
        """Process the relevant elements of the request.

        Returns the HTTP code for the reply, and an HTML page.
        """
        try:
            suma = int(sumandos[0])+int(sumandos[1])
        except ValueError:
            return ("404 ", "<html><body><p> Not Found<p></body></html>")
            sys.exit()
        return ("200 OK", "<html><body><h1>" +
                          "API Sumadora" +
                          "</h1><p>La suma es : " + str(suma) + "<p></body></html>")


