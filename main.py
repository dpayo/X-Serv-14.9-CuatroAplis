#!/usr/bin/python
# -*- coding: utf-8 -*-
import hola
import suma
import aleat
import webappmulti


if __name__ == "__main__":
    sumarApp = suma.Serv_sum()
    saluApp= hola.Serv_sal()
    aleApp = aleat.Serv_Aleat()
    try:    
        testMain = webappmulti.webApp("localhost", 1234, {'/suma': sumarApp,
                                            '/hola': saluApp,
                                            '/adios': saluApp,
                                            '/aleat':aleApp})
    except KeyboardInterrupt:
        print "Closing binded socket"
