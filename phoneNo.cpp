#include <bits/stdc++.h>
using namespace std;
//Question
// Consider telephone book database of N clients.Make use of a hash table implementation to quickly look up client‘s telephone number.Make useof two collision handling techniques and compare them using number of comparisons required to find a set of telephone numbers.



class PhoneBook{
    unordered_map<string,string> phonebook;
    public:
        PhoneBook(){
            cout << "this is a dynamic phone book  , enter the no of students and then try finding the Person's number \n";
            cout << "enter the no of People whose Number you Need to add=>";
            int num;
            cin >> num;
            string name, phoneno;
            for (size_t i = 0; i <num; i++)
            {
                cout << "enter the name of student -" << (i + 1) << "->" << endl;
                cin >> name;
                cout << "enter the phone no =>" << endl;
                cin >> phoneno;
                phonebook[name] = phoneno;
            }
        }
        int find(){
            cout << "Enter the number of ppl u wanna find-> " << endl;
            int a;
            cin >> a; 
            for (size_t i = 0; i < a; i++)
            {
                //! searching and collission handling ;
                cout << "enter the name of student-"<<i<<" to  return the phone no=>" << endl;
                string querie;
                cin >> querie;
                try
                {
                    if (phonebook.find(querie) != phonebook.end())
                    {
                        cout <<"phone-no: "<< phonebook[querie] << endl;
                    }
                    else
                    {
                        throw false;
                    }
                }
                catch (bool)
                {
                    cout << "error the person does not exist" << endl;
                    
                }
            }
            return 0;
        }
};

    int main(){
        PhoneBook a;
        cout << "********************************" << endl;
        a.find();
        return 0;
};




