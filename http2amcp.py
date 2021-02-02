#!/usr/bin/env python3

from vial import Vial

from nxtools import logging
from nxtools.caspar import CasparCG


caspar = CasparCG("localhost")


class App(Vial):
    def handle(self, request):
        if request.method == "POST":

            return self.response.text()


        return self.response.text(f"BAAAAAD", status=400)

app = App(logger=logging)

if __name__ == "__main__":
    app.serve("", 8000)

