#!/usr/bin/env python3

from vial import Vial

from nxtools import logging
from nxtools.caspar import CasparCG

caspar = CasparCG("127.0.0.1")
caspar.query("VERSION")

class App(Vial):
    def handle(self, request):
        if request.method == "POST" and request.path == "/amcp":
            r = caspar.query(request.body.text)

            return self.response.text(
                r.data, 
                status=r.response,
                custom_headers={
                    "Access-Control-Allow-Origin" : "*"
                }
            )

        return self.response.text(f"Bad request", status=400)

app = App(logger=logging)

if __name__ == "__main__":
    app.serve("127.0.0.1", 9731)
