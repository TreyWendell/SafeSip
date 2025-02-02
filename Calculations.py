def CalculateBAC(level, hours):
    bac = None
    #1. Really?
    #2. BAC 0.01–0.04: Altered reaction time, judgment, and behavior. Feeling of wellbeing: Talkative, more relaxed, and more confident
    #3. BAC 0.05–0.06 Relaxed and confident feelings, slightly impaired reasoning and memory
    #4. BAC 0.07 Relaxed and confident feelings, slightly impaired reasoning and memory
    #5. BAC 0.08-.010: Impaired judgment and reduced inhibitions 
    #6. BAC 0.11–0.25: Blurred vision, lack of control
    #7. BAC 0.12-0.14: Speech may be slurred
    #8. BAC 0.15–0.18: Dysphoria will become stronger, and nausea may occur
    #9. BAC 0.19-0.21
    #10.BAC 0.22–0.30: Confused—might not know where they are or what they are saying
    #BAC = [Alcohol consumed in grams / (Body weight in grams x R)] X 100     # Subliminal intoxication 
    #ALC consumer in grams = (BAC * WIG * R) / 100
    #R: is a gender-specific constant, with a value of 0.55 for females and 0.68 for males 
    
    match level:
        
        case 1:
            bac = 0.02
        case 2:
            bac = 0.03
        case 3:
            bac = 0.05
        case 4:
            bac = 0.07
        case 5:
            bac = 0.08
        case 6:
            bac = 0.11
        case 7:
            bac = 0.12
        case 8:
            bac = 0.15
        case 9:
            bac = 0.19
        case 10:
            bac = 0.22
    bac = bac + ((hours - 1) * .015)
    return bac

def CalculateDrinks(weight, gender, bac):

    if (gender == "m" or gender =="M"):
        R = .68

    if (gender == "f" or gender =="F"):
        R = .55
    
    weightInGrams = 453.6 * weight
    alcInGrams = (bac * weightInGrams * R) / 100
    drinks = alcInGrams / 14
    return round(drinks,1)


def CalculateHoursTillLegal(bac):
    if bac < .08:
        return 0.0
    else:
        return  (bac - .08) / 0.015