
byte pin[]= {2,3,4,5,6,7,8,9,10,11,12,13};
byte red_0   = pin[0] , red_1   = pin[3] , red_2   = pin[6] , red_3   = pin[9];
byte green_0 = pin[1] , green_1 = pin[4] , green_2 = pin[7] , green_3 = pin[10];
byte blue_0  = pin[2] , blue_1  = pin[5] , blue_2  = pin[8] , blue_3  = pin[11];

void setup()
{
  
  for (byte index = 0 ; index <=13 ; index++ )
      { pinMode( index , OUTPUT );  }
  Serial.begin(9600);
  
}


void loop()
{
  
  if ( Serial.available() > 0 )
     
     {
       char str = Serial.read();
       Serial.println(str);
       switch(str)
           {
               case '2':
                   digitalWrite(red_0 , HIGH);
                   digitalWrite(green_0 , LOW);
                   digitalWrite(blue_0 , LOW);
                   break;
               case '3':
                   digitalWrite(red_0 , LOW);
                   digitalWrite(green_0 , HIGH);
                   digitalWrite(blue_0 , LOW);
                   break;
               case '4':
                   digitalWrite(red_0 , LOW);
                   digitalWrite(green_0 , LOW);
                   digitalWrite(blue_0 , HIGH);
                   break;  
               case '5':
                   digitalWrite(red_1 , HIGH);
                   digitalWrite(green_1 , LOW);
                   digitalWrite(blue_1 , LOW);
                   break;
               case '6':
                   digitalWrite(red_1 , LOW);
                   digitalWrite(green_1 , HIGH);
                   digitalWrite(blue_1 , LOW);
                   break;
               case '7':
                   digitalWrite(red_1 , LOW);
                   digitalWrite(green_1 , LOW);
                   digitalWrite(blue_1 , HIGH);
                   break;     
               case '8':
                   digitalWrite(red_2 , HIGH);
                   digitalWrite(green_2 , LOW);
                   digitalWrite(blue_2 , LOW);
                   break;
               case '9':
                   digitalWrite(red_2 , LOW);
                   digitalWrite(green_2 , HIGH);
                   digitalWrite(blue_2 , LOW);
                   break;
               case '10':
                   digitalWrite(red_2 , LOW);
                   digitalWrite(green_2 , LOW);
                   digitalWrite(blue_2 , HIGH);
                   break;                
               case 'A':
                   digitalWrite(red_3 , HIGH);
                   digitalWrite(green_3 , LOW);
                   digitalWrite(blue_3 , LOW);
                   break;
               case 'B':
                   digitalWrite(red_3 , LOW);
                   digitalWrite(green_3 , HIGH);
                   digitalWrite(blue_3 , LOW);
                   break;
               case 'D':
                   digitalWrite(red_3 , LOW);
                   digitalWrite(green_3 , LOW);
                   digitalWrite(blue_3 , HIGH);
                   break;
               case '14':
                   digitalWrite(red_0 , LOW);
                   digitalWrite(green_0 , LOW);
                   digitalWrite(blue_0 , LOW);
                   break;
               case '15':
                   digitalWrite(red_1 , LOW);
                   digitalWrite(green_1 , LOW);
                   digitalWrite(blue_1 , LOW);
                   break;
               case '16':
                   digitalWrite(red_2 , LOW);
                   digitalWrite(green_2 , LOW);
                   digitalWrite(blue_2 , LOW);
                   break;
               case '17':
                   digitalWrite(red_3 , LOW);
                   digitalWrite(green_3 , LOW);
                   digitalWrite(blue_3 , LOW);
                   break;
               default:
                   digitalWrite(red_0 , LOW);
                   digitalWrite(green_0 , LOW);
                   digitalWrite(blue_0 , LOW);
                   digitalWrite(red_1 , LOW);
                   digitalWrite(green_1 , LOW);
                   digitalWrite(blue_1 , LOW);
                   digitalWrite(red_2 , LOW);
                   digitalWrite(green_2 , LOW);
                   digitalWrite(blue_2 , LOW);
                   digitalWrite(red_3 , LOW);
                   digitalWrite(green_3 , LOW);
                   digitalWrite(blue_3 , LOW);
                   break;
           }
       
       
     
     }


  
}
