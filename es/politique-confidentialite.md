# Política de privacidad de Plume

**Última actualización: 31 de julio de 2026** — Versión 1.0

---

## Quién es el responsable del tratamiento de sus datos

**SASU RedLine Music**
SIREN 938 277 100 — SIRET `938 277 100 00013`
Abbaye 208-1, 208 Résidence Lavoisier, 18100 Vierzon, France
Contacto: sogacmoi7@gmail.com

La aplicación se publica en Google Play bajo el nombre de editor **openfunworld**.

Esta política describe lo que hace la aplicación Plume en su versión actual. Ha sido redactada leyendo el código de la aplicación, no a partir de una plantilla genérica.

---

## En un minuto

Plume le ayuda a escribir: reformula su texto directamente en la aplicación en la que está escribiendo, y puede traducir el texto mostrado en la pantalla.

Tres cosas que conviene recordar:

1. **Plume no conserva ninguno de sus textos en sus servidores.** Ni sus textos reformulados, ni el texto leído en la pantalla. No guardamos de ellos ni copia ni registro.
2. **Según el motor que elija, su texto sale o no sale de su teléfono.** Dos motores (el Kit local y la IA local) funcionan íntegramente en el dispositivo. El tercero (la IA en la nube) envía el texto a un servicio de inteligencia artificial **situado fuera de la Unión Europea**. Usted elige, y la IA en la nube nunca se activa sin su consentimiento explícito.
3. **Plume necesita permisos potentes** (leer el contenido mostrado en las demás aplicaciones, capturar la pantalla). A continuación explicamos con precisión para qué sirven y para qué no sirven.

---

## 1. Lo que Plume lee en su pantalla, y cuándo

### 1.1 El servicio de accesibilidad

Para reescribir su texto allí donde lo escribe, Plume utiliza el servicio de accesibilidad de Android. Es un permiso que usted mismo activa, en los ajustes del teléfono, después de una pantalla explicativa que Plume le muestra **antes** de solicitárselo.

En concreto:

- **En reposo**, Plume solo sabe qué aplicación está abierta y en qué momento coloca el cursor en un campo de escritura. Eso es lo que hace aparecer la cápsula flotante, y únicamente en las aplicaciones que usted mismo ha configurado.
- **El contenido del campo solo se lee en el instante preciso en que toca la cápsula**, para ser reescrito y luego sustituido en el sitio.
- **Los campos de contraseña quedan excluidos.** La aplicación detecta los campos de tipo contraseña (incluidos los códigos numéricos y los campos web) y se niega a leerlos.
- Este permiso **no permite ninguna captura de imagen** de su pantalla.
- Plume **nunca pulsa en su lugar** dentro de otra aplicación: sustituye el texto de un campo, nada más.

Dos funciones que usted mismo activa —la **Lectura Asistida en modo Texto** y la **traducción de los mensajes recibidos**— leen el texto mostrado de forma continua mientras están en marcha, y se detienen en cuanto usted las corta.

Si rechaza el servicio de accesibilidad, Plume sigue siendo utilizable: puede seleccionar un texto y pasar por el menú «Plume» de la selección de Android, o compartir un texto con Plume.

### 1.2 La captura de pantalla (Lectura Asistida)

La Lectura Asistida superpone una traducción sobre el texto mostrado, por ejemplo los bocadillos de un cómic. Necesita ver la imagen de la pantalla.

- Está **desactivada por defecto** y solo funciona en las aplicaciones que usted haya autorizado explícitamente, una por una.
- **Android le pide su propio consentimiento cada vez que se inicia una sesión.** No es un permiso concedido de una vez por todas: cada sesión exige un nuevo acuerdo. Plume nunca intenta reutilizar ni eludir ese acuerdo.
- Durante toda la sesión, **una notificación permanente y un indicador del sistema permanecen visibles**. Plume no puede capturar su pantalla de forma discreta.
- La sesión **se detiene automáticamente al bloquearse la pantalla**, e inmediatamente cuando usted la detiene.
- Las aplicaciones que protegen su visualización (aplicaciones bancarias, gestores de contraseñas) son **ocultadas por el propio Android** antes de que Plume reciba nada. Es una protección del sistema, real pero parcial: no todas las aplicaciones sensibles la activan. Por eso no la presentamos como una garantía absoluta.
- **Las imágenes capturadas nunca se guardan ni se envían.** Cada imagen se analiza en memoria para extraer el texto y después se descarta. Ninguna imagen sale de su teléfono, nunca, sea cual sea el motor elegido.

