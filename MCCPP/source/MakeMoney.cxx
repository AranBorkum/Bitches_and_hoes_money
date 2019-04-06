#include <iostream>
#include <fstream>
#include <string>
#include <vector>
#include "MakeMoney.hxx"
#include "Overlord.hxx"

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

Overlord InitiateOverlord() {

  double wealth  = 100000;
  double capital = 50000 ;
  double nProp   = 0     ;
  std::vector<std::string> labels;
  
  std::string condo = "Condo";
  std::string house = "House";

  labels.push_back(house);
  labels.push_back(house);
  labels.push_back(house);
  labels.push_back(condo);
  labels.push_back(condo);
  nProp = labels.size();
  
  Overlord Aran = Overlord(wealth,
			   capital,
			   nProp,
			   labels);
  return Aran;
}

void SaveOverlordData() {

  std::ofstream OutputFile;
  OutputFile.open("OverlordData.txt");
  OutputFile << InitiateOverlord() << std::endl;
  OutputFile.close();
  
}


int main() {

  SaveOverlordData();
  std::cout << InitiateProperty() << std::endl;
  return 0;
  
}
