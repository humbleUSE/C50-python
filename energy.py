# Funtion to calculate the energy of a particle
def mass_to_joules():

  # Prompt user for mass
  mass = int(input("Enter the mass: "))
  c = 3 * (10**8)

  # Calculate energy
  joules = mass * (c**2)
  print(f"The energy is {joules} joules.")

  return joules


if __name__ == "__main__":
  mass_to_joules()