---

## 2. Lo que se queda en su teléfono y lo que sale

Es la distinción más importante de esta política, y es usted quien la controla.

### 2.1 Los motores que no hacen salir nada

- **El Kit local** (reconocimiento y traducción de texto sin conexión) funciona íntegramente en el dispositivo.
- **La IA local** es un modelo de inteligencia artificial descargado una vez y luego almacenado en su teléfono (unos 720 MB). Se ejecuta en su dispositivo.

Con estos dos motores, **el texto leído o reformulado no sale de su teléfono.** No hay ninguna llamada de red vinculada al contenido de su texto.

### 2.2 El motor IA en la nube

Cuando elige la IA en la nube, o cuando su dispositivo no es lo bastante potente para la IA local, el texto de que se trate se transmite a nuestros servidores y después a un servicio de inteligencia artificial de un tercero.

**Hay que ser claro sobre el trayecto real:**

- El texto transita por nuestra infraestructura (Supabase), alojada en la **Unión Europea** (región de Europa Central, Fráncfort).
- A continuación se transmite a **openrouter.ai**, un intermediario de enrutamiento **situado fuera de la Unión Europea**, que hace que lo trate el modelo **Mistral Small**.
- **Se trata, por tanto, de una transferencia de datos fuera de la Unión Europea.** No pretendemos lo contrario, y no mostramos ninguna promesa de alojamiento europeo para esta etapa.
- **Plume no conserva su texto.** Ninguna de nuestras funciones de servidor escribe el contenido de su texto: solo registramos un identificador técnico de solicitud y el identificador de su dispositivo, para contabilizar su cuota y detectar abusos.
- **Lo que estos proveedores hagan por su parte, no podemos garantizarlo.** Preferimos decírselo antes que prometerle una retención nula que no estamos en condiciones de verificar.

**La IA en la nube nunca se activa por sí sola.** Una pantalla de consentimiento específica le explica estos puntos antes del primer envío, y nada sale mientras usted no haya aceptado. Si la IA local falla, Plume no cambia a la nube en silencio: se lo señala y espera su decisión. Puede revocar este consentimiento en cualquier momento en los ajustes.

El texto enviado está limitado: 1200 caracteres para una reformulación, 4000 caracteres para un análisis de pantalla.

---

## 3. Los datos que conservamos

No utilizamos **ninguna herramienta de analítica de audiencia, ningún rastreador publicitario de terceros, ninguna herramienta de informe de fallos**. La aplicación no contiene ningún SDK de medición.

Esto es la totalidad de lo que se almacena en nuestros servidores:

| Dato | Por qué | Duración |
|---|---|---|
| **Identificador de dispositivo** (un número aleatorio generado por Plume, sin relación con su identidad ni con un identificador publicitario) | Vincular un dispositivo a una cuenta, aplicar las cuotas, bloquear los abusos | Hasta la supresión de su cuenta |
| **Dirección de correo electrónico de la cuenta** (si crea una cuenta por correo electrónico o a través de Google) | Autenticarle, vincular su suscripción | Hasta la supresión de su cuenta |
| **Contadores de uso** (número de reformulaciones por día y por mes: números, no textos) | Aplicar las cuotas | Hasta la supresión de su cuenta |
| **Historial de compra** (identificador de transacción de Google Play, fechas, estado de la suscripción) | Darle acceso a lo que ha pagado, gestionar las renovaciones, cumplir nuestras obligaciones contables | Conservado incluso tras la supresión de la cuenta, pero **desvinculado de su identidad** (véase el §6) |
| **Sugerencias enviadas voluntariamente** (si nos escribe una sugerencia de persona desde la aplicación) | Mejorar el catálogo. Estas sugerencias nunca se publican. | Hasta la supresión de su cuenta |
| **Señales técnicas de abuso** (excesos repetidos, fallo de control de integridad, sin ningún texto) | Seguridad, lucha contra el fraude | Desvinculadas de su identidad al suprimirse la cuenta |
| **Idioma y versión de la aplicación** | Servir el contenido correcto | Hasta la supresión de su cuenta |

