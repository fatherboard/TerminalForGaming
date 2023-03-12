#include <Joystick.h>

// Definition of all the board pins (Arduino Pro Micro)
const int BUTTON_A_PIN = 0;
const int BUTTON_B_PIN = 1;
const int BUTTON_X_PIN = 2;
const int BUTTON_Y_PIN = 3;
const int BUTTON_UP_PIN = 4;
const int BUTTON_DOWN_PIN = 5;
const int BUTTON_LEFT_PIN = 6;
const int BUTTON_RIGHT_PIN = 7;
const int BUTTON_R1_PIN = 8;
const int BUTTON_R2_PIN = 9;
const int BUTTON_R3_PIN = 10;
const int BUTTON_L1_PIN = 14;
const int BUTTON_L2_PIN = 15;
const int BUTTON_L3_PIN = 16;
const int BUTTON_START_PIN = LED_BUILTIN_RX;
const int BUTTON_SELECT_PIN = LED_BUILTIN_TX;

// Define the joystick pins
const int JOYSTICK_X_PIN = A0;
const int JOYSTICK_Y_PIN = A1;
const int JOYSTICK_Rx_PIN = A2;
const int JOYSTICK_Ry_PIN = A3;


// Create a Joystick object
Joystick_ Joystick(JOYSTICK_DEFAULT_REPORT_ID,JOYSTICK_TYPE_GAMEPAD,
  // Button count, hat switch count, X axis, Y axis, Z axis, RX axis
  16, 0, // Button Count, Hat Switch Count
  true, true, false,    // X, Y Axis, no Z
  true, true, false,    // Rx, Ry Axis, no Rz
  false, false,         // No rudder or throttle
  false, false, false   // No accelerator, brake, or steering
);

void setup() {
  // Set button pins as inputs and enable pull-up resistors
  pinMode(BUTTON_A_PIN, INPUT_PULLUP);
  pinMode(BUTTON_B_PIN, INPUT_PULLUP);
  pinMode(BUTTON_X_PIN, INPUT_PULLUP);
  pinMode(BUTTON_Y_PIN, INPUT_PULLUP);
  pinMode(BUTTON_UP_PIN, INPUT_PULLUP);
  pinMode(BUTTON_DOWN_PIN, INPUT_PULLUP);
  pinMode(BUTTON_LEFT_PIN, INPUT_PULLUP);
  pinMode(BUTTON_RIGHT_PIN, INPUT_PULLUP);
  pinMode(BUTTON_R1_PIN, INPUT_PULLUP);
  pinMode(BUTTON_R2_PIN, INPUT_PULLUP);
  pinMode(BUTTON_R3_PIN, INPUT_PULLUP);
  pinMode(BUTTON_L1_PIN, INPUT_PULLUP);
  pinMode(BUTTON_L2_PIN, INPUT_PULLUP);
  pinMode(BUTTON_L3_PIN, INPUT_PULLUP);
  pinMode(BUTTON_START_PIN, INPUT_PULLUP);
  pinMode(BUTTON_SELECT_PIN, INPUT_PULLUP);
  
  // Initialize the joystick
  Joystick.begin();
}

void loop() {
  // Read Button States
  Joystick.setButton(0, !digitalRead(BUTTON_A_PIN));
  Joystick.setButton(1, !digitalRead(BUTTON_B_PIN));
  Joystick.setButton(2, !digitalRead(BUTTON_X_PIN));
  Joystick.setButton(3, !digitalRead(BUTTON_Y_PIN));
  Joystick.setButton(4, !digitalRead(BUTTON_UP_PIN));
  Joystick.setButton(5, !digitalRead(BUTTON_DOWN_PIN));
  Joystick.setButton(6, !digitalRead(BUTTON_LEFT_PIN));
  Joystick.setButton(7, !digitalRead(BUTTON_RIGHT_PIN));
  Joystick.setButton(8, !digitalRead(BUTTON_R1_PIN));
  Joystick.setButton(9, !digitalRead(BUTTON_R2_PIN));
  Joystick.setButton(10, !digitalRead(BUTTON_R3_PIN));
  Joystick.setButton(11, !digitalRead(BUTTON_L1_PIN));
  Joystick.setButton(12, !digitalRead(BUTTON_L2_PIN));
  Joystick.setButton(13, !digitalRead(BUTTON_L3_PIN));
  Joystick.setButton(14, !digitalRead(BUTTON_START_PIN));
  Joystick.setButton(15, !digitalRead(BUTTON_SELECT_PIN));

  // Read the joystick axes and update the joystick state
  int x = analogRead(JOYSTICK_X_PIN);
  int y = analogRead(JOYSTICK_Y_PIN);
  int rx = analogRead(JOYSTICK_Rx_PIN) / 4;
  int ry = analogRead(JOYSTICK_Ry_PIN) / 4;
  Joystick.setXAxis(x);
  Joystick.setYAxis(y);
  Joystick.setRxAxis(rx);
  Joystick.setRyAxis(ry);

  // Delay (TBD)
  delay(10);
}

