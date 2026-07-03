#Command Calc

#Welcome
txt1='''                           WELCOME TO COMMAND CALC
                            - Legacy Edition.
                                  
                 
Powered by Python                                           ©Illektron Softwares
================================================================================== 
'''

print(txt1)

#General instructions


txt2='''
General Instructions:-
  i). To Execute the Operation press '=' in the Operation section.
  ii). Do not Forget to Press 'ENTER' Everytime you Enter an Input.
  iii). Restart the Program for Another Calculation.

IMPORTANT NOTICE:-

   *The 'π'(Pi) Symbol is not Recognized. Please Enter 3.14 for 'π'.*
   **Scientific Terms are Not Available.**
   ***The Required Answer Will be Shown in Decimal Format.***
   ****If the Calculator Fails to Provide the Solution on Command Prompt,
       please Install Python and Run it on IDLE****
__________________________________________________________________________________        
'''

txt2_1='''
Thanks... Please Proceed.
'''

prompt=input('''Type 'Start' or Type 'Infostart' to view General instructions and start
Your Answer: ''')

if prompt=='start':
  print(txt2_1)
  
elif prompt=='Start':
    print(txt2_1)

elif prompt=='START':
    print(txt2_1)
    
elif prompt=='INFOSTART':
    print(txt2)

elif prompt=='infostart':
    print(txt2)
    
elif prompt=='InfoStart':
    print(txt2)
    
elif prompt=='Infostart':
    print(txt2)
else:
    print("System Would Consider it as 'Start'. ",txt2_1)

#Import Functions

import math
import statistics

#Choose Modes

print('''Please select your Mode:-

1.Basic Calculator.
2.Exponential Operations.
3.Factorials.
4.Basic Trigonometry.
5.Statistics(Minimal Features).
6.Interests.
7.Multiplication Table.
8.Basic Geometry.

''')
mode=input("Enter the Mode: ")
      
if mode=='1':
      
  #Instructions 1

   txt3='''
   Instructions:-

   i). Enter a Number in Integer Form or Decimal Form.
   ii). Enter the Required Operation.

        For Operations,

         Addition:'+'           Subtraction:'-'
         Multiplication:'x'     Division:'/'

   GOOD LUCK!!!

   '''
   txt4='''
   GOOD LUCK!!!

   '''
   
   guide=input("Do you Want to View Instructions? (Yes/No): ")

   if guide=='yes':
     print(txt3)
  
   elif guide=='Yes':
       print(txt3)

   elif guide=='YES':
       print(txt3)
    
   elif guide=='no':
       print(txt4)
    
   elif guide=='No':
       print(txt4)
    
   elif guide=='NO':
       print(txt4)
    
   else:
       print("System Would Consider it as 'NO'. ",txt4)
    
   #Main Program 1

   res=float(input("Enter a Number: "))

   while True:
        o=input("Enter Operator: ")

        if o=='=':
          print('''
  Solution:''',res)
          print('''
          Please Restart for Another Calculation.

               Thanks For Using Our App.''')
          break

        num=float(input("Enter a Number: "))

        if o=='+':
          res += num

        elif o=='-':
            res -= num

        elif o=='x':
            res *= num

        elif o=='*':
            res *= num


        elif o=='/':
            if num != 0:
              res /= num

            else:
                print("Not Defined...")

        else:
            print("Invalid operator.... Please Restart the Program to Continue.")
            break

