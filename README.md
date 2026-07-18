# formwork-pressure-calculator
A simple reference tool to estimate lateral pressure on concrete formwork during placement, based on the ACI 347 approach.


## Formula

This tool uses the ACI 347 recommended formula for lateral pressure on formwork for concrete columns and walls with a pour rate less than 7 ft/hr:

P = 150 + (9000 * R) / (T + 17.8)

Where:

- P = maximum lateral pressure (psf)
- R = rate of concrete placement (ft/hr)
- T = temperature of concrete in the forms (deg F)

The result is capped at a maximum hydrostatic pressure of 150 times the pour height, or 3000 psf, whichever governs.

## Usage

Run the script with Python 3 and follow the prompts for pour rate and concrete temperature:

```
python formwork_pressure.py
```

## Disclaimer

This is a simplified educational reference based on published ACI 347 guidance. It is not a substitute for a project specific engineering analysis or professional judgment.
