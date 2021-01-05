from django import forms
from djchoices import DjangoChoices, ChoiceItem


class RiskProfileTestForm(forms.Form):
    age = forms.IntegerField(min_value=18, max_value=65, label="Su edad")
    liquid_assets = forms.IntegerField(min_value=100, label="Total de sus activos liquidos", help_text="")
    net_annual_income = forms.IntegerField(min_value=1)
    initial_contribution = forms.IntegerField(min_value=500)

    class ExpectedReturn(DjangoChoices):
        conservative = ChoiceItem(label="Mínimo riesgo",
                                  help_text="Minimizar el riesgo en detrimento de la rentabilidad.",
                                  value="conservative")
        aggresive = ChoiceItem(label="Máxima rentabilidad",
                               help_text="Priorizar la rentabilidad sin importar el riesgo.",
                               value="aggresive")
        low = ChoiceItem(label="Entre el 1% y el 2% anual.",
                         help_text="Mitigar la inflación y buscar la estabilidad patrimonial.",
                         value="low")
        medium = ChoiceItem(label="Entre el 3% y el 4% anual.",
                            help_text="Buscar el equilibrio entre estabilidad y crecimiento patrimonial.",
                            value="medium")
        high = ChoiceItem(label="Entre el 5% y el 6% anual.",
                          help_text="Buscar el crecimiento patrimonial asumiendo un nivel de riesgo superior.",
                          value="high")

    class AttitudeToLosses(DjangoChoices):
        sell_all = ChoiceItem()
        limit_sell = ChoiceItem()
        hold = ChoiceItem()
        buy = ChoiceItem()

    class InvestmentExperience(DjangoChoices):
        experienced = ChoiceItem()
        inexperienced = ChoiceItem()
        some_knowledge = ChoiceItem()

    class IncomeStability(DjangoChoices):
        very_steady = ChoiceItem()
        stable = ChoiceItem()
        unstable = ChoiceItem()

    class MonthlyExpenses(DjangoChoices):
        percentile_25 = ChoiceItem()
        percentile_50 = ChoiceItem()
        percentile_75 = ChoiceItem()
        percentile_90 = ChoiceItem()

    class InvestmentTime(DjangoChoices):
        less_1_yr = ChoiceItem()
        from_2_to_5_yrs = ChoiceItem()
        from_5_to_10_yrs = ChoiceItem()
        more_10_yrs = ChoiceItem()

    expected_return = forms.ChoiceField(choices=ExpectedReturn.choices, widget=forms.RadioSelect,
                                        label="¿Qué rentabilidad buscas para tu cartera de inversión?")
    attitude_to_losses = forms.ChoiceField(choices=AttitudeToLosses.choices, widget=forms.RadioSelect)
    investment_experience = forms.ChoiceField(choices=InvestmentExperience.choices, widget=forms.RadioSelect)
    monthly_expenses = forms.ChoiceField(choices=MonthlyExpenses.choices, widget=forms.RadioSelect)
    investment_time = forms.ChoiceField(choices=InvestmentTime.choices, widget=forms.RadioSelect)
