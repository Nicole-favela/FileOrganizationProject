## Python automation for desktop/ folder organization

### Key features:
 * dynamic organization: enter only the file types you want or stick with only images.
 * date based organization: decide on files and have a timeline for easy access.
 * user-friendly: argparse allows you to taylor the script to your needs and get help if needed.

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