# Política de privacidade de Plume

**Última actualización: 31 de xullo de 2026** — Versión 1.0


---

## Quen é o responsable dos seus datos

**SASU RedLine Music**
SIREN 938 277 100 — SIRET `938 277 100 00013`
Abbaye 208-1, 208 Résidence Lavoisier, 18100 Vierzon, France
Contacto: sogacmoi7@gmail.com

A aplicación publícase en Google Play co nome de editor **openfunword**.

Esta política describe o que fai a aplicación Plume na súa versión actual. Foi redactada lendo o código da aplicación, non a partir dun modelo xenérico.

---

## Nun minuto

Plume axúdalle a escribir: reformula o seu texto directamente na aplicación na que está a escribir, e pode traducir o texto amosado na pantalla.

Tres cousas que cómpre lembrar:

1. **Plume non conserva ningún dos seus textos nos seus servidores.** Nin os textos reformulados, nin o texto lido na pantalla. Non gardamos nin copia nin rexistro deles.
2. **Segundo o motor que escolla, o seu texto sae ou non sae do seu teléfono.** Dous motores (o Kit local e a IA local) traballan integramente no dispositivo. O terceiro (a IA Cloud) envía o texto a un servizo de intelixencia artificial **situado fóra da Unión Europea**. Vostede escolle, e a IA Cloud non se activa nunca sen o seu acordo explícito.
3. **Plume precisa permisos potentes** (ler o contido amosado nas outras aplicacións, capturar a pantalla). Máis abaixo explicamos con precisión para que serven e para que non serven.

---

## 1. O que Plume le na súa pantalla, e cando

### 1.1 O servizo de accesibilidade

Para reescribir o seu texto no lugar onde o escribe, Plume utiliza o servizo de accesibilidade de Android. É un permiso que vostede mesmo activa, nos axustes do teléfono, despois dunha pantalla explicativa que Plume lle amosa **antes** de solicitalo.

Concretamente:

- **En repouso**, Plume só sabe que aplicación está aberta e en que momento sitúa o cursor nun campo de texto. Iso é o que fai aparecer a cápsula flotante, e unicamente nas aplicacións que vostede mesmo configurou.
- **O contido do campo só se le no instante preciso en que toca a cápsula**, para ser reescrito e despois substituído no mesmo sitio.
- **Os campos de contrasinal quedan excluídos.** A aplicación detecta os campos de tipo contrasinal (incluídos os códigos numéricos e os campos web) e négase a lelos.
- Este permiso **non permite ningunha captura de imaxe** da súa pantalla.
- Plume **non preme nunca no seu lugar** noutra aplicación: substitúe o texto dun campo, nada máis.

Dúas funcións que vostede mesmo activa —a **Lectura Asistida en modo Texto** e a **tradución das mensaxes recibidas**— len o texto amosado de xeito continuo mentres están en marcha, e páranse en canto as desactiva.

Se rexeita o servizo de accesibilidade, Plume segue a ser utilizable: pode seleccionar un texto e pasar polo menú «Plume» da selección de Android, ou compartir un texto con Plume.

### 1.2 A captura de pantalla (Lectura Asistida)

A Lectura Asistida superpón unha tradución sobre o texto amosado, por exemplo os globos dunha banda deseñada. Precisa ver a imaxe da pantalla.

- Está **desactivada por defecto** e só funciona nas aplicacións que vostede autorizou explicitamente, unha por unha.
- **Android pídelle o seu propio consentimento cada vez que se inicia unha sesión.** Non é un permiso concedido dunha vez para sempre: cada sesión esixe un acordo novo. Plume non tenta nunca reutilizar nin eludir ese acordo.
- Durante toda a sesión, **unha notificación permanente e un indicador do sistema permanecen visibles**. Plume non pode capturar a súa pantalla ás agachadas.
- A sesión **detense automaticamente ao bloquearse a pantalla**, e inmediatamente cando vostede mesmo a detén.
- As aplicacións que protexen a súa visualización (aplicacións bancarias, xestores de contrasinais) quedan **ocultadas polo propio Android** antes de que Plume reciba nada. É unha protección do sistema, real pero parcial: non todas as aplicacións sensibles a activan. Por iso non a presentamos como unha garantía absoluta.
- **As imaxes capturadas non se gardan nin se envían nunca.** Cada imaxe analízase na memoria para extraer dela o texto e despois descártase. Ningunha imaxe sae do seu teléfono, nunca, sexa cal sexa o motor escollido.

