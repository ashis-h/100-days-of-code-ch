import csv
 
with open("aapl.csv","w") as csvfile:
       thewriter = csv.writer(csvfile)
       thewriter.writerow(['Name','Registration','Marks %','Course'])
       thewriter.writerow(['Ashish','1','75','MCA'])
       thewriter.writerow(['Akash','2','70','MCA'])
       thewriter.writerow(['Umang','3','80','MCA'])

       #for i in range(1,10):
         
   
     