elif mode=='2':

    #Choice 1
    print('''
Enter the Type of Operation:-

1.Square and Cube Roots.
2.Raise to Exponential Form.

    ''')
    
    mode1=input("Enter Your Choice: ")

    if mode1=='1':
       #Instructions 2
      
       txt5='''Instructions:-

       For Operations,

          Square Root:'sqrt'
          Cube Root:'cbrt'
     
       GOOD LUCK!!!!

       '''
       txt6='''
       GOOD LUCK!!!

   '''
       guide1=input("Do you Want to View Instructions? (Yes/No): ")

       if guide1=='yes':
         print(txt5)
  
       elif guide1=='Yes':
           print(txt5)

       elif guide1=='YES':
           print(txt5)
    
       elif guide1=='no':
           print(txt6)
    
       elif guide1=='No':
           print(txt6)
    
       elif guide1=='NO':
           print(txt6)
     
       else:
           print("System Would Consider it as 'NO'. ",txt6)
           

       #Main Program 2
        
       num1=int(input("Enter the number: "))
       o1=input("Enter the operation: ")

       if o1=='sqrt':
         print('''
   Square Root: ''',math.sqrt(num1))

       elif o1=='Sqrt':
           print('''
   Square Root: ''',math.sqrt(num1))
           
       elif o1=='SQRT':
           print('''
   Square Root: ''',math.sqrt(num1))
        
       elif o1=='cbrt':
           print('''
   Cube Root: ''',math.cbrt(num1))

       elif o1=='CBRT':
           print('''
   Cube Root: ''',math.cbrt(num1))

       elif o1=='Cbrt':
           print('''
   Cube Root: ''',math.cbrt(num1))

           
       else:
           print("Invalid operator.... Please Restart the Program to Continue.")

       print('''
       Please Restart for Another Calculation.

            Thanks For Using Our App.''')
       

    elif mode1=='2':

        #Instructions 3

        txt7='''Instructions:-

        Enter the Value of Number and Power to the
        Respective Directories.

        GOOD LUCK!!!!

        '''

        txt8='''
        GOOD LUCK!!!!

        '''
        
        guide2=input("Do you Want to View Instructions? (Yes/No): ")

        if guide2=='yes':
          print(txt7)
  
        elif guide2=='Yes':
            print(txt7)

        elif guide2=='YES':
            print(txt7)
    
        elif guide2=='no':
            print(txt8)
    
        elif guide2=='No':
            print(txt8)
    
        elif guide2=='NO':
            print(txt8)
     
        else:
            print("System Would Consider it as 'NO' ",txt8)
            
        #Main Program 3
            
        num2=float(input("Enter the Number: "))
        pwr1=float(input("Enter the Power: "))
          
        print('''
   Solution:''',pow(num2,pwr1))
        print('''
        Please Restart for Another Calculation.

            Thanks For Using Our App.''')

    else:
        print("INVALID CHOICE.... Please Restart the Program to Continue.")
      
elif mode=='3':

    #Instructions 4

    txt9='''Instructions:-

    Enter the Number to Find its Factorial.

    GOOD LUCK!!!!

     '''

    txt10='''
    GOOD LUCK!!!!

        '''
    guide3=input("Do you Want to View Instructions? (Yes/No): ")

    if guide3=='yes':
      print(txt9)
  
    elif guide3=='Yes':
        print(txt9)

    elif guide3=='YES':
        print(txt9)
    
    elif guide3=='no':
        print(txt10)
    
    elif guide3=='No':
        print(txt10)
    
    elif guide3=='NO':
        print(txt10)
     
    else:
        print("System Would Consider it as 'NO'. ",txt10)
            
    #Main Program 4
        
    num3=int(input("Enter the Number: "))
    print('''
   Factorial of''',num3,": ",math.factorial(num3))
    print('''
    Please Restart for Another Calculation.

       Thanks For Using Our App.''')

elif mode=='4':

    #Instructions 4

    txt11='''Instructions:-

    i)Enter the Angle
    ii)for operations,

         Type Sin, Cos, Tan, Cosec, Sec or Cot in the Operation Section.
      
    IMPORTANT NOTICE:-

        *The Solutions shown Below are in Decimal Format and Not
                in Rational Numbers.*
 
    GOOD LUCK!!!!

     '''

    txt12='''
    GOOD LUCK!!!!

        '''
    
    guide4=input("Do you Want to View Instructions? (Yes/No): ")

    if guide4=='yes':
      print(txt11)
  
    elif guide4=='Yes':
        print(txt11)

    elif guide4=='YES':
        print(txt11)
    
    elif guide4=='no':
        print(txt12)
    
    elif guide4=='No':
        print(txt12)
    
    elif guide4=='NO':
        print(txt12)
     
    else:
        print("System Would Consider it as 'NO'. ",txt12)
            
    #Main Program 4

    num4=float(input("Enter the Angle: "))
    ang=math.radians(num4)
    o2=input("Enter the Trigonometric Function: ")

    if o2=='sin':
      print("Sin",num4,":",math.sin(ang))

    elif o2=='SIN':
        print("Sin",num4,":",math.sin(ang))

        
    elif o2=='Sin':
        print("Sin",num4,":",math.sin(ang))

    elif o2=='COS':
        print("Cos",num4,":",math.cos(ang))

    elif o2=='Cos':
        print("Cos",num4,":",math.cos(ang))

    elif o2=='cos':
        print("Cos",num4,":",math.cos(ang))
        
    elif o2=='TAN':
        print("Tan",num4,":",math.tan(ang))

    elif o2=='Tan':
        print("Tan",num4,":",math.tan(ang))

    elif o2=='tan':
        print("Tan",num4,":",math.tan(ang))

    elif o2=='cosec':
        print("Cosec",num4,":",1/math.sin(ang))

    elif o2=='COSEC':
        print("Cosec",num4,":",1/math.sin(ang))

    elif o2=='Cosec':
        print("Cosec",num4,":",1/math.sin(ang))

    elif o2=='sec':
        print("Sec",num4,":",1/math.cos(ang))

    elif o2=='Sec':
        print("Sec",num4,":",1/math.cos(ang))

    elif o2=='SEC':
        print("Sec",num4,":",1/math.cos(ang))

    elif o2=='cot':
        print("Cot",num4,":",1/math.tan(ang))

    elif o2=='COT':
        print("Cot",num4,":",1/math.tan(ang))
        
    elif o2=='Cot':
        print("Cot",num4,":",1/math.tan(ang))

    else:
        print("Invalid operator.... Please Restart the Program to Continue.")

    print('''
       Please Restart for Another Calculation.

            Thanks For Using Our App.''')

