## ZopfliPNG wrapper for python

### This library wraps the zopflipng extension to implement lossless compression of PNG.

- Lossless compression of PNGS implemented by zopfli typically results in a compression ratio of 5% more than other lossless compression tools at the expense of longer compression time.

#### Install
    pip install zopflipng

 #### Usage：

 ```
# a simple example, using the default configuration

from zopflipng import png_optimize

data = open('test.png', 'rb').read()
result, code = png_optimize(data)
# if code ==0 ,png compression success
if code == 0:
    # save png
    with open('result.png','wb') as f:
        f.write(result)
        f.close()
 ```

<br>

- Use quick, but not very good, compression:

 ```
result, code = png_optimize(data, use_zopfli=False)
 ```

- Compress really good and trying all filter strategies:

 ```
result, code = png_optimize(data, lossy_8bit=True, lossy_transparent=True, filter_strategies='01234mepb', num_iterations=500)
 ```


If you want to process multiple images, use multiprocessing