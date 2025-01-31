from django import forms

class MenstrualTrackingForm(forms.Form):
    cycle_length = forms.IntegerField(label="Cycle Length (in days)")
    last_period_start = forms.DateField(label="Last Period Start Date",
                                        widget=forms.DateInput(attrs={'type': 'date'}))

class SymptomTrackingForm(forms.Form):
    cramps = forms.ChoiceField(choices=[
        ('None', 'None'), ('Mild', 'Mild'), ('Moderate', 'Moderate'), ('Severe', 'Severe')
    ], label="Cramps")
    mood = forms.ChoiceField(choices=[
        ('Happy', 'Happy'), ('Neutral', 'Neutral'), ('Irritable', 'Irritable'),
        ('Anxious', 'Anxious'), ('Sad', 'Sad')
    ], label="Mood")
    trained_today = forms.BooleanField(label="Did you train today?", required=False)
    performance_rating = forms.IntegerField(label="Performance Rating (1-5)",
                                            min_value=1, max_value=5, required=False)
