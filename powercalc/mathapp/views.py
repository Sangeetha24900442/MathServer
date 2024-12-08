from django.shortcuts import render

def power(request):
    # Default context for rendering the form
    context = {
        'current': '0',  # Default input for current
        'resistance': '0',  # Default input for resistance
        'power': '0',  # Default calculated power
    }
    
    # Process form submission
    if request.method == 'POST':
        # Get user inputs from the form
        current = request.POST.get('current', '0')
        resistance = request.POST.get('resistance', '0')

        try:
            # Convert inputs to float
            current = float(current)
            resistance = float(resistance)

            # Calculate power: P = I²R
            power = current ** 2 * resistance
            context['power'] = round(power, 2)  # Add calculated power to context

        except ValueError:
            # Handle invalid input
            context['error'] = "Please enter valid numeric values for current and resistance."
            print("Received POST data:", request.POST)

    
    return render(request, 'mathapp/math.html', context)