#include <bits/stdc++.h>
using namespace std;
#define int long long

signed main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, l, r;
        cin >> n >> l >> r;
        l--;
        r--;
        vector<int> L(n);
        for (int i = 0; i < n; i++)
        {
            cin >> L[i];
        }
        vector<int> b = L;
        sort(b.begin() + l, b.end());
        vector<int> c = L;
        // sort(c.begin(), c.begin() + r + 1, greater<int>());
        sort(c.begin(), c.begin() + r + 1);
        reverse(c.begin(),  c.begin() + r + 1);
        // sort(c.rbegin() + n - r - 1, c.rend());
        int sumb = 0, sumc = 0;
        for (int i = l; i <= r; i++)
        {
            sumb += b[i];
            sumc += c[i];
        }
        cout << min(sumb, sumc) << endl;
    }
    return 0;
}
