# Política de privacidade da Plume

**Última atualização: 31 de julho de 2026** — Versão 1.0

---

## Quem é o responsável pelo tratamento dos seus dados

**SASU RedLine Music**
SIREN 938 277 100 — SIRET `938 277 100 00013`
Abbaye 208-1, 208 Résidence Lavoisier, 18100 Vierzon, France
Contacto: sogacmoi7@gmail.com

A aplicação é publicada no Google Play com o nome de editor **openfunword**.

Esta política descreve o que a aplicação Plume faz na sua versão atual. Foi redigida com base na leitura do código da aplicação, e não a partir de um modelo genérico.

---

## Num minuto

A Plume ajuda-o a escrever: reformula o seu texto diretamente na aplicação onde está a escrever, e pode traduzir texto apresentado no ecrã.

Três coisas a reter:

1. **A Plume não conserva nenhum dos seus textos nos seus servidores.** Nem os textos reformulados, nem o texto lido no ecrã. Não guardamos deles nem cópia nem registo.
2. **Consoante o motor que escolher, o seu texto sai ou não sai do seu telemóvel.** Dois motores (o Kit local e a IA local) trabalham inteiramente no dispositivo. O terceiro (a IA na nuvem) envia o texto para um serviço de inteligência artificial **situado fora da União Europeia**. A escolha é sua, e a IA na nuvem nunca se ativa sem o seu consentimento explícito.
3. **A Plume precisa de autorizações poderosas** (ler o conteúdo apresentado nas outras aplicações, capturar o ecrã). Explicamos abaixo, com precisão, para que servem e para que não servem.

---

## 1. O que a Plume lê no seu ecrã, e quando

### 1.1 O serviço de acessibilidade

Para reescrever o seu texto no local onde o escreve, a Plume utiliza o serviço de acessibilidade do Android. É uma autorização que o próprio utilizador ativa, nas definições do telemóvel, depois de um ecrã explicativo que a Plume mostra **antes** de a pedir.

Em concreto:

- **Em repouso**, a Plume sabe apenas que aplicação está aberta e em que momento coloca o cursor num campo de escrita. É isso que faz aparecer a cápsula flutuante — e unicamente nas aplicações que o próprio utilizador configurou.
- **O conteúdo do campo só é lido no instante preciso em que toca na cápsula**, para ser reescrito e depois substituído no lugar.
- **Os campos de palavra-passe são excluídos.** A aplicação deteta os campos do tipo palavra-passe (incluindo os códigos numéricos e os campos web) e recusa-se a lê-los.
- Esta autorização **não permite qualquer captura de imagem** do seu ecrã.
- A Plume **nunca toca no ecrã em seu lugar** noutra aplicação: substitui o texto de um campo, mais nada.

Duas funções que o próprio utilizador ativa — a **Leitura Assistida em modo Texto** e a **tradução das mensagens recebidas** — leem o texto apresentado de forma contínua enquanto estiverem a funcionar, e param assim que as desligar.

Se recusar o serviço de acessibilidade, a Plume continua utilizável: pode selecionar um texto e passar pelo menu «Plume» da seleção do Android, ou partilhar um texto com a Plume.

### 1.2 A captura de ecrã (Leitura Assistida)

A Leitura Assistida sobrepõe uma tradução ao texto apresentado — por exemplo, os balões de uma banda desenhada. Precisa de ver a imagem do ecrã.

- Está **desativada por predefinição** e só funciona nas aplicações que autorizou explicitamente, uma a uma.
- **O Android pede o seu próprio consentimento a cada início de sessão.** Não é uma permissão concedida de uma vez por todas: cada sessão exige um novo acordo. A Plume nunca procura reutilizar nem contornar esse acordo.
- Durante toda a sessão, **uma notificação permanente e um indicador do sistema permanecem visíveis**. A Plume não pode capturar o seu ecrã discretamente.
- A sessão **para automaticamente quando o ecrã é bloqueado**, e imediatamente quando o próprio utilizador a para.
- As aplicações que protegem a sua visualização (aplicações bancárias, gestores de palavras-passe) são **ocultadas pelo próprio Android** antes de a Plume receber seja o que for. É uma proteção do sistema, real mas parcial: nem todas as aplicações sensíveis a ativam. Por isso, não a apresentamos como uma garantia absoluta.
- **As imagens capturadas nunca são guardadas nem enviadas.** Cada imagem é analisada em memória para dela se extrair o texto, sendo depois abandonada. Nenhuma imagem sai do seu telemóvel, nunca, qualquer que seja o motor escolhido.