---

## 2. O que queda no seu teléfono e o que sae del

É a distinción máis importante desta política, e é vostede quen a controla.

### 2.1 Os motores que non fan saír nada

- **O Kit local** (recoñecemento e tradución de texto sen conexión) funciona integramente no dispositivo.
- **A IA local** é un modelo de intelixencia artificial que se descarga unha soa vez e despois se garda no seu teléfono (uns 720 MB). Execútase no seu dispositivo.

Con estes dous motores, **o texto lido ou reformulado non sae do seu teléfono.** Non hai ningunha petición de rede ligada ao contido do seu texto.

### 2.2 O motor IA Cloud

Cando escolle a IA Cloud, ou cando o seu dispositivo non é abondo potente para a IA local, o texto correspondente transmítese aos nosos servidores e, despois, a un servizo de intelixencia artificial de terceiros.

**Cómpre ser claros sobre o traxecto real:**

- O texto pasa pola nosa infraestrutura (Supabase), aloxada na **Unión Europea** (rexión de Europa central, Frankfurt).
- A seguir transmítese a **openrouter.ai**, un intermediario de encamiñamento **situado fóra da Unión Europea**, que fai que o procese o modelo **Mistral Small**.
- **Trátase, polo tanto, dunha transferencia de datos fóra da Unión Europea.** Non pretendemos o contrario, e non amosamos ningunha promesa de aloxamento europeo para esta etapa.
- **Plume non conserva o seu texto.** Ningunha das nosas funcións de servidor escribe o contido do seu texto: só rexistramos un identificador técnico de solicitude e o identificador do seu dispositivo, para contar a súa cota e detectar os abusos.
- **O que eses provedores fagan pola súa banda, non o podemos garantir.** Preferimos dicirllo antes que prometerlle unha retención nula que non estamos en condicións de verificar.

**A IA Cloud non se activa nunca por si soa.** Unha pantalla de consentimento dedicada explícalle estes puntos antes do primeiro envío, e non sae nada mentres non o acepte. Se a IA local falla, Plume non pasa á nube en silencio: indícallo e agarda a súa decisión. Pode revogar ese acordo en calquera momento nos axustes.

O texto enviado ten un límite: 1.200 caracteres para unha reformulación, 4.000 caracteres para unha análise de pantalla.

---

## 3. Os datos que conservamos

Non utilizamos **ningunha ferramenta de analítica de audiencia, ningún rastrexador publicitario de terceiros, ningunha ferramenta de informe de fallos**. A aplicación non contén ningún SDK de medición.

Isto é todo o que se almacena nos nosos servidores:

| Dato | Por que | Duración |
|---|---|---|
| **Identificador de dispositivo** (un número aleatorio xerado por Plume, sen relación coa súa identidade nin cun identificador publicitario) | Vincular un dispositivo a unha conta, aplicar as cotas, bloquear os abusos | Ata a supresión da súa conta |
| **Enderezo de correo electrónico da conta** (se crea unha conta por correo electrónico ou mediante Google) | Autenticalo, vincular a súa subscrición | Ata a supresión da súa conta |
| **Contadores de uso** (número de reformulacións por día e por mes: cifras, non textos) | Aplicar as cotas | Ata a supresión da súa conta |
| **Historial de compras** (identificador de transacción de Google Play, datas, estado da subscrición) | Darlle acceso ao que pagou, xestionar as renovacións, cumprir as nosas obrigas contables | Conservado mesmo despois da supresión da conta, pero **desvinculado da súa identidade** (véxase §6) |
| **Suxestións enviadas voluntariamente** (se nos escribe unha suxestión de persona desde a aplicación) | Mellorar o catálogo. Estas suxestións non se publican nunca. | Ata a supresión da súa conta |
| **Sinais técnicos de abuso** (excesos repetidos, fallo do control de integridade, sen ningún texto) | Seguridade, loita contra a fraude | Desvinculados da súa identidade ao suprimir a conta |
| **Idioma e versión da aplicación** | Servir o contido correcto | Ata a supresión da súa conta |

