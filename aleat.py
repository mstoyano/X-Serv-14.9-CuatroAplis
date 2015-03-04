#!/usr/bin/python
# -*- coding: utf-8 -*-

import random


class aleat:

    def parse(self, request, rest):
        return None

    def process(self, parsedRequest):

        Num_Aleatorio = str(random.randint(0, 10000000))
        return("200 OK", "<html><body>Hola. <a href=http://localhost:1234/" +
               "aleat/" + Num_Aleatorio + ">Dame otra</a></p></h1>" +
               "</body></html>")
