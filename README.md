# bookbot

BookBot is my first [Boot.dev](https://www.boot.dev) project!

## What I learned

While trying to generate the sorted list of dictionaries, at first I tried doing this

```py
return list_of_dicts.sort(reverse=True, key=sort_on)
```

Of course, this did not work. I learned that although `.sort()` does the sorting, it does so in place and returns `None`. I fixed it by calling `.sort()` first, and then returning the sorted list.

```py
list_of_dicts.sort(reverse=True, key=sort_on)
return list_of_dicts 
```
