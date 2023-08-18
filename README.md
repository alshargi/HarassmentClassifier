
  #HarassmentClassifier
   Arabic Harassment classifier


#### install the library:
```bash
pip install git+https://github.com/alshargi/HarassmentClassifier.git
```
#### Demo of some of the features:
```python

from QahtanClassifier import get_pred_label
xx = ['ليبراليه شويه صعاليك ',
       ' الاسم شاهين والشكل والتفكير حمار',
      'يلعن امك يا ابن الحمار',
      'ست اوبي ي زنو
MyResult = predict.get_pred_label(xx)
for i in MyResult:
    subRes =  i.split("\t")
    for s in subRes:
        print(s)
    print("########")

```

#### Result
```bash



```