---

## 2. O que fica no seu telemóvel e o que sai

É a distinção mais importante desta política, e é o utilizador que a controla.

### 2.1 Os motores que não fazem sair nada

- **O Kit local** (reconhecimento e tradução de texto offline) funciona inteiramente no dispositivo.
- **A IA local** é um modelo de inteligência artificial transferido uma vez e depois armazenado no seu telemóvel (cerca de 720 MB). É executado no seu dispositivo.

Com estes dois motores, **o texto lido ou reformulado não sai do seu telemóvel.** Não existe qualquer chamada de rede ligada ao conteúdo do seu texto.

### 2.2 O motor IA na nuvem

Quando escolhe a IA na nuvem, ou quando o seu dispositivo não é suficientemente potente para a IA local, o texto em causa é transmitido aos nossos servidores e, depois, a um serviço de inteligência artificial terceiro.

**É preciso ser claro quanto ao trajeto real:**

- O texto transita pela nossa infraestrutura (Supabase), alojada na **União Europeia** (região Europa Central, Frankfurt).
- É em seguida transmitido ao **openrouter.ai**, um intermediário de encaminhamento **situado fora da União Europeia**, que o faz tratar pelo modelo **Mistral Small**.
- **Trata-se, portanto, de uma transferência de dados para fora da União Europeia.** Não pretendemos o contrário, e não apresentamos qualquer promessa de alojamento europeu para esta etapa.
- **A Plume não conserva o seu texto.** Nenhuma das nossas funções de servidor escreve o conteúdo do seu texto: registamos apenas um identificador técnico de pedido e o identificador do seu dispositivo, para contabilizar a sua quota e detetar abusos.
- **O que estes prestadores fazem do seu lado, não o podemos garantir.** Preferimos dizê-lo a prometer-lhe uma retenção nula que não estamos em condições de verificar.

**A IA na nuvem nunca se ativa sozinha.** Um ecrã de consentimento dedicado explica-lhe estes pontos antes do primeiro envio, e nada sai enquanto não tiver aceitado. Se a IA local falhar, a Plume não muda para a nuvem em silêncio: assinala-o e aguarda a sua decisão. Pode revogar este consentimento a qualquer momento nas definições.

O texto enviado tem um limite máximo: 1200 caracteres para uma reformulação, 4000 caracteres para uma análise de ecrã.

---

## 3. Os dados que conservamos

Não utilizamos **qualquer ferramenta de análise de audiência, qualquer rastreador publicitário de terceiros, qualquer ferramenta de relatório de falhas**. A aplicação não contém qualquer SDK de medição.

Eis a totalidade do que é armazenado nos nossos servidores:

| Dado | Porquê | Duração |
|---|---|---|
| **Identificador do dispositivo** (um número aleatório gerado pela Plume, sem ligação à sua identidade nem a um identificador publicitário) | Associar um dispositivo a uma conta, aplicar as quotas, bloquear os abusos | Até à eliminação da sua conta |
| **Endereço de e-mail da conta** (se criar uma conta por e-mail ou através da Google) | Autenticá-lo, associar a sua subscrição | Até à eliminação da sua conta |
| **Contadores de utilização** (número de reformulações por dia e por mês — números, não textos) | Aplicar as quotas | Até à eliminação da sua conta |
| **Histórico de compras** (identificador de transação do Google Play, datas, estado da subscrição) | Dar-lhe acesso àquilo que pagou, gerir as renovações, cumprir as nossas obrigações contabilísticas | Conservado mesmo após a eliminação da conta, mas **desligado da sua identidade** (ver o §6) |
| **Sugestões enviadas voluntariamente** (se nos escrever uma sugestão de persona a partir da aplicação) | Melhorar o catálogo. Estas sugestões nunca são publicadas. | Até à eliminação da sua conta |
| **Sinais técnicos de abuso** (excessos repetidos, falha do controlo de integridade — sem qualquer texto) | Segurança, luta contra a fraude | Desligados da sua identidade aquando da eliminação da conta |
| **Idioma e versão da aplicação** | Servir o conteúdo correto | Até à eliminação da sua conta |