elif mode=='5':

    #Instructions 5

    txt13='''Instructions:-

    i)Enter the Numbers as in Format:
           2 4 56.4 234 
    ii)for operations,

         Type Mean, Median, Mode, Variance or Standard Deviation
         in the Operation Section.

         
    IMPORTANT NOTICE:-

        *Please Note that this statistics Mode is Only For Raw/Ungrouped Data.*
                  eg:- 6,5,3,7,28,4,34,5,11,56.

        
    GOOD LUCK!!!!

     '''

    txt14='''
    GOOD LUCK!!!!

        '''
    
    guide5=input("Do you Want to View Instructions? (Yes/No): ")

    if guide5=='yes':
      print(txt13)
  
    elif guide5=='Yes':
        print(txt13)

    elif guide5=='YES':
        print(txt13)
    
    elif guide5=='no':
        print(txt14)
    
    elif guide5=='No':
        print(txt14)
    
    elif guide5=='NO':
        print(txt14)
     
    else:
        print("System Would Consider it as 'NO'. ",txt14)
            
    #Main Program 5

    statinp=input("Enter the Data With Spaces: ")
    statdata=list(map(float, statinp.split()))
    o3=input("Enter the Operation: ")

    if o3=='mean':
      print("Mean: ",statistics.mean(statdata))

    elif o3=='Mean':
        print("Mean: ",statistics.mean(statdata))
        
    elif o3=='MEAN':
        print("Mean: ",statistics.mean(statdata))

    elif o3=='MEDIAN':
        print("Median: ",statistics.median(statdata))

    elif o3=='median':
        print("Median: ",statistics.median(statdata))

    elif o3=='Median':
        print("Median: ",statistics.median(statdata))
        
    elif o3=='Mode':
        print("Mode: ",statistics.mode(statdata))

    elif o3=='MODE':
        print("Mode: ",statistics.mode(statdata))

    elif o3=='mode':
        print("Mode: ",statistics.mode(statdata))

    elif o3=='VARIANCE':
        print("Variance: ",statistics.variance(statdata))

    elif o3=='Variance':
        print("Variance: ",statistics.variance(statdata))

    elif o3=='variance':
        print("Variance: ",statistics.variance(statdata))

    elif o3=='standard deviation':
        print("Standard Deviation: ",statistics.stdev(statdata))
        
    elif o3=='Standard Deviation':
        print("Standard Deviation: ",statistics.stdev(statdata))
        
    elif o3=='STANDARD DEVIATION':
        print("Standard Deviation: ",statistics.stdev(statdata))

    elif o3=='standarddeviation':
        print("Standard Deviation: ",statistics.stdev(statdata))
        
    elif o3=='StandardDeviation':
        print("Standard Deviation: ",statistics.stdev(statdata))
        
    elif o3=='STANDARDDEVIATION':
        print("Standard Deviation: ",statistics.stdev(statdata))


    else:
        print("Invalid operator.... Please Restart the Program to Continue.")

    print('''
       Please Restart for Another Calculation.

            Thanks For Using Our App.''')

