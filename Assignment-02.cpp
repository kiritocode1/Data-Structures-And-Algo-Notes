#include <bits/stdc++.h>
using namespace std;

class Record {
    public: 
        vector<pair<string, string>> phonebook;
        Record(){
            cout << " this is another example of the Record system done in cpp \n";
        }
    int insert(string name , string number ){
        phonebook.push_back({name , number});
        return 0;
    }
    int print(){
        for (auto x : phonebook){
            cout << "name: " << x.first <<" phone Number:"<<x.second << "\n";
        }
        return 0;
    }
    int print_specific(int n){
        if (n<phonebook.size()&& n>=0){
            cout <<" name : "<< phonebook[n].first << "phone no :  " << phonebook[n].   second << "\n";
            return 0; 
        }
        cout << "index out of range please try again";
        return 0;
    }
    int delete_at_specific_index(int n){
        auto i = n ;
        phonebook.erase(phonebook.begin() + i);
        return 0;
    }
    int insert_at_specific_index(int index, pair<string , string> name_and_number){
        auto i = index;
        phonebook.insert(phonebook.begin() + i, name_and_number);
        return 0;
    }
    void operator+(Record other){
        for(auto x : other.phonebook){
            phonebook.push_back(x);
        }
    }
    int find_by_name(string name){
        for(auto x : phonebook){
            if (x.first == name){
                cout << x.second << "\n";
                }
        }
        return 0;
    }
    int find_by_number(string number){
        for (auto X : phonebook){
            if (X.second ==number){
                cout << X.first << "\n";
            }
        }
        return 0;
    }
    
};

int main()
{
    Record a;
    a.insert("aryan", "999999");
    a.insert_at_specific_index(0, {"kirito", "111111"});
    a.insert_at_specific_index(0, {"kirito", "222222"});
    a.delete_at_specific_index(1);
    a.print();
    return 0;
};