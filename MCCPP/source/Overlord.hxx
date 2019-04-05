#include <iostream>
#include <vector>
#include <string>

/*
|  Define the class of overlords.
|  This is going to include things such as number of houses owned,
|  local wealth, starting money, etc...
*/

class Overlord {

private:
  double fPersonalWealth  ;
  double fStartingCapital ;
  double fNPropertiesOwned;

  std::vector<std::string> fPropertyLabels;
  
public:

  // Outline for the basic constructor. I think this should only really be made once
  Overlord(double cPersonalWealth  ,
	   double cStartingCapital ,
	   double cNPropertiesOwned,
	   std::vector<std::string>cPropertyLabels  ) {
    fPersonalWealth   = cPersonalWealth  ;
    fStartingCapital  = cStartingCapital ;
    fNPropertiesOwned = cNPropertiesOwned;
    fPropertyLabels   = cPropertyLabels  ;
  }

  // Get functions for returning various storred features
  double                   GetPersonalWealth  () {return fPersonalWealth  ;}
  double                   GetStartingCapital () {return fStartingCapital ;}
  double                   GetNPropertiesOwned() {return fNPropertiesOwned;}
  std::vector<std::string> GetPropertyLabels  () {return fPropertyLabels  ;}

  // Set function which will no doubt be the most important
  void SetPersonalWealth  (double      n) {fPersonalWealth          = n;}
  void SetStartingCapital (double      n) {fStartingCapital         = n;}
  void SetNPropertiesOwned(double      n) {fNPropertiesOwned        = n;}
  void SetPropertyLabels  (std::string n) {fPropertyLabels.push_back(n);}

  // Definition of a print overloader
  friend std::ostream& operator<<(std::ostream& os, House h);


  
};

std::ostream& operator<<(std::ostream& os, Overlord o){
  os << "Personal Wealth :\t" << o.GetPersonalWealth  () << "\n"
     << "Starting Capital:\t" << o.GetStartingCapital () << "\n"
     << "Properties Owned:\t" << o.GetNPropertiesOwned() << "\n";
    for (int i=0; i<o.GetPropertyLabels().size(); ++i) {
      os << "Property Type   :\t" << o.GetPropertyLabels()[i] << "\n";
    }
  return os;
}
