#!/usr/bin/python

import webapp
import random


class Serv_Aleat(webapp.app):
    
    def process(self, parsedRequest):
        """Process the relevant elements of the request.

        Returns the HTTP code for the reply, and an HTML page.
        """
        num = str(random.randint(1, 10000000))
        resp = "<a href= http://localhost:1234/aleat/" +num + " >Dame Otra! </a>"
        return ("200 OK", "<html><body><h1>API Url's Aleatorias</h1><h2>"+resp+"</h2></body></html>")

