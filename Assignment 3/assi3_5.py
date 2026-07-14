s1 = float(input("Enter first s1 :"))
s2 = float(input("Enter first s2 :"))
s3 = float(input("Enter first s3 :"))
if (s1 +s2>s3 and s2+ s3 >s1 and s1+s3 >s2):
   if s1==s2==s3 or s1==s3:
       print("The triangle is Equilateral")
elif s1==s2 or s2==s3 or s1==s3:
 print("The triangle is Isosceles")
else:
     print("The triangle is Scalene.")