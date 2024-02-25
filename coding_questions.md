<link rel="stylesheet" href="./test/style.css">

# [Coding Questions](./coding_questions.md)

> ## 1. Problem Statement:

You are given a string of lowercase English alphabets. Your task is to find whether two exactly same strings can be formed using all the characters given in the input string, if not possible then print 'Not Possibl'
If possible then you have to display the new generated string in which all the characters are lexicographically sorted.

#### Constraints:
- The string consists of lowercase English alphabets a-z.
- String length 1:1<= 1 <= 10^5

#### Input Format:

- The first and the only line containing a string.

#### Output Format:

- If Possible to divide the given string into two exactly the same strings, then the output would be one of the two strings. Else
  the output would be 'Not Possible'.

Input 1:

```bash
abcfdcbafada
```

Output 1:

```bash
aabcdf
```

Input 2:

```bash
abcdcb
```

Output 1:

```bash
Not Possible
```

Input 1:

```bash
abcabcde
```

Output 1:

```bash
Not Possible
```

code:

```cpp
#include <iostream>
#include <string>
#include <algorithm>
#include <unordered_map>

using namespace std;

string rearrangeString(string s)
{
    unordered_map<char, int> freq;

    for (char c : s)
    {
        freq[c]++;
    }

    for (auto &p : freq)
    {
        if (p.second % 2 != 0)
        {
            return "Not Possible";
        }
    }

    sort(s.begin(), s.end());

    string str = "";
    for (int i = 0; i < s.size(); i = i + 2)
    {
        str += s[i];
    }

    return str;
}

int main()
{
    string input;
    cin >> input;

    string result = rearrangeString(input);

    cout << result << endl;

    return 0;
}
```

---

---

> ## 2. Problem Statement

Alice owns a Cola stand, where each cola costs $5.
Customers are standing in a queue to buy from Alice, and order one at a time (in the order specified by invoice).
Each customer will only buy one cola and pay with either a $5, $10, or $20 invoice: Alice must provide the correct change to each customer, so that the net transaction is that the customer pays $5.

Note:

- Alice don't have any change in hand at first.

Print true if and only if Alice can provide every customer with correct change else print false.

#### Input Format

- First line contains an integer N, denoting the number of customers
- Next N line contains invoice

#### Constraints

- 0 <= N <= 10000
- invoice[i] will be either 5, 10, or 20.

#### Output Format

- Single line containing the result value

#### Evaluation Parameters

Sample Input1

```
5
5
5
5
5
20
```

Sample Output1

```
true
```

#### Explanation:

From the first 4 customers, Alice collect three $5 invoice in order From the fifth customer, Alice collect a $20 bill and give back a $10 and a $5 invoice. Since all customers got correct change, we output true.

Sample Input2

```
4
5
10
10
20
```

Sample Output2

```
false
```

Execution time limit
2 seconds

code:

```cpp
int N = invoice.size();
    int count5 = 0;
    int count10 = 0;
    for (int i = 0; i < N; i++)
    {
        if (invoice[i] == 5)
        {
            count5++;
        }
        else if (invoice[i] == 10)
        {
            if (count5 < 1)
            {
                return "false";
            }
            count5--;
            count10++;
        }
        else if (invoice[i] == 20)
        {
            if (count10 >= 1 && count5 >= 1)
            {
                count10--;
                count5--;
            }
            else if (count5 >= 3)
            {
                count5 -= 3;
            }
            else
            {
                return "false";
            }
        }
    }
    return "true";
```

---

> ## 3. Problem Statement

You are given a array of plot prices arr[] and a amount N, you have to find the minimum number of consecutive plots you can buy in that amount and print their positions in the array. The amount has to be fully exhausted/spent, If you are unable to spend the amount return array of positions [-1]
Examples:
when input is arr = [2,4,5,4,1,2,5], N = 3
then output is [4,5]
Note: array indexing starts at 0

#### Input Format

- The first line will contain arr space separated integers denoting the input array.
- The second line of each test case will contain a integer N denoting the amount.

#### Output Format

- For each test case, output space-separated integers in a separate line - positions of plots.

#### Evaluation parameters

Sample Input 1

```
2 4 5 4 1 2 5
3
```

Sample Output 1

```
4 5
```

code:

