#!/usr/bin/python

import webapp
import random
import hola
import suma
import aleat


class Serv_Aleat(webapp.app):
    
    def process(self, parsedRequest):
        """Process the relevant elements of the request.

        Returns the HTTP code for the reply, and an HTML page.
        """
        num = str(random.randint(1, 10000000))
        resp = "<a href= http://localhost:1234/aleat/" +num + " >Dame Otra! </a>"
        return ("200 OK", "<html><body><h1>API Url's Aleatorias</h1><h2>"+resp+"</h2></body></html>")



if __name__ == "__main__":
    sumarApp = suma.Serv_sum()
    saluApp= hola.Serv_sal()
    aleApp = aleat.Serv_Aleat()
    try:    
        testMain = webapp.webApp("localhost", 1234, {'/suma': sumarApp,
                                            '/hola': saluApp,
                                            '/adios': saluApp,
                                            '/aleat':aleApp})
    except KeyboardInterrupt:
        print "Closing binded socket"
