#include <bits/stdc++.h>

#define MAX 2 * 123456

using namespace std;

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  vector<bool> isPrime(MAX + 1, true);
  isPrime[0] = isPrime[1] = false;

  for (int i = 2; i * i <= MAX; i++) {
    if (isPrime[i]) {
      for (int j = i * i; j <= MAX; j += i)
        isPrime[j] = false;
    }
  }

  while (true) {
    int n; cin >> n;

    if (n == 0) break ;

    int cntPrime = 0;
    for (int i = n + 1; i <= 2 * n; i++)
      if (isPrime[i]) cntPrime++;

    cout << cntPrime << "\n";
  }

  return 0;
}