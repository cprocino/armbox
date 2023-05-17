# Robot Arm

For this project we had to create a robot arm that could pick up and move an object. Chris and nixon created a box with robot arm that would pick up a small ball and drop it into a container that would eventualy shoot it out. Our first challenge was design which we solved by our proof of concept box, then the actual creation took over in import. We also would end scratching the shooting box part as that just wouldnt work and would take way to long.

For our planning we really only had a rough idea of a plan per say. We knew we had to be done ny valentines day anf that was are deadline to finish. for the first week we decided to get a rough outline of what we wanted to do and how to do it. The next couple of weeks would just be making the project and doing cad stuff for the most part with me doing the cade and chris making a way to pickup the ball. we then started fabricating and doing code as it came togheter which took lonmger than we thought it would take for sure. For the final week we just documented and finished our project and got the documentation or the majority of it done.

![WIN_20230130_15_15_34_Pro](https://user-images.githubusercontent.com/71406784/216708005-1a48c74b-902f-4250-b6ba-4a320e8df95a.jpg)

![WIN_20230130_15_16_32_Pro](https://user-images.githubusercontent.com/71406784/216708013-ea3af834-308b-46c2-a769-1af261489e62.jpg)

![WIN_20230130_15_17_07_Pro](https://user-images.githubusercontent.com/71406784/216708019-9c5c536e-f08e-460b-a5d1-a88bf794d68d.jpg)

![WIN_20230130_15_17_13_Pro](https://user-images.githubusercontent.com/71406784/216708025-a9427c3f-2bbc-4665-b73c-2790705b03f5.jpg)

![WIN_20230130_15_17_23_Pro](https://user-images.githubusercontent.com/71406784/216708029-d1aba0f0-2a14-448c-81c1-5dd367c8cbf8.jpg)


![Screenshot 2023-03-10 151436](https://user-images.githubusercontent.com/71406784/224419123-5a04b894-4155-4c1d-9c21-99cb2b80ea5a.png)

![mygif](https://github.com/cprocino/armbox/blob/master/media/ezgif-2-b9d27cdedb.gif)

Making the project itself was definitely no easy task to say the least. The onshape model seemed easy at first but after further in-depth looks at the project its flaws were quickly revealed. The need for wheels on the main arm base and the need for further stabling of the main arm was clear. After adding caster wheels and two brackets the project was closer to being done. The project also needed better measures to work as a friction fit design meaning I needed to add extra width to each part so they would fit together better. Then we were ready to print! The friction fit did work, but it wasn't the sturdiest so we added duck tape to hold the sides together so we could be a little rougher on it. The function of the arm was pretty good and the wheels helped with support. The main problem being the need for a heavier counter weight then the one designed in onshape. The solution was simple: duck tape 2 batteries to the back of the designed counter weight. Upon adding the counter weight we saw immediate success the arm was able to be stable. The main branch of the arm did bend when the ping pong ball and its grabber were attached, but it still worked and was able to move. So, while multiple hillbilly duck tape innovations had to be made it did still function successfully.



the code for the project was relatively simple as all we needed to do was have two servos fire with one click of a button. Very complex stuff for me and nixon but we were smart enough to ask for help. Huge thanks to Graham Gilbert-schroeer for a lot of help with the code. the code is as follows:

    #include <Arduino.h>

    #include <Servo.h>


    Servo Myservo1;

    Servo Myservo2;

    int SERVO_PIN1 = 3;

    int SERVO_PIN2 = 5;

    int ServoButton = 4;


     int dropTime = 2000;


     void setup() {

      Serial.begin(9600);
  
      Myservo1.attach(SERVO_PIN1);
    
      Myservo2.attach(SERVO_PIN2);
  
     }

       void loop() {

      Serial.println(digitalRead(ServoButton));
  
      if (digitalRead(ServoButton) == 1) {
  
       Myservo1.write(180);
    
       delay(1000);
    
       Myservo2.write(180);
    
        delay(dropTime);
    
       Myservo2.write(0);
    
        delay(1000);
    
       Myservo1.write(0);
    
    }
  
      else{
  
        Serial.println("No");
    
     }
  
      delay(500);
  
   }
   
   
 While this code was simple it achivied its goal of picking up the ball and putting it in another location.
  
