from django.shortcuts import render
from .forms import MenstrualTrackingForm, SymptomTrackingForm
from .models import MenstrualTracking
from datetime import timedelta

def home(request):
    next_period_date = None
    if request.method == 'POST':
        menstrual_form = MenstrualTrackingForm(request.POST)
        symptom_form = SymptomTrackingForm(request.POST)

        if menstrual_form.is_valid():
            cycle_length = menstrual_form.cleaned_data['cycle_length']
            last_period_start = menstrual_form.cleaned_data['last_period_start']

            # Save data
            MenstrualTracking.objects.create(
                cycle_length=cycle_length,
                last_period_start=last_period_start,
            )

            # Calculate next period date
            next_period_date = last_period_start + timedelta(days=cycle_length)

    else:
        menstrual_form = MenstrualTrackingForm()
        symptom_form = SymptomTrackingForm()

    return render(request, 'cycletracker/home.html', {
        'menstrual_form': menstrual_form,
        'symptom_form': symptom_form,
        'next_period_date': next_period_date,
    })