**O que non recollemos:** o seu nome, os seus contactos, a súa localización, a súa axenda de enderezos, as súas fotos, o seu calendario, o historial das súas aplicacións. Plume non pide ningún deses permisos.

**O que queda unicamente no seu teléfono:** as súas personas personalizadas e os seus avatares, os seus axustes, as súas regras por aplicación, a memoria caché de tradución da Lectura Asistida (borrada ao final de cada sesión). Nada disto se envía aos nosos servidores.

---

## 4. O ditado por voz

Un botón de micrófono permítelle ditar en vez de escribir. O permiso de acceso ao micrófono pídese **no momento preciso en que preme ese botón**, nunca ao iniciar a aplicación, e o micrófono só se abre nese instante. Plume non escoita nunca en segundo plano.

**Plume non recibe, non almacena e non transmite ningunha gravación de audio.** O ditado confíaselle ao motor de recoñecemento de voz integrado no seu teléfono (o de Android). Plume só recupera o texto transcrito.

**Un punto importante e honesto:** ese motor do sistema pertence ao seu teléfono, xeralmente a Google. Segundo o seu dispositivo, os seus axustes e os módulos de idioma instalados, **pode transmitir o audio aos servidores do seu editor** para transcribilo. Ese tratamento escapa a Plume e depende da política de privacidade do editor do seu sistema. Polo tanto, non podemos afirmar que a súa voz quede no dispositivo: iso depende do seu teléfono, non de nós.

Se rexeita o permiso do micrófono, a escritura co teclado segue evidentemente dispoñible.

---

## 5. Publicidade

O servizo é gratuíto dentro dun certo límite de uso diario. Máis alá dese límite, pode **escoller** ver un anuncio con recompensa para desbloquear usos adicionais. Non se impón nunca: se non ve ningún anuncio, simplemente conserva aquilo a que ten dereito.

- Os anuncios fornéceos **Google AdMob**.
- Aparecen **unicamente dentro da propia aplicación Plume**, nunca na cápsula flotante e nunca por riba doutra aplicación.
- **Os subscritores non ven ningún anuncio.**
- No Espazo Económico Europeo, no Reino Unido e en Suíza preséntaselle un formulario de consentimento fornecido por unha plataforma certificada por Google **antes do primeiro anuncio**. Mentres non se recolla a súa escolla, non se solicita ningún anuncio. Se o rexeita, os anuncios seguen a ser **non personalizados** e **non se lle retira ningunha funcionalidade**. Pode mudar esa escolla en calquera momento desde os axustes.
- Para acreditarlle a recompensa de xeito fiable, o identificador do seu dispositivo Plume transmítese a AdMob. Google pode, ademais, recoller os seus propios datos consonte a súa política de privacidade.

*Na data de redacción, a difusión publicitaria está desactivada no servidor. Esta sección describe o funcionamento a partir do momento en que se active.*

---

## 6. Subscricións e compras

As subscricións e os paquetes véndense **a través de Google Play**. Non vemos nunca os seus datos bancarios: trátaos Google, que é o vendedor para os efectos da facturación.

Recibimos de Google un xustificante de compra que o noso servidor verifica, e conservamos o seu rastro (identificador de transacción, datas, estado). Ese rastro consérvase por razóns contables e para impedir que unha mesma compra sirva dúas veces, pero queda **desvinculado da súa identidade** cando suprime a súa conta.

---

## 7. Os seus dereitos

Dispón dos dereitos de acceso, de rectificación, de supresión, de limitación, de oposición e de portabilidade previstos no Regulamento Xeral de Protección de Datos (RXPD).

**O máis sinxelo e o máis rápido: a supresión está integrada na aplicación.**
Axustes → Privacidade → Eliminar os meus datos. Execútase **inmediatamente**, non se pon en ningunha cola de espera. O detalle do que se borra e do que se conserva figura na nosa páxina dedicada: `https://readit0.github.io/plume-legal/suppression-compte`.

Tamén pode suprimir a súa conta **sen instalar a aplicación**, escribindo a sogacmoi7@gmail.com.

Para calquera outra solicitude, escriba a **sogacmoi7@gmail.com**. Respondemos no prazo dun mes.

