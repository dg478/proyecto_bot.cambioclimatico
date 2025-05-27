import random

preguntas = [
    {
        "pregunta": "¿Cuál de los siguientes fenómenos es un efecto del cambio climático?",
        "opciones": [
            "A: Aumento en la frecuencia de inundaciones",
            "B: Incremento de eventos de tornados",
            "C: Prolongadas sequías",
            "D: Todas las anteriores"
        ],
        "respuesta": "D",
        "explicacion": "El cambio climático influye en todos estos fenómenos."
    },
    {
        "pregunta": "¿Qué gas de efecto invernadero es el más abundante en la atmósfera?",
        "opciones": [
            "A: Dióxido de carbono (CO2)",
            "B: Metano (CH4)",
            "C: Vapor de agua (H2O)",
            "D: Óxido nitroso (N2O)"
        ],
        "respuesta": "C",
        "explicacion": "El vapor de agua es el gas de efecto invernadero más abundante en la atmósfera."
    },
    {
        "pregunta": "¿Cuál es una de las principales causas del cambio climático?",
        "opciones": [
            "A: La rotación de la Tierra",
            "B: La quema de combustibles fósiles",
            "C: El ciclo lunar",
            "D: La fotosíntesis de las plantas"
        ],
        "respuesta": "B",
        "explicacion": "La quema de combustibles fósiles es una de las principales causas del cambio climático."
    },
    {
        "pregunta": "¿Cuál de las siguientes es una causa principal del cambio climático?",
        "opciones": [
            "A: El movimiento de las placas tectónicas",
            "B: El uso de combustibles fósiles ",
            "C: Las fases lunares",
            "D: La rotación de la Tierra"
        ],
        "respuesta": "B",
        "explicacion": "Quemar combustibles fósiles libera gases que calientan el planeta."
    },
    {
        "pregunta": "¿Cuál es una de las consecuencias más visibles del cambio climático?",
        "opciones": [
            "A: El aumento de la productividad agrícola",
            "B: La disminución del nivel del mar",
            "C: Las lluvias de estrellas",
            "D: Fenómenos extremos como huracanes y sequías"
        ],
        "respuesta": "D",
        "explicacion": " El cambio climático hace más fuertes y frecuentes estos desastres."
    },
    {
        "pregunta": "¿Cómo afecta el cambio climático a la sociedad?",
        "opciones": [
            "A: Reduce la desigualdad entre países",
            "B: Genera migraciones y afecta a los más vulnerables ",
            "C: Mejora la salud pública",
            "D: Facilita el acceso al agua potable"
        ],
        "respuesta": "B",
        "explicacion": " Las personas pobres o en zonas de riesgo sufren más sus efectos."
    }
]

def obtener_pregunta_aleatoria():
    return random.choice(preguntas)