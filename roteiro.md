SSH
===

- Introdução
    - O que é
    - Para que serve
    - História
    - Protocolo v2 + OpenSSH, Protocol 2
- Autenticação
    - Chaves versus senhas -> PasswordAuthentication no, AuthorizedKeysFile,
      PubKeyAuthentication
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
- BatchMode (para rodar scripts)
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
