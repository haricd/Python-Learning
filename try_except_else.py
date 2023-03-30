def cal_bmi(height, weight):
    return  weight / height**2

def evaluate_bmi(bmi):
    if 18.5 <= bmi <= 25.3:
        return 'healthy'
    if bmi >= 25:
        return 'overweight'

    return 'underweight'

def main():
    try:
        height = float(input('Enter your height (meters):'))
        weight = float(input('Enter your weight (kilograms):'))

    except Exception as error:
        print(error)
    else:
        bmi = round(cal_bmi(height, weight), 1)
        evaluation = evaluate_bmi(bmi)

        print(f'Your body mass index is {bmi}')
        print(f'This is considered {evaluation}!')

main()
