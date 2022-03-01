#include <iostream>
using namespace std;
struct node
{
    int roll_no;
    string name;
    node *next;
};
node *head;
void insert_after_president(int rol, string nae)
{
    node *temp = new node;
    temp->roll_no = rol;
    temp->name = nae;
    temp->next = head->next;
    head->next = temp;
}
void president_set(int rol, string nae)
{
    head->roll_no = rol;
    head->name = nae;
    head->next = NULL;
}
void print()
{
    node *temp = head;
    while (temp->next != NULL)
    {
        cout << temp->name << " " << temp->roll_no << "->";
    }
    cout << temp->name << " " << temp->roll_no << "->null";
}
int main()
{
    president_set(3, "hello");
    insert_after_president(5,"student-1");
    print();
    return 0;
    }

