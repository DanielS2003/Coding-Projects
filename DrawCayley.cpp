#include <iostream>
#include <vector>

/*This is a program of my design meant to draw Cayley diagrams.
Cayley diagrams are a way of representing groups which are objects in abstract algebra.*/

int main (){
    int genamt; //number of generators for group G

    std::cout << "Your group will be called G. How many generators of G will there be?(up to 5): ";
    std::cin >> genamt;
    std::cin.ignore();

    if (genamt < 1 || genamt > 5) { // Validate input
        std::cout << "Invalid number of generators! Must be between 1 and 5.\n";
        return 1;
    }

    std::vector<char> group(genamt);  // Use vector instead of array

    for (int i = 0; i < genamt; i++) {
        group[i] = 'a' + i;  // Store 'a', 'b', 'c', etc.
    }

    std::cout << "You have chosen the number " << genamt << ". The generators are: ";
    for (char element : group){
        std::cout << element << " ";
    }

    std::cout << '\n';
    std::cout << "The default operation will be multiplication. What powers of your generators will return the identity element?\n";

    std::cout << "Each generator will be listed and you will enter the number corresponding to the power which returns the identity element.\n";
    int epowers[genamt];
    for(int j=0; j<genamt; j++){
        std::cout << "For " << group[j] << ": ";
        std::cin >> epowers[j];
    }


    return 0;
}