```cpp
#include <iostream>
#include <vector>

using namespace std;

vector<int> findConsecutivePlots(vector<int> arr, int N)
{
    vector<int> positions;
    int sum = 0, start = 0;

    for (int i = 0; i < arr.size(); ++i)
    {
        sum += arr[i];

        while (sum > N)
        {
            sum -= arr[start];
            start++;
        }

        if (sum == N)
        {
            for (int j = start; j <= i; ++j)
            {
                positions.push_back(j);
            }
            return positions;
        }
    }

    return {-1};
}

int main()
{
    vector<int> arr;
    int num, N;
    char c;

    // Input array
    while (cin >> num)
    {
        arr.push_back(num);
        if (cin.peek() == '\n')
            break;
    }

    // Input amount
    cin >> N;

    // Find positions of consecutive plots
    vector<int> result = findConsecutivePlots(arr, N);

    // Output positions
    for (int i = 0; i < result.size(); ++i)
    {
        cout << result[i];
        if (i != result.size() - 1)
            cout << " ";
    }
    cout << endl;

    return 0;
}
```

---

> ## 4. Problem Statement

You are given a bag full of Legos (Toy plastic blocks that can join with another block to form a big plastic toy Building). The bag contains N legos of 2 different colors(Red and Yellow), all of the different heights. You have to select M legos from the bag such that it follows two conditions-

1. No two consecutive lego are of the same color
2. The length of the toy building should be maximum

#### Input Format

- First-line contains the value of S1 and S2, the number of red legos, and a number of yellow legos respectively
- Second-line contains the space-separated height of different red legos
- The third line contains space-separated heights of different yellow legos

#### Output format

Print the possible largest height of the building

#### Constraints
- 1<=S1.S210<=10^4
- 1<= height of legos either red or yellow<=100

#### Evaluation Parameter

Sample Input

```
3 5
2 3 1
5 6 2 1 9
```

Sample Output

```
28
```

#### Explanation

- Firstly we will selective yellow color lego of length 9
- Then select red color lego offength 3
- Select yellow color lego of length 6
- Select red lego of ength 2
- Select yellow lego of length 5
- Select red lego of length 1
- Select red leg0 of length 2

Therefore tota ecth of the toy bulding =
9+3+6+2+5+1+2 = 28

Execution time limit
2 seconds

code:

```cpp
#include <bits/stdc++.h>
using namespace std;

int maxBuildingHeight(priority_queue<int> &red_legos, priority_queue<int> &yellow_legos)
{
    int total_height = 0;
    while (!red_legos.empty() && !red_legos.empty())
    {
        total_height += red_legos.top() + yellow_legos.top();
        red_legos.pop();
        yellow_legos.pop();
    }
    if (!red_legos.empty())
    {
        total_height += red_legos.top();
    }
    else
    {
        total_height += yellow_legos.top();
    }

    return total_height;
}

int main()
{
    int S1, S2;
    cin >> S1 >> S2;

    priority_queue<int> red_legos;

    priority_queue<int> yellow_legos;
    int val;
    for (int i = 0; i < S1; i++)
    {
        cin >> val;
        red_legos.push(val);
    }

    for (int i = 0; i < S2; i++)
    {
        cin >> val;
        yellow_legos.push(val);
    }

    cout << maxBuildingHeight(red_legos, yellow_legos) << endl;

    return 0;
}
```

---

> ## 5. Problem Statement:

Customise Zig-zag Traversal

You are given a graph (which is in the form of a complete binary tree). You have to traverse the tree level-wise and print the first value that is present in each level, alternatively from left (if it is an even level) and then right (if it is an odd level), and so on.

Suppose the tree is like this:

![](./img/tree.png)

The customized zig-zag traversal will be [1, 2, 9]. (Take it as 1-based leveling.)

Note: The input will be in the sequence of level-order traversals of the complete binary tree.

#### Input Format

- First-line will contain an integer h, denoting the height of the tree
- Next-line will contain an integer n, denoting the maximum number of nodes that can be present in the complete binary tree of the given height.
- The next n lines will contain an integer each.

#### Constraints

- 1<=h<=20
- n=2^h - 1
- node value = (-1, integer> -1 and inveger < 101)

#### Output Format

- Return an integer array denoting the custom order traversal.

#### Evaluation Parameters

#### Sample Input

```
3
7
1
2
5
3
4
4
9
```

#### sample output:

```
1
2
9
```

#### code:

```cpp
#include <bits/stdc++.h>
using namespace std;

vector<int> customZigZag(int h, vector<int> node)
{
    vector<int> result;
    int sum = 0;
    for (int i = 0; i < h; i++)
    {
        if (i % 2 == 0)
        {
            sum = pow(2, i + 1) - 2;
            result.push_back(node[sum]);
        }
        else
        {
            sum = pow(2, i) - 1;
            result.push_back(node[sum]);
        }
    }

    return result;
}

int main()
{
    vector<int> result;
    result = customZigZag(3, {1, 2, 5, 3, 4});
}
```