**Lo que no recogemos:** su nombre, sus contactos, su ubicación, su libreta de direcciones, sus fotos, su calendario, el historial de sus aplicaciones. Plume no solicita ninguno de estos permisos.

**Lo que se queda únicamente en su teléfono:** sus personas personalizados y sus avatares, sus ajustes, sus reglas por aplicación, la caché de traducción de la Lectura Asistida (borrada al final de cada sesión). Nada de esto se envía a nuestros servidores.

---

## 4. El dictado por voz

Un botón de micrófono le permite dictar en lugar de escribir. El permiso de acceso al micrófono se solicita **en el momento preciso en que pulsa ese botón**, nunca al arrancar, y el micrófono solo se abre en ese instante. Plume nunca escucha en segundo plano.

**Plume no recibe, no almacena ni transmite ninguna grabación de audio.** El dictado se confía al motor de reconocimiento de voz integrado en su teléfono (el de Android). Plume solo recupera el texto transcrito.

**Punto importante y honesto:** ese motor del sistema pertenece a su teléfono, generalmente a Google. Según su dispositivo, sus ajustes y los módulos de idioma instalados, **puede transmitir el audio a los servidores de su editor** para transcribirlo. Ese tratamiento escapa a Plume y depende de la política de privacidad del editor de su sistema. Por tanto, no podemos afirmar que su voz permanezca en el dispositivo: eso depende de su teléfono, no de nosotros.

Si rechaza el permiso del micrófono, la escritura con el teclado sigue estando disponible, evidentemente.

---

## 5. Publicidad

El servicio es gratuito dentro de un cierto límite de uso al día. Por encima de ese límite, puede **elegir** ver un anuncio recompensado para desbloquear usos adicionales. Nunca se impone: si no ve ningún anuncio, simplemente conserva aquello a lo que tiene derecho.

- Los anuncios los proporciona **Google AdMob**.
- Aparecen **únicamente dentro de la propia aplicación Plume**, nunca en la cápsula flotante y nunca por encima de otra aplicación.
- **Los suscriptores no ven ningún anuncio.**
- En el Espacio Económico Europeo, el Reino Unido y Suiza, se le presenta un formulario de consentimiento facilitado por una plataforma certificada por Google **antes del primer anuncio**. Mientras no se recoja su elección, no se solicita ningún anuncio. Si rechaza, los anuncios siguen siendo **no personalizados** y **no se le retira ninguna funcionalidad**. Puede cambiar esta elección en cualquier momento desde los ajustes.
- Para acreditar su recompensa de forma fiable, su identificador de dispositivo de Plume se transmite a AdMob. Google puede, además, recoger sus propios datos con arreglo a su política de privacidad.

*A la fecha de redacción, la difusión publicitaria está desactivada en el servidor. Esta sección describe el funcionamiento a partir del momento en que se active.*

---

## 6. Suscripciones y compras

Las suscripciones y los packs se venden **a través de Google Play**. Nunca vemos sus datos bancarios: los trata Google, que es el vendedor a efectos de la facturación.

Recibimos de Google un justificante de compra que nuestro servidor verifica, y conservamos su rastro (identificador de transacción, fechas, estado). Ese rastro se conserva por razones contables y para impedir que una misma compra sirva dos veces, pero queda **desvinculado de su identidad** cuando usted suprime su cuenta.

---

## 7. Sus derechos

Usted dispone de los derechos de acceso, rectificación, supresión, limitación, oposición y portabilidad previstos por el RGPD.

**Lo más sencillo y lo más rápido: la supresión está integrada en la aplicación.**
Ajustes → Privacidad → Eliminar mis datos. Se **ejecuta inmediatamente**, no se pone en una cola de espera. El detalle de lo que se borra y de lo que se conserva figura en nuestra página dedicada: `https://readit0.github.io/plume-legal/suppression-compte`.

También puede suprimir su cuenta **sin instalar la aplicación**, escribiendo a sogacmoi7@gmail.com.

Para cualquier otra solicitud, escriba a **sogacmoi7@gmail.com**. Respondemos en el plazo de un mes.

**Bases jurídicas:** la ejecución del contrato (prestar el servicio que usted solicita, gestionar su suscripción), su consentimiento (servicio de accesibilidad, captura de pantalla, envío a la IA en la nube, publicidad personalizada), nuestro interés legítimo (seguridad, lucha contra el fraude) y nuestras obligaciones legales (contabilidad).

