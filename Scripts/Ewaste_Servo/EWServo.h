#include <Wire.h>

class EWServo{
  public:
    EWServo(const int in1, const int in2, const int out);
    void calibrate();
    bool write(int pos);
    void stop();  
    void setLims(const int min, const int max);
  private:
    int input1;
    int input2;
    int feedback;
    int pot_pos;
    int servo_pos;
    int min_servo; 
    int max_servo;
    void drivePos();
    void driveNeg();
    void driveStop();
 
 };
