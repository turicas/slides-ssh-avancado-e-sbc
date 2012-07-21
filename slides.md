SSH: dicas & truques sensacionais que (quase) ninguém conhece
=============================================================


Apresentação
------------

- Álvaro Justen

- Flávio Amieiro


Introdução
----------

- SSH = Secure Shell

- Protocolo que permite fazer logins remotos e acessar outros serviços de rede
  de maneira segura em uma rede não confiável.

- Serve para acessar um shell em uma outra máquina da rede, mas também pra um
  monte de outras coisas.


História
--------

![ssh-timeline](file:///home/amieiro/workspace/palestras/SSH-dicas_e_truques_sensacionais_que_quase_ninguém_conhece/images/ssh-timeline.svg)


O protocolo
-----------

- RFC452{0..4}

- 3 componentes principais:

    - Protocolo de camada de transporte: responsável pela autenticação do
      servidor, confidencialidade e integridade da comunicação.

    - Protocolo de autenticação: identifica o cliente ao servidor. Roda
      sobre o protocolo de camada de transporte.

    - Protocolo de conexão: fornece uma gama maior de serviços em cima da
      camada de transporte, como multiplexação, controle de fluxo, execução
      remota de programas, __forwarding de conexões__ etc.
