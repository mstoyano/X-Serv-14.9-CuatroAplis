#!/usr/bin/python


class suma:

    def parse(self, request, rest):

        try:
            numero = int(rest[1:])
        except ValueError:
            return None
        return numero

    def process(self, parsedRequest):

        if not parsedRequest:
            self.guardado = None
            return("400 Bad Request", "<h1>Eror! Introduce: /suma/numero</h1>")
        else:
            try:
                print self.guardado
            except AttributeError:
                self.guardado = 0

            if self.guardado is None:
                self.guardado = 0
            print "SELF: " + str(self.guardado)

            if self.guardado:
                resultado = int(self.guardado) + int(parsedRequest)
                answer = str(self.guardado) + "+" + str(parsedRequest)
                answer = answer + "=" + str(resultado)
                self.guardado = 0
            else:
                answer = "Dame otro numero"
                self.guardado = parsedRequest

        return("200 OK", "<html><body><h1>" + answer + "</h1></body></html>")