elif mode=='6':

    #Choice 2
    print('''
Enter the Type of Operation:-

1.Simple Interest.
2.Compound Interest.

    ''')
    
    mode2=input("Enter Your Choice: ")

    if mode2=='1':
       #Instructions 6_1
      
       txt15='''Instructions:-

       i) Enter the Principal amount, rate of Interest and Time Period.
       ii) Press 'Enter' and wait for the Answers.
     
       GOOD LUCK!!!!

       '''
       txt16='''
       GOOD LUCK!!!

       '''
       guide6_1=input("Do you Want to View Instructions? (Yes/No): ")

       if guide6_1=='yes':
         print(txt15)
  
       elif guide6_1=='Yes':
           print(txt15)

       elif guide6_1=='YES':
           print(txt15)
    
       elif guide6_1=='no':
           print(txt16)
    
       elif guide6_1=='No':
           print(txt16)
    
       elif guide6_1=='NO':
           print(txt16)
     
       else:
           print("System Would Consider it as 'NO'. ",txt16)
           
       #Main Program 6_1
        
       prinamt=float(input("Enter the Total Principal Amount: "))
       rateint=float(input("Enter the Rate of Interest: "))
       tp=float(input("Enter Time in years: "))

       simpint=(prinamt*rateint*tp)/100
       amtpay=prinamt+simpint

       print('Simple Interest: ',simpint)

       print('Amount Payable: ',amtpay)

       print('''
       Please Restart for Another Calculation.

            Thanks For Using Our App.''')
       

    elif mode2=='2':

        #Instructions 6_2

        txt17='''Instructions:-

       i) Enter the Principal amount, rate of Interest and Time Period.
       ii) Press 'Enter' and wait for the Answers.

        GOOD LUCK!!!!

        '''

        txt18='''
        GOOD LUCK!!!!

        '''
        
        guide6_2=input("Do you Want to View Instructions? (Yes/No): ")

        if guide6_2=='yes':
          print(txt17)
  
        elif guide6_2=='Yes':
            print(txt17)

        elif guide6_2=='YES':
            print(txt17)
    
        elif guide6_2=='no':
            print(txt18)
    
        elif guide6_2=='No':
            print(txt18)
    
        elif guide6_2=='NO':
            print(txt18)
     
        else:
            print("System Would Consider it as 'NO' ",txt18)
            
        #Main Program 6_2
            
        prinamt1=float(input("Enter the Total Principal Amount: "))
        rateint1=float(input("Enter the Rate of Interest: "))
        tp1=float(input("Enter Time in years: "))
          
        amtpay1=prinamt1*(1+rateint1/100)**tp1
        compint=amtpay1-prinamt1

        print('Compound Interest: ',compint)

        print('Amount Payable: ',amtpay1)

        print('''
        Please Restart for Another Calculation.

            Thanks For Using Our App.''')

    else:
        print("INVALID CHOICE.... Please Restart the Program to Continue.")
      
elif mode=='7':

    #Instructions 7

    txt19='''Instructions:-

    i) Enter the Number in the Number section and Maximum Multiplier.
    ii) Maximum multiplier- The Maximum Number of Lines to Generate in the Table.
    iii) The table will be Automatically generated in an Instant.

    GOOD LUCK!!!!

     '''

    txt20='''
    GOOD LUCK!!!!

        '''
    guide7=input("Do you Want to View Instructions? (Yes/No): ")

    if guide7=='yes':
      print(txt19)
  
    elif guide7=='Yes':
        print(txt19)

    elif guide7=='YES':
        print(txt19)
    
    elif guide7=='no':
        print(txt20)
    
    elif guide7=='No':
        print(txt20)
    
    elif guide7=='NO':
        print(txt20)
     
    else:
        print("System Would Consider it as 'NO'. ",txt20)
            
    #Main Program 7
        
    mul=int(input("Enter the Number for Generating table: "))
    mul1=int(input("Enter the Maximum Multiplier: "))

    print('''
 Multiplication Table for ''',mul,''':
''')
    for i in range(1,mul1+1):
        table=mul*i
        print(mul,"x",i,"=",table)

    print('''
     Please Restart for Another Calculation.

       Thanks For Using Our App.''')