Puede presentar una reclamación ante la **CNIL** (www.cnil.fr), autoridad de control del editor, o, **si reside en la Unión Europea**, ante la autoridad de control de su país de residencia — el artículo 77 del RGPD le deja elegir.

---

## 8. Los menores

Plume es una herramienta de ayuda a la redacción, destinada a un público **de 16 años o más**. No recogemos conscientemente datos de menores de 16 años y la aplicación no está diseñada ni promocionada para ellos. Si usted es titular de la patria potestad y cree que su hijo nos ha transmitido datos, escriba a sogacmoi7@gmail.com: suprimiremos la cuenta.

Como la aplicación permite reformular un texto libre y muestra publicidad, no es apta para los programas destinados a las familias de Google Play.

---

## 9. Encargados del tratamiento y destinatarios

| Proveedor | Función | Dónde |
|---|---|---|
| **Supabase** | Alojamiento de la base de datos, autenticación, funciones de servidor | Unión Europea (Fráncfort) |
| **OpenRouter** | Encaminamiento de las solicitudes hacia el modelo de IA | **Fuera de la Unión Europea** |
| **Mistral AI** (a través de OpenRouter) | Modelo que trata el texto (Mistral Small) | Tratamiento a través del intermediario anterior |
| **Google Play / Google Billing** | Pago, suscripciones | Google Ireland / Estados Unidos |
| **Google AdMob** | Publicidad recompensada | Google Ireland / Estados Unidos |
| **Google (servicios del sistema del teléfono)** | Reconocimiento de voz, módulos de traducción sin conexión | Según su dispositivo |

**No vendemos ningún dato ni cedemos ninguno a intermediarios de datos.**

**Transferencias fuera de la Unión Europea:** el recurso a OpenRouter, a Google Play y a AdMob implica una transferencia de datos fuera de la Unión Europea. El marco jurídico de estas transferencias (cláusulas contractuales tipo, decisión de adecuación) **debe ser verificado y documentado por un profesional antes de la publicación**; véase la nota al final del documento.

---

## 10. Seguridad

Los intercambios entre la aplicación y nuestros servidores están cifrados (HTTPS/TLS). El acceso a los datos en la base está restringido por reglas de servidor: las funciones sensibles no son accesibles desde la aplicación. Ningún sistema es perfectamente seguro, pero ningún texto que usted reformula se almacena en nuestros sistemas, lo que limita mecánicamente lo que una intrusión podría revelar.

---

## 11. Modificaciones

Toda modificación de esta política se publicará en la dirección `https://readit0.github.io/plume-legal` con una nueva fecha. En caso de cambio importante en la circulación de sus datos, se lo comunicaremos en la aplicación.

---

## Condiciones generales

Las condiciones de uso del servicio (cuotas, suscripciones, cancelación) figuran en un documento distinto: `https://readit0.github.io/plume-legal/conditions-generales`.

---

> ### Pendiente de revisión por un profesional
>
> Este documento se ha redactado midiendo el comportamiento real de la aplicación, pero **no lo ha redactado un jurista**. Cuatro puntos merecen prioritariamente un dictamen profesional:
>
> 1. **La transferencia de datos fuera de la Unión Europea** hacia OpenRouter. Es el punto más sensible: hay que determinar el mecanismo de transferencia aplicable, verificar que existe un contrato de encargo del tratamiento con este proveedor, y escribirlo aquí. Mientras eso no se haga, este documento describe la transferencia sin afirmar que esté enmarcada jurídicamente.
> 2. **Las bases jurídicas** elegidas en el §7, en particular el reparto entre consentimiento e interés legítimo para el servicio de accesibilidad.
> 3. **La edad mínima** (16 años) y su coherencia con el cuestionario de clasificación de contenido de Google Play.
> 4. **La mención relativa a la IA** en virtud del Reglamento europeo de inteligencia artificial (obligación de transparencia para un sistema de riesgo limitado).

---

Este documento es una traducción de la versión francesa, disponible en la dirección https://readit0.github.io/plume-legal/. Se facilita a título informativo. En caso de divergencia, contáctenos en sogacmoi7@gmail.com.
