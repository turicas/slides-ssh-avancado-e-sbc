SSH
===

- Introdução
    - O que é
    - Para que serve
    - [História](https://en.wikipedia.org/wiki/Secure_Shell#History_and_development)
    - Protocolo v2 + OpenSSH, Protocol 2
    - A palestra é, em sua maior parte, sobre funcionalidades do OpenSSH, não
      sobre o protocolo

- Autenticação
    - Chaves versus senhas -> PasswordAuthentication no, AuthorizedKeysFile,
      PubKeyAuthentication
        - Breve explicação de como funcionam chaves: uma privada e uma pública.
          A pública você coloca no servidor (e pode ser divulgada sem
          problemas) e a privada você protege o máximo possível.
    - Autenticação do root -> PermitRootLogin no
    - PAM
    - AllowUsers
    - StrictModes
- Quebrando proxies
    - Port -> 443, 80, ListenAddress
    - httptunnel
    - `-D` (DynamicForward) -> proxy SOCKS, AllowTcpForwarding, PermitOpen
    - PermitTunnel
- .ssh/config
- Escape char
- [BatchMode](http://www.thegeekstuff.com/2009/10/how-to-execute-ssh-and-scp-in-batch-mode-only-when-passwordless-login-is-enabled/) (para rodar scripts)
- SFTP versus scp
- `-X` -> X11Forwarding yes, X11DisplayOffset
- [ControlMaster
  auto](http://sshmenu.sourceforge.net/articles/transparent-mulithop.html),
  ControlPath, ControlPersist
- [bcvi](http://sshmenu.sourceforge.net/articles/bcvi/) e
  [sbc](https://github.com/turicas/sbc)
- `-L` (e `-g` ou `-o GatewayPorts`)
- `-R` e `GatewayPorts`
- [ProxyCommand](http://www.undeadly.org/cgi?action=article&sid=20070925181947)
    - [Mais ProxyCommand](http://www.statusq.org/archives/2008/07/03/1916/)
    - [ProxyCommand + Bash + FD redirection](http://unix.stackexchange.com/questions/19604/all-about-ssh-proxycommand#19607)
- Ver: Subsystem, UseDNS
- Ler man ssh
- Ler man sshd
- Ler man ssh\_config a partir de HashKnownHosts