**Bases xurídicas:** a execución do contrato (prestar o servizo que nos pide, xestionar a súa subscrición), o seu consentimento (servizo de accesibilidade, captura de pantalla, envío á IA Cloud, publicidade personalizada), o noso interese lexítimo (seguridade, loita contra a fraude) e as nosas obrigas legais (contabilidade).

Pode presentar unha reclamación ante a **CNIL** (www.cnil.fr), autoridade de control do editor, ou, **se reside na Unión Europea**, ante a autoridade de control do seu país de residencia: o artigo 77 do RXPD déixalle a escolla.

---

## 8. Os menores

Plume é unha ferramenta de axuda á redacción, destinada a un público **de 16 anos ou máis**. Non recollemos conscientemente datos de nenos menores de 16 anos e a aplicación non está deseñada nin promovida para eles. Se vostede é titular da patria potestade e pensa que o seu fillo ou filla nos transmitiu datos, escriba a sogacmoi7@gmail.com: suprimiremos a conta.

Dado que a aplicación permite reformular un texto libre e amosa publicidade, non é elixible para os programas de Google Play destinados ás familias.

---

## 9. Encargados do tratamento e destinatarios

| Provedor | Función | Onde |
|---|---|---|
| **Supabase** | Aloxamento da base de datos, autenticación, funcións de servidor | Unión Europea (Frankfurt) |
| **OpenRouter** | Encamiñamento das solicitudes cara ao modelo de IA | **Fóra da Unión Europea** |
| **Mistral AI** (mediante OpenRouter) | Modelo que procesa o texto (Mistral Small) | Tratamento a través do intermediario anterior |
| **Google Play / Google Billing** | Pagamento, subscricións | Google Ireland / Estados Unidos |
| **Google AdMob** | Publicidade con recompensa | Google Ireland / Estados Unidos |
| **Google (servizos de sistema do teléfono)** | Recoñecemento de voz, módulos de tradución sen conexión | Segundo o seu dispositivo |

**Non vendemos ningún dato nin cedemos ningún a corredores de datos.**

**Transferencias fóra da Unión Europea:** o recurso a OpenRouter, a Google Play e a AdMob implica unha transferencia de datos fóra da Unión Europea. O marco xurídico desas transferencias (cláusulas contractuais tipo, decisión de adecuación) **debe ser verificado e documentado por un profesional antes da publicación**: véxase a nota ao final do documento.

---

## 10. Seguridade

Os intercambios entre a aplicación e os nosos servidores están cifrados (HTTPS/TLS). O acceso aos datos da base está restrinxido por regras de servidor: as funcións sensibles non son accesibles desde a aplicación. Ningún sistema é perfectamente seguro, pero ningún texto que vostede reformula se almacena na nosa casa, o que limita mecanicamente o que unha intrusión podería revelar.

---

## 11. Modificacións

Calquera modificación desta política publicarase no enderezo `https://readit0.github.io/plume-legal` cunha data nova. En caso de cambio importante na circulación dos seus datos, informarémolo dentro da aplicación.

---

## Condicións xerais

As condicións de uso do servizo (cotas, subscricións, cancelación) figuran nun documento separado: `https://readit0.github.io/plume-legal/conditions-generales`.

---

> ### Pendente de revisión por un profesional
>
> Este documento foi redactado medindo o comportamento real da aplicación, pero **non o redactou ningún xurista**. Catro puntos merecen prioritariamente un ditame profesional:
>
> 1. **A transferencia de datos fóra da Unión Europea** cara a OpenRouter. É o punto máis sensible: cómpre determinar o mecanismo de transferencia aplicable, verificar que existe un acordo de tratamento con ese provedor e escribilo aquí. Mentres iso non se faga, este documento describe a transferencia sen afirmar que estea debidamente amparada.
> 2. **As bases xurídicas** adoptadas no §7, en particular o reparto entre consentimento e interese lexítimo para o servizo de accesibilidade.
> 3. **A idade mínima** (16 anos) e a súa coherencia co cuestionario de clasificación de contido de Google Play.
> 4. **A mención relativa á IA** en virtude do regulamento europeo sobre a intelixencia artificial (obriga de transparencia para un sistema de risco limitado).

---

Este documento é unha tradución da versión francesa, dispoñible no enderezo https://readit0.github.io/plume-legal/. Fornécese a título informativo. En caso de diverxencia, contacte connosco en sogacmoi7@gmail.com.
