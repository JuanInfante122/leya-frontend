from dataclasses import dataclass


@dataclass
class EntradaConocimiento:
    categoria:      str
    respuesta:      str
    fuentes:        list[dict]
    palabras_clave: list[str]


BASE_CONOCIMIENTO: list[EntradaConocimiento] = [

    EntradaConocimiento(
        categoria="despido_indemnizacion",
        palabras_clave=["despido", "despedir", "indemnización", "indemnizacion",
                        "justa causa", "sin justa causa", "me echaron",
                        "terminación", "terminacion", "liquidación"],
        respuesta=(
            "Si fue despedido sin justa causa, tiene derecho a una indemnización "
            "según el artículo 64 del Código Sustantivo del Trabajo (CST). "
            "Para contratos a término indefinido: si lleva menos de 1 año, "
            "le corresponden 30 días de salario. Por cada año adicional, "
            "20 días más. Si su salario es superior a 10 SMMLV, la fórmula "
            "cambia según lo estipulado en el mismo artículo. Adicionalmente, "
            "tiene derecho a la liquidación completa: cesantías, intereses sobre "
            "cesantías, prima de servicios, vacaciones proporcionales y salarios "
            "pendientes. Tiene 3 años para reclamar ante el juez laboral "
            "(artículo 488 CST). Le recomendamos consultar con un abogado "
            "laboralista para evaluar su caso específico."
        ),
        fuentes=[
            {"norma": "CST Art. 64", "descripcion": "Terminación unilateral del contrato e indemnizaciones"},
            {"norma": "CST Art. 488", "descripcion": "Prescripción de las acciones laborales (3 años)"},
        ]
    ),

    EntradaConocimiento(
        categoria="salario_minimo",
        palabras_clave=["salario mínimo", "salario minimo", "smlmv", "smmlv",
                        "cuánto gana", "cuanto gana", "salario", "pago",
                        "sueldo mínimo", "sueldo minimo"],
        respuesta=(
            "El salario mínimo mensual legal vigente (SMMLV) en Colombia para 2026 "
            "es de $1.423.500 pesos, más un auxilio de transporte de $201.963 para "
            "quienes devenguen hasta 2 SMMLV. Ningún empleador puede pagar menos de "
            "este valor por una jornada completa (artículo 145 del CST). Si trabaja "
            "medio tiempo, el salario puede ser proporcional. El incumplimiento de "
            "esta norma puede ser denunciado ante el Ministerio de Trabajo."
        ),
        fuentes=[
            {"norma": "CST Art. 145", "descripcion": "Salario mínimo legal"},
            {"norma": "Decreto 2654 de 2025", "descripcion": "Fijación del SMMLV para 2026"},
        ]
    ),

    EntradaConocimiento(
        categoria="jornada_laboral",
        palabras_clave=["horas", "jornada", "overtime", "horas extras", "extra",
                        "nocturno", "dominical", "festivo", "trabajo",
                        "cuántas horas", "cuantas horas", "horario"],
        respuesta=(
            "La jornada laboral ordinaria en Colombia es de 8 horas diarias y "
            "47 horas semanales (artículo 161 del CST, modificado por la Ley 2101 "
            "de 2021 que redujo progresivamente la jornada). Las horas extras "
            "diurnas (entre 6:00 a.m. y 9:00 p.m.) se pagan con un recargo del "
            "25 % sobre el valor hora ordinaria. Las horas extras nocturnas "
            "(entre 9:00 p.m. y 6:00 a.m.) tienen un recargo del 75 %. "
            "El trabajo dominical o en festivo tiene un recargo del 75 %. "
            "Nadie puede trabajar más de 2 horas extras al día ni más de 12 "
            "horas extras a la semana."
        ),
        fuentes=[
            {"norma": "CST Art. 161", "descripcion": "Jornada ordinaria de trabajo"},
            {"norma": "Ley 2101 de 2021", "descripcion": "Reducción progresiva de la jornada laboral"},
            {"norma": "CST Art. 168", "descripcion": "Recargos por trabajo nocturno, dominical y festivo"},
        ]
    ),

    EntradaConocimiento(
        categoria="cesantias",
        palabras_clave=["cesantías", "cesantias", "fondo de cesantías",
                        "retiro cesantías", "cesantia", "auxilio de cesantías"],
        respuesta=(
            "Las cesantías equivalen a 1 mes de salario por cada año trabajado "
            "(artículo 249 del CST). Su empleador debe consignarlas en el fondo "
            "de cesantías de su elección antes del 14 de febrero de cada año. "
            "Puede retirarlas parcialmente para compra o mejora de vivienda, "
            "o para pagar matrícula en educación superior. Al terminar el contrato, "
            "tiene derecho a retirarlas en su totalidad. Si el empleador no las "
            "consigna oportunamente, debe pagar un día de salario por cada día "
            "de retardo (artículo 65 del CST)."
        ),
        fuentes=[
            {"norma": "CST Art. 249", "descripcion": "Derecho a las cesantías"},
            {"norma": "CST Art. 65", "descripcion": "Indemnización moratoria por no pago de cesantías"},
            {"norma": "Ley 50 de 1990", "descripcion": "Régimen de cesantías con fondo privado"},
        ]
    ),

    EntradaConocimiento(
        categoria="vacaciones",
        palabras_clave=["vacaciones", "descanso", "días de vacaciones",
                        "vacaciones remuneradas", "cuántos días", "dias libres"],
        respuesta=(
            "Todo trabajador tiene derecho a 15 días hábiles de vacaciones "
            "remuneradas por cada año de trabajo (artículo 186 del CST). "
            "El empleador debe programarlas de acuerdo con las necesidades "
            "del servicio, pero no puede negarse a otorgarlas indefinidamente. "
            "Se pueden acumular hasta por 2 años. Si el contrato termina antes "
            "de completar el año, tiene derecho a vacaciones proporcionales. "
            "El empleador no puede compensar en dinero las vacaciones, excepto "
            "cuando el contrato termina antes de disfrutarlas."
        ),
        fuentes=[
            {"norma": "CST Art. 186", "descripcion": "Derecho a vacaciones remuneradas"},
            {"norma": "CST Art. 189", "descripcion": "Época de las vacaciones"},
        ]
    ),

    EntradaConocimiento(
        categoria="acoso_laboral",
        palabras_clave=["acoso", "hostigamiento", "maltrato", "bullying",
                        "acoso laboral", "presión laboral", "intimidación",
                        "humillación", "ley 1010"],
        respuesta=(
            "El acoso laboral está prohibido en Colombia por la Ley 1010 de 2006. "
            "Se define como toda conducta persistente y demostrable de un empleador "
            "o compañero de trabajo que busque infundir miedo, intimidar, o causar "
            "perjuicio laboral o desmejora en el trabajo. Si lo está sufriendo, "
            "puede: (1) presentar queja ante el Comité de Convivencia Laboral de "
            "su empresa, (2) denunciar ante el Inspector de Trabajo del Ministerio "
            "de Trabajo, o (3) presentar denuncia penal. Las conductas de acoso "
            "pueden generar multas para el acosador y, en casos graves, terminación "
            "con justa causa del contrato del agresor."
        ),
        fuentes=[
            {"norma": "Ley 1010 de 2006", "descripcion": "Medidas para prevenir y sancionar el acoso laboral"},
            {"norma": "CST Art. 62 lit. f", "descripcion": "Terminación con justa causa por acoso"},
        ]
    ),

    EntradaConocimiento(
        categoria="prima_servicios",
        palabras_clave=["prima", "prima de servicios", "prima de navidad",
                        "prima semestral", "cuándo se paga la prima",
                        "cuando se paga prima"],
        respuesta=(
            "La prima de servicios equivale a 15 días de salario y se paga "
            "dos veces al año: la primera entre el 1 y el 30 de junio, y la "
            "segunda entre el 1 y el 20 de diciembre (artículo 306 del CST). "
            "Si trabajó menos de un semestre completo, tiene derecho a la prima "
            "proporcional al tiempo laborado. La prima se liquida con base en el "
            "salario promedio del semestre. Si su empleador no la paga en los "
            "plazos establecidos, puede denunciar ante el Ministerio de Trabajo."
        ),
        fuentes=[
            {"norma": "CST Art. 306", "descripcion": "Prima de servicios"},
        ]
    ),

    EntradaConocimiento(
        categoria="contrato_trabajo",
        palabras_clave=["contrato", "tipo de contrato", "contrato indefinido",
                        "contrato fijo", "contrato a término", "contrato verbal",
                        "contrato escrito", "periodo de prueba"],
        respuesta=(
            "En Colombia existen varios tipos de contrato laboral. El contrato "
            "a término indefinido no tiene fecha de vencimiento y es el que más "
            "protección ofrece al trabajador. El contrato a término fijo tiene "
            "una duración determinada (máximo 3 años, renovable) y debe constar "
            "por escrito. El contrato de obra o labor termina cuando se finaliza "
            "la tarea específica. El período de prueba no puede superar 2 meses "
            "y debe pactarse por escrito; durante este período cualquiera de las "
            "partes puede terminar el contrato sin preaviso ni indemnización "
            "(artículo 78 del CST). Todo contrato, verbal o escrito, genera "
            "las mismas obligaciones para el empleador."
        ),
        fuentes=[
            {"norma": "CST Art. 45", "descripcion": "Clases de contrato de trabajo"},
            {"norma": "CST Art. 78", "descripcion": "Período de prueba"},
        ]
    ),

]

