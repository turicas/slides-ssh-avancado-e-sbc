SSH
===

- Introdução
    - O que é
        - SSH = Secure Shell # ["Um protocolo para logins remotos seguros e
          outros serviços de rede seguros em uma rede insegura."][RFC4521]
    - Para que serve
        - O uso mais comum é acessar um shell em uma outra máquina da rede, mas
          vamos ver que serve também pra outras coisas.

    - [História][hist] (segundo a Wikipedia)
        - Primeira versão do protocolo criada em 1995 por um pesquisador
          finlandês com uma implementação gratuita, baseada em software livre
          (como a GNU libgmp).
        - O criador fundou uma empresa (SSH Secure Communications) e mais tarde
          a implementação dele virou proprietária e paga.
        - [história do OpenSSH] | Alguém pegou a última versão do SSH que podia
          ser usada livremente, e começou a corrigir bugs (em 1999). Os
          desenvolvedores do OpenBSD forkaram esse projeto e a versão 2.6 do
          OpenBSD (lançada em dezembro de 1999) já incluía o OpenSSH.
        - O protocolo tinha muitos problemas, e em 2006 uma segunda versão foi
          publicada. Com melhorias de segurança e novas features.

    - Arquitetura do protocolo

        - Protocolo de camada de transporte: responsável pela autenticação do
          servidor, confidencialidade e integridade da comunicação.

        - Protocolo de autenticação: identifica o cliente ao servidor. Roda
          sobre o protocolo de camada de transporte.

        - Protocolo de conexão: fornece uma gama maior de serviços em cima da
          camada de transporte, como multiplexação, controle de fluxo, execução
          remota de programas, __forwarding de conexões__ etc.

        > "This open architecture provides considerable flexibility, allowing
        > SSH to be used for a variety of purposes beyond a secure shell. The
        > functionality of the transport layer alone is comparable to Transport
        > Layer Security (TLS); the user authentication layer is highly
        > extensible with custom authentication methods; and the connection
        > layer provides the ability to multiplex many secondary sessions into
        > a single SSH connection, a feature comparable to BEEP and not
        > available in TLS."[1][wikipedia-arquitetura]

        - Isso significa que dá pra usar partes da estrutura do SSH para outras
          coisas, como prover autenticação e segurança para outras tarefas.


- Configuração
    - Servidor
        - Protocolo v2 + OpenSSH, Protocol 2
        - Autenticação
            - Chaves versus senhas -> PasswordAuthentication no,
              AuthorizedKeysFile, PubKeyAuthentication
                - Breve explicação de como funcionam chaves: uma privada e uma
                  pública.  A pública você coloca no servidor (e pode ser
                  divulgada sem problemas) e a privada você protege o máximo
                  possível.
            - Autenticação do root -> PermitRootLogin no
            - PAM
            - AllowUsers
            - StrictModes

    - Cliente
        - .ssh/config
        - [ControlMaster][ControlMaster]
          ControlPath, ControlPersist


- Usos do OpenSSH

    Acho que pra cada uma dessas possibilidades a gente precisa de uma breve
    explicação, um cenário em que isso seria útil, e um exemplo de comando (e,
    em alguns casos, uma demonstração ao vivo).

    - Quebrando proxies/firewalls
        - Port -> 443, 80, ListenAddress
        - httptunnel
        - `-D` (DynamicForward) -> proxy SOCKS, AllowTcpForwarding, PermitOpen
        - PermitTunnel
        - `-L` (e `-g` ou `-o GatewayPorts`)
        - `-R` e `GatewayPorts`

    - [ProxyCommand][ProxyCommand-1]
        - [ProxyCommand-2]
        - [ProxyCommand + Bash + FD redirection][ProxyCommand-3]

    - `-X` -> X11Forwarding yes, X11DisplayOffset

- Misc
    - Escape char
    - [BatchMode][batch]
    - SFTP versus scp

- [bcvi][bcvi] e [sbc][bcvi]



TODO:
-----

- Ver: Subsystem, UseDNS
- Ler man ssh
- Ler man sshd
- Ler man ssh\_config a partir de HashKnownHosts

[hist]: https://en.wikipedia.org/wiki/Secure_Shell#History_and_development
[batch]: http://www.thegeekstuff.com/2009/10/how-to-execute-ssh-and-scp-in-batch-mode-only-when-passwordless-login-is-enabled/
[wikipedia-arquitetura]: https://en.wikipedia.org/wiki/Secure_Shell#Architecture
[ControlMaster]: http://sshmenu.sourceforge.net/articles/transparent-mulithop.html
[bcvi]: http://sshmenu.sourceforge.net/articles/bcvi/
[sbc]: https://github.com/turicas/sbc
[ProxyCommand-1]: http://www.undeadly.org/cgi?action=article&sid=20070925181947
[ProxyCommand-2]: http://www.statusq.org/archives/2008/07/03/1916/
[ProxyCommand-3]: http://unix.stackexchange.com/questions/19604/all-about-ssh-proxycommand#19607
[openssh-hist]: http://openssh.com/history.html
[RFC4521]: https://tools.ietf.org/html/rfc4251
