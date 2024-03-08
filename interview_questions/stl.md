<link rel="stylesheet" href="../test/style.css">

# [STL](stl.md)

<details>
<summary style="font-size:20px;" id="map">STL</summary>

- [STL](#stl)
  - [map](#map)
    - [Construct map](#construct-map)
    - [operator=](#operator)
    - [begin](#begin)
    - [end](#end)
    - [empty](#empty)
    - [size](#size)
    - [operator\[\]](#operator-1)
    - [at](#at)
    - [insert](#insert)
    - [erase](#erase)
    - [clear](#clear)
    - [find](#find)
    - [count](#count)
    - [multimap](#multimap)

</details>

## [map](https://cplusplus.com/reference/map/)

### [Construct map](https://cplusplus.com/reference/map/map/map/)

```cpp
// constructing maps
#include <iostream>
#include <map>

bool fncomp (char lhs, char rhs) {return lhs<rhs;}

struct classcomp {
  bool operator() (const char& lhs, const char& rhs) const
  {return lhs<rhs;}
};

int main ()
{
  std::map<char,int> first;

  first['a']=10;
  first['b']=30;
  first['c']=50;
  first['d']=70;

  std::map<char,int> second (first.begin(),first.end());

  std::map<char,int> third (second);

  std::map<char,int,classcomp> fourth;                 // class as Compare

  bool(*fn_pt)(char,char) = fncomp;
  std::map<char,int,bool(*)(char,char)> fifth (fn_pt); // function pointer as Compare

  return 0;
}
```

### [operator=](https://cplusplus.com/reference/map/map/operator=/)

```cpp
// assignment operator with maps
#include <iostream>
#include <map>

int main ()
{
  std::map<char,int> first;
  std::map<char,int> second;

  first['x']=8;
  first['y']=16;
  first['z']=32;

  second=first;                // second now contains 3 ints
  first=std::map<char,int>();  // and first is now empty

  std::cout << "Size of first: " << first.size() << '\n';
  std::cout << "Size of second: " << second.size() << '\n';
  return 0;
}

```

```bash
Output:
Size of first: 0
Size of second: 3
```

### [begin](https://cplusplus.com/reference/map/map/begin/)

```cpp
// map::begin/end
#include <iostream>
#include <map>

int main ()
{
  std::map<char,int> mymap;

  mymap['b'] = 100;
  mymap['a'] = 200;
  mymap['c'] = 300;

  // show content:
  for (std::map<char,int>::iterator it=mymap.begin(); it!=mymap.end(); ++it)
    std::cout << it->first << " => " << it->second << '\n';

  return 0;
}
```

```bash
output:
a => 200
b => 100
c => 300
```

### [end](https://cplusplus.com/reference/map/map/end/)

```cpp
#include <iostream>
#include <map>

int main ()
{
  std::map<char,int> mymap;

  mymap['b'] = 100;
  mymap['a'] = 200;
  mymap['c'] = 300;

  // show content:
  for (std::map<char,int>::iterator it=mymap.begin(); it!=mymap.end(); ++it)
    std::cout << it->first << " => " << it->second << '\n';

  return 0;
}
```

```bash
Output:
a => 200
b => 100
c => 300
```

### [empty](https://cplusplus.com/reference/map/map/empty/)

```cpp
#include <iostream>
#include <map>

int main ()
{
  std::map<char,int> mymap;

  mymap['a']=10;
  mymap['b']=20;
  mymap['c']=30;

  while (!mymap.empty())
  {
    std::cout << mymap.begin()->first << " => " << mymap.begin()->second << '\n';
    mymap.erase(mymap.begin());
  }

  return 0;
}
 Edit & run on cpp.sh
```

```bash
Output:
a => 10
b => 20
c => 30
```

### [size](https://cplusplus.com/reference/map/map/size/)

```cpp
// map::size
#include <iostream>
#include <map>

int main ()
{
  std::map<char,int> mymap;
  mymap['a']=101;
  mymap['b']=202;
  mymap['c']=302;

  std::cout << "mymap.size() is " << mymap.size() << '\n';

  return 0;
}
```

```bash
Output:
mymap.size() is 3
```

### [operator[]](https://cplusplus.com/reference/map/map/operator[]/)

```cpp
// accessing mapped values
#include <iostream>
#include <map>
#include <string>

int main ()
{
  std::map<char,std::string> mymap;

  mymap['a']="an element";
  mymap['b']="another element";
  mymap['c']=mymap['b'];

  std::cout << "mymap['a'] is " << mymap['a'] << '\n';
  std::cout << "mymap['b'] is " << mymap['b'] << '\n';
  std::cout << "mymap['c'] is " << mymap['c'] << '\n';
  std::cout << "mymap['d'] is " << mymap['d'] << '\n';

  std::cout << "mymap now contains " << mymap.size() << " elements.\n";

  return 0;
}
```

Notice how the last access (to element 'd') inserts a new element in the map with that key and initialized to its default value (an empty string) even though it is accessed only to retrieve its value. Member function map::find does not produce this effect.

```bash
Output:
mymap['a'] is an element
mymap['b'] is another element
mymap['c'] is another element
mymap['d'] is
mymap now contains 4 elements.
```

### [at](https://cplusplus.com/reference/map/map/at/)

```cpp
// map::at
#include <iostream>
#include <string>
#include <map>

int main ()
{
  std::map<std::string,int> mymap = {
                { "alpha", 0 },
                { "beta", 0 },
                { "gamma", 0 } };

  mymap.at("alpha") = 10;
  mymap.at("beta") = 20;
  mymap.at("gamma") = 30;

  for (auto& x: mymap) {
    std::cout << x.first << ": " << x.second << '\n';
  }

  return 0;
}
```

```bash
Possible output:
alpha: 10
beta: 20
gamma: 30
```

### [insert](https://cplusplus.com/reference/map/map/insert/)

```cpp
// map::insert (C++98)
#include <iostream>
#include <map>

int main ()
{
  std::map<char,int> mymap;

  // first insert function version (single parameter):
  mymap.insert ( std::pair<char,int>('a',100) );
  mymap.insert ( std::pair<char,int>('z',200) );

  std::pair<std::map<char,int>::iterator,bool> ret;
  ret = mymap.insert ( std::pair<char,int>('z',500) );
  if (ret.second==false) {
    std::cout << "element 'z' already existed";
    std::cout << " with a value of " << ret.first->second << '\n';
  }

  // second insert function version (with hint position):
  std::map<char,int>::iterator it = mymap.begin();
  mymap.insert (it, std::pair<char,int>('b',300));  // max efficiency inserting
  mymap.insert (it, std::pair<char,int>('c',400));  // no max efficiency inserting

  // third insert function version (range insertion):
  std::map<char,int> anothermap;
  anothermap.insert(mymap.begin(),mymap.find('c'));

  // showing contents:
  std::cout << "mymap contains:\n";
  for (it=mymap.begin(); it!=mymap.end(); ++it)
    std::cout << it->first << " => " << it->second << '\n';

  std::cout << "anothermap contains:\n";
  for (it=anothermap.begin(); it!=anothermap.end(); ++it)
    std::cout << it->first << " => " << it->second << '\n';

  return 0;
}
```

```bash
Output:
element 'z' already existed with a value of 200
mymap contains:
a => 100
b => 300
c => 400
z => 200
anothermap contains:
a => 100
b => 300
```

### [erase](https://cplusplus.com/reference/map/map/erase/)

```cpp
// erasing from map
#include <iostream>
#include <map>

int main ()
{
  std::map<char,int> mymap;
  std::map<char,int>::iterator it;

  // insert some values:
  mymap['a']=10;
  mymap['b']=20;
  mymap['c']=30;
  mymap['d']=40;
  mymap['e']=50;
  mymap['f']=60;

  it=mymap.find('b');
  mymap.erase (it);                   // erasing by iterator

  mymap.erase ('c');                  // erasing by key

  it=mymap.find ('e');
  mymap.erase ( it, mymap.end() );    // erasing by range

  // show content:
  for (it=mymap.begin(); it!=mymap.end(); ++it)
    std::cout << it->first << " => " << it->second << '\n';

  return 0;
}
```

```bash
Output:
a => 10
d => 40
```

### [clear](https://cplusplus.com/reference/map/map/clear/)

```cpp
// map::clear
#include <iostream>
#include <map>

int main ()
{
  std::map<char,int> mymap;

  mymap['x']=100;
  mymap['y']=200;
  mymap['z']=300;

  std::cout << "mymap contains:\n";
  for (std::map<char,int>::iterator it=mymap.begin(); it!=mymap.end(); ++it)
    std::cout << it->first << " => " << it->second << '\n';

  mymap.clear();
  mymap['a']=1101;
  mymap['b']=2202;

  std::cout << "mymap contains:\n";
  for (std::map<char,int>::iterator it=mymap.begin(); it!=mymap.end(); ++it)
    std::cout << it->first << " => " << it->second << '\n';

  return 0;
}
```

```bash
Output:
mymap contains:
x => 100
y => 200
z => 300
mymap contains:
a => 1101
b => 2202
```

### [find](https://cplusplus.com/reference/map/map/find/)

```cpp
// map::find
#include <iostream>
#include <map>

int main ()
{
  std::map<char,int> mymap;
  std::map<char,int>::iterator it;

  mymap['a']=50;
  mymap['b']=100;
  mymap['c']=150;
  mymap['d']=200;

  it = mymap.find('b');
  if (it != mymap.end())
    mymap.erase (it);

  // print content:
  std::cout << "elements in mymap:" << '\n';
  std::cout << "a => " << mymap.find('a')->second << '\n';
  std::cout << "c => " << mymap.find('c')->second << '\n';
  std::cout << "d => " << mymap.find('d')->second << '\n';

  return 0;
}
```

```bash
Output:
elements in mymap:
a => 50
c => 150
d => 200
```

### [count](https://cplusplus.com/reference/map/map/count/)

```cpp
// map::count
#include <iostream>
#include <map>

int main ()
{
  std::map<char,int> mymap;
  char c;

  mymap ['a']=101;
  mymap ['c']=202;
  mymap ['f']=303;

  for (c='a'; c<'h'; c++)
  {
    std::cout << c;
    if (mymap.count(c)>0)
      std::cout << " is an element of mymap.\n";
    else
      std::cout << " is not an element of mymap.\n";
  }

  return 0;
}
```

```bash
Output:
a is an element of mymap.
b is not an element of mymap.
c is an element of mymap.
d is not an element of mymap.
e is not an element of mymap.
f is an element of mymap.
g is not an element of mymap.
```

### [multimap](https://cplusplus.com/reference/map/multimap/)

```cpp
// multimap::begin/end
#include <iostream>
#include <map>

int main ()
{
  std::multimap<char,int> mymultimap;

  mymultimap.insert (std::pair<char,int>('a',10));
  mymultimap.insert (std::pair<char,int>('b',20));
  mymultimap.insert (std::pair<char,int>('b',150));

  // show content:
  for (std::multimap<char,int>::iterator it=mymultimap.begin(); it!=mymultimap.end(); ++it)
    std::cout << (*it).first << " => " << (*it).second << '\n';

  return 0;
}
```

```bash
Output:
a => 10
b => 20
b => 150
```
