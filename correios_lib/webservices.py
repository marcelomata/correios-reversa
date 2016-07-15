# -*- coding: utf-8 -*-
# #############################################################################
#
# The MIT License (MIT)
#
# Copyright (c) 2016 Trocafone
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
###############################################################################


from correios_lib.base import WebserviceBase, WebserviceError
from correios_lib.requests import RequestSolicitarPostagemReversa


class LogisticaReversa(WebserviceBase):

    def get_env(self, env):
        envs = {
            'HOMOLOG': 'https://apphom.correios.com.br/logisticaReversaWS/'
                       'logisticaReversaService/logisticaReversaWS?wsdl',
            'PROD': 'https://cws.correios.com.br/logisticaReversaWS/'
                    'logisticaReversaService/logisticaReversaWS?wsdl',
        }

        return envs[env]

    def SolicitarPostagemReversa(self, request):
        if not isinstance(request, RequestSolicitarPostagemReversa):
            raise WebserviceError(
                'Request must be an instance of correios_lib' +
                '.requests.RequestSolicitarPostagemReversa'
            )

        return self.call('solicitarPostagemReversa', request)
