try:
    h1 = input('Enter your height(in metres): ')
    height = float(h1)
except:
    print("Invalid input, try again")
    h1 = input('Enter your height(in metres): ')
    height = float(h1)

try:
    m1 = input('Enter your mass(in kg): ')
    mass = float(m1)
except:
    print("Invalid input, try again!")
    m1 = input('Enter your mass(in kg): ')
    mass = float(m1)

bmi = mass/(height**2)

if bmi < 18.5:
    info = 'under weight'
elif bmi >= 18.5 and bmi <= 24.9:
    info = 'normal weight'
elif bmi >= 25 and bmi <= 29.9:
    info = 'over weight'
elif bmi >= 30:
    info = 'obese'

print('\n')
print('Your BMI is {0} and you are {1}'.format(round(bmi, 4), info))
