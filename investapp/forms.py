from django import forms
from djchoices import DjangoChoices, ChoiceItem


class RiskProfileTestForm(forms.Form):
    class Question1(DjangoChoices):
        a = ChoiceItem(label="Un amante del riesgo.",
                       value="4")
        b = ChoiceItem(label="Alguien dispuesto a tomar riesgos después de una investigación adecuada.",
                       value="3")
        c = ChoiceItem(label="Una persona cautelosa.",
                       value="2")
        d = ChoiceItem(label="Una persona que evita el riesgo a toda costa.",
                       value="1")

    class Question2(DjangoChoices):
        a = ChoiceItem(label="Ganar 1.000€.",
                       value="1")
        b = ChoiceItem(label="Una probabilidad del 50% de ganar 5.000€.",
                       value="2")
        c = ChoiceItem(label="Una probabilidad del 25% de ganar 10.000€.",
                       value="3")
        d = ChoiceItem(label="Una probabilidad del 5% de ganar 100.000€.",
                       value="4")

    class Question3(DjangoChoices):
        a = ChoiceItem(label="Cancelar las vacaciones.",
                       value="1")
        b = ChoiceItem(label="Reducir los planes para recortar gastos.",
                       value="2")
        c = ChoiceItem(label="Seguir con el plan, ya que utilizará ese tiempo para preparar su búsqueda "
                             "de un nuevo empleo.",
                       value="3")
        d = ChoiceItem(label="Extender sus vacaciones, ya que estas podrían ser sus últimas vacaciones a lo grande.",
                       value="4")

    class Question4(DjangoChoices):
        a = ChoiceItem(label="Cierto.",
                       value="1")
        b = ChoiceItem(label="Podría ser.",
                       value="2")
        c = ChoiceItem(label="En absoluto.",
                       value="3")

    class Question5(DjangoChoices):
        a = ChoiceItem(label="Depositarlos en una cuenta de ahorro o invertir en deuda de corto plazo (Money Market).",
                       value="1")
        b = ChoiceItem(label="Invertir en bonos de alta calidad o fondos de inversión de bonos.",
                       value="2")
        c = ChoiceItem(label="Invertir en acciones o fondos de inversión de acciones.",
                       value="3")

    class Question6(DjangoChoices):
        a = ChoiceItem(label="Me genera incomodidad.",
                       value="1")
        b = ChoiceItem(label="Me siento más o menos cómodo.",
                       value="2")
        c = ChoiceItem(label="Me siento bastante confiado.",
                       value="3")

    class Question7(DjangoChoices):
        a = ChoiceItem(label="Ganar 50.000€ en un concurso.",
                       value="2")
        b = ChoiceItem(label="Heredar 50.000€ de un pariente rico.",
                       value="1")
        c = ChoiceItem(label="Ganar 50.000€ habiendo arriesgado 1.000€ en el mercado de acciones.",
                       value="3")
        d = ChoiceItem(label="Cualquiera de las anteriores está bien, en cualquier caso, ha ganado 50.000€.",
                       value="1")

    class Question8(DjangoChoices):
        a = ChoiceItem(label="Pérdidas.",
                       value="1")
        b = ChoiceItem(label="Incertidumbre.",
                       value="2")
        c = ChoiceItem(label="Oportunidad.",
                       value="3")
        d = ChoiceItem(label="Emoción.",
                       value="4")

    class Question9(DjangoChoices):
        a = ChoiceItem(label="Vender la casa.",
                       value="1")
        b = ChoiceItem(label="Alquilar sin reparación.",
                       value="2")
        c = ChoiceItem(label="Arreglarla y alquilarla después.",
                       value="3")

    class Question10(DjangoChoices):
        a = ChoiceItem(label="Es más importante asegurar mi dinero evitando pérdidas o robos.",
                       value="1")
        b = ChoiceItem(label="Es más importante estar protegido frente a la inflación.",
                       value="3")

    class Question11(DjangoChoices):
        a = ChoiceItem(label="Garantizar el empleo por 5 años.",
                       value="1")
        b = ChoiceItem(label="Un bonus de 25.000€.",
                       value="2")
        c = ChoiceItem(label="Acciones de la compañía por valor de 25.000€ "
                             "con la intención de venderlas a mayor valor más tarde.",
                       value="3")

    class Question12(DjangoChoices):
        a = ChoiceItem(label="Mantener los bonos.",
                       value="1")
        b = ChoiceItem(label="Vender los bonos, invertir la mitad de las ganancias en deuda a corto plazo (Money Market),"
                             " y la otra mitad en bienes tangibles.",
                       value="2")
        c = ChoiceItem(label="Vender los bonos y utilizar todas las ganancias en bienes tangibles.",
                       value="3")
        d = ChoiceItem(label="Vender los bonos y utilizar todas las ganancias además de dinero adicional "
                             "en bienes tangibles.",
                       value="4")

    class Question13(DjangoChoices):
        a = ChoiceItem(label="Comprar una casa que le permita pagar las mensualidades de la hipoteca de forma cómoda.",
                       value="1")
        b = ChoiceItem(label="Comprar la casa que realmente le gusta, aunque tenga que apretarse el cinturón.",
                       value="2")
        c = ChoiceItem(label="Comprar la casa más cara que pueda permitirse.",
                       value="3")
        d = ChoiceItem(label="Pedir algo de dinero a amigos y familia para poder obtener una hipoteca mayor.",
                       value="4")

    class Question14(DjangoChoices):
        a = ChoiceItem(label="200€ de ganancias en el mejor caso, ninguna pérdida en el peor caso.",
                       value="1")
        b = ChoiceItem(label="800€ de ganancias en el mejor caso, 200€ de pérdidas en el peor caso.",
                       value="2")
        c = ChoiceItem(label="2.600€ de ganancias en el mejor caso, 800€ de pérdidas en el peor caso.",
                       value="3")
        d = ChoiceItem(label="4.800€ de ganancias en el mejor caso, 2.400€ de pérdidas en el peor caso.",
                       value="4")

    q1 = forms.ChoiceField(choices=Question1.choices, widget=forms.RadioSelect,
                           label="¿Cómo cree que le describiría su mejor amigo en cuanto a la toma de riesgos?")

    q2 = forms.ChoiceField(choices=Question2.choices, widget=forms.RadioSelect,
                           label="Está participando en un concurso y debe escoger una de las siguientes opciones, "
                                 "¿Cúal escogería?")

    q3 = forms.ChoiceField(choices=Question3.choices, widget=forms.RadioSelect,
                           label="Acaba de terminar de ahorrar para unas vacaciones de lujo. "
                                 "A tres semanas antes de irse, pierde su empleo, ¿Qué haría?")

    q4 = forms.ChoiceField(choices=Question4.choices, widget=forms.RadioSelect,
                           label="Considere la siguiente afirmación, 'Es difícil que deje pasar una oferta.'")

    q5 = forms.ChoiceField(choices=Question5.choices, widget=forms.RadioSelect,
                           label="Recibe 20.000€ para dedicarlos a inversión, ¿qué haría?")

    q6 = forms.ChoiceField(choices=Question6.choices, widget=forms.RadioSelect,
                           label="A la hora de invertir en acciones o fondos de acciones, ¿Cómo de cómodo se siente?")

    q7 = forms.ChoiceField(choices=Question7.choices, widget=forms.RadioSelect,
                           label="¿Cuál de las siguientes situaciones le daría más alegría?")

    q8 = forms.ChoiceField(choices=Question8.choices, widget=forms.RadioSelect,
                           label="¿Qué idea le evoca la palabra 'riesgo'?")

    q9 = forms.ChoiceField(choices=Question9.choices, widget=forms.RadioSelect,
                           label="Ha heredado una propiedad libre de cargas con un valor de 200.000€. "
                                 "Usted espera que su valor aumente más rápido que la inflación, "
                                 "sin embargo, necesita arreglos. Si la alquila ahora, recibirá 600€ mensuales, "
                                 "pero si la arregla antes, serán 800€. Para financiar los arreglos, "
                                 "tendría que hipotecarla, ¿que haría?")

    q10 = forms.ChoiceField(choices=Question10.choices, widget=forms.RadioSelect,
                           label="¿Cuál de las dos afirmaciones es más importante para usted?")

    q11 = forms.ChoiceField(choices=Question11.choices, widget=forms.RadioSelect,
                            label="Consigue empleo en una 'start-up' de rápido crecimiento. "
                                  "Tras el primer año se le ofrecen las siguientes opciones, ¿cuál escogería?")

    q12 = forms.ChoiceField(choices=Question12.choices, widget=forms.RadioSelect,
                            label="Algunos expertos predicen que el valor de los bonos podría caer mientras que el valor"
                                  " de activos como el oro o los bienes inmobiliarios (bienes tangibles),"
                                  " incrementarán su valor. Por otro lado, la mayoría de los expertos coinciden en que"
                                  " los bonos estatales son bastante seguros. La mayoría de su cartera está formada por "
                                  "bonos estatales. ¿Qué haría?")

    q13 = forms.ChoiceField(choices=Question13.choices, widget=forms.RadioSelect,
                            label="Está planeando comprar una casa en las próximas semanas, ¿qué estrategia seguiría?")

    q14 = forms.ChoiceField(choices=Question14.choices, widget=forms.RadioSelect,
                            label="¿Cuál de las siguientes 4 inversiones prefiere?")