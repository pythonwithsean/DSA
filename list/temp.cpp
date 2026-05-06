#include <iostream>
#include <algorithm>
#include <math.h>

int findMin(int arr[], size_t size)
{
  int minimum = arr[0];
  std::array<int, size - 1> slice;
  return findMin(minimum)
};

int main()
{
  int arr[5] = {122, 100, 10, 1, 40};
  std::cout << findMin(arr, 5) << std::endl;
  return 0;
}
