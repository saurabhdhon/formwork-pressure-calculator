"""Formwork lateral pressure calculator.

Estimates the maximum lateral pressure on formwork for concrete
placement using the ACI 347 formula for pour rates up to 7 ft/hr.
"""

def calculate_pressure(rate_ft_per_hr, temp_f, pour_height_ft):
  """Return the design lateral pressure in psf.

  rate_ft_per_hr: rate of concrete placement, in feet per hour
  temp_f: temperature of the concrete in the forms, in Fahrenheit
  pour_height_ft: total height of the pour, in feet
  """
  pressure = 150 + (9000 * rate_ft_per_hr) / (temp_f + 17.8)
  hydrostatic_cap = 150 * pour_height_ft
  max_pressure = min(pressure, hydrostatic_cap, 3000)
  return max_pressure

def main():
  print("Formwork Lateral Pressure Calculator (ACI 347 reference)")
  rate = float(input("Pour rate (ft/hr): "))
  temp = float(input("Concrete temperature (deg F): "))
  height = float(input("Total pour height (ft): "))


  result = calculate_pressure(rate, temp, height)
  print(f"Estimated design pressure: {result:.1f} psf")

if __name__ == "__main__":
  main()
