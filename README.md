## Python automation for desktop/ folder organization

### organize files in a given source directory over n months 

#### To run:
```$python organize.py /full/path/to/messyfolder /full/path/to/target --extensions jpg png --months n```

---

#### note: 

```--extensions and --months are optional but have default [jpg, png] and 12 respectively```


---

*output:*
#### folders (named by YY-mm modified) containing the moved files in messyfolder with jpg and png extensions that were modified in the last n months
#### For help and detailed descriptions run:
```$python organize.py --help```