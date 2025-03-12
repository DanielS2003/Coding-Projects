#include <iostream>
#include <vector>
#include <ctime>
#include <cstdlib> //needed for rand and srand


void matcher(std::vector <int> &deck);
void cardswap(std::vector<int> &deck, int selection,std::vector<int> &deck2);

int main (){
    std::cout << "You are about to play a game of old maid against a computer, do you want to know the rules?\n";
    std::cout << "Type yes or no: ";
    std::string confirm;
    std::cin >> confirm;

    if (confirm == "yes"){
        std::cout << "Both you and the computer will be given a set of cards. Matching numbers, will be discarded and the queen is number 13.\n";
        std::cout << "One person will get the Queen which has no match. You will take turns drawing from each other's deck.\n";
        std::cout << "This will continue until one person is out of cards.\n";
        std::cout << "If a situation comes up where drawing from eachother's deck will not result one side winning, it is a draw.\n";
    }
    else if (confirm == "no"){
        std::cout << "Let's begin!\n";
    }
    else if (confirm != "yes" && confirm != "no") {
        std::cout << "You did not enter yes or no.\n";
        return 0; //stops the program
    }

    srand(time(NULL)); // Seed the random number generator (call only once)

    std::vector<int> comdeck; // Computer's deck
    std::vector<int> humdeck; // Player's deck

    // Fill decks with random numbers from 0 to 12
    for (int i = 0; i < 10; i++) {
        comdeck.push_back(rand() % 13); // Generates numbers between 0 and 12
        humdeck.push_back(rand() % 13);
    }

    int queenpick = rand() % 2; // Determines who gets the queen (value 13)

    if (queenpick == 0) {
        comdeck[rand() % 10] = 13;
    } 
    else {
        humdeck[rand() % 10] = 13;
    }

    std::cout << "Your deck: ";
    for (int i = 0; i < humdeck.size(); i++) {
        std::cout << humdeck[i] << " ";
    }
    std::cout << "\n";

    matcher(humdeck);
    matcher(comdeck);

    std::cout << "Your deck after matching is: ";
    for (int i = 0; i < humdeck.size(); i++) {
        std::cout << humdeck[i] << " ";
    }
    std::cout << "\n";

    int remaining;
    remaining=comdeck.size();

    while (comdeck.size()>0 && humdeck.size()>0 ){
        std::cout << "It's your turn. The computer has " << remaining << " cards.\n";
        std::cout << "Your choices are: ";
        for (int i=0; i<comdeck.size();i++){
        std::cout << i << " ";
        }
        std::cout << '\n';
        int selection;
        std::cout << "Your selection: ";
        std::cin >> selection;

        //display results from swapping
        cardswap(comdeck, selection, humdeck);
        std::cout << "Your deck: ";
        for (int i = 0; i < humdeck.size(); i++) {
            std::cout << humdeck[i] << " ";
        }
        std::cout << '\n';
        matcher(humdeck);
        std::cout << "Your deck after matching is: ";
        for (int i = 0; i < humdeck.size(); i++) {
            std::cout << humdeck[i] << " ";
        }
        std::cout << '\n';
        int humremaining=humdeck.size()-1;
        int n= rand() % humremaining;
        cardswap(humdeck, n, comdeck);
        matcher(comdeck);

        std::cout << "The computer chose something from your deck\n";
        std::cout << "Your deck is now: ";
        for (int i = 0; i < humdeck.size(); i++) {
            std::cout << humdeck[i] << " ";
        }
        std::cout << '\n';

        remaining=comdeck.size();

        std::cout << "\n";
        if (comdeck.size()==0){
            std::cout << "The computer won!";
        }
        else if (humdeck.size()==0){
            std::cout << "The computer won!";
        }
        }

    return 0;
}

void matcher(std::vector<int> &deck) { // Pass by reference to modify the original deck
    for (size_t i = 0; i < deck.size(); i++) {
        for (size_t j = i + 1; j < deck.size(); j++) { // Start j at i+1 to avoid self-matching
            if (deck[i] == deck[j]) { 
                // Remove elements in reverse order to prevent index shifting issues
                deck.erase(deck.begin() + j);
                deck.erase(deck.begin() + i);

                // Restart loop after deletion to avoid skipping elements
                i = -1; // Will become 0 after i++ in the for-loop
                break; 
            }
        }
    }
}

void cardswap(std::vector<int> &deck, int selection, std::vector<int> &deck2){
    deck2.push_back(deck[selection]);
    deck.erase(deck.begin()+selection);
}
