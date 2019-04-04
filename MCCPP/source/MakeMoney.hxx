#include <iostream>
#include <string>

/*
|  Define the class of houses.
|  This is going to include things such as starting capital, average house price,
|  length of morgage, etc...
*/

class House {

private:

  int         fPriceOfHouse        ;
  int         fLengthOfMorgage     ;
  int         fNumberOfBedrooms    ;
  double      fNumberOfBathrooms   ;
  double      fIntrestRateOnMorgage;
  std::string fTypeOfHouse         ;   //Country, city, etc...

    
public:

  // Conctructor for the House object
  House(int         cPriceOfHouse        ,
	int         cLengthOfMorgage     ,
	int         cNumberOfBedrooms    ,
	double      cNumberOfBathrooms   ,
	double      cIntrestRateOnMorgage,
	std::string cTypeOfHouse         )
  {
    fPriceOfHouse         = cPriceOfHouse        ,
    fLengthOfMorgage      = cLengthOfMorgage     ,
    fNumberOfBedrooms     = cNumberOfBedrooms    ,
    fNumberOfBathrooms    = cNumberOfBathrooms   ,
    fIntrestRateOnMorgage = cIntrestRateOnMorgage,
    fTypeOfHouse          = cTypeOfHouse         ;
  }

  // Destructor for the House object
  ~House() {}

  // Simple get functions for the class
  int         GetPriceOfHouse        () {return fPriceOfHouse        ;}
  int         GetLengthOfMorgage     () {return fLengthOfMorgage     ;}
  int         GetNumberOfBedrooms    () {return fNumberOfBedrooms    ;}
  double      GetNumberOfBathrooms   () {return fNumberOfBathrooms   ;}
  double      GetIntrestRateOnMorgage() {return fIntrestRateOnMorgage;}
  std::string GetTypeOfHouse         () {return fTypeOfHouse         ;}

  // Simple set functions for the class
  int         SetPriceOfHouse        (int         n) {fPriceOfHouse         = n; return 0;}
  int         SetLengthOfMorgage     (int         n) {fLengthOfMorgage      = n; return 0;}
  int         SetNumberOfBedrooms    (int         n) {fNumberOfBedrooms     = n; return 0;}
  double      SetNumberOfBathrooms   (double      n) {fNumberOfBathrooms    = n; return 0;}
  double      SetIntrestRateOnMorgage(double      n) {fIntrestRateOnMorgage = n; return 0;}
  std::string SetTypeOfHouse         (std::string n) {fTypeOfHouse          = n; return 0;}
	
  // Overloading the cout operator so it prints something worth looking at
  friend std::ostream& operator<<(std::ostream& os, House h);


};

std::ostream& operator<<(std::ostream& os, House h){
  os << "Initial Price of the house:      " << h.GetPriceOfHouse        () << "\n"
     << "Length of the agreed morgage:    " << h.GetLengthOfMorgage     () << "\n"
     << "Agreed interest rate on morgage: " << h.GetIntrestRateOnMorgage() << "\n"
     << "Features of the house"                                            << "\n"
     << "Style of the house:              " << h.GetTypeOfHouse         () << "\n"     
     << "Number of bedrooms:              " << h.GetNumberOfBedrooms    () << "\n"
     << "Number of bathrooms:             " << h.GetNumberOfBathrooms   () << "\n";
    return os;
}
