#include <bits/stdc++.h>
using namespace std;

unordered_map<int, int> dfs(vector<int> L, unordered_map<int, int> fD = {}, int c = 0)
{
    if (L.empty() == true)
        return fD;
    auto max_it = max_element(L.begin(), L.end());
    int maxi = *max_it;
    int ind = distance(L.begin(), max_it);
    fD[maxi] = c++;
    vector<int> left(L.begin(), L.begin() + ind);
    vector<int> right(L.begin() + ind + 1, L.end());
    fD = dfs(left, fD, c);
    fD = dfs(right, fD, c);
    return fD;
}

int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n;
        cin >> n;
        vector<int> L(n);
        for (int i = 0; i < n; i++)
        {
            cin >> L[i];
        }
        unordered_map<int, int> fD = dfs(L);
        for (int i = 0; i < n; i++)
        {
            cout << fD[L[i]] << " ";
        }
        cout << endl;
    }

    return 0;
}