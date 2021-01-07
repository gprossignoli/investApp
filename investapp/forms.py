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
