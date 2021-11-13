
#Oppgave 2 Mappeinnlevering nr 2 for MAT611

#Lag et program i Python som regner ut BMI:

def main():
    bmi = getBMI()
    
    while bmi<0:
        bmi = getBMI()

    Tabell = tabell(bmi)


    
# beregne BMI kg/m^2

def getBMI():
    kg = round(float(input('Skriv inn hvor mange kg du veier ' )),2)
    print()
    cm = float(input('Skriv inn din høyde i cm ' ))
    print()
    if cm >=0 and cm <= 215 and kg >=0:
        meter = cm/100
     
        bmi = round(float(kg/meter**2),2)
        
        print('Din BMI er',bmi)
        

    else:
        print('Du har tastet feil, skriv inn din vekt i kg og din høyde i cm.')
        print('Husk at desimaltall skrives med punktum i stedet for komma.')
              
        bmi = -1
    return bmi


#a) Sammenlign din BMI med tabell
def tabell(bmi):
    undervekt = 18.5
    normalvekt = 25
    overvekt = 30
    
    
    if bmi <= undervekt:
        print('Med BMI på',round(float(bmi),2),'er du undervektig og kan få helseprobelemer.')
              

    elif bmi >= undervekt and bmi <= normalvekt:
        print('Med BMI på',round(float(bmi),2),'er har du normal vekt, og lav risiko for helseprobelemer.') 

    elif bmi >= normalvekt and bmi <= overvekt:
        print('Med BMI på',round(float(bmi),2),'er du overvektig og kan få diabetes og andre helseprobelemer.')

    elif bmi >=overvekt:
        print('Med BMI på',round(float(bmi),2),'har du fedme og økt risiko for diabetes og andre få helseprobelemer.') 
 
    return bmi

def showBMI():
    print('BMI står for Body Mass Index og gir deg et tall som forteller om du er over-, under- eller normal vektig. BMI skiller ikke på muskel eller fettmasse')
    input()

print('Vil du lese om hva BMI er ? (ja/nei)')
if input().lower().startswith('j'):
    showBMI()    
    
main()
