#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

int main() {
	ios_base::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL);
	int n;
	cin >> n;
	//5의 갯수
	int ans = -1;
	for (int i = 0; i < 10000; i++) {
		if (5 * i > n) {
			break;
		}
		int div = n - 5 * i;
		if (div % 3 == 0) {
			if (ans == -1) {
				ans = i + div / 3;
			}
			else {
				ans = min(ans, i + div / 3);
			}
		}
	}
	cout << ans;
}