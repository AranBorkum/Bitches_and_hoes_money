#include <iostream>
#include <string>
#include "MakeMoney.hxx"

// Here would be a good place to define the starting variables
// These will be global variables and will not be changed.
// These can be considered to be the input parameters for the test



House InitiateProperty() {

  int         PropertyValue = 200000;
  int         Morgage       = 200000;
  int         NumberOfBeds  = 3;
  double      NumberOfBaths = 2;
  double      InterestRate  = 0.3;
  std::string PropertyType  = "Urban";

  House Property = House(PropertyValue,
			 Morgage      ,
			 NumberOfBeds ,
			 NumberOfBaths,
			 InterestRate ,
			 PropertyType );
  return Property;
}

int main() {

  std::cout << InitiateProperty() << std::endl;
  return 0;
  
}
