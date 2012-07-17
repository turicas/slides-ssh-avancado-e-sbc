Título
------

**SSH: dicas & truques sensacionais que (quase) ninguém conhece**

Sumário
-------

Muitas pessoas utilizam o SSH apenas para conectar-se a um shell remoto. Esta
palestra apresentará vários recursos menos conhecidos e como usar o SSH para
furar proxies e firewalls, utilizar aplicativos gráficos remotamente, tornar
seguro o uso de redes não confiáveis, acessar máquinas inacessíveis diretamente
de sua estação local e muitas outras. Também será apresentado o sbc, software
que utiliza o SSH para facilitar ainda mais o dia-a-dia de administradores de
servidores.

Proposta
--------

SSH é uma ferramenta extremamente difundida entre administradores de sistemas,
porém a maioria de seus usuários utiliza apenas sua funcionalidade mais básica:
abrir shells remotos seguros. Apesar disso, o SSH possui inúmeros recursos que
facilitam e otimizam o dia-a-dia de administradores de rede e desenvolvedores
de software. Nesta palestra serão apresentados vários recursos menos conhecidos
do SSH e o que eles nos permitem fazer.

Serão abordadas as seguintes funcionalidades:

- Redirecionamento de portas locais e remotas
- Autenticação com chaves
- Criação de VPN
- Redirecionamento de tráfego do X server
- Multiplexação de conexões
- Utilizar comandos como proxies para a conexão SSH

E suas aplicações:

- Furar NAT/proxy/firewall
- Maior segurança com tunelamento de tráfego IP criptografado
- Utilização de softwares gráficos remotos
- Menor latência para múltiplas conexões
- Tunelar tráfego SSH através de proxy HTTP, utilizar “multihop” SSH de forma
  transparente
- Criar comunicação entre processos remotos e locais através de pipes
- Maior facilidade e agilidade ao administrar servidores

Além disso, será apresentado o [sbc][https://github.com/turicas/sbc], um
software livre desenvolvido utilizando funcionalidades incluídas por padrão no
SSH, que tem como objetivo encurtar a distância entre o cliente e o servidor,
tornando a experiência de administração remota mais ágil e menos trabalhosa.
