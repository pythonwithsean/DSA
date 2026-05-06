#include <iostream>
#include <string>

using namespace std;

#define MAX_ARR_CAPACITY 10

template <typename T>
class ArrayList
{
private:
	int size;
	int capacity;
	T *arr;

public:
	ArrayList() : size(0), capacity(MAX_ARR_CAPACITY)
	{
		arr = new T[capacity];
	};
	int Size()
	{
		return this->size;
	}
	int Get(int index) const
	{
		if (index >= size)
		{
			cerr << "Out of bounds" << endl;
			throw runtime_error("Out of Bounds");
		}
		return arr[index];
	}
	void Add(T item)
	{
		if (size == capacity)
		{
			cerr << "out of space Resizing" << endl;
			capacity *= 2;
			int *temp = new int[capacity];
			for (int i = 0; i < size; i++)
			{
				temp[i] = arr[i];
			}
			delete[] arr;
			arr = temp;
		}
		arr[size++] = item;
	}
	void showArray() const
	{
		cout << "[";
		for (int i = 0; i < size; i++)
		{
			cout << arr[i];
			if (i != size - 1)
				cout << ",";
		}
		cout << "]" << "\n";
	}
};

int main()
{

	return 0;
}