## ZopfliPNG python wrapper

#### Implementing lossless compression of PNG typically results in a loss rate of 5% more than other lossless compression tools at the expense of much longer compression time

#### Install
    pip install zopflipng

 #### usage：

 ```
data = open('test.png','rb').read()
result = png_optimize(data)
with open('result.png','wb') as f:
f.close()
 ```

It's so easy