**O que não recolhemos:** o seu nome, os seus contactos, a sua localização, a sua lista de contactos, as suas fotografias, o seu calendário, o histórico das suas aplicações. A Plume não pede nenhuma destas autorizações.

**O que fica unicamente no seu telemóvel:** os seus personas personalizados e os respetivos avatares, as suas definições, as suas regras por aplicação, a cache de tradução da Leitura Assistida (apagada no final de cada sessão). Nada disto é enviado aos nossos servidores.

---

## 4. O ditado por voz

Um botão de microfone permite-lhe ditar em vez de escrever. A autorização de acesso ao microfone é pedida **no momento preciso em que carrega nesse botão**, nunca no arranque, e o microfone só se abre nesse instante. A Plume nunca escuta em segundo plano.

**A Plume não recebe, não armazena e não transmite qualquer gravação áudio.** O ditado é confiado ao motor de reconhecimento de voz integrado no seu telemóvel (o do Android). A Plume recupera apenas o texto transcrito.

**Ponto importante e honesto:** esse motor do sistema pertence ao seu telemóvel, geralmente à Google. Consoante o seu dispositivo, as suas definições e os módulos de idioma instalados, **pode transmitir o áudio aos servidores do respetivo editor** para o transcrever. Esse tratamento escapa à Plume e depende da política de privacidade do editor do seu sistema. Não podemos, portanto, afirmar que a sua voz permanece no dispositivo — isso depende do seu telemóvel, não de nós.

Se recusar a autorização do microfone, a escrita pelo teclado continua evidentemente disponível.

---

## 5. Publicidade

O serviço é gratuito dentro de um certo limite de utilização por dia. Para além desse limite, pode **escolher** ver um anúncio com recompensa para desbloquear utilizações suplementares. Nunca é imposto: se não vir nenhum anúncio, mantém simplesmente aquilo a que tem direito.

- Os anúncios são fornecidos pela **Google AdMob**.
- Aparecem **unicamente dentro da própria aplicação Plume**, nunca na cápsula flutuante e nunca por cima de outra aplicação.
- **Os subscritores não veem qualquer publicidade.**
- No Espaço Económico Europeu, no Reino Unido e na Suíça, é-lhe apresentado um formulário de consentimento fornecido por uma plataforma certificada pela Google **antes do primeiro anúncio**. Enquanto a sua escolha não for recolhida, não é pedido qualquer anúncio. Se recusar, os anúncios permanecem **não personalizados** e **nenhuma funcionalidade lhe é retirada**. Pode voltar a esta escolha a qualquer momento a partir das definições.
- Para creditar a sua recompensa de forma fiável, o seu identificador de dispositivo da Plume é transmitido à AdMob. A Google pode, além disso, recolher os seus próprios dados em conformidade com a sua política de privacidade.

*À data de redação, a difusão publicitária está desativada do lado do servidor. Esta secção descreve o funcionamento a partir do momento em que for ativada.*

---

## 6. Subscrições e compras

As subscrições e os pacotes são vendidos **através do Google Play**. Nunca vemos os seus dados bancários: são tratados pela Google, que é o vendedor para efeitos de faturação.

Recebemos da Google um comprovativo de compra que o nosso servidor verifica, e conservamos o respetivo registo (identificador de transação, datas, estado). Esse registo é conservado por razões contabilísticas e para impedir que uma mesma compra sirva duas vezes — mas é **desligado da sua identidade** quando elimina a sua conta.

---

## 7. Os seus direitos

Dispõe dos direitos de acesso, retificação, apagamento, limitação, oposição e portabilidade previstos no RGPD.

**O mais simples e o mais rápido: a eliminação está integrada na aplicação.**
Definições → Privacidade → Eliminar os meus dados. É **executada imediatamente**, não é colocada numa fila de espera. O detalhe do que é apagado e do que é conservado consta da nossa página dedicada: `https://readit0.github.io/plume-legal/suppression-compte`.

Também pode eliminar a sua conta **sem instalar a aplicação**, escrevendo para sogacmoi7@gmail.com.

Para qualquer outro pedido, escreva para **sogacmoi7@gmail.com**. Respondemos no prazo de um mês.

