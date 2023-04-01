import openai

openai.api_key = "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"

nombre = "German"


text1 = "Vos sos mi asistente de emails. Mi nombre es "
text2 = " Recién recibí este mail de parte de "
text3 = " Necesito que me digas de qué se trata, a modo de resumen. Decime solo " \
        "la información nueva que necesito saber. El resumen tiene que ser más corto que el original. " \
"Indicar claramente cual es el asunto del mail y cual el resumen. Si hay fechas, indicarlas. " \

input = '''Messages:
Remitente:  GitHub <noreply@github.com>
Asunto:  [GitHub] Please verify your device
Hey GermanTarnoski!

A sign in attempt requires further verification because we did not recognize your device. To complete the sign in, enter the verification code on the unrecognized device.

Device: Firefox on Windows
Verification code: 058039

If you did not attempt to sign in to your account, your password may be compromised. Visit https://github.com/settings/security to create a new, strong password for your GitHub account.

If you'd like to automatically verify devices in the future, consider enabling two-factor authentication on your account. Visit https://docs.github.com/articles/configuring-two-factor-authentication to learn about two-factor authentication.

If you decide to enable two-factor authentication, ensure you retain access to one or more account recovery methods. See https://docs.github.com/articles/configuring-two-factor-authentication-recovery-methods in the GitHub Help.

Thanks,
The GitHub Team





Remitente:  "No contestar a este correo  (vía Webcampus3UCEMA)" <noreply@ucema.edu.ar>
Asunto:  Usted ha realizado su entrega en la tarea Laboratorio 1

RE-2653-RH-2023-1S -> Tarea -> Laboratorio 1
---------------------------------------------------------------------
Usted ha realizado una entrega en la tarea Laboratorio 1

Puede ver el estado de su entrega en

https://ucema.edu.ar/webcampus3/mod/assign/view.php?id=98900

---------------------------------------------------------------------

This email has an attachment.




Remitente:  UCEMA OnLine <online@ucema.edu.ar>
Asunto:  Programación de próximas clases

<p>Estimado alumno,</p>

<p>A continuación, se muestran las clases (híbridas ó virtuales) a las que deberá asistir durante los próximos días:</p><p><strong>Economia -ININF-</strong><br>lunes  3 de abril, 18:00 hs</p>
<p><strong>Economia -ININF-</strong><br>lunes  3 de abril, 21:00 hs</p>
<p><strong>Base de Datos I - ININF-</strong><br>martes  4 de abril, 18:00 hs</p>
<p><strong>Base de Datos I - ININF-</strong><br>martes  4 de abril, 21:00 hs</p>
<p><strong>Sistemas de Informacion LIDE - LICP -LIRI - LIMA</strong><br>miércoles  5 de abril, 18:00 hs</p>
<p><strong>Sistemas de Informacion LIDE - LICP -LIRI - LIMA</strong><br>miércoles  5 de abril, 21:00 hs</p>

<p>Para acceder a sus clases deberá ingresar
al siguiente <a href="https://ucema.edu.ar/misclases">enlace</a>.
Allí deberá colocar su usuario y contraseña UCEMA, y luego
hacer click en el botón "ir a mi clase".</p>
<p>NOTA: Por favor, si Ud. tiene alguna duda o problema para 
acceder, comuníquese con secretaría académica 
(<strong>alumnosgrado@ucema.edu.ar</strong> o 
<strong>alumnosposgrado@ucema.edu.ar</strong>), o bien, puede acceder al 
siguiente enlace donde encontrará instructivos y mayor información: 
<a href="https://ucema.edu.ar/ensenanzaonline">https://ucema.edu.ar/ensenanzaonline</a></p>
<address>
--<br>
UCEMA OnLine
</address>





Remitente:  UCEMA OnLine <clasesonline@ucema.edu.ar>
Asunto:  Recordatorio de comienzo de clase Híbrida /   Online
<p>Estimado alumno:</p>
<p>Le informamos que para acceder a sus clases (híbridas ó virtuales) deberá ingresar
al siguiente <a href="https://ucema.edu.ar/misclases">enlace</a>.</p>
<p>Allí deberá colocar su usuario y contraseña UCEMA, y luego
hacer click en el botón "ir a mi clase".</p>
<p>Recuerde que a las 18:00 Hs comienza la clase  <strong>Redes II - ININF-</strong></p><p>NOTA: Por favor, si Ud. tiene alguna duda o problema para 
acceder, comuníquese con secretaría académica 
(<strong>alumnosgrado@ucema.edu.ar</strong> o 
<strong>alumnosposgrado@ucema.edu.ar</strong>), o bien, puede acceder al 
siguiente enlace donde encontrará instructivos y mayor información: 
<a href="https://ucema.edu.ar/ensenanzaonline">https://ucema.edu.ar/ensenanzaonline</a>.</p>
<address>
--<br>
UCEMA OnLine
</address>





Remitente:  international <international@ucema.edu.ar>
Asunto:  Cursos Cortos en el Exterior
Estimados alumnos,

Esperamos que este correo los encuentre muy bien!

Queremos compartir con ustedes la oferta actualizada de cursos cortos de verano (junio/julio/agosto) de nuestras universidades partner en el hemisferio norte. Estos cursos ofrecen la oportunidad de realizar una experiencia de corta duración en destinos internacionales sobre una variedad de temáticas disponibles. Además, se ofrecen programas culturales, visitas a empresas y actividades de intercambio con estudiantes del mundo entero.

Los alumnos UCEMA cuentan con beneficios especiales en el marco de los convenios existentes entre nuestra institución y las universidades extranjeras.

¿Qué cursos se ofrecen?

Podrán conocer la oferta disponible aquí.

¿Cómo es el proceso de postulación?

En caso de estar interesados, deberán completar el siguiente formulario web y enviar la documentación requerida a exchange@ucema.edu.ar. Una vez recibida la postulación, nos pondremos en contacto con ustedes para finalizar el proceso.

Quedamos a disposición ante cualquier duda o consulta

Saludos

Departamento de Relaciones Internacionales

-----------------------------------------------------------------------

 E-MAIL: exchange@ucema.edu.ar
 11 5028-0535/ 011-6314-3000 (Int. 262)
 Av. Córdoba 637 | C1054AAP |
 CABA | Argentina ucema.edu.ar

Elegí quién querés ser


This email has an attachment.




Remitente:  comunidad <comunidad@ucema.edu.ar>
Asunto:  Cursos y Talleres UCEMA ¡Te esperamos!
[ Versión web ]

 Cursos y Talleres UCEMA

Espacios de formación continua, pensados para que los participantes desarrollen diversas capacidades y adquieran herramientas importantes para su crecimiento personal, profesional y social.

Preparación examen TOEFL iBT

Dictado por Iliana Graziano

 Se propone que los alumnos conozcan y se familiaricen con el examen y sus 4 secciones: Reading, Listening, Speaking and Writing. Afiancen y orienten sus habilidades en el idioma para responder a los requerimientos de cada sección. Desmenucen cada sección e incorporen estrategias específicas para alcanzar su mejor puntaje. Profundicen sobre la estructura de plantillas y ensayos, estructuras gramaticales y vocabulario específico.

 En clase, revisen sus propios ensayos (Writing) y practiquen cada uno de los ejercicios correspondientes a la sección Speaking. Cumplimenten los requerimientos del taller semana tras semana.

8 encuentros semanales. Asistencia obligatoria, la falta significará la adjudicación de la plaza a otra persona.
 Fechas: viernes del 28 de abril al 23 de junio 
 Horario: 17 a 18:30h

Develop your English Language skills

Dictado por Martina Benitez Vibart

 Un curso para afianzar tus conocimientos en la lengua inglesa, ahondando especialmente en la gramática, para poder desenvolverse y comunicarse de manera óptima en relaciones tanto laborales como en cualquier contexto, con el principal objetivo de consolidar el nivel First Certificate of English de la Universidad de Cambridge, que es de referencia a nivel internacional.

 Se ejercitará principalmente desde la lectura, la escritura, la escucha y el diálogo, para reforzar estas habilidades, y comprender así mejor el idioma de manera integral, buscando incluir en cada caso los intereses e inquietudes de los alumnos, para que sea más llevadero el aprendizaje y la expresión con un idioma que puede parecer difícil, pero cuando se lo desglosa resulta muy enriquecedor.

8 encuentros semanales. Asistencia obligatoria, la falta significará la adjudicación de la plaza a otra persona.
 Fechas: miércoles del 12 de abril al 31 de mayo 
 Horario: 17:30 a 19h

Taller de Ajedrez para principiantes

Dictado por Guadalupe Encina

 En este curso aprenderás las reglas e ideas básicas sobre el ajedrez, además sabrás cuáles son las fases de la partida y qué debemos hacer en cada una de ellas, así como, técnicas y herramientas para aprender y mejorar tus habilidades. Además, hablaremos y analizaremos qué es la estrategia y la táctica en el ajedrez y cómo calcular y analizarlas.      Al final del curso, lograrás comprender profundamente el ajedrez: no sólo mejorarás tu nivel, sino que también entenderás toto lo que puede      suceder dentro de un tablero. ¡Te volverás un/a ajedrecista!

5 encuentros
 Fechas: martes del 11 de abril al 9 de mayo 
 Horario: 18 a 19:30h

Taller de Ortografía

Dictado por Natalia Imperiali

 El objetivo del Taller de Ortografía es que los alumnos aprendan las principales reglas de ortografía para que puedan mejorar sus habilidades de escritura y la calidad de sus producciones.

 Se abordarán cinco ejes temáticos: acentuación, mayúsculas, abreviación, prefijos y puntuación. En primer lugar, vamos a estudiar la teoría. Vamos a abordar las dudas más frecuentes y a aprender técnicas para corregir errores comunes. Después, vamos a pasar a la parte lúdica y a poner en práctica lo estudiado.

4 encuentros
 Fechas: jueves 13 de abril al 4 de mayo 
 Horario: 17 a 19h

 Inscripción acá

 Sin costo para la comunidad universitaria. Clases sincrónicas a través de la plataforma Zoom. Los cupos son limitados y serán asignados por orden de inscripción.

 Importante: Las clases no son grabadas. Al final del curso/taller puede ofrecerse, a pedido del estudiante, un Certificado de participación siempre que el estudiante haya asistido al 75% de las clases.

 UCEMA | Universidad del CEMA
 Av. Córdoba 374, (C1054AAP) Ciudad de Buenos Aires, Argentina
 (011) 6314-3000

(C) UCEMA | Universidad del CEMA

 Para desuscribirse de las notificaciones de la Universidad del CEMA


This email has an attachment.




Remitente:  "Nicolás Suarez Durrels" <nsuarezdurrels@itba.edu.ar>
Asunto:  Fwd: HackITBA '23
---------- Mensaje reenviado ---------
De: Computer Society <computersociety@itba.edu.ar>
Fecha: El mié, 22 de mar. de 2023 a la(s) 20:55
Asunto: HackITBA '23
Para: Nicolás Suarez Durrels <nsuarezdurrels@itba.edu.ar>, <
germantarnoski@gmail.com>, BRUNO ENZO BAUMGART <bbaumgart@itba.edu.ar>



¡Han sido seleccionados!



¡Ya casi! Les comunicamos que ahora mismo se encuentran en la lista de
preseleccionados para participar de HackITBA ‘23 el próximo 31 de marzo, 1
y 2 de abril en las sedes del Instituto Tecnológico de Buenos Aires.




Competencia completamente gratuita

Se premiarán a los mejores de cada categoría

Se proveerá comida y bebida

Evento presencial de 36hs consecutivas




Como podrás notar, este año la tasa de inscriptos fue superior a lo
esperado y solo los 25 equipos que, según nuestro criterio, más podrán
disfrutar de la experiencia, fueron seleccionados para participar de la
competencia. Considerando esto, necesitamos como primer paso que confirmen
su presencia en el evento. Para esto necesitamos que nos envíes:

Confirmación de asistencia en el evento

Categoría de preferencia (su categoría será informada el primer día del
evento)

Restricciones alimentarias.

Una vez enviada la confirmación, te recomendamos que revises los documentos
adjuntados y leas las recomendaciones para los participantes, todos estos
documentos serán entregados y completados durante la acreditación, por lo
que saber previamente su contenido puede resultar recomendable. Además,
considerar que la lectura del reglamento es de carácter obligatorio.

Documentación y Reglamento <http://bit.ly/CS_docs>


¡Nos vemos pronto!


Equipo de Computer Society ITBA.

This email has an attachment.'''

#put all emails on a list. Each email starts with "Remitente:"
emails = input.split("Remitente:")[1:]

#put all the remintentes on a list called remitentes

for email in emails:
    partes_mail = email.split("\n")
    remitente = partes_mail[0]
    prompt = text1 + nombre + "." + text2 + remitente + text3
    i = 0
    for parte in partes_mail:
        if i == 0:
            continue
        else:
            prompt += parte
        i += 1

    completion = openai.Completion.create(engine="text-davinci-003", prompt=prompt, max_tokens=2048)


    with open("output.txt", "a") as f:
        f.write(completion.choices[0].text)

