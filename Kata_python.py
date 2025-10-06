public class Kata{
   
  //public static double getCelcius(double fahrenheit){

    // double celcius = 5 * (fahrenheit - 32) / 9;
    // return celcius;
//}
    // public static boolean isOdd(int num){
  // if(num % 2 != 0){
    //return true;

//}
    //return false;
//}

     //public static void printStars(int numberOfRows){
         
  //for(int row = 1; row <= 5; row++){
  //for(int column = 1; column <= row; column++){
     //System.out.print("*");
  //}
  //System.out.println();
  //}
   //}

    public static boolean isEven(int num){
    if(num % 2 == 0){
    return true;
     }
    return false;

    }
      
    public static int calculateFactorial(int num){
    int fact = 1;
    for(int i = num; i >0; i--){ 
    fact = fact * i;

     }

    return fact;
   
    }

    public static int Squareofthenumber(int number){
    int square = 0;
    for(int count = 1; count <= number; count++){
     square = count * count;
}
     return square;
}    


      public static int factorOf(int number){
     int factor = 0;
	for(int counter = 1; counter <= number; counter++){
		if(number % counter == 0){
		factor = factor + 1;
	}

          }

	return factor;
	
	}
         
       public static boolean isPrime(int number){
       if(number <= 1){
           return false;
}

       for(int count = 2; count <= number; count++){
        if(number % 2 == 0){
          return false;
} 
    
}
           return true;

}
      public static boolean isSquare(int num){
      int square = 0;
       
      for(int count = 1;count<= num; count++){
      square = count * count;
       if((count * count) == num ){
        return true;
}
}
          return false;
}
  
        public  static boolean isPalindrome(int num){
        int a = num;
        int rev = 0;

        while(num != 0){
        rev = rev * 10 + num % 10;
        num = num/10;

}
          if(a == rev){
           return true;
}
         return false;

}

        public static int subtract(int num1, int num2){
        int largest = num1;
        int result;
        if(num2 > largest){
         largest = num2;
}
        result = (largest - num1) + (largest - num2);

        return result;
}
        public static  float divide(int num1, int num2){
        if(num1 % num2 == 0){

}       
        int result = num1 % num2;
        if(num2 == 0){
}
         return 0;
  }
             
    }




