RESPUESTA_DEFAULT = EntradaConocimiento(
    categoria="orientacion_general",
    palabras_clave=[],
    respuesta=(
        "Gracias por tu consulta. En este momento Leya v1.0 está especializada "
        "en derecho laboral colombiano: contratos, salarios, jornadas, cesantías, "
        "vacaciones, primas, acoso laboral e indemnizaciones por despido. "
        "Si tu pregunta está relacionada con alguno de estos temas, intenta "
        "reformularla con más detalle. Para consultas sobre otras ramas del "
        "derecho (civil, penal, comercial), te recomendamos consultar con un "
        "abogado o visitar las Casas de Justicia de tu municipio."
    ),
    fuentes=[
        {"norma": "CST — Código Sustantivo del Trabajo",
         "descripcion": "Normativa laboral colombiana vigente"},
    ]
)


def buscar_respuesta(pregunta: str) -> EntradaConocimiento:
    pregunta_lower = pregunta.lower()
    mejor_puntaje  = 0
    mejor_entrada  = None

    for entrada in BASE_CONOCIMIENTO:
        puntaje = sum(1 for kw in entrada.palabras_clave if kw.lower() in pregunta_lower)
        if puntaje > mejor_puntaje:
            mejor_puntaje = puntaje
            mejor_entrada = entrada

    return mejor_entrada if mejor_entrada else RESPUESTA_DEFAULT