**Fundamentos jurídicos:** a execução do contrato (prestar o serviço que solicita, gerir a sua subscrição), o seu consentimento (serviço de acessibilidade, captura de ecrã, envio para a IA na nuvem, publicidade personalizada), o nosso interesse legítimo (segurança, luta contra a fraude) e as nossas obrigações legais (contabilidade).

Pode apresentar uma reclamação junto da **CNIL** (www.cnil.fr), autoridade de controlo do editor, ou, **se residir na União Europeia**, junto da autoridade de controlo do seu país de residência — o artigo 77.º do RGPD deixa-lhe a escolha.

---

## 8. Os menores

A Plume é uma ferramenta de apoio à escrita, destinada a um público **de 16 anos ou mais**. Não recolhemos conscientemente dados de crianças com menos de 16 anos e a aplicação não é concebida nem promovida para elas. Se exerce as responsabilidades parentais e considera que o seu filho nos transmitiu dados, escreva para sogacmoi7@gmail.com: eliminaremos a conta.

Uma vez que a aplicação permite reformular texto livre e apresenta publicidade, não é elegível para os programas destinados às famílias do Google Play.

---

## 9. Subcontratantes e destinatários

| Prestador | Função | Onde |
|---|---|---|
| **Supabase** | Alojamento da base de dados, autenticação, funções de servidor | União Europeia (Frankfurt) |
| **OpenRouter** | Encaminhamento dos pedidos para o modelo de IA | **Fora da União Europeia** |
| **Mistral AI** (através do OpenRouter) | Modelo que trata o texto (Mistral Small) | Tratamento através do intermediário acima |
| **Google Play / Google Billing** | Pagamento, subscrições | Google Ireland / Estados Unidos |
| **Google AdMob** | Publicidade com recompensa | Google Ireland / Estados Unidos |
| **Google (serviços de sistema do telemóvel)** | Reconhecimento de voz, módulos de tradução offline | Consoante o seu dispositivo |

**Não vendemos quaisquer dados nem os cedemos a corretores de dados.**

**Transferências para fora da União Europeia:** o recurso ao OpenRouter, ao Google Play e à AdMob implica uma transferência de dados para fora da União Europeia. O enquadramento jurídico destas transferências (cláusulas contratuais-tipo, decisão de adequação) **tem de ser verificado e documentado por um profissional antes da publicação** — ver a nota no final do documento.

---

## 10. Segurança

As trocas entre a aplicação e os nossos servidores são cifradas (HTTPS/TLS). O acesso aos dados na base é restringido por regras do servidor: as funções sensíveis não são acessíveis a partir da aplicação. Nenhum sistema é perfeitamente seguro, mas nenhum texto que reformula fica armazenado connosco — o que limita mecanicamente aquilo que uma intrusão poderia revelar.

---

## 11. Alterações

Qualquer alteração desta política será publicada no endereço `https://readit0.github.io/plume-legal` com uma nova data. Em caso de alteração importante na circulação dos seus dados, informá-lo-emos na aplicação.

---

## Condições gerais

As condições de utilização do serviço (quotas, subscrições, cancelamento) constam de um documento distinto: `https://readit0.github.io/plume-legal/conditions-generales`.

---

> ### A rever por um profissional
>
> Este documento foi redigido medindo o comportamento real da aplicação, mas **não foi redigido por um jurista**. Quatro pontos merecem prioritariamente um parecer profissional:
>
> 1. **A transferência de dados para fora da União Europeia** para o OpenRouter. É o ponto mais sensível: é preciso determinar o mecanismo de transferência aplicável, verificar que existe um contrato de subcontratação com este prestador, e escrevê-lo aqui. Enquanto isso não for feito, este documento descreve a transferência sem afirmar que está juridicamente enquadrada.
> 2. **Os fundamentos jurídicos** escolhidos no §7, em especial a repartição entre consentimento e interesse legítimo para o serviço de acessibilidade.
> 3. **A idade mínima** (16 anos) e a sua coerência com o questionário de classificação de conteúdos do Google Play.
> 4. **A menção relativa à IA** ao abrigo do regulamento europeu sobre a inteligência artificial (obrigação de transparência para um sistema de risco limitado).

---

Este documento é uma tradução da versão francesa, disponível no endereço https://readit0.github.io/plume-legal/. É fornecida a título informativo. Em caso de divergência, contacte-nos através de sogacmoi7@gmail.com.