elif mode=='8':

    #Instructions 8
    txt21='''Instructions:-

    i). Follow the Instructions Given by the Software.
    ii). Enter Dimensions Wherever Required.

    IMPORTANT NOTICE:-

        *Please Ensure that the Measurements are of UNIFORM UNITS*
        **Please Check the Values Before Entering to Avoid Getting Wrong Answers**

    GOOD LUCK!!!!
     '''

    txt22='''
    GOOD LUCK!!!!

        '''
    
    guide8=input("Do you Want to View Instructions? (Yes/No): ")

    if guide8=='yes':
        print(txt21)
  
    elif guide8=='Yes':
        print(txt21)

    elif guide8=='YES':
        print(txt21)
    
    elif guide8=='no':
        print(txt22)
    
    elif guide8=='No':
        print(txt22)
    
    elif guide8=='NO':
        print(txt22)
     
    else:
        print("System Would Consider it as 'NO'. ",txt22)

    print('''
Please select the Dimension:-

1.Two Dimensional (2-D) Shapes.
2.Three Dimensional (3-D) Shapes.

    ''')

    mode3=input("Enter Your Choice: ")

    if mode3=='1':
        print('''
Please select your Requirement:-

1.Triangular Geometry.
2.Quadrilateral Geometry.
3.Circular Geometry.

        ''')

        dim1=input("Enter your Requirement: ")

        if dim1=='1':
            print('''
Please select the Type of Triangle:-

1.Equilateral Triangle.
2.Isosceles Triangle.
3.Scalene Triangle.

            ''')

            tri=input("Enter the Type of Triangle: ")
        
            if tri=='1':
                sideeqt=float(input("Enter the Length: "))

                if sideeqt<=0:
                    print("INVALID DIMENSIONS.... Please Try again.")
                else:
                    peeqt=sideeqt*3
                    semipeeqt=peeqt/2
                    areqt=math.sqrt(3)/4*sideeqt*sideeqt

                    print("Perimeter: ",peeqt)
                    print("Semi Perimeter: ",semipeeqt)
                    print("Area: ",areqt)

            elif tri=='2':
                sideorheight=input("Is Height given (Yes/No): ")
            
                if sideorheight=='yes' or sideorheight=='Yes' or sideorheight=='YES' or sideorheight=='y' or sideorheight=='Y':
                    base1=float(input("Enter the Base: "))
                    height1=float(input("Enter the Height: "))

                    if base1<=0 or height1<=0:
                        print("INVALID DIMENSIONS.... Please Try again.")
                    else:
                        eqside1=math.sqrt((base1/2)**2+height1**2)
                        ariso1=0.5*base1*height1
                        peiso1=base1+2*eqside1
                        semipeiso1=peiso1/2
 
                        print("Equal Side Length: ",eqside1)
                        print("Perimeter: ",peiso1)
                        print("Semi Perimeter: ",semipeiso1)
                        print("Area: ",ariso1)
     
                elif sideorheight=='no' or sideorheight=='No' or sideorheight=='NO' or sideorheight=='n' or sideorheight=='N':
                    eqside1=float(input("Enter the Equal Side Length: "))
                    base1=float(input("Enter the Base: "))

                    if eqside1<=base1/2 or eqside1<=0 or base1<=0:
                        print("INVALID DIMENSIONS.... Please Try again.")
                    else:
                        height1=math.sqrt(eqside1**2-(base1/2)**2)
                        ariso1=0.5*base1*height1
                        peiso1=base1+2*eqside1
                        semipeiso1=peiso1/2

                        print("Height: ",height1)
                        print("Perimeter: ",peiso1)
                        print("Semi Perimeter: ",semipeiso1)
                        print("Area: ",ariso1)
                else:
                    print("INVALID CHOICE.... Please Try Again.")

            elif tri=='3':
                s1=float(input("Enter first Side: "))
                s2=float(input("Enter Second Side: "))
                s3=float(input("Enter Third Side: "))

                if s1+s2>s3 and s2+s3>s1 and s1+s3>s2 and s1>0 and s2>0 and s3>0:
                    pesc=s1+s2+s3
                    semipesc=pesc/2
                    arsc=math.sqrt(semipesc*(semipesc-s1)*(semipesc-s2)*(semipesc-s3))

                    print("Perimeter: ",pesc)
                    print("Semi-perimeter: ",semipesc)
                    print("Area: ",arsc)
                else:
                    print("INVALID DIMENSIONS.... Please Try again.")
            else:
                print("INVALID CHOICE.... Please Try Again.")

        elif dim1=='2':
            print('''
Please select the Type of Quadrilateral:-

1.Square.
2.Rectangle.
3.Parallelogram.
4.Rhombus.
5.Trapezium / Trapezoid.
6.Kite.

            ''')

            quad=input("Enter the Type of Quadrilateral: ")
        
            if quad=='1':
                sidesq=float(input("Enter the Length: "))

                if sidesq<=0:
                    print("INVALID DIMENSIONS.... Please Try again.")
                else:
                    pesq=sidesq*4
                    arsq=sidesq*sidesq
     
                    print("Perimeter: ",pesq)
                    print("Area: ",arsq)
          
            elif quad=='2':
                rect1=float(input("Enter the Length: "))
                rect2=float(input("Enter the Breadth: "))

                if rect1<=0 or rect2<=0:
                    print("INVALID DIMENSIONS.... Please Try again.")
                else:
                    perect=2*(rect1+rect2)
                    arrect=rect1*rect2

                    print("Perimeter: ",perect)
                    print("Area: ",arrect)
            
            elif quad=='3':
                parabase=float(input("Enter the Base: "))
                paraside=float(input("Enter the Side Length: "))

                if parabase<=0 or paraside<=0:
                    print("INVALID DIMENSIONS.... Please Try again.")
                else:
                    pepara=2*(parabase+paraside)
                    hinfo=input("Do you Know the Height? (Yes/No): ")

                    if hinfo=='yes' or hinfo=='Yes' or hinfo=='YES' or hinfo=='y' or hinfo=='Y':
                        paraheight=float(input("Enter the Height: "))
                        if paraheight<=0:
                            print("INVALID DIMENSIONS.... Please Try again.")
                        else:
                            paraarea=parabase*paraheight
                            print("Perimeter: ",pepara)
                            print("Area: ",paraarea)
                
                    elif hinfo=='no' or hinfo=='No' or hinfo=='NO' or hinfo=='n' or hinfo=='N':
                        print("Perimeter: ",pepara)
                        print("Area: Calculation requires Height...... ")
                    else:
                        print("INVALID CHOICE.... Please Try Again.")
                                 
            elif quad=='4':
                rhombside=float(input("Enter the Side Length: "))

                if rhombside<=0:
                     print("INVALID DIMENSIONS.... Please Try again.")
                else:
                    perhomb=4*rhombside
                    hinfo1=input("Do you Know the Height or Diagonals? (H / D / No): ")

                    if hinfo1=='h' or hinfo1=='H':
                        rhombheight=float(input("Enter the Height: "))
                        if rhombheight<=0:
                            print("INVALID DIMENSIONS.... Please Try again.")
                        else:
                            arrhomb=rhombside*rhombheight
                            print("Perimeter: ",perhomb)
                            print("Area: ",arrhomb)
                
                    elif hinfo1=='d' or hinfo1=='D':
                        diagrhomb1=float(input("Enter the First Diagonal: "))
                        diagrhomb2=float(input("Enter the Second Diagonal: "))

                        if diagrhomb1<=0 or diagrhomb2<=0:
                            print("INVALID DIMENSIONS.... Please Try again.")
                        else:
                            arrhomb=(diagrhomb1*diagrhomb2)/2
                            print("Perimeter: ",perhomb)
                            print("Area: ",arrhomb)
                
                    elif hinfo1=='no' or hinfo1=='No' or hinfo1=='NO':
                        print("Perimeter: ",perhomb)
                        print("Area: Either Height or Diagonal is Required....")
                    else:
                        print("INVALID CHOICE.... Please Try Again.")
                                 
            elif quad=='5':
                trasidep1 = float(input("Enter the first parallel side: "))
                trasidep2 = float(input("Enter the second parallel side: "))
                trasidenp1 = float(input("Enter the first non-parallel side: "))
                trasidenp2 = float(input("Enter the second non-parallel side: "))

                if trasidep1<=0 or trasidep2<=0 or trasidenp1<=0 or trasidenp2<=0:
                    print("INVALID DIMENSIONS.... Please Try again.")
                else:
                    petrap=trasidep1+trasidep2+trasidenp1+trasidenp2
                    hinfo2=input("Do you Know the Height? (Yes/No): ")

                    if hinfo2=='yes' or hinfo2=='Yes' or hinfo2=='YES' or hinfo2=='y' or hinfo2=='Y':
                        trapheight=float(input("Enter the Height: "))
                        if trapheight <= 0:
                            print("INVALID DIMENSIONS.... Please Try again.")
                        else:
                            artrap=0.5*(trasidep1+trasidep2)*trapheight
                            print("Perimeter: ",petrap)
                            print("Area: ",artrap)

                    elif hinfo2=='no' or hinfo2=='No' or hinfo2=='NO' or hinfo2=='n' or hinfo2=='N':
                        print("Perimeter: ",petrap)
                        print("Area: Calculation requires Height......")
                    else:
                        print("INVALID CHOICE.... Please Try Again.")

            elif quad=='6':
                kite1=float(input("Enter the Length of First Pair of Equal Sides: "))
                kite2=float(input("Enter the Length of Second Pair of Equal Sides: "))

                if kite1<=0 or kite2<=0:
                    print("INVALID DIMENSIONS.... Please Try again.")
                else:
                    pekite=2*(kite1+kite2)
                    hinfo3=input("Do you Know the Height or Diagonals? (H / D / No): ")

                    if hinfo3=='h' or hinfo3=='H':
                        print("Height Must be Perpendicular to One Equal Side")
                        kiteheight=float(input("Enter the Height: "))
                        if kiteheight<=0:
                            print("INVALID DIMENSIONS.... Please Try again.")
                        else:
                            arkite=kite1*kiteheight
                            print("Perimeter: ",pekite)
                            print("Area: ",arkite)

                    elif hinfo3=='d' or hinfo3=='D':
                        diagkite1=float(input("Enter the First Diagonal: "))
                        diagkite2=float(input("Enter the Second Diagonal: "))

                        if diagkite1<=0 or diagkite2<=0:
                            print("INVALID DIMENSIONS.... Please Try again.")
                        else:
                            arkite1=0.5*diagkite1*diagkite2
                            print("Perimeter: ",pekite)
                            print("Area: ",arkite1)

                    elif hinfo3=='no' or hinfo3=='No' or hinfo3=='NO':
                        print("Perimeter: ",pekite)
                        print("Area: Either Height or Diagonal is Required....")
                    else:
                        print("INVALID CHOICE.... Please Try Again.")
            else:
                print("INVALID CHOICE.... Please Try Again.")

        elif dim1=='3':
            print('''
Please select the Type of Circular Models:-

1.Circle.
2.Semi-circle.
3.Sector.
4.Segment.

            ''')
            cir1=input("Enter the Type of Circular Operation: ")

            if cir1=='1':
                radii1=float(input("Enter the Radius: "))
                if radii1<=0:
                    print("INVALID DIMENSIONS.... Please Try again.")
                else:
                    circum=2*math.pi*radii1
                    carea=math.pi*radii1*radii1
                    print("Circumference: ",circum)
                    print("Area: ",carea)

            elif cir1=='2':
                radii2=float(input("Enter the Radius: "))
                if radii2<=0:
                    print("INVALID DIMENSIONS.... Please Try again.")
                else:
                    scircum=math.pi*radii2+2*radii2
                    sarea=0.5*math.pi*radii2*radii2
                    print("Perimeter: ",scircum)
                    print("Area: ",sarea)

            elif cir1=='3':
                radii3=float(input("Enter the Radius: "))
                ang1=float(input("Enter the Angle: "))
                if radii3<=0 or ang1<=0:
                    print("INVALID DIMENSIONS.... Please Try again.")
                else:
                    arclen=2*math.pi*radii3*(ang1/360)
                    arsec1=math.pi*radii3*radii3*(ang1/360)
                    print("Arc Length: ",arclen)
                    print("Area of Sector: ",arsec1)

            elif cir1=='4':
                radii4=float(input("Enter the Radius: "))
                ang2=float(input("Enter the Angle: "))
                if radii4<=0 or ang2<=0:
                    print("INVALID DIMENSIONS.... Please Try again.")
                else:
                    arsec2=math.pi*radii4*radii4*(ang2/360)
                    artri=0.5*radii4*radii4*math.sin(math.radians(ang2))
                    arseg=arsec2-artri
                    print("Area of Segment: ",arseg)
            else:
                print("INVALID CHOICE.... Please Try Again.")
        else:
            print("INVALID CHOICE.... Please Try Again.")

    elif mode3=='2':
        print('''
Please select your Figure:-

1.Sphere.
2.Hemisphere.
3.Cube.
4.Cuboid.
5.Cone.
6.Cylinder.
7.Pyramid (Square Pyramid).
8.Frustum.

        ''')
        dim2=input("Enter the Figure Type: ")

        if dim2=='1':
            radsph=float(input("Enter the Radius: "))
            if radsph<=0:
                print("INVALID DIMENSIONS.... Please Try again.")
            else:
                spvol=(4/3)*math.pi*radsph**3
                spsa=4*math.pi*radsph**2
                print("Volume: ",spvol)
                print("Surface Area: ",spsa)

        elif dim2=='2':
            radhsph=float(input("Enter the Radius: "))
            if radhsph<=0:
                print("INVALID DIMENSIONS.... Please Try again.")
            else:
                hspvol=(2/3)*math.pi*radhsph**3
                hspcsa=2*math.pi*radhsph**2
                hsptsa=3*math.pi*radhsph**2
                print("Volume: ",hspvol)
                print("Curved Surface Area (CSA): ",hspcsa)
                print("Total Surface Area (TSA): ",hsptsa)

        elif dim2=='3':
            cuside=float(input("Enter the Side Length: "))
            if cuside<=0:
                print("INVALID DIMENSIONS.... Please Try again.")
            else:
                cuvol=cuside**3
                culsa=4*cuside**2
                cutsa=6*cuside**2
                print("Volume: ",cuvol)
                print("Lateral Surface Area (LSA): ",culsa)
                print("Total Surface Area (TSA): ",cutsa)

        elif dim2=='4':
            lencud=float(input("Enter the Length: "))
            brthcud=float(input("Enter the Breadth: "))
            heightcud=float(input("Enter the Height: "))
            if lencud<=0 or brthcud<=0 or heightcud<=0:
                print("INVALID DIMENSIONS.... Please Try again.")
            else:
                cudvol=lencud*brthcud*heightcud
                cudlsa=2*heightcud*(lencud+brthcud)
                cudtsa=2*(lencud*brthcud+brthcud*heightcud+heightcud*lencud)
                print("Volume: ",cudvol)
                print("Lateral Surface Area (LSA): ",cudlsa)
                print("Total Surface Area (TSA): ",cudtsa)

        elif dim2=='5':
            radcone=float(input("Enter the Radius of Base: "))
            heightcone=float(input("Enter the Height: "))
            if radcone<=0 or heightcone<=0:
                print("INVALID DIMENSIONS.... Please Try again.")
            else:
                slant=math.sqrt(heightcone**2+radcone**2)
                conevol=(1/3)*math.pi*radcone**2*heightcone
                conecsa=math.pi*radcone*slant
                conetsa=conecsa+math.pi*radcone**2
                print("Volume: ",conevol)
                print("Curved Surface Area (CSA): ",conecsa)
                print("Total Surface Area (TSA): ",conetsa)

        elif dim2=='6':
            radcyl=float(input("Enter the Radius of Base: "))
            heightcyl=float(input("Enter the Height: "))
            if radcyl<=0 or heightcyl<=0:
                print("INVALID DIMENSIONS.... Please Try again.")
            else:
                cylvol=math.pi*radcyl**2*heightcyl
                cylcsa=2*math.pi*radcyl*heightcyl
                cyltsa=cylcsa+2*math.pi*radcyl**2
                print("Volume: ",cylvol)
                print("Curved Surface Area (CSA): ",cylcsa)
                print("Total Surface Area (TSA): ",cyltsa)

        elif dim2=='7':
            basepyr=float(input("Enter the Base Side Length: "))
            heightpyr=float(input("Enter the Height: "))
            if basepyr<=0 or heightpyr<=0:
                print("INVALID DIMENSIONS.... Please Try again.")
            else:
                slant1=math.sqrt((basepyr/2)**2+heightpyr**2)
                pyrvol=(1/3)*basepyr**2*heightpyr
                pyrlsa=2*basepyr*slant1
                pyrtsa=basepyr**2+pyrlsa
                print("Volume: ",pyrvol)
                print("Lateral Surface Area (LSA): ",pyrlsa)
                print("Total Surface Area (TSA): ",pyrtsa)

        elif dim2=='8':
            frurad1=float(input("Enter the Radius of Larger Base: "))
            frurad2=float(input("Enter the Radius of Smaller Base: "))
            fruheight=float(input("Enter the Height: "))
            if frurad1<=0 or frurad2<=0 or fruheight<=0:
                print("INVALID DIMENSIONS.... Please Try again.")
            else:
                slant2=math.sqrt(fruheight**2+(frurad1-frurad2)**2)
                fruvol=(1/3)*math.pi*fruheight*(frurad1**2+frurad2**2+frurad1*frurad2)
                frucsa=math.pi*(frurad1+frurad2)*slant2
                frutsa=frucsa+math.pi*(frurad1**2+frurad2**2)
                print("Volume: ",fruvol)
                print("Curved Surface Area (CSA): ",frucsa)
                print("Total Surface Area (TSA): ",frutsa)
        else:
            print("INVALID CHOICE.... Please Try Again.")
    else:
        print("INVALID CHOICE.... Please Try Again.")

    print('''
     Please Restart for Another Calculation.

       Thanks For Using Our App.''')
    
else:
    print("INVALID CHOICE.... Please Restart the Program to Continue.")


input("Press ENTER")

